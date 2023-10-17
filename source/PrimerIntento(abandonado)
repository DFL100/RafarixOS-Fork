//0.-Preparativos para comenzar con LFS

usuario@ubuntu18:~$ su
Contraseña: 
root@ubuntu18:/home/usuario# echo $LFS

root@ubuntu18:/home/usuario# export LFS=/mnt/lfs
root@ubuntu18:/home/usuario# export LFS=/mnt/lfs
root@ubuntu18:/home/usuario# echo $LFS
/mnt/lfs
root@ubuntu18:/home/usuario# mkdir -pv $LFS/{bin,etc,lib,sbin,usr,var}
mkdir: se ha creado el directorio '/mnt/lfs/bin'
mkdir: se ha creado el directorio '/mnt/lfs/etc'
mkdir: se ha creado el directorio '/mnt/lfs/lib'
mkdir: se ha creado el directorio '/mnt/lfs/sbin'
mkdir: se ha creado el directorio '/mnt/lfs/usr'
mkdir: se ha creado el directorio '/mnt/lfs/var'
root@ubuntu18:/home/usuario# mkdir -pv $LFS/{bin,etc,lib,sbin,usr,var}
root@ubuntu18:/home/usuario# case $(uname -m) in
> x86_64) mkdir -pv $LFS/lib64 ;;
> esac
mkdir: se ha creado el directorio '/mnt/lfs/lib64'
root@ubuntu18:/home/usuario# mkdir -v $LFS/tools
mkdir: se ha creado el directorio '/mnt/lfs/tools'
root@ubuntu18:/home/usuario# groupadd lfs
root@ubuntu18:/home/usuario# useradd -s /bin/bash -g lfs -m -k /dev/null lfs
root@ubuntu18:/home/usuario# passwd lfs
Introduzca la nueva contraseña de UNIX: 
Vuelva a escribir la nueva contraseña de UNIX: 
passwd: contraseña actualizada correctamente
root@ubuntu18:/home/usuario# chown -v lfs 
chown: falta un operando después de «lfs»
Pruebe 'chown --help' para más información.
root@ubuntu18:/home/usuario# $LFS/{usr,lib,var,etc,bin,sbin,tools}
bash: /mnt/lfs/usr: Es un directorio
root@ubuntu18:/home/usuario# case $(uname -m) in
>  x86_64) chown -v lfs $LFS/lib64 ;;
> esac
cambiado el propietario de '/mnt/lfs/lib64' de root a lfs
root@ubuntu18:/home/usuario# chown -v lfs $LFS/sources
cambiado el propietario de '/mnt/lfs/sources' de root a lfs
root@ubuntu18:/home/usuario# su - lfs

//0.1.Preparamos todo para compilar todos los paquetes

lfs@ubuntu18:~$ cat > ~/.bash_profile << "EOF"
> exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w$ ' /bin/bash
> EOF
lfs@ubuntu18:~$ cat > ~/.bashrc << "EOF"
> set +h
> umask 022
> LFS=/mnt/lfs
> LC_ALL=POSIX
> LFS_TGT=$(uname -m)-lfs-linux-gnu
> PATH=/usr/bin
> if [ ! -L /bin ]; then PATH=/bin:$PATH; fi
> PATH=$LFS/tools/bin:$PATH
> CONFIG_SITE=$LFS/usr/share/config.site
> export LFS LC_ALL LFS_TGT PATH CONFIG_SITE
> EOF
lfs@ubuntu18:~$ source ~/.bash_profile
lfs@ubuntu18:~$ echo $LFS
/mnt/lfs
lfs@ubuntu18:~$ echo $LC_ALL
POSIX
lfs@ubuntu18:~$ echo $LFS_TGT
x86_64-lfs-linux-gnu
lfs@ubuntu18:~$ echo $PATH
/mnt/lfs/tools/bin:/bin:/usr/bin

//1.-Compilación cruzada de herramientas temporales.

