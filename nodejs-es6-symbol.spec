%{?scl:%scl_package nodejs-es6-symbol}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename es6-symbol
%global enable_tests 0
# tests disabled due to missing npm(tad) test suite

Name:		%{?scl_prefix}nodejs-es6-symbol
Version:	3.1.0
Release:	2%{?dist}
Summary:	ECMAScript 6 Symbol polyfill

License:	MIT
URL:		https://github.com/medikoo/es6-symbol.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tad)
%endif

%description
ECMAScript 6 Symbol polyfill

%prep
%setup -q -n package

%nodejs_fixdep d
# allow either the 0.1.x or 1.x.x series of npm(d)

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} %{nodejs_sitelib}/tad/bin/tad
%else
echo "Tests have been disabled..."
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md CHANGES
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.0-2
- Rebuild for rhscl

* Thu Jul 14 2016 Jared Smith <jsmith@fedoraproject.org> - 3.1.0-1
- Update to upstream 3.1.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Jared Smith <jsmith@fedoraproject.org> - 3.0.2-2
- Allow newer version of npm(d)

* Fri Dec 18 2015 Jared Smith <jsmith@fedoraproject.org> - 3.0.2-1
- Update to upstream 3.0.2 release
- disable self-test until we get all the run-time dependencies into Rawhide

* Tue Nov 10 2015 Jared Smith <jsmith@fedoraproject.org> - 3.0.1-1
- Initial packaging
