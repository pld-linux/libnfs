Summary:	Client library for accessing NFS shares over network
Summary(pl.UTF-8):	Biblioteka kliencka do dostępu do udziałów NFS poprzez sieć
Name:		libnfs
Version:	1.9.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://sites.google.com/site/libnfstarballs/li/%{name}-%{version}.tar.gz
# Source0-md5:	a07656eeca58ad8d4870da546745628a
URL:		https://github.com/sahlberg/libnfs
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libnfs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnfs.

%package static
Summary:	Static libnfs library
Summary(pl.UTF-8):	Statyczna biblioteka libnfs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnfs library.

%description static -l pl.UTF-8
Statyczna biblioteka libnfs.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnfs.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libnfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnfs.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnfs.so
%{_includedir}/nfsc
%{_pkgconfigdir}/libnfs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnfs.a