lfs@ubuntu18:~$ echo $LFS
/mnt/lfs
lfs@ubuntu18:~$ echo $LC_ALL
POSIX
lfs@ubuntu18:~$ echo $LFS_TGT
x86_64-lfs-linux-gnu
lfs@ubuntu18:~$ echo $PATH
/mnt/lfs/tools/bin:/bin:/usr/bin
lfs@ubuntu18:~$ cd $LFS/sources

//1.1.Descomprimir paquetes previamente creados

lfs@ubuntu18:/mnt/lfs/sources$ tar -xf binutils-2.36.1.tar.xz
lfs@ubuntu18:/mnt/lfs/sources$ cd binutils-2.36.1
lfs@ubuntu18:/mnt/lfs/sources/binutils-2.36.1$ mkdir -v build 
mkdir: created directory 'build'
lfs@ubuntu18:/mnt/lfs/sources/binutils-2.36.1$ cd build

//1.1.1.Preparación para compilar

[Compilation1.2](https://github.com/xoanxc/RafarixOS/blob/main/source/compilations/compilation-1.2.)

//1.1.2.Instalación de paquetes

lfs@ubuntu18:/mnt/lfs/sources/binutils-2.36.1/build$ make install
make[1]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build'
/bin/sh ../mkinstalldirs /mnt/lfs/tools /mnt/lfs/tools
make[2]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
make  install-recursive
make[3]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
Making install in doc
make[4]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd/doc'
 /bin/mkdir -p '/mnt/lfs/tools/share/info'
/bin/mkdir: cannot create directory '/mnt/lfs/tools/share': Permission denied
Makefile:824: recipe for target 'install-info-am' failed
make[4]: *** [install-info-am] Error 1
make[4]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd/doc'
Makefile:1643: recipe for target 'install-recursive' failed
make[3]: *** [install-recursive] Error 1
make[3]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
Makefile:1751: recipe for target 'install' failed
make[2]: *** [install] Error 2
make[2]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
Makefile:2833: recipe for target 'install-bfd' failed
make[1]: *** [install-bfd] Error 2
make[1]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build'
Makefile:2288: recipe for target 'install' failed
make: *** [install] Error 2
lfs@ubuntu18:/mnt/lfs/sources/binutils-2.36.1/build$ make install
make[1]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build'
/bin/sh ../mkinstalldirs /mnt/lfs/tools /mnt/lfs/tools
make[2]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
make  install-recursive
make[3]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
Making install in doc
make[4]: Entering directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd/doc'
 /bin/mkdir -p '/mnt/lfs/tools/share/info'
/bin/mkdir: cannot create directory '/mnt/lfs/tools/share': Permission denied
Makefile:824: recipe for target 'install-info-am' failed
make[4]: *** [install-info-am] Error 1
make[4]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd/doc'
Makefile:1643: recipe for target 'install-recursive' failed
make[3]: *** [install-recursive] Error 1
make[3]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
Makefile:1751: recipe for target 'install' failed
make[2]: *** [install] Error 2
make[2]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build/bfd'
Makefile:2833: recipe for target 'install-bfd' failed
make[1]: *** [install-bfd] Error 2
make[1]: Leaving directory '/mnt/lfs/sources/binutils-2.36.1/build'
Makefile:2288: recipe for target 'install' failed
make: *** [install] Error 2

//1.3.1.Eliminar Carpeta binultis

lfs@ubuntu18:/home/usuario$ cd ../..
lfs@ubuntu18:/$ pwd
/
lfs@ubuntu18:/$ cd mnt
lfs@ubuntu18:/mnt$ cd lfs
lfs@ubuntu18:/mnt/lfs$ cd sources
lfs@ubuntu18:/mnt/lfs/sources$ rm -rf binutils-2.36.1

//1.2.-GCC paso 1

lfs@ubuntu18:/mnt/lfs/sources$ tar -xf gcc-10.2.0.tar.xz
lfs@ubuntu18:/mnt/lfs/sources$ cd gcc-10.2.0
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ tar -xf ../mpfr-4.1.0.tar.xz
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ mv -v mpfr-4.1.0 mpfr
renamed 'mpfr-4.1.0' -> 'mpfr'
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ tar -xf ../gmp-6.2.1.tar.xz
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ mv -v gmp-6.2.1 gmp
renamed 'gmp-6.2.1' -> 'gmp'
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ tar -xf ../mpc-1.2.1.tar.gz
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ mv -v mpc-1.2.1 mpc
renamed 'mpc-1.2.1' -> 'mpc'
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ case $(uname -m) in
>  x86_64)
> sed -e '/m64=/s/lib64/lib/' \
> -i.orig gcc/config/i386/t-linux64
> ;;
> esac
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ mkdir -v build
mkdir: created directory 'build'
lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0$ cd build

