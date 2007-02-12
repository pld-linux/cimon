%include	/usr/lib/rpm/macros.perl
Summary:	Monitors CPU and memory usage on Cisco routers
Summary(pl.UTF-8):	Monitorowanie zużycia procesora i pamięci w routerach Cisco
Name:		cimon
Version:	0.3
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	http://rousse.pm.org/cimon/%{name}-%{version}.tar.gz
# Source0-md5:	841eb90c00d45d30d40ca5df6af30eba
URL:		http://rousse.pm.org/cimon/
BuildRequires:	rpm-perlprov
Requires:	rrdtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cimon is Perl program which monitors the load (memory and CPU) on
Cisco routers using SNMP, and generates graphics with statistics using
rrdtool. It's a good source for information about your router's
health. It also has the ability to make IP accounting via Cisco IP
accounting features. It creates rrd graphics with the bandwidth usage
and traffic logfiles. The logfiles are the same as these produced by
sasacct so you can use it for date-to-date statistics and on-the-fly
graphic generation.

%description -l pl.UTF-8
Cimon to napisany w Perlu program monitorujący obciążenie (pamięci i
procesora) w routerach Cisco przy użyciu SNMP i generujący wykresy ze
statystykami przy użyciu rrdtool. Jest to dobre źródło informacji o
stanie urządzenia. Ma także możliwość tworzenia accountingu IP poprzez
możliwości Cisco. Tworzy wykresy rrd z wykorzystaniem pasma i logami
ruchu. Logi ruchu są te same, co produkowane przez sasacct, więc można
używać ich do statystyk w przedziałach czasu oraz do generowania
wykresów w locie.

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
%doc CHANGES INSTALL README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/*
