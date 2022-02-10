# Utility-Collection
Collection of utility scripts, instructions and many more!


## Table of contents
1. [DFTB+](###I.-DFTB+)
2. [Core Utilities](###II.-Core-Utilities)
3. [Smith Utilities](###III.-Smit-Utilities)

## Contents Description
### I. DFTB+ 
- `dftbplus/`
- This folder contains specific instructions on how to compile the DFTB+ code using the environment available in the "smith" cluster of Osaka University. Comments and notes are also made to guide compilation using custom environment. 

### II. Core Utilities 
- `coreutils/`
- This folder contains instructions on how to compile and use custom `cp` and `mv`. Theses particular custom commands have progress bar with them which is useful. 

### III. Smith Utilities
-  `smith_util/`
- This folder contains a set of scripts that helps the user interface with the "smith" cluster. 
- Example scripts:
  - `smith_connect` - Initiates ssh connection to smith
  - `smith_share` - Mounts the smith filesystem to local system for easier environment control.
  - `smith_tunnel` - Establishes the connection to Osaka University's network to make non-local connection.  