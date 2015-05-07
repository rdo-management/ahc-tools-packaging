%{?!_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}}

Name:           ahc-tools
Summary:        Tools for RDO-manager automatic health checks
Version:        0.1.0
Release:        1%{?dist}
License:        ASL 2.0
Group:          System Environment/Base
URL:            https://pypi.python.org/pypi/ahc-tools

Source0: https://pypi.python.org/packages/source/a/ahc-tools/ahc-tools-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: python-hardware
Requires: python-ironicclient
Requires: python-oslo-config

%prep
%autosetup -v -p 1 -n %{name}-%{upstream_version}
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}


%description
Reporting and matching tools for RDO-manager automatic health checks.

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/ahc_tools*
%exclude %{python2_sitelib}/ahc_tools/test*
%{_bindir}/ahc-report
%{_bindir}/ahc-match

%changelog
* Tue Apr 28 2015 John Trowbridge <jtrowbri@redhat.com> - 0.1.0
- Initial package build

