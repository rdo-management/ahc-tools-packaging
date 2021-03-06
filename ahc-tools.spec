%{?!_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}}

Name:           ahc-tools
Summary:        Tools for RDO-Manager automatic health checks
Version:        0.2.0
Release:        1%{?dist}
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/ahc-tools

Source0:        https://pypi.python.org/packages/source/a/ahc-tools/ahc-tools-%{upstream_version}.tar.gz
Source1:        compute.specs
Source2:        control.specs
Source3:        state
Source4:        compute.cmdb.example
Source5:        control.cmdb.example

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: python-hardware
Requires: python-ironicclient
Requires: python-swiftclient
Requires: python-oslo-config

%description
Reporting and matching tools for RDO-manager automatic health checks.

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

# configuration contains passwords, thus 640
install -p -D -m 640 example.conf %{buildroot}/%{_sysconfdir}/ahc-tools/ahc-tools.conf

# edeploy matching configuration files
install -p -D -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/ahc-tools/edeploy/compute.specs
install -p -D -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/ahc-tools/edeploy/control.specs
install -p -D -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/ahc-tools/edeploy/state
install -p -D -m 644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/ahc-tools/edeploy/compute.cmdb.example
install -p -D -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/ahc-tools/edeploy/control.cmdb.example

%files
%license LICENSE
%config(noreplace) %attr(-,root,root) %{_sysconfdir}/ahc-tools
%doc README.rst
%{python2_sitelib}/ahc_tools*
%exclude %{python2_sitelib}/ahc_tools/test*
%{_bindir}/ahc-report
%{_bindir}/ahc-match

%changelog
* Fri Jun 19 2015 John Trowbridge <trown@redhat.com> - 0.2.0-1
- Add ahc-tools.conf to store Ironic and Swift API credentials
- Add dependency on python-swiftclient

* Fri May 08 2015 John Trowbridge <trown@redhat.com> - 0.1.1-1
- Add default configuration for using edeploy matching

* Tue Apr 28 2015 John Trowbridge <jtrowbri@redhat.com> - 0.1.0-1
- Initial package build
