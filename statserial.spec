Summary:	A tool which displays the status of serial port modem lines
Summary(de.UTF-8):	zeigt den Status der seriellen Leitungen in einem Terminal an
Summary(es.UTF-8):	Enseña el estado de una línea serial en un terminal
Summary(fr.UTF-8):	Affiche l'état des lignes série dans un terminal
Summary(pl.UTF-8):	Narzędzie wyświetlające stan linii modemowych portu szeregowego
Summary(pt_BR.UTF-8):	Mostra o estado de uma linha serial em um terminal
Summary(ru.UTF-8):	Показывает состояние последовательных портов системы
Summary(tr.UTF-8):	Bir uçbirimde seri hatların durumlarını gösterir
Summary(uk.UTF-8):	Відображає статус серіальних портів системи
Summary(zh_CN.UTF-8):	一个显示串口调制解调器状态的工具
Name:		statserial
Version:	1.1
Release:	37
License:	BSD
Group:		Applications/System
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tar.gz
# Source0-md5:	bcd90fb0881c64024396bf1070de7e64
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

%description -l de.UTF-8
Statserial zeigt eine Tabelle mit den Signalen auf einem
Standard-9-Pin oder 25-Pin seriellen Port an und meldet den Status der
Handshaking- Leitungen. Nützlich zum Debuggen von Problemen mit
seriellen Ports oder Modems.

%description -l es.UTF-8
Statserial enseña una tabla de las señales en un puerto serial padrón
de 9 o 25 pinos y indica el estado de las líneas de handshaking. Puede
ser útil en la depuración de problemas con puertos seriales o módems.

%description -l fr.UTF-8
Statserial affiche une table des signaux sur un port série standard 9
ou 25 broches, et indique l'état des lignes reliées. il peut être
utile pour déboguer des problèmes de port série ou de modem.

%description -l pl.UTF-8
Statserial jest narzędziem wyświetlającym tabelę sygnałów w
standardowym 9 lub 25 pinowym złączu portu szeregowego i pokazującym
aktualny stan linii sterujących przepływem. Statserial jest użyteczny
przy usuwaniu błędów konfiguracji portu szeregowego i/lub modemu.

%description -l pt_BR.UTF-8
Statserial mostra uma tabela dos sinais em uma porta serial padrão de
9 ou 25 pinos e indica o status das linhas de handshaking. Pode ser
útil na depuração de problemas com portas seriais ou modems.

%description -l ru.UTF-8
Statserial выводит таблицу сигналов на стандартном последовательном
порту DB9 или DB25 и показывает состояние сигнальных линий. Может
пригодится для устранения проблем с последовательными портами и
модемами.

%description -l tr.UTF-8
Statserial, seri bağlantı noktası üzerindeki işaretlerin bir tablosunu
gösterir ve elsıkışma hatlarının durumunu belirtir. Seri bağlantı
noktaları ya da modemlerle ilgili hataları belirlemekte
kullanılabilir.

%description -l uk.UTF-8
Statserial відображає таблицю сигналів на стандартному серіальному
порту DB9 чи DB25 та статус сигнальних ліній. Може бути корисним при
пошуку причини проблем з серіальними портами та модемами.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed 's/CFLAGS.*=.*//' Makefile > Makefile.new
mv -f Makefile.new Makefile

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install statserial   $RPM_BUILD_ROOT%{_bindir}/statserial
install statserial.1 $RPM_BUILD_ROOT%{_mandir}/man1/statserial.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/statserial
%{_mandir}/man1/statserial.1*
