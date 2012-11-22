%global glacier_hash .e98ade8

Name:		glacier-cli
Version:	0.0
Release:	0%{glacier_hash}%{?dist}
Summary:	Command-line interface to Amazon Glacier

Group:		Applications/Internet
License:	MIT
URL:		https://github.com/basak/glacier-cli
# git clone git://github.com/xsuchy/glacier-cli.git
# cd glacier-cli
# tito build --tgz
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	python-devel
Requires:	python-boto

%description
This tool provides a sysadmin-friendly command line interface to Amazon
Glacier, turning Glacier into an easy-to-use storage backend. It automates
tasks which would otherwise require a number of separate steps (job submission,
polling for job completion and retrieving the results of jobs). It provides
integration with git-annex, making Glacier even more useful.

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -m755 glacier.py %{buildroot}%{_bindir}/glacier



%files
%doc COPYING README.md
%{_bindir}/glacier


%changelog

