Summary:	A tool which displays the status of serial port modem lines
Summary(de):	zeigt den Status der seriellen Leitungen in einem Terminal an
Summary(fr):	Affiche l'état des lignes série dans un terminal
Summary(pl):	Narzêdzie wy¶wietlaj±ce stan linii modemowych portu szeregowego
Summary(tr):	Bir uçbirimde seri hatlarýn durumlarýný gösterir
Name:		statserial
Version:	1.1
Release:	22
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
Patch1:		%{name}-dev.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The statserial utility displays a table of the signals on a standard
9-pin or 25-pin serial port and indicates the status of the
handshaking lines. Statserial is useful for debugging serial port
and/or modem problems.

Install the statserial package if you need a tool to help debug serial
port or modem problems.

%description -l de
Statserial zeigt eine Tabelle mit den Signalen auf einem
Standard-9-Pin oder 25-Pin seriellen Port an und meldet den Status der
Handshaking- Leitungen. Nützlich zum Debuggen von Problemen mit
seriellen Ports oder Modems.

%description -l fr
Statserial affiche une table des signaux sur un port série standard 9
ou 25 broches, et indique l'état des lignes reliées. il peut être
utile pour déboguer des problèmes de port série ou de modem.

%description -l pl
Statserial jest narzêdziem wy¶wietlaj±cym tabelê sygna³ów w
standardowym 9 lub 25 pinowym z³±czu portu szeregowego i pokazuj±cym
aktualny stan linii steruj±cych przep³ywem. Statserial jest u¿yteczny
przy usuwaniu b³êdów konfiguracji portu szeregowego i/lub modemu.

%description -l tr
Statserial, seri baðlantý noktasý üzerindeki iþaretlerin bir tablosunu
gösterir ve elsýkýþma hatlarýnýn durumunu belirtir. Seri baðlantý
noktalarý ya da modemlerle ilgili hatalarý belirlemekte
kullanýlabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed 's/CFLAGS.*=.*//' Makefile > Makefile.new
mv -f Makefile.new Makefile

%build
%{__make} CFLAGS="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

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
