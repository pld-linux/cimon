%include	/usr/lib/rpm/macros.perl
Summary:	Monitors CPU and memory usage on Cisco routers
Summary(pl):	Monitorowanie zu¿ycia procesora i pamiêci w routerach Cisco
Name:		cimon
Version:	0.3
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	http://rousse.pm.org/cimon/%{name}-%{version}.tar.gz
URL:		http://rousse.pm.org/cimon/
BuildRequires:	rpm-perlprov
Requires:	rrdtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cimon is Perl program wich monitors the load (memory and CPU) on Cisco
routers using SNMP, and generates graphics with statistics using
rrdtool. It's a good source for information about your router's
health. It also has the abillity to make IP accounting via Cisco IP
accounting features. It creates rrd graphics with the bandwith usage
and traffic logfiles. The logfiles are the same as these produced by
sasacct so you can use it for date-to-date statistics and on-the-fly
graphic generation.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install %{name}.plx $RPM_BUILD_ROOT%{_bindir}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/*
