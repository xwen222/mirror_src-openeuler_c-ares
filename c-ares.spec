Name:           c-ares
Version:        1.18.1
Release:        4
Summary:        A C library for asynchronous DNS requests

License:        MIT
URL:            https://github.com/c-ares/c-ares
Source0:        https://github.com/c-ares/c-ares/releases/download/cares-1_18_1/%{name}-%{version}.tar.gz

BuildRequires:  gcc autoconf automake libtool g++
# Patch0 from Redhat is applied for stopping overriding AC_CONFIG_MACRO_DIR
Patch0:         0000-Use-RPM-compiler-options.patch
Patch1:         backport-disable-live-tests.patch
Patch2:         backport-add-str-len-check-in-config_sortlist-to-avoid-stack-overflow.patch

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
%configure --enable-shared --disable-static --disable-dependency-tracking
make %{?_smp_mflags}

%install
%make_install
%delete_la
%ldconfig_scriptlets

%check
cd test
./configure
cd ../
%make_build -C test
./test/arestest

%files
%doc CHANGES LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libcares.so
%{_includedir}/*.h

%files help
%doc NEWS README.cares README.md
%{_mandir}/man3/*

%changelog
* Fri Feb 10 2023 xignwei <xingwei14@h-partners.com> - 1.18.1-4
- Type:cves
- CVE:CVE-2022-4904
- SUG:NA
- DESC:fix CVE-2022-4904

* Tue Aug 02 2022 gaihuiying <eaglegai@163.com> - 1.18.1-3
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:rebuild to 1.18.1-3

* Wed Feb 9 2022 chengyechun <chengyechun1@huawei.com> - 1.18.1-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:enable test and disable live tests

* Wed Jan 12 2022 gaihuiying <gaihuiying1@huawei.com> - 1.18.1-1
- Type:requirement
- Id:NA
- SUG:NA
- DESC:update c-ares to 1.18.1

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
