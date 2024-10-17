%define major 3

%define libname %mklibname dsk %major
%define libname_devel %mklibname -d dsk

Name:		libdsk
Summary:	A library for accessing floppy drives and disk images transparently
Version:	1.3.8
Release:	6
License:	GPL
Group:		System/Libraries
URL:		https://www.seasip.demon.co.uk/Unix/LibDsk/
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
%configure2_5x --disable-static
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

%files progs
%doc doc/COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

