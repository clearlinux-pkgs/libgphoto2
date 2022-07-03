#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : libgphoto2
Version  : 2.5.29
Release  : 30
URL      : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.29/libgphoto2-2.5.29.tar.xz
Source0  : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.29/libgphoto2-2.5.29.tar.xz
Source1  : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.29/libgphoto2-2.5.29.tar.xz.asc
Summary  : Library for easy access to digital cameras
Group    : Development/Tools
License  : GPL-2.0
Requires: libgphoto2-bin = %{version}-%{release}
Requires: libgphoto2-data = %{version}-%{release}
Requires: libgphoto2-filemap = %{version}-%{release}
Requires: libgphoto2-lib = %{version}-%{release}
Requires: libgphoto2-license = %{version}-%{release}
Requires: libgphoto2-locales = %{version}-%{release}
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : gettext
BuildRequires : graphviz
BuildRequires : libexif-dev
BuildRequires : libgd-dev
BuildRequires : libusb-dev
BuildRequires : libxml2-dev
BuildRequires : perl(XML::Parser)
BuildRequires : sed

%description
libgphoto2 2.5.28 release
general:
* OS/2 support removed (broken and unused since at least 2006)
* remove built-in rpm packaging (use distro packaging instead)
* remove linux-hotplug rule creation (removed from distros around 2006)
* remaining text which was iso-8859 is UTF-8 now (except one po file)
* To override docdir and htmldir, use configure arguments --docdir=
and --htmldir= instead of --with-doc-dir= and --with-html-dir=
* some code cleanups, especially handling of include files and i18n handling

%package bin
Summary: bin components for the libgphoto2 package.
Group: Binaries
Requires: libgphoto2-data = %{version}-%{release}
Requires: libgphoto2-license = %{version}-%{release}

%description bin
bin components for the libgphoto2 package.


%package data
Summary: data components for the libgphoto2 package.
Group: Data

%description data
data components for the libgphoto2 package.


%package dev
Summary: dev components for the libgphoto2 package.
Group: Development
Requires: libgphoto2-lib = %{version}-%{release}
Requires: libgphoto2-bin = %{version}-%{release}
Requires: libgphoto2-data = %{version}-%{release}
Provides: libgphoto2-devel = %{version}-%{release}
Requires: libgphoto2 = %{version}-%{release}

%description dev
dev components for the libgphoto2 package.


%package filemap
Summary: filemap components for the octave package.
Group: Default

%description filemap
filemap components for the octave package.


%package doc
Summary: doc components for the libgphoto2 package.
Group: Documentation

%description doc
doc components for the libgphoto2 package.


%package lib
Summary: lib components for the libgphoto2 package.
Group: Libraries
Requires: libgphoto2-data = %{version}-%{release}
Requires: libgphoto2-license = %{version}-%{release}
Requires: libgphoto2-filemap = %{version}-%{release}

%description lib
lib components for the libgphoto2 package.


%package license
Summary: license components for the libgphoto2 package.
Group: Default

%description license
license components for the libgphoto2 package.


%package locales
Summary: locales components for the libgphoto2 package.
Group: Default

%description locales
locales components for the libgphoto2 package.


%prep
%setup -q -n libgphoto2-2.5.29
cd %{_builddir}/libgphoto2-2.5.29
pushd ..
cp -a libgphoto2-2.5.29 buildavx2
popd
pushd ..
cp -a libgphoto2-2.5.29 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656130449
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656130449
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgphoto2
cp %{_builddir}/libgphoto2-2.5.29/camlibs/konica/COPYING %{buildroot}/usr/share/package-licenses/libgphoto2/c5b09578f14b2217fb4da494d2eddff60f9991db
cp %{_builddir}/libgphoto2-2.5.29/camlibs/minolta/dimagev/COPYING %{buildroot}/usr/share/package-licenses/libgphoto2/4c1641cf299b15191aa58b0f707ce430454d9a56
cp %{_builddir}/libgphoto2-2.5.29/camlibs/stv0680/LICENCE %{buildroot}/usr/share/package-licenses/libgphoto2/183e5621272b24b44444a6d7afc9452ddbab2900
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
%find_lang libgphoto2-6
%find_lang libgphoto2_port-12
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/libgphoto2/print-camera-list
/usr/lib64/udev/check-ptp-camera

%files bin
%defattr(-,root,root,-)
/usr/bin/gphoto2-config
/usr/bin/gphoto2-port-config

%files data
%defattr(-,root,root,-)
/usr/share/libgphoto2/2.5.29/konica/english
/usr/share/libgphoto2/2.5.29/konica/french
/usr/share/libgphoto2/2.5.29/konica/german
/usr/share/libgphoto2/2.5.29/konica/japanese
/usr/share/libgphoto2/2.5.29/konica/korean
/usr/share/libgphoto2/2.5.29/konica/spanish
/usr/share/libgphoto2_port/0.12.0/vcamera/README.txt

