Summary:	A tool which displays the status of serial port modem lines.
Summary(pl):	Narzêdzie wy¶wietlaj±ce stan linii modemowych portu szeregowego
Name:		statserial
Version:	1.1
Release:	14
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.1-config.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The statserial utility displays a table of the signals on a standard
9-pin or 25-pin serial port and indicates the status of the
handshaking lines. Statserial is useful for debugging serial port
and/or modem problems.

Install the statserial package if you need a tool to help debug serial
port or modem problems.

%description -l pl
Statserial jest narzêdziem wy¶wietlaj±cym tabelê sygna³ów w
standardowym 9 lub 25 pinowym z³±czu portu szeregowego i pokazuj±cym
aktualny stan linii steruj±cych przep³ywem. Statserial jest u¿yteczny
przy usuwaniu b³êdów konfiguracji portu szeregowego i/lub modemu.

%prep
%setup -q
%patch -p1 -b .config

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install statserial   $RPM_BUILD_ROOT%{_bindir}/statserial
install statserial.1 $RPM_BUILD_ROOT%{_mandir}/man1/statserial.1

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/statserial
%{_mandir}/man1/statserial.1*
%doc {README,ChangeLog}.gz
