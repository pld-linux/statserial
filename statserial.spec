Summary: A tool which displays the status of serial port modem lines.
Name: statserial
Version: 1.1
Release: 13
Copyright: BSD
Group: Applications/System
Source: ftp://sunsite.unc.edu/pub/Linux/system/serial/statserial-1.1.tar.gz
Patch: statserial-1.1-config.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The statserial utility displays a table of the signals on a standard
9-pin or 25-pin serial port and indicates the status of the
handshaking lines.  Statserial is useful for debugging serial port
and/or modem problems.

Install the statserial package if you need a tool to help debug serial
port or modem problems.

%prep
%setup -q
%patch -p1 -b .config

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -m 755 -s statserial $RPM_BUILD_ROOT/usr/bin/statserial
install -m 444 statserial.1 $RPM_BUILD_ROOT/usr/man/man1/statserial.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/statserial
/usr/man/man1/statserial.1
