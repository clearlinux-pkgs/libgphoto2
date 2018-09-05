#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : libgphoto2
Version  : 2.5.19
Release  : 12
URL      : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.19/libgphoto2-2.5.19.tar.bz2
Source0  : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.19/libgphoto2-2.5.19.tar.bz2
Source99 : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.19/libgphoto2-2.5.19.tar.bz2.asc
Summary  : Software for accessing digital cameras
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: libgphoto2-bin
Requires: libgphoto2-lib
Requires: libgphoto2-license
Requires: libgphoto2-data
Requires: libgphoto2-locales
BuildRequires : bison
BuildRequires : buildreq-qmake
BuildRequires : flex
BuildRequires : libexif-dev
BuildRequires : libgd-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libusb-dev
BuildRequires : libxml2-dev

%description
The gPhoto2 project is a universal, free application and library
framework that lets you download images from several different
digital camera models, including the newer models with USB
connections. Note that
a) for some older camera models you must use the old "gphoto" package.
b) for USB mass storage models you must use the driver in the kernel

This libgphoto2 package contains only the library that digital 
camera applications can use.

Frontend like the command-line utility gphoto2 and other (GUI)
frontends are available seperately.

%package bin
Summary: bin components for the libgphoto2 package.
Group: Binaries
Requires: libgphoto2-data
Requires: libgphoto2-license

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
Requires: libgphoto2-lib
Requires: libgphoto2-bin
Requires: libgphoto2-data
Provides: libgphoto2-devel

%description dev
dev components for the libgphoto2 package.


%package doc
Summary: doc components for the libgphoto2 package.
Group: Documentation

%description doc
doc components for the libgphoto2 package.


%package lib
Summary: lib components for the libgphoto2 package.
Group: Libraries
Requires: libgphoto2-data
Requires: libgphoto2-license

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
%setup -q -n libgphoto2-2.5.19
pushd ..
cp -a libgphoto2-2.5.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536134084
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536134084
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libgphoto2
cp COPYING %{buildroot}/usr/share/doc/libgphoto2/COPYING
cp camlibs/konica/COPYING %{buildroot}/usr/share/doc/libgphoto2/camlibs_konica_COPYING
cp camlibs/minolta/dimagev/COPYING %{buildroot}/usr/share/doc/libgphoto2/camlibs_minolta_dimagev_COPYING
cp camlibs/stv0680/LICENCE %{buildroot}/usr/share/doc/libgphoto2/camlibs_stv0680_LICENCE
cp libgphoto2_port/COPYING.LIB %{buildroot}/usr/share/doc/libgphoto2/libgphoto2_port_COPYING.LIB
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
%find_lang libgphoto2-6
%find_lang libgphoto2_port-12

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
/usr/share/libgphoto2/2.5.19/konica/english
/usr/share/libgphoto2/2.5.19/konica/french
/usr/share/libgphoto2/2.5.19/konica/german
/usr/share/libgphoto2/2.5.19/konica/japanese
/usr/share/libgphoto2/2.5.19/konica/korean
/usr/share/libgphoto2/2.5.19/konica/spanish
/usr/share/libgphoto2_port/0.12.0/vcamera/README.txt

