%global srcname dbus-python-client-gen

Name:           python-%{srcname}
Version:        0.7
Release:        3%{?dist}
Summary:        Python Library for Generating dbus-python Client Code

License:        MPLv2.0
URL:            https://github.com/stratis-storage/dbus-python-client-gen
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
%{summary}.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-dbus
BuildRequires:  python3-into-dbus-python >= 0.06
Requires:       python3-dbus
Requires:       python3-into-dbus-python >= 0.06

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v tests

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/dbus_python_client_gen/
%{python3_sitelib}/dbus_python_client_gen-*.egg-info/

%changelog
* Wed Oct 30 2019  Dennis Keefe <dkeefe@redhat.com> - 0.7-3
- Update to 0.7-3
 
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6-1
- Update to 0.6

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5-1
- Initial import
