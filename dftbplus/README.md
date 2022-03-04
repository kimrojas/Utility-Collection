# DFTB+ Installation guide

This document is meant to reproduce my installation of DFTB+ in smith cluster. The guide is mainly based on the [installation instruction from the DFTB+ team](https://github.com/dftbplus/dftbplus/blob/21.2/INSTALL.rst) with tweaks to accomodate the intel compilers, mpi, and mkl as well the the required environment variables in the smith cluster.

> **STATUS**: Basic installation only, no advanced solvers yet (e.g. ELSI, MAGMA)

---
## FAST SETUP (TL;DR) - easy as 1,2,3
1. Download `install_script.py`
2. Follow the following commands (on login node with internet access)
```bash
# Load enviroment
module load cmake/3.18.3
module load intel/2020.2.254
module load intelmpi/2020.2.254
module load python/3.8

# Create a Python conda environment
PACKAGE='python=3.8 numpy scipy ase cymem cython decorator mpi4py pytest'
conda create --name DFTBplus -c conda-forge $PACKAGE -y

# Activate the new Python conda
source activate DFTBplus

# Download the installation script
svn export https://github.com/kimrojas/Utility-Collection/trunk/dftbplus/install_script.py

# Run the installation script
python install_script.py

# Download Installation script

# Run automated installation script
python install_script.py

##### (OPTIONAL) Create module files for simplicity of using `module load` ####
# Download the easy script
svn export https://github.com/kimrojas/Utility-Collection/trunk/dftbplus/install_module.py
# Run script
python install_module.py
# Add the module file to the environment so environment modules can detect it
echo "module use --append $(pwd)/modulefiles"

# - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - -
#                       DONE - CONGRATULATIONS !!!
# - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - -

```
3. export environment PATH and variables based on the script's last output. 
4. Download slakos files from https://dftb.org/parameters/download/all-sk-files
---

## ADVANCED DETAILS

> UNDER CONSTRUCTION: This part is under construction





## I. Obtaining Source Code

### Source files from website download page

Download the release package from the link below. At this time, DFTB+ v21.2 is the latest stable release hence the version-specific-link was used. 

**Download page is available in [link](https://dftbplus.org/download/dftb-stable/)**

```bash
wget https://github.com/dftbplus/dftbplus/releases/download/21.2/dftbplus-21.2.tar.xz
tar xvf dftbplus-21.2.tar.xz 
cd dftbplus-21.2
./utils/get_opt_externals
```
>*NOTE: Documentation says that the stable release already contains the external components but no they don't*

### Source files from github (optional method)
Clone the public git repository and download all license compatible optional external components.

```bash
git clone https://github.com/dftbplus/dftbplus.git
cd dftbplus
./utils/get_opt_externals
```

## II. Preparing requirements

### Activate pre-requisite modules
This part is specific to the smith cluster's environment modules. 

```bash
module load cmake/3.18.3
module load intel/2020.2.254
module load intelmpi/2020.2.254
module load python/3.8

module load cmake/3.18.3 intel/2020.2.254 intelmpi/2020.2.254 python/3.8
``` 

job script
```
module load cmake/3.18.3 intel/2020.2.254 intelmpi/2020.2.254 python/3.8
source activate 
conda activate dftb
```


Confirm that it is loaded using the `module list` command.  
*EXPECTED OUTPUT:*
```bash
Currently Loaded Modulefiles:
  1) intel/2020.2.254      2) intelmpi/2020.2.254   3) cmake/3.18.3          4) python/3.8
```

### Options for non-smith installation

If there is a need to compile this from scratch or on a different cluster/pc, it basically needs the following:

1. Intel compilers, MPI and MKL (all included in oneapi)
2. cmake v3.16 or newer
3. Python (version >= 3.2) for the source preprocessor


### Prepare python
For PYTHON API compatability
```bash
conda create -n dftb -c conda-forge python ase 
source activate
conda activate dftb
```

## III. Configure, build and test
In this section we will use a custom installer script to help you. Feel free to browse the script to get the exact compilation commands implemented. 

I have prepared two installer scripts that corresponds to the two MPI paralleization techniques that can be emplyed. 

1. `setup_intel_omp` - uses OpenMPI link
2. `setup_intel_mpi` - uses MPI link

In the following section, I will use `run_intel_mpi` for demonstration.

> *Note: As of the moment, both installation have not yet rigourously tested*

### Download the script
```bash
# Go to DFTB+ directory
cd dftbplus-21.2/ 
# Download script
wget https://raw.githubusercontent.com/kimrojas/Utility-Collection/main/dftbplus/setup_intel_mpi
# Enable execution 
chmod +x setup_intel_mpi
```

### Run the script
```bash
# If you don't want to wait, RUN ALL
# ./run_intelmpi config && ./run_intelmpi build && ./run_intelmpi test
# Run configuration protocol
./setup_intel_mpi config  
# Run build protocol
./setup_intel_mpi build
# Run test protocol
./setup_intel_mpi test
# If test results are fine, run install
./setup_intel_mpi install
```

## IV. Usage

### Setup installation 

The binary files will be located in `dftbplus-21.2/intelmpi_build/install_directory/bin`.  
Simply add this to your environment by using 
```bash
## ASSUMING YOU ARE IN THE SOURCE DIRECTORY
## Assuming ~/.bashrc is your default startup environment
dftb_bin=$(realpath intelmpi_build/install_directory/bin)
echo "export PATH=$PATH:$dftb_bin" >> ~/.bashrc
source ~/.bashrc

# Check if it was successfully located
which dftb+
# Expected output:
# [krojas@smith2 dftbplus-21.2]$ which dftb+
# ~/DFTB/PRIMARY/dftbplus-21.2/intelmpi_build/install_directory/bin/dftb+
```

### Using dftb+

#### Download example files
For example input files you can download an already prepared archive here.   
> Note 1: The examples archive is based on the [recipe given by the dftb+ team](https://dftbplus-recipes.readthedocs.io/en/latest/introduction.html#) but I've predownloaded the pre-requisites due some problem with smith decompressing issues.
> Note 2: the `mpirun` cannot be run on smith. Please use `rsh` to login to a compute node to try the examples (e.g. `rsh xs15` to login to ). 
```bash
# Download and extract example folder
wget https://github.com/kimrojas/Utility-Collection/raw/main/dftbplus/usage/example.tar.gz && tar zxvf example.tar.gz
```

#### Running dftb+
```bash
# The following instructions assumes that you are logged in to a mpirun-viable machine (e.g. the compute node of smith cluster)
cd example/moleculardynamics/initialstructure
module load intel/2020.2.254 intelmpi/2020.2.254

# Do a serial run
dftb+ > output
grep 'MPI processes' output 
#|| MPI processes:               1
grep BLACS output 
#|| BLACS orbital grid size:     1 x 1
#|| BLACS atom grid size:        1 x 1

# Do a parallel run
mpirun dftb+ > output
grep 'MPI processes' output 
#|| MPI processes:               16
grep BLACS output 
#|| BLACS orbital grid size:     4 x 4
#|| BLACS atom grid size:        2 x 2

# Do a parallel run with controlled num of processes
mpirun -n 8 dftb+ > output
grep 'MPI processes' output 
#|| MPI processes:               8
grep BLACS output 
#|| BLACS orbital grid size:     2 x 4
#|| BLACS atom grid size:        2 x 2
```

#### Job script

```bash
TO BE CONTINUED 
```



## Known issues
Here are some known issues when `./run_intelmpi build` is invoked. I honestly don't know what is happening but everything seems to work well.

```
warning #6843: A dummy argument with an explicit INTENT(OUT) declaration is not given an explicit value.

remark #8291: Recommended relationship between field width 'W' and the number of fractional digits 'D' in this edit
descriptor is 'W>=D+7'.
```

