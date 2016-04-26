%define major 0
%define libname %mklibname vterm %{major}
%define devname %mklibname vterm -d

Name:           libvterm
Version:        0~bzr681
Release:        1
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator
License:        MIT
Group:          Development/C
Url:            https://launchpad.net/libvterm
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libtool

%description
An abstract C99 library which implements a VT220 or xterm-like terminal
emulator.

%package -n	%{libname}
Summary:        Shared library package of libvterm
Group:          System/Libraries

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
%setup -q

%build
%setup_compile_flags
%make PREFIX=%{_prefix} \
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