//1.2.1.GCC Compilación

lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0/build$ ../configure \
>  --target=$LFS_TGT \
>  --prefix=$LFS/tools \
>  --with-glibc-version=2.11 \
>  --with-sysroot=$LFS \
>  --with-newlib \
>  --without-headers \
>  --enable-initfini-array \
>  --disable-nls \
>  --disable-shared \
>  --disable-multilib \
>  --disable-decimal-float \
>  --disable-threads \
>  --disable-libatomic \
>  --disable-libgomp \
>  --disable-libquadmath \
>  --disable-libssp \
>  --disable-libvtv \
>  --disable-libstdcxx \
>  --enable-languages=c,c++
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking target system type... x86_64-lfs-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether ln works... yes
checking whether ln -s works... yes
checking for a sed that does not truncate output... /bin/sed
checking for gawk... gawk
checking for libitm support... yes
checking for libsanitizer support... yes
checking for libhsail-rt support... yes
checking for libphobos support... yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking whether g++ accepts -static-libstdc++ -static-libgcc... yes
checking for gnatbind... no
checking for gnatmake... no
checking whether compiler driver understands Ada... no
checking how to compare bootstrapped objects... cmp --ignore-initial=16 $$f1 $$f2
checking for objdir... .libs
checking for isl 0.15 or later... no
required isl version is 0.15 or later
*** This configuration is not supported in the following subdirectories:
     target-libquadmath target-libstdc++-v3 gnattools gotools target-libada target-libhsail-rt target-libphobos target-zlib target-libbacktrace target-libgfortran target-libgo target-libffi target-libobjc target-libgomp target-liboffloadmic target-libatomic target-libvtv target-libssp target-libitm target-libsanitizer
    (Any other directories should still work fine.)
