Summary:	A Commodore 64 music player and SID chip emulator library
Summary(pl):	Biblioteka odtwarzaj±ca muzyczki z Commodore 64 i emuluj±ca uk³ad SID
Name:		libsidplay2
Version:	2.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sidplay2/sidplay-libs-%{version}.tar.gz
# Source0-md5:	7ea0ba5dc1da4604d15eaae001f7d2a7
URL:		http://sidplay2.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sidplay 2 is the second in the Sidplay series originally developed by
Michael Schwendt. This version is written by Simon White and is cycle
accurate for improved sound reproduction. Sidplay 2 is capable of
playing all C64 mono and stereo file formats.

%description -l pl
Sidplay 2 to druga wersja z serii Sidplay oryginalnie stworzonej przez
Michaela Schwendta. Ta wersja zosta³a napisana przez Simona White'a i
jest dok³adna co do cyklu w celu zwiêkszonej wierno¶ci reprodukcji
d¼wiêku. Sidplay 2 mo¿e odtwarzaæ wszystkie formaty plików mono i
stereo z C64.

%package devel
Summary:	Header files for compiling apps that use libsidplay
Summary(pl):	Pliki nag³ówkowe do budowania aplikacji u¿ywaj±cych libsidplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files for compiling applications that
use libsidplay.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do budowania aplikacji u¿ywaj±cych
biblioteki libsidplay.

%package static
Summary:	Static libsidplay library
Summary(pl):	Statyczna biblioteka libsidplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libsidplay.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê libsidplay.

%prep
%setup -q -n sidplay-libs-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc libsidplay/{AUTHORS,ChangeLog,TODO}
%attr(755,root,root) %{_libdir}/libsidplay2.so.*.*.*
%attr(755,root,root) %{_libdir}/libsidutils.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsidplay2.so
%attr(755,root,root) %{_libdir}/libsidutils.so
%{_libdir}/libsidplay2.la
%{_libdir}/libsidutils.la
%{_libdir}/sidplay
%{_includedir}/sidplay
%{_pkgconfigdir}/libsidplay2.pc
%{_pkgconfigdir}/libsidutils.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsidplay2.a
%{_libdir}/libsidutils.a
