
1. Download https://www.tddft.org/programs/libxc/download/
2. untar `tar zxvf libxc*`
3. go to folder `cd libxc*`
4. 
```bash
cmake -H. -Bobjdir -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX="./installation" -DCMAKE_C_COMPILER=icc -DCMAKE_C_FLAGS="-O2 -fPIC" | tee out_1.log
cd objdir
make -j | tee out_2.log
make -j2 test | tee out_3.log
make install
```