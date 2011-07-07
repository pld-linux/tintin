Summary:	A mud client that runs in console mode
Summary(pl.UTF-8):	Klient mudowy uruchamiany na terminalu tekstowym
Name:		tintin
Version:	2.00.7
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/tintin/%{name}-%{version}.tar.gz
# Source0-md5:	f6791783a7077058a49a216f5caf8093
Patch0:		%{name}-cflags.patch
URL:		http://tintin.sourceforge.net/
BuildRequires:	pcre-devel
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
%attr(755,root,root) %{_bindir}/tintin
