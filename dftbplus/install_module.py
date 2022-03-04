import subprocess
import os
import sys
import shutil

# Get installation directory name
with open('dftbplus-21.2/buildlog.path', 'r') as f:
    lines = f.read().splitlines()
    
for line in lines:
    if 'BASE DIRECTORY' in line:
        base_directory = line.split()[-1]
        break



# Initialization for  module file
moddir = 'modulefiles/dftbplus'
os.makedirs(moddir, exist_ok=True)

if len(sys.argv) == 1:
    modfile = '21.2_OpenMP'
    print(f'Using default module file name: {modfile}')
elif len(sys.argv) == 2:
    modfile = sys.argv[1]
    print(f'Using custom module file name: {modfile}')
else:
    raise ValueError(f'Expected maximum arguments is 1, I detected {len(sys.argv)-1}')

fullmodfile = os.path.join(moddir, modfile)






modfile_str = """\
#%Module

proc ModulesHelp { } {
    global majorver
    global minorver
    global bindir
    global libdir
    global incdir
    global pyapi
    global pydptools

    puts stderr "DFTB+ ($majorver $minorver) environment loader"
    puts stderr ""
    puts stderr "Details:"
    puts stderr ""
    puts stderr "\tEnvironment variables:"
    puts stderr "\t\tDFTB_COMMAND ${bindir}/dftb+"
    puts stderr "\t\tDFTB_LIB     ${libdir}/libdftbplus"
    puts stderr ""
    puts stderr "\tPathing:"
    puts stderr "\t\tprepend-path PATH               ${bindir}"
    puts stderr "\t\tprepend-path LD_LIBRARY_PATH    ${libdir}"
    puts stderr "\t\tprepend-path LIBRARY_PATH       ${libdir}"
    puts stderr "\t\tprepend-path CPATH              ${incdir}"
    puts stderr "\t\tprepend-path PYTHONPATH         ${pyapi}"
    puts stderr "\t\tprepend-path PYTHONPATH         ${pydptools}"
    puts stderr ""
}
 
module-whatis "This module prepares the dftb+ (v21.2 OpenMP) environment\n"

module load cmake/3.18.3
module load intel/2020.2.254
module load intelmpi/2020.2.254
module load python/3.8

set majorver    v21.2
set minorver    OpenMP
set basedir     <__BASEDIR__>
set libdir      "${basedir}/lib64"
set bindir      "${basedir}/bin"
set incdir      "${basedir}/include"
set pypackage   "${basedir}/lib/python3.8/site-packages"

setenv DFTB_COMMAND ${bindir}/dftb+
setenv DFTB_LIB     ${libdir}/libdftbplus
setenv DFTB_SLAKOS  /home/krojas/share/lib/slakos

prepend-path PATH               ${bindir}
prepend-path LD_LIBRARY_PATH    ${libdir}
prepend-path LIBRARY_PATH       ${libdir}
prepend-path CPATH              ${incdir}
prepend-path PYTHONPATH         ${pypackage}
    """


modified_modfile_str = modfile_str.replace('<__BASEDIR__>', base_directory)

with open(fullmodfile, 'w') as f:
    f.write(modified_modfile_str)
    
print(f'Module file prepared !')
print(f'File location: {fullmodfile}')