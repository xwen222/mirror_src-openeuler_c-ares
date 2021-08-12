Name:           c-ares
Version:        1.17.1
Release:        2
Summary:        A C library for asynchronous DNS requests

License:        MIT
URL:            https://github.com/c-ares/c-ares
Source0:        https://github.com/c-ares/c-ares/releases/download/cares-1_17_1/%{name}-%{version}.tar.gz

BuildRequires:  gcc autoconf automake libtool
# Patch0 from Redhat is applied for stopping overriding AC_CONFIG_MACRO_DIR
Patch0:     0000-Use-RPM-compiler-options.patch
Patch1:     backport-001-CVE-2021-3672.patch
Patch2:     backport-002-CVE-2021-3672.patch
%description
This is c-ares, an asynchronous resolver library. It is intended for applications
which need to perform DNS queries without blocking, or need to perform multiple

%package        devel
Summary:        C-ares development files
Requires:       %{name} = %{version}-%{release} pkgconfig

%description    devel
The headers and libraries files that c-ares required to compile applications or
shared objects are contained in %{name}-devel package.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -if
%configure --enable-shared --disable-dependency-tracking
make %{?_smp_mflags}

%install
%make_install
%delete_la
%ldconfig_scriptlets

%files
%doc CHANGES LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libcares.so
%{_libdir}/libcares.a
%{_includedir}/*.h

%files help
%doc NEWS README.cares README.md
%{_mandir}/man3/*

%changelog
* Thu Aug 12 2021 gaihuiying <gaihuiying1@huawei.com> - 1.17.1-2
- fix CVE-2021-3672

* Sat Jan 30 2021 xihaochen <xihaochen@huawei.com> - 1.17.1-1
- Type:requirements
- Id:NA
- SUG:NA
- DESC:update c-ares to 1.17.1

* Tue Sep 8 2020 lunankun <lunankun@huawei.com> - 1.16.1-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix source0 url

* Wed Jul 22 2020 gaihuiying <gaihuiying1@huawei.com> - 1.16.1-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update c-ares version to 1.16.1

* Mon Sep 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.15.0-1
- Package Init
