# DFTB+ Installation guide

This document is meant to reproduce my installation of DFTB+ in smith cluster. The guide is mainly based on the [installation instruction from the DFTB+ team](https://github.com/dftbplus/dftbplus/blob/21.2/INSTALL.rst) with tweaks to accomodate the intel compilers, mpi, and mkl as well the the required environment variables in the smith cluster.

> **STATUS**: Basic installation only, no advanced solvers yet (e.g. ELSI, MAGMA)

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
wget https://raw.githubusercontent.com/kimrojas/Utility-Collection/main/dftb%2B/run_intelmpi
# Enable execution 
chmod +x run_intelmpi
```

### Run the script
```bash
# RUN ALL
# ./run_intelmpi config && ./run_intelmpi build && ./run_intelmpi test
# Run configuration protocol
./run_intelmpi config  
# Run build protocol
./run_intelmpi build
# Run test protocol
./run_intelmpi test
```



## Known issues
Here are some known issues when `./run_intelmpi build` is invoked. I honestly don't know what is happening but everything seems to work well.

```
warning #6843: A dummy argument with an explicit INTENT(OUT) declaration is not given an explicit value.

remark #8291: Recommended relationship between field width 'W' and the number of fractional digits 'D' in this edit
descriptor is 'W>=D+7'.
```

