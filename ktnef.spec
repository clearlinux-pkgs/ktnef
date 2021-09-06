#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : ktnef
Version  : 21.08.1
Release  : 31
URL      : https://download.kde.org/stable/release-service/21.08.1/src/ktnef-21.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.1/src/ktnef-21.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.1/src/ktnef-21.08.1.tar.xz.sig
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
BuildRequires : ki18n-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n ktnef-21.08.1
cd %{_builddir}/ktnef-21.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630963866
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1630963866
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktnef
cp %{_builddir}/ktnef-21.08.1/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/ktnef/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/ktnef-21.08.1/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktnef/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/ktnef-21.08.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktnef/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/ktnef-21.08.1/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/ktnef/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang libktnef5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/ktnef.categories
/usr/share/qlogging-categories5/ktnef.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KTNEF/KTNEF/Formatter
/usr/include/KF5/KTNEF/KTNEF/KTNEFAttach
/usr/include/KF5/KTNEF/KTNEF/KTNEFDefs
/usr/include/KF5/KTNEF/KTNEF/KTNEFMessage
/usr/include/KF5/KTNEF/KTNEF/KTNEFParser
/usr/include/KF5/KTNEF/KTNEF/KTNEFProperty
/usr/include/KF5/KTNEF/KTNEF/KTNEFPropertySet
/usr/include/KF5/KTNEF/KTNEF/KTNEFWriter
/usr/include/KF5/KTNEF/ktnef/formatter.h
/usr/include/KF5/KTNEF/ktnef/ktnef_export.h
/usr/include/KF5/KTNEF/ktnef/ktnefattach.h
/usr/include/KF5/KTNEF/ktnef/ktnefdefs.h
/usr/include/KF5/KTNEF/ktnef/ktnefmessage.h
/usr/include/KF5/KTNEF/ktnef/ktnefparser.h
/usr/include/KF5/KTNEF/ktnef/ktnefproperty.h
/usr/include/KF5/KTNEF/ktnef/ktnefpropertyset.h
/usr/include/KF5/KTNEF/ktnef/ktnefwriter.h
/usr/include/KF5/ktnef_version.h
/usr/lib64/cmake/KF5Tnef/KF5TnefConfig.cmake
/usr/lib64/cmake/KF5Tnef/KF5TnefConfigVersion.cmake
/usr/lib64/cmake/KF5Tnef/KF5TnefTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Tnef/KF5TnefTargets.cmake
/usr/lib64/libKF5Tnef.so
/usr/lib64/qt5/mkspecs/modules/qt_KTNef.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Tnef.so.5
/usr/lib64/libKF5Tnef.so.5.18.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktnef/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ktnef/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/ktnef/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/ktnef/8287b608d3fa40ef401339fd907ca1260c964123

%files locales -f libktnef5.lang
%defattr(-,root,root,-)

