Summary:	A mud client that runs in console mode
Summary(pl):	Klient mudowy uruchamiany spod konsoli
Name:		tintin
Version:	1.96.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/tintin/%{name}-%{version}.tar.gz
# Source0-md5:	4f171b8f73d29dd88934992114a5b683
URL:		http://tintin.sourceforge.net/
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinTin++ is a mud client that runs in console mode.

%description -l pl
TinTin++ jest klientem mudowym uruchamianym spod konsoli.

%prep
%setup -q -n tt
%{__sed} -i -e 's@/usr/bin@$(DESTDIR)/usr/bin@g' src/Makefile.in

%build
cd src/
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C src/ install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS FAQ README TODO docs/*.txt
%attr(755,root,root) %{_bindir}/*
