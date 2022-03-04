#!/usr/bin/env python3
import os
import shutil 
import sys
import subprocess as sp



# DFTB+ VERSION 21.2 (OpenMP)
# SMITH INSTALLATION using INTEL COMPILERS
# REQUIREMENTS:
#       Pre-load environment modules = cmake, intel, intelmpi, python
#       `module load cmake python intel intelmpi`

def process(line):
    print('\033[96m'+line+'\033[0m')

# Download and extract Source code
process('DOWNLOADING FILE')
tarlink = "https://github.com/dftbplus/dftbplus/releases/download/21.2/dftbplus-21.2.tar.xz"
tarfile = "dftbplus-21.2.tar.xz"
srcdir = "dftbplus-21.2"
sp.run(f'wget -q -O {tarfile} {tarlink}', shell=True)
print("    "+tarfile+" downloaded")
process("EXTRACTING FILE")
sp.run(f'tar xf {tarfile}', shell=True)
print("    "+tarfile+" extracted to "+srcdir)
os.rmdir(tarfile)


# Prepare source directory
process("PREPARING SOURCE FILES")
os.chdir("./" + srcdir)
sp.run('./utils/get_opt_externals', shell=True)

# Prepare input parameters and other essentials
# **OpenMP version parameters**
builddir = "_build"
srcdir_full = os.getcwd()
installdir = "_install"
installdir_full = os.path.join(srcdir_full,installdir)
COMPILER_OPT = 'FC=mpiifort  CC=mpiicc'
python_opt = '-DENABLE_DYNAMIC_LOADING=1 -DWITH_PYTHON=1 -DBUILD_SHARED_LIBS=1 -DWITH_API=1'
ase_opt = '-DWITH_SOCKETS=1'
CMAKE_OPT = f"-DCMAKE_INSTALL_PREFIX={installdir_full} {python_opt} {ase_opt} -DTEST_OMP_THREADS=2"

# Rebuild build directory
process("REBUILDING BUILD DIRECTORY")
loc = os.getcwd()
builddir_full = os.path.join(loc,builddir)
shutil.rmtree(builddir_full, ignore_errors=True)
os.makedirs(builddir)
print("    "+"Rebuilding successful:   "+builddir_full)

# CMAKE configuration protocol
process("CMAKE CONFIGURATION PROTOCOL")
command = f"{COMPILER_OPT} cmake {CMAKE_OPT} -B {builddir} ./"
logfile = open('buildlog.config', 'w')
proc = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True, shell=True)
for line in proc.stdout:
    sys.stdout.write("    "+line)
    logfile.write(line)
proc.wait()
logfile.close()


# CMAKE build protocol
process("CMAKE BUILD PROTOCOL")
command = f"cmake --build {builddir} -- -j"
logfile = open('buildlog.build', 'w')
proc = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True, shell=True)
for line in proc.stdout:
    sys.stdout.write("    "+line)
    logfile.write(line)
proc.wait()
logfile.close()

# CMAKE test protocol
process("CMAKE TEST PROTOCOL")
os.chdir(builddir)
command = f"ctest -j4"
logfile = open('buildlog.test', 'w')
proc = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True, shell=True)
for line in proc.stdout:
    sys.stdout.write("    "+line)
    logfile.write(line)
proc.wait()
logfile.close()
os.chdir('../')


# CMAKE install protocol
process("CMAKE INSTALL PROTOCOL")
command = f"cmake --install {builddir}"
logfile = open('buildlog.install', 'w')
proc = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, universal_newlines=True, shell=True)
for line in proc.stdout:
    sys.stdout.write("    "+line)
    logfile.write(line)
proc.wait()
logfile.close()

# PATHing guide
process("SHOWING IMPORTANT PATHS")
logfile = open("buildlog.path",'w')
paths = []
paths.append(f"{'BIN directory':25}  |  {'add to PATH':40}  |  {installdir_full+'/bin'}") 
paths.append(f"{'LIB directory':25}  |  {'add to LD_LIBRARY_PATH':40}  |  {installdir_full+'/lib64'}") 
paths.append(f"{'LIB file':25}  |  {'save to an environment variable (ex.DFTB_LIB)':40}  |  {installdir_full+'/lib64/libdftbplus.so'}") 
paths.append(f"{'PYTHON API & ASE file':25}  |  {'add to PYTHONPATH':40}  |  {installdir_full+'/python3.8/site-packages'}")
paths.append(f"SLAKOS FILES")
paths.append(f"https://dftb.org/parameters/download/all-sk-files")


logfile.write('SHOWING IMPORTANT PATHS'+'\n')
for p in paths:
    logfile.write(p+'\n')
    print(p)

logfile.close()


