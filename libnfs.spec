Summary:	Client library for accessing NFS shares over network
Summary(pl.UTF-8):	Biblioteka kliencka do dostępu do udziałów NFS poprzez sieć
Name:		libnfs
Version:	5.0.2
Release:	1
# library code is LGPL, protocol definition files are BSD licensed
License:	LGPL v2.1+ and BSD
Group:		Libraries
#Source0Download: https://github.com/sahlberg/libnfs/tags
Source0:	https://github.com/sahlberg/libnfs/archive/libnfs-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	115034aab322d05235a9555d057f8b14
URL:		https://github.com/sahlberg/libnfs
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client library for accessing NFS shares over network.

%description -l pl.UTF-8
Biblioteka kliencka do dostępu do udziałów NFS poprzez sieć.

%package devel
Summary:	Header files for libnfs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnfs
License:	LGPL v2.1+ and BSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and examples for libnfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz przykłady dla biblioteki libnfs.

%package static
Summary:	Static libnfs library
Summary(pl.UTF-8):	Statyczna biblioteka libnfs
License:	LGPL v2.1+ and BSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnfs library.

%description static -l pl.UTF-8
Statyczna biblioteka libnfs.

%package examples
Summary:	Example code for libnfs library
Summary(pl.UTF-8):	Przykładowy kod źródłowy wykorzystujący bibliotekę libnfs
License:	GPL v3+
Group:		Documentation

%description examples
Example code for libnfs library.

%description examples -l pl.UTF-8
Przykładowy kod źródłowy wykorzystujący bibliotekę libnfs.

%package utils
Summary:	Utils for accessing NFS servers
Summary(pl.UTF-8):	Narzędzia służące do dostępu do serwerów NFS
License:	GPL v3+
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description utils
Simple client programs for accessing NFS servers using libnfs.

%description utils -l pl.UTF-8
Proste programy klienckie służące do dostępu do serwerów NFS przy
użyciu biblioteki libnfs.

%prep
%setup -q -n %{name}-libnfs-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnfs.la

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING LICENCE-BSD.txt README
%attr(755,root,root) %{_libdir}/libnfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnfs.so.14

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnfs.so
%{_includedir}/nfsc
%{_pkgconfigdir}/libnfs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnfs.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nfs-cat
%attr(755,root,root) %{_bindir}/nfs-cp
%attr(755,root,root) %{_bindir}/nfs-ls
%attr(755,root,root) %{_bindir}/nfs-stat
%{_mandir}/man1/nfs-cat.1*
%{_mandir}/man1/nfs-cp.1*
%{_mandir}/man1/nfs-ls.1*
