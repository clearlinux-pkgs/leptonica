#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : leptonica
Version  : 1.83.0
Release  : 5
URL      : https://github.com/DanBloomberg/leptonica/releases/download/1.83.0/leptonica-1.83.0.tar.gz
Source0  : https://github.com/DanBloomberg/leptonica/releases/download/1.83.0/leptonica-1.83.0.tar.gz
Summary  : An open source C library for efficient image processing and image analysis operations
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(libjpeg)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libwebp)
BuildRequires : pkgconfig(libwebpmux)
BuildRequires : pkgconfig(zlib)

%description
# Leptonica Library #
[![Build Status](https://api.travis-ci.com/DanBloomberg/leptonica.svg?branch=master)](https://app.travis-ci.com/github/DanBloomberg/leptonica)
[![Build status](https://ci.appveyor.com/api/projects/status/vsk607rr6n4j2tmk?svg=true)](https://ci.appveyor.com/project/DanBloomberg/leptonica)
![Build status](https://github.com/DanBloomberg/leptonica/workflows/sw/badge.svg)

%prep
%setup -q -n leptonica-1.83.0
cd %{_builddir}/leptonica-1.83.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672179661
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1672179661
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/leptonica
cp %{_builddir}/leptonica-%{version}/leptonica-license.txt %{buildroot}/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
cp %{_builddir}/leptonica-%{version}/prog/leptonica-license.txt %{buildroot}/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
cp %{_builddir}/leptonica-%{version}/src/leptonica-license.txt %{buildroot}/usr/share/package-licenses/leptonica/e0b1dceebde3eb567f610aa97227aa6a5e713810
%make_install

%files
%defattr(-,root,root,-)
