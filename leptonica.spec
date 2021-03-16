#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : leptonica
Version  : 1.80.0
Release  : 3
URL      : https://github.com/DanBloomberg/leptonica/releases/download/1.80.0/leptonica-1.80.0.tar.gz
Source0  : https://github.com/DanBloomberg/leptonica/releases/download/1.80.0/leptonica-1.80.0.tar.gz
Summary  : An open source C library for efficient image processing and image analysis operations
Group    : Development/Tools
License  : BSD-2-Clause
Requires: leptonica-bin = %{version}-%{release}
Requires: leptonica-lib = %{version}-%{release}
Requires: leptonica-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : gnuplot
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : pkgconfig(zlib)

%description
# Leptonica Library #
[![Build Status](https://travis-ci.org/DanBloomberg/leptonica.svg?branch=master)](https://travis-ci.org/DanBloomberg/leptonica)
[![Build status](https://ci.appveyor.com/api/projects/status/vsk607rr6n4j2tmk?svg=true)](https://ci.appveyor.com/project/DanBloomberg/leptonica)
![Build status](https://github.com/DanBloomberg/leptonica/workflows/sw/badge.svg)<br>
[![Coverity Scan Build Status](https://scan.coverity.com/projects/leptonica/badge.svg)](https://scan.coverity.com/projects/leptonica)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/g/DanBloomberg/leptonica.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/DanBloomberg/leptonica/context:cpp)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/DanBloomberg/leptonica.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/DanBloomberg/leptonica/alerts)

%package bin
Summary: bin components for the leptonica package.
Group: Binaries
Requires: leptonica-license = %{version}-%{release}

%description bin
bin components for the leptonica package.


%package dev
Summary: dev components for the leptonica package.
Group: Development
Requires: leptonica-lib = %{version}-%{release}
Requires: leptonica-bin = %{version}-%{release}
Provides: leptonica-devel = %{version}-%{release}
Requires: leptonica = %{version}-%{release}

%description dev
dev components for the leptonica package.


%package lib
Summary: lib components for the leptonica package.
Group: Libraries
Requires: leptonica-license = %{version}-%{release}

%description lib
lib components for the leptonica package.


%package license
Summary: license components for the leptonica package.
Group: Default

%description license
license components for the leptonica package.


%prep
%setup -q -n leptonica-1.80.0
cd %{_builddir}/leptonica-1.80.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615868796
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1615868796
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/leptonica
cp %{_builddir}/leptonica-1.80.0/leptonica-license.txt %{buildroot}/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
cp %{_builddir}/leptonica-1.80.0/prog/leptonica-license.txt %{buildroot}/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
cp %{_builddir}/leptonica-1.80.0/src/leptonica-license.txt %{buildroot}/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/convertfilestopdf
/usr/bin/convertfilestops
/usr/bin/convertformat
/usr/bin/convertsegfilestopdf
/usr/bin/convertsegfilestops
/usr/bin/converttopdf
/usr/bin/converttops
/usr/bin/fileinfo
/usr/bin/imagetops
/usr/bin/xtractprotos

%files dev
%defattr(-,root,root,-)
/usr/include/leptonica/allheaders.h
/usr/include/leptonica/alltypes.h
/usr/include/leptonica/array.h
/usr/include/leptonica/arrayaccess.h
/usr/include/leptonica/bbuffer.h
/usr/include/leptonica/bilateral.h
/usr/include/leptonica/bmf.h
/usr/include/leptonica/bmfdata.h
/usr/include/leptonica/bmp.h
/usr/include/leptonica/ccbord.h
/usr/include/leptonica/colorfill.h
/usr/include/leptonica/dewarp.h
/usr/include/leptonica/endianness.h
/usr/include/leptonica/environ.h
/usr/include/leptonica/gplot.h
/usr/include/leptonica/heap.h
/usr/include/leptonica/imageio.h
/usr/include/leptonica/jbclass.h
/usr/include/leptonica/leptwin.h
/usr/include/leptonica/list.h
/usr/include/leptonica/morph.h
/usr/include/leptonica/pix.h
/usr/include/leptonica/ptra.h
/usr/include/leptonica/queue.h
/usr/include/leptonica/rbtree.h
/usr/include/leptonica/readbarcode.h
/usr/include/leptonica/recog.h
/usr/include/leptonica/regutils.h
/usr/include/leptonica/stack.h
/usr/include/leptonica/stringcode.h
/usr/include/leptonica/sudoku.h
/usr/include/leptonica/watershed.h
/usr/lib64/cmake/LeptonicaConfig-version.cmake
/usr/lib64/cmake/LeptonicaConfig.cmake
/usr/lib64/liblept.so
/usr/lib64/libleptonica.so
/usr/lib64/pkgconfig/lept.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblept.so.5
/usr/lib64/liblept.so.5.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
