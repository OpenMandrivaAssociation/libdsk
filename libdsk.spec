%define major 3

%define libname %mklibname dsk %major
%define libname_devel %mklibname -d dsk
%define libname_static_devel %mklibname -s -d dsk

Name:		libdsk
Summary:	A library for accessing floppy drives and disk images transparently
Version:	1.2.1
Release:	4
License:	GPL
Group:		System/Libraries
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
Source:		http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(zlib)

%description
LibDsk is a library intended to give transparent access to floppy drives and
to the "disc image files" used by emulators to represent floppy drives.

%package -n %{libname}
Summary:	A library for accessing floppy drives and disk images transparently
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
LibDsk is a library intended to give transparent access to floppy drives and
to the "disc image files" used by emulators to represent floppy drives.

Install the libdsk package if you need to manipulate DSK files. You should
also install the libdsk-progs package.

%package -n %{libname_devel}
Summary:	Development files for programs which will use the libdsk library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
This package contains the header files and documentation necessary for
development of programs that will use the libdsk library to load and save
DSK format disc image files.

You should install this package if you need to develop programs which will
use the libdsk library functions for loading and saving DSK format disc
image files. You'll also need to install the libdsk package.

%package -n %{libname_static_devel}
Summary:	Static libraries for programs which will use the libdsk library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Provides:	lib%{name}-static-devel = %{version}-%{release}

%description -n %{libname_static_devel}
This package contains the static libraries, necessary for development of
programs that will use the libdsk library to load and save DSK format
disc image files.

You should install this package if you need to develop programs which
will use the libdsk library functions for loading and saving DSK format
disc image files. You'll also need to install the libdsk package.

%package progs
Summary:	Programs for manipulating DSK format disc image files
Group:		Emulators
Requires:	%{libname} = %{version}-%{release}

%description progs
The libdsk-progs package contains various programs for manipulating
DSK format disc image files.

Install this package if you need to manipulate DSK format disc image
files. You'll also need to install the libdsk package.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%doc ChangeLog doc/COPYING doc/README doc/TODO
%{_libdir}/lib*.so.%{major}*

%files -n %{libname_devel}
%doc doc/COPYING doc/cfi.html doc/libdsk.*
%{_libdir}/lib*.so
%{_includedir}/*.h

%files -n %{libname_static_devel}
%doc doc/COPYING
%{_libdir}/lib*.a

%files progs
%doc doc/COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdv2011.0
+ Revision: 609740
- rebuild

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 1.2.1-2mdv2010.1
+ Revision: 508567
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 17 2008 Emmanuel Andry <eandry@mandriva.org> 1.2.1-1mdv2009.0
+ Revision: 272914
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Funda Wang <fwang@mandriva.org> 1.1.14-1mdv2008.0
+ Revision: 67016
- New version 1.14
- new devel pacakge policy


* Fri Mar 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.1.12-1mdv2007.0
+ Revision: 131621
- 1.1.12
- Import libdsk

* Wed May 17 2006 Emmanuel Andry <eandry@mandriva.org> 1.1.10-1mdk
- 1.1.10

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 1.1.8-1mdk
- 1.1.8

* Mon Nov 28 2005 Olivier Thauvin <nanardon@mandriva.org> 1.1.6-2mdk
- reupload

* Mon Oct 17 2005 Olivier Thauvin <nanardon@mandriva.org> 1.1.6-1mdk
- 1.1.6

* Mon May 24 2004 Stefan van der Eijk <stefan@mandrake.org> 1.1.1-3mdk
- rebuild to fix version issue (-2mdk was never released)

* Fri May 14 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.1-2mdk
- major =~ s/2/3/ (Reported by Miguel Barrio Orsikowsky <mik@forward.to>)

* Thu Apr 22 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.1-1mdk
- 1.1.1

