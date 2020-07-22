Name:           c-ares
Version:        1.16.1
Release:        1
Summary:        A C library for asynchronous DNS requests

License:        MIT
URL:            https://github.com/c-ares/c-ares
Source0:        https://github.com/c-ares/c-ares/releases/tag/%{name}-%{version}.tar.gz

BuildRequires:  gcc autoconf automake libtool
# Patch0 from Redhat is applied for stopping overriding AC_CONFIG_MACRO_DIR
Patch0000:     0000-Use-RPM-compiler-options.patch
Patch0001:     0001-Fix-invalid-read-in-ares_parse_soa_reply.patch
Patch0002:     0002-Fix-sizeof-sizeof-addr.saX-sizeof-addr.saX-in-readad.patch
Patch0003:     0003-Avoid-buffer-overflow-in-RC4-loop-comparison-336.patch
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
* Wed Jul 22 2020 gaihuiying <gaihuiying1@huawei.com> - 1.16.1-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update c-ares version to 1.16.1

* Mon Sep 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.15.0-1
- Package Init
