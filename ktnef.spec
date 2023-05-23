#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ktnef
Version  : 23.04.1
Release  : 53
URL      : https://download.kde.org/stable/release-service/23.04.1/src/ktnef-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/ktnef-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/ktnef-23.04.1.tar.xz.sig
Summary  : API for handling TNEF data
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: ktnef-data = %{version}-%{release}
Requires: ktnef-lib = %{version}-%{release}
Requires: ktnef-license = %{version}-%{release}
Requires: ktnef-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kcalendarcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
TNEF test files are taken from tnef.sf.net.

%package data
Summary: data components for the ktnef package.
Group: Data

%description data
data components for the ktnef package.


%package dev
Summary: dev components for the ktnef package.
Group: Development
Requires: ktnef-lib = %{version}-%{release}
Requires: ktnef-data = %{version}-%{release}
Provides: ktnef-devel = %{version}-%{release}
Requires: ktnef = %{version}-%{release}

%description dev
dev components for the ktnef package.


%package lib
Summary: lib components for the ktnef package.
Group: Libraries
Requires: ktnef-data = %{version}-%{release}
Requires: ktnef-license = %{version}-%{release}

%description lib
lib components for the ktnef package.


%package license
Summary: license components for the ktnef package.
Group: Default

%description license
license components for the ktnef package.


%package locales
Summary: locales components for the ktnef package.
Group: Default

%description locales
locales components for the ktnef package.


%prep
%setup -q -n ktnef-23.04.1
cd %{_builddir}/ktnef-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684852451
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684852451
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktnef
cp %{_builddir}/ktnef-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/ktnef/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/ktnef-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktnef/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/ktnef-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktnef/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ktnef-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/ktnef/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang libktnef5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/ktnef.categories
/usr/share/qlogging-categories5/ktnef.renamecategories

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5Tnef.so
/usr/include/KPim5/KTNEF/KTNEF/Formatter
/usr/include/KPim5/KTNEF/KTNEF/KTNEFAttach
/usr/include/KPim5/KTNEF/KTNEF/KTNEFDefs
/usr/include/KPim5/KTNEF/KTNEF/KTNEFMessage
/usr/include/KPim5/KTNEF/KTNEF/KTNEFParser
/usr/include/KPim5/KTNEF/KTNEF/KTNEFProperty
/usr/include/KPim5/KTNEF/KTNEF/KTNEFPropertySet
/usr/include/KPim5/KTNEF/KTNEF/KTNEFWriter
/usr/include/KPim5/KTNEF/ktnef/formatter.h
/usr/include/KPim5/KTNEF/ktnef/ktnef_export.h
/usr/include/KPim5/KTNEF/ktnef/ktnefattach.h
/usr/include/KPim5/KTNEF/ktnef/ktnefdefs.h
/usr/include/KPim5/KTNEF/ktnef/ktnefmessage.h
/usr/include/KPim5/KTNEF/ktnef/ktnefparser.h
/usr/include/KPim5/KTNEF/ktnef/ktnefproperty.h
/usr/include/KPim5/KTNEF/ktnef/ktnefpropertyset.h
/usr/include/KPim5/KTNEF/ktnef/ktnefwriter.h
/usr/include/KPim5/KTNEF/ktnef_version.h
/usr/lib64/cmake/KF5Tnef/KF5TnefConfig.cmake
/usr/lib64/cmake/KF5Tnef/KF5TnefConfigVersion.cmake
/usr/lib64/cmake/KF5Tnef/KPim5TnefTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Tnef/KPim5TnefTargets.cmake
/usr/lib64/cmake/KPim5Tnef/KPim5TnefConfig.cmake
/usr/lib64/cmake/KPim5Tnef/KPim5TnefConfigVersion.cmake
/usr/lib64/cmake/KPim5Tnef/KPim5TnefTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5Tnef/KPim5TnefTargets.cmake
/usr/lib64/libKPim5Tnef.so
/usr/lib64/qt5/mkspecs/modules/qt_KTNef.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5Tnef.so.5
/V3/usr/lib64/libKPim5Tnef.so.5.23.1
/usr/lib64/libKPim5Tnef.so.5
/usr/lib64/libKPim5Tnef.so.5.23.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktnef/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ktnef/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/ktnef/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/ktnef/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libktnef5.lang
%defattr(-,root,root,-)