%files dev
%defattr(-,root,root,-)
/usr/include/gphoto2/gphoto2-abilities-list.h
/usr/include/gphoto2/gphoto2-camera.h
/usr/include/gphoto2/gphoto2-context.h
/usr/include/gphoto2/gphoto2-file.h
/usr/include/gphoto2/gphoto2-filesys.h
/usr/include/gphoto2/gphoto2-library.h
/usr/include/gphoto2/gphoto2-list.h
/usr/include/gphoto2/gphoto2-port-info-list.h
/usr/include/gphoto2/gphoto2-port-log.h
/usr/include/gphoto2/gphoto2-port-portability.h
/usr/include/gphoto2/gphoto2-port-result.h
/usr/include/gphoto2/gphoto2-port-version.h
/usr/include/gphoto2/gphoto2-port.h
/usr/include/gphoto2/gphoto2-result.h
/usr/include/gphoto2/gphoto2-setting.h
/usr/include/gphoto2/gphoto2-version.h
/usr/include/gphoto2/gphoto2-widget.h
/usr/include/gphoto2/gphoto2.h
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2_port.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libgphoto2.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libgphoto2_port.so
/usr/lib64/libgphoto2.so
/usr/lib64/libgphoto2_port.so
/usr/lib64/pkgconfig/libgphoto2.pc
/usr/lib64/pkgconfig/libgphoto2_port.pc
/usr/share/man/man3/libgphoto2.3
/usr/share/man/man3/libgphoto2_port.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libgphoto2/*
/usr/share/doc/libgphoto2_port/AUTHORS
/usr/share/doc/libgphoto2_port/NEWS
/usr/share/doc/libgphoto2_port/README

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libgphoto2

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2.so.6
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2.so.6.2.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2_port.so.12
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2_port.so.12.0.0
/usr/lib64/glibc-hwcaps/x86-64-v4/libgphoto2.so.6
/usr/lib64/glibc-hwcaps/x86-64-v4/libgphoto2.so.6.2.0
/usr/lib64/glibc-hwcaps/x86-64-v4/libgphoto2_port.so.12
/usr/lib64/glibc-hwcaps/x86-64-v4/libgphoto2_port.so.12.0.0
/usr/lib64/libgphoto2.so.6
/usr/lib64/libgphoto2.so.6.2.0
/usr/lib64/libgphoto2/2.5.29/ax203.so
/usr/lib64/libgphoto2/2.5.29/canon.so
/usr/lib64/libgphoto2/2.5.29/digigr8.so
/usr/lib64/libgphoto2/2.5.29/dimagev.so
/usr/lib64/libgphoto2/2.5.29/directory.so
/usr/lib64/libgphoto2/2.5.29/docupen.so
/usr/lib64/libgphoto2/2.5.29/jl2005a.so
/usr/lib64/libgphoto2/2.5.29/jl2005c.so
/usr/lib64/libgphoto2/2.5.29/kodak_dc240.so
/usr/lib64/libgphoto2/2.5.29/lumix.so
/usr/lib64/libgphoto2/2.5.29/mars.so
/usr/lib64/libgphoto2/2.5.29/pentax.so
/usr/lib64/libgphoto2/2.5.29/ptp2.so
/usr/lib64/libgphoto2/2.5.29/ricoh_g3.so
/usr/lib64/libgphoto2/2.5.29/sierra.so
/usr/lib64/libgphoto2/2.5.29/sonix.so
/usr/lib64/libgphoto2/2.5.29/sq905.so
/usr/lib64/libgphoto2/2.5.29/st2205.so
/usr/lib64/libgphoto2/2.5.29/topfield.so
/usr/lib64/libgphoto2/2.5.29/tp6801.so
/usr/lib64/libgphoto2_port.so.12
/usr/lib64/libgphoto2_port.so.12.0.0
/usr/lib64/libgphoto2_port/0.12.0/disk.so
/usr/lib64/libgphoto2_port/0.12.0/ptpip.so
/usr/lib64/libgphoto2_port/0.12.0/serial.so
/usr/lib64/libgphoto2_port/0.12.0/usb1.so
/usr/lib64/libgphoto2_port/0.12.0/usbdiskdirect.so
/usr/lib64/libgphoto2_port/0.12.0/usbscsi.so
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgphoto2/183e5621272b24b44444a6d7afc9452ddbab2900
/usr/share/package-licenses/libgphoto2/4c1641cf299b15191aa58b0f707ce430454d9a56
/usr/share/package-licenses/libgphoto2/c5b09578f14b2217fb4da494d2eddff60f9991db

%files locales -f libgphoto2-6.lang -f libgphoto2_port-12.lang
%defattr(-,root,root,-)

