Summary:	A mud client that runs in console mode
Summary(pl.UTF-8):	Klient mudowy uruchamiany na terminalu tekstowym
Name:		tintin
Version:	1.99.4
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/tintin/%{name}-%{version}.tar.gz
# Source0-md5:	68ed5944e629d8c239ff9088d45b96c4
Patch0:		%{name}-cflags.patch
URL:		http://tintin.sourceforge.net/
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinTin++ is a mud client that runs in console mode.

%description -l pl.UTF-8
TinTin++ jest klientem mudowym uruchamianym na terminalu tekstowym.

%prep
%setup -q -n tt
%patch0 -p1
%{__sed} -i -e 's@/usr/bin@$(DESTDIR)/usr/bin@g' src/Makefile.in

# change binary file name to better one
%{__sed} -i -e 's@tt++@tintin@g' src/Makefile.in

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS FAQ README TODO docs/*.txt
%attr(755,root,root) %{_bindir}/*