%files dev
%defattr(-,root,root,-)
/usr/include/gphoto2/gphoto2
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
/usr/lib64/haswell/libgphoto2.so
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libgphoto2.so.6
/usr/lib64/haswell/libgphoto2.so.6.1.0
/usr/lib64/libgphoto2.so.6
/usr/lib64/libgphoto2.so.6.1.0
/usr/lib64/libgphoto2/2.5.19/adc65.so
/usr/lib64/libgphoto2/2.5.19/agfa_cl20.so
/usr/lib64/libgphoto2/2.5.19/aox.so
/usr/lib64/libgphoto2/2.5.19/ax203.so
/usr/lib64/libgphoto2/2.5.19/barbie.so
/usr/lib64/libgphoto2/2.5.19/canon.so
/usr/lib64/libgphoto2/2.5.19/casio_qv.so
/usr/lib64/libgphoto2/2.5.19/clicksmart310.so
/usr/lib64/libgphoto2/2.5.19/digigr8.so
/usr/lib64/libgphoto2/2.5.19/digita.so
/usr/lib64/libgphoto2/2.5.19/dimagev.so
/usr/lib64/libgphoto2/2.5.19/dimera3500.so
/usr/lib64/libgphoto2/2.5.19/directory.so
/usr/lib64/libgphoto2/2.5.19/enigma13.so
/usr/lib64/libgphoto2/2.5.19/fuji.so
/usr/lib64/libgphoto2/2.5.19/gsmart300.so
/usr/lib64/libgphoto2/2.5.19/haswell/adc65.so
/usr/lib64/libgphoto2/2.5.19/haswell/agfa_cl20.so
/usr/lib64/libgphoto2/2.5.19/haswell/aox.so
/usr/lib64/libgphoto2/2.5.19/haswell/ax203.so
/usr/lib64/libgphoto2/2.5.19/haswell/barbie.so
/usr/lib64/libgphoto2/2.5.19/haswell/canon.so
/usr/lib64/libgphoto2/2.5.19/haswell/casio_qv.so
/usr/lib64/libgphoto2/2.5.19/haswell/clicksmart310.so
/usr/lib64/libgphoto2/2.5.19/haswell/digigr8.so
/usr/lib64/libgphoto2/2.5.19/haswell/digita.so
/usr/lib64/libgphoto2/2.5.19/haswell/dimagev.so
/usr/lib64/libgphoto2/2.5.19/haswell/dimera3500.so
/usr/lib64/libgphoto2/2.5.19/haswell/directory.so
/usr/lib64/libgphoto2/2.5.19/haswell/enigma13.so
/usr/lib64/libgphoto2/2.5.19/haswell/fuji.so
/usr/lib64/libgphoto2/2.5.19/haswell/gsmart300.so
/usr/lib64/libgphoto2/2.5.19/haswell/hp215.so
/usr/lib64/libgphoto2/2.5.19/haswell/iclick.so
/usr/lib64/libgphoto2/2.5.19/haswell/jamcam.so
/usr/lib64/libgphoto2/2.5.19/haswell/jd11.so
/usr/lib64/libgphoto2/2.5.19/haswell/jl2005a.so
/usr/lib64/libgphoto2/2.5.19/haswell/jl2005c.so
/usr/lib64/libgphoto2/2.5.19/haswell/kodak_dc120.so
/usr/lib64/libgphoto2/2.5.19/haswell/kodak_dc210.so
/usr/lib64/libgphoto2/2.5.19/haswell/kodak_dc240.so
/usr/lib64/libgphoto2/2.5.19/haswell/kodak_dc3200.so
/usr/lib64/libgphoto2/2.5.19/haswell/kodak_ez200.so
/usr/lib64/libgphoto2/2.5.19/haswell/konica.so
/usr/lib64/libgphoto2/2.5.19/haswell/konica_qm150.so
/usr/lib64/libgphoto2/2.5.19/haswell/largan.so
/usr/lib64/libgphoto2/2.5.19/haswell/lg_gsm.so
/usr/lib64/libgphoto2/2.5.19/haswell/mars.so
/usr/lib64/libgphoto2/2.5.19/haswell/mustek.so
/usr/lib64/libgphoto2/2.5.19/haswell/panasonic_coolshot.so
/usr/lib64/libgphoto2/2.5.19/haswell/panasonic_dc1000.so
/usr/lib64/libgphoto2/2.5.19/haswell/panasonic_dc1580.so
/usr/lib64/libgphoto2/2.5.19/haswell/panasonic_l859.so
/usr/lib64/libgphoto2/2.5.19/haswell/pccam300.so
/usr/lib64/libgphoto2/2.5.19/haswell/pccam600.so
/usr/lib64/libgphoto2/2.5.19/haswell/pentax.so
/usr/lib64/libgphoto2/2.5.19/haswell/polaroid_pdc320.so
/usr/lib64/libgphoto2/2.5.19/haswell/polaroid_pdc640.so
/usr/lib64/libgphoto2/2.5.19/haswell/polaroid_pdc700.so
/usr/lib64/libgphoto2/2.5.19/haswell/ptp2.so
/usr/lib64/libgphoto2/2.5.19/haswell/ricoh.so
/usr/lib64/libgphoto2/2.5.19/haswell/ricoh_g3.so
/usr/lib64/libgphoto2/2.5.19/haswell/samsung.so
/usr/lib64/libgphoto2/2.5.19/haswell/sierra.so
/usr/lib64/libgphoto2/2.5.19/haswell/sipix_blink2.so
/usr/lib64/libgphoto2/2.5.19/haswell/sipix_web2.so
/usr/lib64/libgphoto2/2.5.19/haswell/smal.so
/usr/lib64/libgphoto2/2.5.19/haswell/sonix.so
/usr/lib64/libgphoto2/2.5.19/haswell/sony_dscf1.so
/usr/lib64/libgphoto2/2.5.19/haswell/sony_dscf55.so
/usr/lib64/libgphoto2/2.5.19/haswell/soundvision.so
/usr/lib64/libgphoto2/2.5.19/haswell/spca50x.so
/usr/lib64/libgphoto2/2.5.19/haswell/sq905.so
/usr/lib64/libgphoto2/2.5.19/haswell/st2205.so
/usr/lib64/libgphoto2/2.5.19/haswell/stv0674.so
/usr/lib64/libgphoto2/2.5.19/haswell/stv0680.so
/usr/lib64/libgphoto2/2.5.19/haswell/sx330z.so
/usr/lib64/libgphoto2/2.5.19/haswell/topfield.so
/usr/lib64/libgphoto2/2.5.19/haswell/toshiba_pdrm11.so
/usr/lib64/libgphoto2/2.5.19/haswell/tp6801.so
/usr/lib64/libgphoto2/2.5.19/hp215.so
/usr/lib64/libgphoto2/2.5.19/iclick.so
/usr/lib64/libgphoto2/2.5.19/jamcam.so
/usr/lib64/libgphoto2/2.5.19/jd11.so
/usr/lib64/libgphoto2/2.5.19/jl2005a.so
/usr/lib64/libgphoto2/2.5.19/jl2005c.so
/usr/lib64/libgphoto2/2.5.19/kodak_dc120.so
/usr/lib64/libgphoto2/2.5.19/kodak_dc210.so
/usr/lib64/libgphoto2/2.5.19/kodak_dc240.so
/usr/lib64/libgphoto2/2.5.19/kodak_dc3200.so
/usr/lib64/libgphoto2/2.5.19/kodak_ez200.so
/usr/lib64/libgphoto2/2.5.19/konica.so
/usr/lib64/libgphoto2/2.5.19/konica_qm150.so
/usr/lib64/libgphoto2/2.5.19/largan.so
/usr/lib64/libgphoto2/2.5.19/lg_gsm.so
/usr/lib64/libgphoto2/2.5.19/mars.so
/usr/lib64/libgphoto2/2.5.19/mustek.so
/usr/lib64/libgphoto2/2.5.19/panasonic_coolshot.so
/usr/lib64/libgphoto2/2.5.19/panasonic_dc1000.so
/usr/lib64/libgphoto2/2.5.19/panasonic_dc1580.so
/usr/lib64/libgphoto2/2.5.19/panasonic_l859.so
/usr/lib64/libgphoto2/2.5.19/pccam300.so
/usr/lib64/libgphoto2/2.5.19/pccam600.so
/usr/lib64/libgphoto2/2.5.19/pentax.so
/usr/lib64/libgphoto2/2.5.19/polaroid_pdc320.so
/usr/lib64/libgphoto2/2.5.19/polaroid_pdc640.so
/usr/lib64/libgphoto2/2.5.19/polaroid_pdc700.so
/usr/lib64/libgphoto2/2.5.19/ptp2.so
/usr/lib64/libgphoto2/2.5.19/ricoh.so
/usr/lib64/libgphoto2/2.5.19/ricoh_g3.so
/usr/lib64/libgphoto2/2.5.19/samsung.so
/usr/lib64/libgphoto2/2.5.19/sierra.so
/usr/lib64/libgphoto2/2.5.19/sipix_blink2.so
/usr/lib64/libgphoto2/2.5.19/sipix_web2.so
/usr/lib64/libgphoto2/2.5.19/smal.so
/usr/lib64/libgphoto2/2.5.19/sonix.so
/usr/lib64/libgphoto2/2.5.19/sony_dscf1.so
/usr/lib64/libgphoto2/2.5.19/sony_dscf55.so
/usr/lib64/libgphoto2/2.5.19/soundvision.so
/usr/lib64/libgphoto2/2.5.19/spca50x.so
/usr/lib64/libgphoto2/2.5.19/sq905.so
/usr/lib64/libgphoto2/2.5.19/st2205.so
/usr/lib64/libgphoto2/2.5.19/stv0674.so
/usr/lib64/libgphoto2/2.5.19/stv0680.so
/usr/lib64/libgphoto2/2.5.19/sx330z.so
/usr/lib64/libgphoto2/2.5.19/topfield.so
/usr/lib64/libgphoto2/2.5.19/toshiba_pdrm11.so
/usr/lib64/libgphoto2/2.5.19/tp6801.so
/usr/lib64/libgphoto2_port.so.12
/usr/lib64/libgphoto2_port.so.12.0.0
/usr/lib64/libgphoto2_port/0.12.0/disk.so
/usr/lib64/libgphoto2_port/0.12.0/haswell/disk.so
/usr/lib64/libgphoto2_port/0.12.0/haswell/ptpip.so
/usr/lib64/libgphoto2_port/0.12.0/haswell/serial.so
/usr/lib64/libgphoto2_port/0.12.0/haswell/usb1.so
/usr/lib64/libgphoto2_port/0.12.0/haswell/usbdiskdirect.so
/usr/lib64/libgphoto2_port/0.12.0/haswell/usbscsi.so
/usr/lib64/libgphoto2_port/0.12.0/ptpip.so
/usr/lib64/libgphoto2_port/0.12.0/serial.so
/usr/lib64/libgphoto2_port/0.12.0/usb1.so
/usr/lib64/libgphoto2_port/0.12.0/usbdiskdirect.so
/usr/lib64/libgphoto2_port/0.12.0/usbscsi.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/libgphoto2/COPYING
/usr/share/doc/libgphoto2/camlibs_konica_COPYING
/usr/share/doc/libgphoto2/camlibs_minolta_dimagev_COPYING
/usr/share/doc/libgphoto2/libgphoto2_port_COPYING.LIB

%files locales -f libgphoto2-6.lang -f libgphoto2_port-12.lang
%defattr(-,root,root,-)

