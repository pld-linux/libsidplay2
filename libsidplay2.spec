#
# TODO:
# - fix symlinks to libraries
# - split out resid/hardsid builders as external specs, or find other hacks that will allow building of them(they requries libsidplay2 lib, so its recursive dependency). Lack of them is probably cause of MPD refusing to build with c64's SID support.
# - replace skip_post_check_so with nicer solution

Summary:	A Commodore 64 music player and SID chip emulator library
Summary(pl.UTF-8):	Biblioteka odtwarzająca muzyczki z Commodore 64 i emulująca układ SID
Name:		libsidplay2
Version:	2.1.1
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sidplay2/sidplay-libs-%{version}.tar.gz
# Source0-md5:	7ea0ba5dc1da4604d15eaae001f7d2a7
Patch0:		%{name}-debian_fixes.patch
URL:		http://sidplay2.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so libsidplay2.so.1.0.1 libsidutils.so.0.0.4

%description
Sidplay 2 is the second in the Sidplay series originally developed by
Michael Schwendt. This version is written by Simon White and is cycle
accurate for improved sound reproduction. Sidplay 2 is capable of
playing all C64 mono and stereo file formats.

%description -l pl.UTF-8
Sidplay 2 to druga wersja z serii Sidplay oryginalnie stworzonej przez
Michaela Schwendta. Ta wersja została napisana przez Simona White'a i
jest dokładna co do cyklu w celu zwiększonej wierności reprodukcji
dźwięku. Sidplay 2 może odtwarzać wszystkie formaty plików mono i
stereo z C64.

%package devel
Summary:	Header files for compiling apps that use libsidplay
Summary(pl.UTF-8):	Pliki nagłówkowe do budowania aplikacji używających libsidplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
This package contains the header files for compiling applications that
use libsidplay.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do budowania aplikacji używających
biblioteki libsidplay.

%package static
Summary:	Static libsidplay library
Summary(pl.UTF-8):	Statyczna biblioteka libsidplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static version of libsidplay.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję libsidplay.

%prep
%setup -q -n sidplay-libs-%{version}
%patch0 -p1

%build
cp -f /usr/share/automake/config.* unix
cp -f /usr/share/automake/config.* libsidplay/unix
cp -f /usr/share/automake/config.* libsidutils/unix
cp -f /usr/share/automake/config.* resid
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
%attr(755,root,root) %ghost %{_libdir}/libsidplay2.so.1
%attr(755,root,root) %{_libdir}/libsidplay2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsidutils.so.0
%attr(755,root,root) %{_libdir}/libsidutils.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsidplay2.so
%attr(755,root,root) %{_libdir}/libsidutils.so
%{_libdir}/libhardsid-builder.la
%{_libdir}/libresid-builder.la
%{_libdir}/libsidplay2.la
%{_libdir}/libsidutils.la
%{_includedir}/sidplay
%{_pkgconfigdir}/libsidplay2.pc
%{_pkgconfigdir}/libsidutils.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhardsid-builder.a
%{_libdir}/libresid-builder.a
%{_libdir}/libsidplay2.a
%{_libdir}/libsidutils.a
