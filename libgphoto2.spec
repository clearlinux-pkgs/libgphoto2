#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2209D6902F969C95 (meissner@suse.de)
#
Name     : libgphoto2
Version  : 2.5.16
Release  : 4
URL      : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.16/libgphoto2-2.5.16.tar.bz2
Source0  : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.16/libgphoto2-2.5.16.tar.bz2
Source99 : https://sourceforge.net/projects/gphoto/files/libgphoto/2.5.16/libgphoto2-2.5.16.tar.bz2.asc
Summary  : Software for accessing digital cameras
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: libgphoto2-bin
Requires: libgphoto2-lib
Requires: libgphoto2-doc
Requires: libgphoto2-data
Requires: libgphoto2-locales
BuildRequires : bison
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

%description lib
lib components for the libgphoto2 package.


%package locales
Summary: locales components for the libgphoto2 package.
Group: Default

%description locales
locales components for the libgphoto2 package.


%prep
%setup -q -n libgphoto2-2.5.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509321686
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1509321686
rm -rf %{buildroot}
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
/usr/share/doc/libgphoto2_port/AUTHORS
/usr/share/doc/libgphoto2_port/NEWS
/usr/share/doc/libgphoto2_port/README
/usr/share/libgphoto2/2.5.16/konica/english
/usr/share/libgphoto2/2.5.16/konica/french
/usr/share/libgphoto2/2.5.16/konica/german
/usr/share/libgphoto2/2.5.16/konica/japanese
/usr/share/libgphoto2/2.5.16/konica/korean
/usr/share/libgphoto2/2.5.16/konica/spanish
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
/usr/lib64/libgphoto2.so
/usr/lib64/libgphoto2_port.so
/usr/lib64/pkgconfig/libgphoto2.pc
/usr/lib64/pkgconfig/libgphoto2_port.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libgphoto2/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgphoto2.so.6
/usr/lib64/libgphoto2.so.6.0.0
/usr/lib64/libgphoto2/2.5.16/adc65.so
/usr/lib64/libgphoto2/2.5.16/agfa_cl20.so
/usr/lib64/libgphoto2/2.5.16/aox.so
/usr/lib64/libgphoto2/2.5.16/ax203.so
/usr/lib64/libgphoto2/2.5.16/barbie.so
/usr/lib64/libgphoto2/2.5.16/canon.so
/usr/lib64/libgphoto2/2.5.16/casio_qv.so
/usr/lib64/libgphoto2/2.5.16/clicksmart310.so
/usr/lib64/libgphoto2/2.5.16/digigr8.so
/usr/lib64/libgphoto2/2.5.16/digita.so
/usr/lib64/libgphoto2/2.5.16/dimagev.so
/usr/lib64/libgphoto2/2.5.16/dimera3500.so
/usr/lib64/libgphoto2/2.5.16/directory.so
/usr/lib64/libgphoto2/2.5.16/enigma13.so
/usr/lib64/libgphoto2/2.5.16/fuji.so
/usr/lib64/libgphoto2/2.5.16/gsmart300.so
/usr/lib64/libgphoto2/2.5.16/hp215.so
/usr/lib64/libgphoto2/2.5.16/iclick.so
/usr/lib64/libgphoto2/2.5.16/jamcam.so
/usr/lib64/libgphoto2/2.5.16/jd11.so
/usr/lib64/libgphoto2/2.5.16/jl2005a.so
/usr/lib64/libgphoto2/2.5.16/jl2005c.so
/usr/lib64/libgphoto2/2.5.16/kodak_dc120.so
/usr/lib64/libgphoto2/2.5.16/kodak_dc210.so
/usr/lib64/libgphoto2/2.5.16/kodak_dc240.so
/usr/lib64/libgphoto2/2.5.16/kodak_dc3200.so
/usr/lib64/libgphoto2/2.5.16/kodak_ez200.so
/usr/lib64/libgphoto2/2.5.16/konica.so
/usr/lib64/libgphoto2/2.5.16/konica_qm150.so
/usr/lib64/libgphoto2/2.5.16/largan.so
/usr/lib64/libgphoto2/2.5.16/lg_gsm.so
/usr/lib64/libgphoto2/2.5.16/mars.so
/usr/lib64/libgphoto2/2.5.16/mustek.so
/usr/lib64/libgphoto2/2.5.16/panasonic_coolshot.so
/usr/lib64/libgphoto2/2.5.16/panasonic_dc1000.so
/usr/lib64/libgphoto2/2.5.16/panasonic_dc1580.so
/usr/lib64/libgphoto2/2.5.16/panasonic_l859.so
/usr/lib64/libgphoto2/2.5.16/pccam300.so
/usr/lib64/libgphoto2/2.5.16/pccam600.so
/usr/lib64/libgphoto2/2.5.16/pentax.so
/usr/lib64/libgphoto2/2.5.16/polaroid_pdc320.so
/usr/lib64/libgphoto2/2.5.16/polaroid_pdc640.so
/usr/lib64/libgphoto2/2.5.16/polaroid_pdc700.so
/usr/lib64/libgphoto2/2.5.16/ptp2.so
/usr/lib64/libgphoto2/2.5.16/ricoh.so
/usr/lib64/libgphoto2/2.5.16/ricoh_g3.so
/usr/lib64/libgphoto2/2.5.16/samsung.so
/usr/lib64/libgphoto2/2.5.16/sierra.so
/usr/lib64/libgphoto2/2.5.16/sipix_blink2.so
/usr/lib64/libgphoto2/2.5.16/sipix_web2.so
/usr/lib64/libgphoto2/2.5.16/smal.so
/usr/lib64/libgphoto2/2.5.16/sonix.so
/usr/lib64/libgphoto2/2.5.16/sony_dscf1.so
/usr/lib64/libgphoto2/2.5.16/sony_dscf55.so
/usr/lib64/libgphoto2/2.5.16/soundvision.so
/usr/lib64/libgphoto2/2.5.16/spca50x.so
/usr/lib64/libgphoto2/2.5.16/sq905.so
/usr/lib64/libgphoto2/2.5.16/st2205.so
/usr/lib64/libgphoto2/2.5.16/stv0674.so
/usr/lib64/libgphoto2/2.5.16/stv0680.so
/usr/lib64/libgphoto2/2.5.16/sx330z.so
/usr/lib64/libgphoto2/2.5.16/topfield.so
/usr/lib64/libgphoto2/2.5.16/toshiba_pdrm11.so
/usr/lib64/libgphoto2/2.5.16/tp6801.so
/usr/lib64/libgphoto2_port.so.12
/usr/lib64/libgphoto2_port.so.12.0.0
/usr/lib64/libgphoto2_port/0.12.0/disk.so
/usr/lib64/libgphoto2_port/0.12.0/ptpip.so
/usr/lib64/libgphoto2_port/0.12.0/serial.so
/usr/lib64/libgphoto2_port/0.12.0/usb1.so
/usr/lib64/libgphoto2_port/0.12.0/usbdiskdirect.so
/usr/lib64/libgphoto2_port/0.12.0/usbscsi.so

%files locales -f libgphoto2-6.lang -f libgphoto2_port-12.lang
%defattr(-,root,root,-)

