%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           icepapcms
Version:        1.16
Release:        1%{?dist}.maxlab
Summary:        IcePAP CMS application

Group:          Applications/Engineering
License:        Unknown
URL:            http://www.cells.es
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:		%{_builddir}/%{name}-%{version}-%{release}
BuildRequires:  python-setuptools
Requires:		pyIcePAP
Requires:       python-storm

%description
IcePAP CMS application

%prep
%setup -q

%build
cd src
%{__python} setup.py build

%install
cd src
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check

%files
%doc src/README src/VERSION src/doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python_sitelib}/*

%changelog
* Tue Mar 05 2013 Andreas Persson <andreas_g.persson@maxlab.lu.se> - 1.16-1
- initial package
