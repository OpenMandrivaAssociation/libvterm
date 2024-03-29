%define major 0
%define oldlibname %mklibname vterm 0
%define libname %mklibname vterm
%define devname %mklibname vterm -d

Name:           libvterm
Version:        0.3.3
Release:        1
Source0:        https://launchpad.net/libvterm/trunk/v%(echo %{version}|cut -d. -f1-2)/+download/libvterm-%{version}.tar.gz
# Libtool is good for nothing and breaks crosscompiling. Let's kill it.
Patch0:		libvterm-0.3.3-libtool-die-die-die.patch
Summary:        An abstract C99 library which implements a VT220 or xterm-like terminal.
License:        MIT
Url:            https://launchpad.net/libvterm

%description
An abstract C99 library which implements a VT220 or xterm-like terminal
emulator.

%package -n	%{libname}
Summary:        Shared library package of libvterm
Group:          System/Libraries
%rename %{oldlibname}

%description -n %{libname}
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It does not use any particular graphics toolkit or
output system. Instead, it invokes callback function pointers that
its embedding program should provide it to draw on its behalf.

%package -n	%{devname}
Summary:        Development files of libvterm
Group:          Development/C
Requires:       %{libname} = %{EVRD}

%description -n	%{devname}
This package contains the development files of libvterm.

%package tools
Summary:        Tools for libvterm

%description tools
This package contains tools for libvterm.

%prep
%autosetup -p1

%build
%setup_compile_flags
%make	PREFIX=%{_prefix} \
	CC="%{__cc}" \
	LIBDIR=%{_libdir}

%install
%make PREFIX=%{_prefix} \
     LIBDIR=%{_libdir} \
     DESTDIR=%{buildroot} \
     install

%files -n %{libname}
%{_libdir}/%{name}.so.*

%files -n %{devname}
%doc LICENSE
%{_includedir}/vterm*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/vterm.pc

%files tools
%{_bindir}/unterm
%{_bindir}/vterm-ctrl
%{_bindir}/vterm-dump
