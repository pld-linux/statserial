Summary:	A tool which displays the status of serial port modem lines
Summary(de):	zeigt den Status der seriellen Leitungen in einem Terminal an
Summary(es):	Ense�a el estado de una l�nea serial en un terminal
Summary(fr):	Affiche l'�tat des lignes s�rie dans un terminal
Summary(pl):	Narz�dzie wy�wietlaj�ce stan linii modemowych portu szeregowego
Summary(pt_BR):	Mostra o estado de uma linha serial em um terminal
Summary(ru):	���������� ��������� ���������������� ������ �������
Summary(tr):	Bir u�birimde seri hatlar�n durumlar�n� g�sterir
Summary(uk):	���������� ������ ��Ҧ������ ���Ԧ� �������
Summary(zh_CN):	һ����ʾ���ڵ��ƽ����״̬�Ĺ���
Name:		statserial
Version:	1.1
Release:	31
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

%description -l de
Statserial zeigt eine Tabelle mit den Signalen auf einem
Standard-9-Pin oder 25-Pin seriellen Port an und meldet den Status der
Handshaking- Leitungen. N�tzlich zum Debuggen von Problemen mit
seriellen Ports oder Modems.

%description -l es
Statserial ense�a una tabla de las se�ales en un puerto serial padr�n
de 9 o 25 pinos y indica el estado de las l�neas de handshaking. Puede
ser �til en la depuraci�n de problemas con puertos seriales o m�dems.

%description -l fr
Statserial affiche une table des signaux sur un port s�rie standard 9
ou 25 broches, et indique l'�tat des lignes reli�es. il peut �tre
utile pour d�boguer des probl�mes de port s�rie ou de modem.

%description -l pl
Statserial jest narz�dziem wy�wietlaj�cym tabel� sygna��w w
standardowym 9 lub 25 pinowym z��czu portu szeregowego i pokazuj�cym
aktualny stan linii steruj�cych przep�ywem. Statserial jest u�yteczny
przy usuwaniu b��d�w konfiguracji portu szeregowego i/lub modemu.

%description -l pt_BR
Statserial mostra uma tabela dos sinais em uma porta serial padr�o de
9 ou 25 pinos e indica o status das linhas de handshaking. Pode ser
�til na depura��o de problemas com portas seriais ou modems.

%description -l ru
Statserial ������� ������� �������� �� ����������� ����������������
����� DB9 ��� DB25 � ���������� ��������� ���������� �����. �����
���������� ��� ���������� ������� � ����������������� ������� �
��������.

%description -l tr
Statserial, seri ba�lant� noktas� �zerindeki i�aretlerin bir tablosunu
g�sterir ve els�k��ma hatlar�n�n durumunu belirtir. Seri ba�lant�
noktalar� ya da modemlerle ilgili hatalar� belirlemekte
kullan�labilir.

%description -l uk
Statserial צ�������� ������� �����̦� �� ������������ ��Ҧ�������
����� DB9 �� DB25 �� ������ ���������� ̦Φ�. ���� ���� �������� ���
������ ������� ������� � ��Ҧ������� ������� �� ��������.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed 's/CFLAGS.*=.*//' Makefile > Makefile.new
mv -f Makefile.new Makefile

%build
%{__make} CFLAGS="%{rpmcflags}"

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
