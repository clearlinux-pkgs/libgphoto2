#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : libgphoto2
Version  : 2.5.30
Release  : 35
URL      : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.30/libgphoto2-2.5.30.tar.xz
Source0  : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.30/libgphoto2-2.5.30.tar.xz
Source1  : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.30/libgphoto2-2.5.30.tar.xz.asc
Summary  : Library for easy access to digital cameras
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
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
libgphoto2 2.5.29 release
general:
* fixes build failures of libgphoto2 frontends and builds using the
wrong libgphoto2 headers (issue #717)

%package bin
Summary: bin components for the libgphoto2 package.
Group: Binaries
Requires: libgphoto2-data = %{version}-%{release}
Requires: libgphoto2-license = %{version}-%{release}
Requires: libgphoto2-filemap = %{version}-%{release}

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


%package doc
Summary: doc components for the libgphoto2 package.
Group: Documentation

%description doc
doc components for the libgphoto2 package.


%package filemap
Summary: filemap components for the libgphoto2 package.
Group: Default

%description filemap
filemap components for the libgphoto2 package.


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
%setup -q -n libgphoto2-2.5.30
cd %{_builddir}/libgphoto2-2.5.30
pushd ..
cp -a libgphoto2-2.5.30 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664295396
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
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1664295396
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgphoto2
cp %{_builddir}/libgphoto2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libgphoto2/b58e72a0ebf963edaf5a2080c87bd2977d634bec
cp %{_builddir}/libgphoto2-%{version}/camlibs/konica/COPYING %{buildroot}/usr/share/package-licenses/libgphoto2/c5b09578f14b2217fb4da494d2eddff60f9991db
cp %{_builddir}/libgphoto2-%{version}/camlibs/minolta/dimagev/COPYING %{buildroot}/usr/share/package-licenses/libgphoto2/4c1641cf299b15191aa58b0f707ce430454d9a56
cp %{_builddir}/libgphoto2-%{version}/camlibs/stv0680/LICENCE %{buildroot}/usr/share/package-licenses/libgphoto2/183e5621272b24b44444a6d7afc9452ddbab2900
cp %{_builddir}/libgphoto2-%{version}/libgphoto2_port/COPYING.LIB %{buildroot}/usr/share/package-licenses/libgphoto2/e232665954c3f0f10d5c3ee4264b5a7d881d273d
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang libgphoto2-6
%find_lang libgphoto2_port-12
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/libgphoto2/2.5.30/konica/english
/usr/share/libgphoto2/2.5.30/konica/french
/usr/share/libgphoto2/2.5.30/konica/german
/usr/share/libgphoto2/2.5.30/konica/japanese
/usr/share/libgphoto2/2.5.30/konica/korean
/usr/share/libgphoto2/2.5.30/konica/spanish
/usr/share/libgphoto2_port/0.12.1/vcamera/README.txt

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
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2.so.6.3.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2_port.so.12
/usr/lib64/glibc-hwcaps/x86-64-v3/libgphoto2_port.so.12.1.0
/usr/lib64/libgphoto2.so.6
/usr/lib64/libgphoto2.so.6.3.0
/usr/lib64/libgphoto2/2.5.30/ax203.so
/usr/lib64/libgphoto2/2.5.30/canon.so
/usr/lib64/libgphoto2/2.5.30/digigr8.so
/usr/lib64/libgphoto2/2.5.30/dimagev.so
/usr/lib64/libgphoto2/2.5.30/directory.so
/usr/lib64/libgphoto2/2.5.30/docupen.so
/usr/lib64/libgphoto2/2.5.30/jl2005a.so
/usr/lib64/libgphoto2/2.5.30/jl2005c.so
/usr/lib64/libgphoto2/2.5.30/kodak_dc240.so
/usr/lib64/libgphoto2/2.5.30/lumix.so
/usr/lib64/libgphoto2/2.5.30/mars.so
/usr/lib64/libgphoto2/2.5.30/pentax.so
/usr/lib64/libgphoto2/2.5.30/ptp2.so
/usr/lib64/libgphoto2/2.5.30/ricoh_g3.so
/usr/lib64/libgphoto2/2.5.30/sierra.so
/usr/lib64/libgphoto2/2.5.30/sonix.so
/usr/lib64/libgphoto2/2.5.30/sq905.so
/usr/lib64/libgphoto2/2.5.30/st2205.so
/usr/lib64/libgphoto2/2.5.30/topfield.so
/usr/lib64/libgphoto2/2.5.30/tp6801.so
/usr/lib64/libgphoto2_port.so.12
/usr/lib64/libgphoto2_port.so.12.1.0
/usr/lib64/libgphoto2_port/0.12.1/disk.so
/usr/lib64/libgphoto2_port/0.12.1/ptpip.so
/usr/lib64/libgphoto2_port/0.12.1/serial.so
/usr/lib64/libgphoto2_port/0.12.1/usb1.so
/usr/lib64/libgphoto2_port/0.12.1/usbdiskdirect.so
/usr/lib64/libgphoto2_port/0.12.1/usbscsi.so
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgphoto2/183e5621272b24b44444a6d7afc9452ddbab2900
/usr/share/package-licenses/libgphoto2/4c1641cf299b15191aa58b0f707ce430454d9a56
/usr/share/package-licenses/libgphoto2/b58e72a0ebf963edaf5a2080c87bd2977d634bec
/usr/share/package-licenses/libgphoto2/c5b09578f14b2217fb4da494d2eddff60f9991db
/usr/share/package-licenses/libgphoto2/e232665954c3f0f10d5c3ee4264b5a7d881d273d

%files locales -f libgphoto2-6.lang -f libgphoto2_port-12.lang
%defattr(-,root,root,-)

