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
```


### Source files from github (optional method)
Clone the public git repository and download all license compatible optional external components.

```bash
git clone https://github.com/dftbplus/dftbplus.git
cd dftbplus
./utils/get_opt_externals
```

## II. Compilation

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
  1) intel/2020.2.254      2) intelmpi/2020.2.254   3) cmake/3.18.3
```

If there is a need to compile this from scratch or on a different cluster/pc, it basically needs the following:

1. Intel compilers, MPI and MKL (all included in oneapi)
2. cmake v3.16 or newer
3. Python (version >= 3.2) for the source preprocessor

### Configure



```bash
cd dftbplus-21.2/
suffix='intel'
option='FC=mpiifort CC=mpiicc'
builddir="${suffix}_build"
cmake_opt="-DCMAKE_INSTALL_PREFIX=${builddir}/bin -DWITH_MPI=TRUE -DWITH_OMP=FALSE -DTEST_MPI_PROCS=6"
srcdir="./"
```
