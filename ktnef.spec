#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : ktnef
Version  : 18.08.0
Release  : 2
URL      : https://download.kde.org/stable/applications/18.08.0/src/ktnef-18.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/18.08.0/src/ktnef-18.08.0.tar.xz
Source99 : https://download.kde.org/stable/applications/18.08.0/src/ktnef-18.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: ktnef-lib
Requires: ktnef-license
Requires: ktnef-locales
Requires: ktnef-data
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalcore-dev
BuildRequires : kcalutils-dev
BuildRequires : kcontacts-dev
BuildRequires : qtbase-dev qtbase-extras mesa-dev

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
Requires: ktnef-lib
Requires: ktnef-data
Provides: ktnef-devel

%description dev
dev components for the ktnef package.


%package lib
Summary: lib components for the ktnef package.
Group: Libraries
Requires: ktnef-data
Requires: ktnef-license

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
%setup -q -n ktnef-18.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535432928
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535432928
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ktnef
cp COPYING.LIB %{buildroot}/usr/share/doc/ktnef/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libktnef5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/xdg/ktnef.categories
/usr/share/xdg/ktnef.renamecategories

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
/usr/lib64/libKF5Tnef.so.5.9.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/ktnef/COPYING.LIB

%files locales -f libktnef5.lang
%defattr(-,root,root,-)

