# DFTB+ Installation guide

This document is meant to reproduce my installation of DFTB+ in smith cluster. The guide is mainly based on the [installation instruction from the DFTB+ team](https://github.com/dftbplus/dftbplus/blob/21.2/INSTALL.rst) with tweaks to accomodate the intel compilers, mpi, and mkl as well the the required environment variables in the smith cluster.

## Obtaining from source

### *Source files*
Clone the public git repository. The tagged revisions correspond to stable releases, while the default branch contains the latest development version.

```bash
git clone https://github.com/dftbplus/dftbplus.git
cd dftbplus
```

### *Optional extra components*
This will download all license compatible optional external components. These include the Slater-Koster (slako) data for testing the compiled code.

```bash
./utils/get_opt_externals
```

## Compilation

### Activate pre-requisite modules
This part is specific to the smith cluster's environment modules. 

```bash
module load cmake/3.18.3
module load intel/2020.2.254
module load intelmpi/2020.2.254
``` 

If there is a need to compile this from scratch or on a different cluster/pc, it basically needs the following:

1. Intel compilers, MPI and MKL (all included in oneapi)
2. cmake v3.16 or newer
3. Python (version >= 3.2) for the source preprocessor

### **Configure**