checking for default BUILD_CONFIG... 
checking for --enable-vtable-verify... no
checking for bison... bison -y
checking for bison... bison
checking for gm4... no
checking for gnum4... no
checking for m4... m4
checking for flex... no
checking for lex... no
checking for flex... no
checking for makeinfo... makeinfo
checking for expect... no
checking for runtest... no
checking for ar... ar
checking for as... as
checking for dlltool... no
checking for ld... ld
checking for lipo... no
checking for nm... nm
checking for ranlib... ranlib
checking for strip... strip
checking for windres... no
checking for windmc... no
checking for objcopy... objcopy
checking for objdump... objdump
checking for otool... no
checking for readelf... readelf
checking for x86_64-lfs-linux-gnu-cc... no
checking for x86_64-lfs-linux-gnu-gcc... no
checking for x86_64-lfs-linux-gnu-c++... no
checking for x86_64-lfs-linux-gnu-g++... no
checking for x86_64-lfs-linux-gnu-cxx... no
checking for x86_64-lfs-linux-gnu-gxx... no
checking for x86_64-lfs-linux-gnu-gcc... no
checking for x86_64-lfs-linux-gnu-gfortran... no
checking for x86_64-lfs-linux-gnu-gccgo... no
checking for x86_64-lfs-linux-gnu-gdc... no
checking for ar... no
checking for x86_64-lfs-linux-gnu-ar... no
checking for as... no
checking for x86_64-lfs-linux-gnu-as... no
checking for dlltool... no
checking for x86_64-lfs-linux-gnu-dlltool... no
checking for ld... no
checking for x86_64-lfs-linux-gnu-ld... no
checking for lipo... no
checking for x86_64-lfs-linux-gnu-lipo... no
checking for nm... no
checking for x86_64-lfs-linux-gnu-nm... no
checking for objcopy... no
checking for x86_64-lfs-linux-gnu-objcopy... no
checking for objdump... no
checking for x86_64-lfs-linux-gnu-objdump... no
checking for otool... no
checking for x86_64-lfs-linux-gnu-otool... no
checking for ranlib... no
checking for x86_64-lfs-linux-gnu-ranlib... no
checking for readelf... no
checking for x86_64-lfs-linux-gnu-readelf... no
checking for strip... no
checking for x86_64-lfs-linux-gnu-strip... no
checking for windres... no
checking for x86_64-lfs-linux-gnu-windres... no
checking for windmc... no
checking for x86_64-lfs-linux-gnu-windmc... no
checking where to find the target ar... pre-installed
checking where to find the target as... pre-installed
checking where to find the target cc... just compiled
checking where to find the target c++... just compiled
checking where to find the target c++ for libstdc++... just compiled
checking where to find the target dlltool... pre-installed
checking where to find the target gcc... just compiled
checking where to find the target gfortran... pre-installed
checking where to find the target gccgo... pre-installed
checking where to find the target gdc... pre-installed
checking where to find the target ld... pre-installed
checking where to find the target lipo... pre-installed
checking where to find the target nm... pre-installed
checking where to find the target objcopy... pre-installed
checking where to find the target objdump... pre-installed
checking where to find the target otool... pre-installed
checking where to find the target ranlib... pre-installed
checking where to find the target readelf... pre-installed
checking where to find the target strip... pre-installed
checking where to find the target windres... pre-installed
checking where to find the target windmc... pre-installed
checking whether to enable maintainer-specific portions of Makefiles... no
configure: creating ./config.status
config.status: creating Makefile

//1.2.2.Compilación

[Compilation1.2](https://github.com/xoanxc/RafarixOS/blob/main/source/compilations/compilation-1.2.2)

//Instalación

lfs@ubuntu18:/mnt/lfs/sources/gcc-10.2.0/build$ make install
make[1]: Entering directory '/mnt/lfs/sources/gcc-10.2.0/build'
/bin/sh ../mkinstalldirs /mnt/lfs/tools /mnt/lfs/tools
make[2]: Entering directory '/mnt/lfs/sources/gcc-10.2.0/build/fixincludes'
rm -rf /mnt/lfs/tools/libexec/gcc/x86_64-lfs-linux-gnu/10.2.0/install-tools
/bin/sh ../../fixincludes/../mkinstalldirs /mnt/lfs/tools/libexec/gcc/x86_64-lfs-linux-gnu/10.2.0/install-tools
mkdir -p -- /mnt/lfs/tools/libexec/gcc/x86_64-lfs-linux-gnu/10.2.0/install-tools
mkdir: cannot create directory '/mnt/lfs/tools/libexec': Permission denied
Makefile:181: recipe for target 'install' failed
make[2]: *** [install] Error 1
make[2]: Leaving directory '/mnt/lfs/sources/gcc-10.2.0/build/fixincludes'
Makefile:3797: recipe for target 'install-fixincludes' failed
make[1]: *** [install-fixincludes] Error 2
make[1]: Leaving directory '/mnt/lfs/sources/gcc-10.2.0/build'
Makefile:2384: recipe for target 'install' failed
make: *** [install] Error 2

//Erorres varios, recontruccion en la forma de subir el codigo en el nuevo ejemplo.
