%undefine __cmake_in_source_build
%global debug_package %{nil}

Name: cxxopts
Version: 2.2.0
Release: 2%{?dist}

Summary: Lightweight C++ command line option parser
License: MIT
URL: https://github.com/jarro2783/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/jarro2783/cxxopts/pull/226
Patch100: %{name}-fix-installation.patch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake

%description
CXXOpts is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCXXOPTS_ENABLE_INSTALL=ON \
    -DCXXOPTS_BUILD_EXAMPLES=OFF \
    -DCXXOPTS_BUILD_TESTS=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_libdir}/cmake/%{name}/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1
- Initial SPEC release.
