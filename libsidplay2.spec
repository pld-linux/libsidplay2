Summary:	A Commodore 64 music player and SID chip emulator library
Summary(pl):	Biblioteka odtwarzaj±ca muzyczki z Commodore 64 i emuluj±ca uk³ad SID
Name:		libsidplay2
Version:	2.1.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.sourceforge.net/sidplay2/sidplay-libs-%{version}.tar.gz
# Source0-md5:	40e61c8edbce16e1a8d0e31169869d99
URL:		http://sidplay2.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sidplay 2 is the second in the Sidplay series originally developed by
Michael Schwendt. This version is written by Simon White and is cycle
accurate for improved sound reproduction. Sidplay 2 is capable of
playing all C64 mono and stereo file formats.

%package devel
Summary:	Header files for compiling apps that use libsidplay
Summary(pl):	Pliki nag³ówkowe do budowania aplikacji u¿ywaj±cych libsidplay
Group:		Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the header files for compiling applications that
use libsidplay.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do budowania aplikacji u¿ywaj±cych
biblioteki libsidplay.

%package static
Summary:	Static libsidplay library
Summary(pl):	Statyczna biblioteka libsidplay
Group:		Libraries

%description static
This package contains static version of libsidplay.

%description static -l pl
Ten pakiet zawiera statyczn± wersjê libsidplay.

%prep
%setup -q -n sidplay-libs-%{version}

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc libsidplay/{AUTHORS,ChangeLog,TODO}
%attr(755,root,root) %{_libdir}/libsidplay2.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsidplay2.so
%{_libdir}/libsidplay2.la
%{_includedir}/sidplay
%{_libdir}/pkgconfig/libsidplay2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsidplay2.a
