%define	oname	gstreamer

%define major	0
%define api	0.10
%define libname		%mklibname %{name}_ %{major}
%define libgstbase	%mklibname gstbase%{api}_ %{major}
%define libgstcheck	%mklibname gstcheck%{api}_ %{major}
%define libgstcontroller	%mklibname gstcontroller%{api}_ %{major}
%define libgstdataprocol	%mklibname gstdataprocol%{api}_ %{major}
%define libgstnet	%mklibname gstnet%{api}_ %{major}
%define girname		%mklibname gst-gir %{api}
%define devname	%mklibname -d %{name}

%bcond_with	docs
%bcond_with	bootstrap

Name:		gstreamer%{api}
Summary: 	GStreamer Streaming-media framework runtime
Version: 	0.10.36
Release: 	8
License: 	LGPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/gstreamer/%{api}/%{oname}-%{version}.tar.xz
Patch0:		gstreamer-inspect-rpm-format.patch

BuildRequires:	bison
BuildRequires:	chrpath
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(popt)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
BuildRequires:	pkgconfig(valgrind)
%endif
%if %{with docs}
BuildRequires:	gtk-doc >= 0.7
BuildRequires:	transfig
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-dtd412-xml
BuildRequires:	ghostscript
BuildRequires:	python-pyxml
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package	tools
Summary:	GStreamer Streaming-media framework runtime
Group:		Sound
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2
%rename		gstreamer

%description	tools
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package -n	%{libname}
Summary:	Library for GStreamer streaming-media framework
Group:		System/Libraries
Suggests:	%{name}-tools >= %{EVRD}
Obsoletes:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n	%{libname}
This package contains the library for %{name}.

%package -n	%{libgstbase}
Summary:	Library for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n	%{libgstbase}
This package contains the library for %{name}base.

%package -n	%{libgstcheck}
Summary:	Library for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n	%{libgstcheck}
This package contains the library for %{name}check.

%package -n	%{libgstcontroller}
Summary:	Library for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n	%{libgstcontroller}
This package contains the library for %{name}controller.

%package -n	%{libgstdataprocol}
Summary:	Library for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n %{libgstdataprocol}
This package contains the library for %{name}dataprocol.

%package -n	%{libgstnet}
Summary:	Library for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n	%{libgstnet}
This package contains the library for %{name}net.

%if !%{with bootstrap}
%package -n	%{girname}
Summary:	GObject Introspection interface libraries for %{name}
Group:		System/Libraries
Conflicts:	%mklibname %{oname} 0.10 0.10 < 0.10.35-2

%description -n %{girname}
GObject Introspection interface libraries for %{name}.
%endif

%package -n	%{devname}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libgstbase} = %{version}-%{release}
Requires:	%{libgstcheck} = %{version}-%{release}
Requires:	%{libgstcontroller} = %{version}-%{release}
Requires:	%{libgstdataprocol} = %{version}-%{release}
Requires:	%{libgstnet} = %{version}-%{release}
%if !%{with bootstrap}
Requires:	%{girname} = %{version}-%{release}
%endif
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-debug \
	--with-package-name='%{distribution} %{name} package' \
	--with-package-origin='%{disturl}' \
	--disable-tests \
	--disable-examples \
%if %{with bootstrap}
	--enable-introspection=no \
%endif
%if %{with docs}
	--enable-docbook \
	--enable-gtk-doc \
%else	
	--disable-docbook \
	--disable-gtk-doc \
%endif
%ifarch %{mips}
	--disable-valgrind \
%endif
	--with-html-dir=%{_datadir}/gtk-doc/html

%make

%check
#cd tests/check
#make check

%install  
%makeinstall_std
mkdir -p %{buildroot}%{_var}/cache/%{oname}-%{api}
#clean the files we don't want to install 
rm -f %{buildroot}%{_bindir}/gst-feedback
rm -f %{buildroot}%{_bindir}/gst-inspect
rm -f %{buildroot}%{_bindir}/gst-launch
rm -f %{buildroot}%{_bindir}/gst-md5sum
rm -f %{buildroot}%{_bindir}/gst-typefind
rm -f %{buildroot}%{_bindir}/gst-xmlinspect
rm -f %{buildroot}%{_bindir}/gst-xmllaunch

%find_lang %{oname}-%{api}

#gw really remove rpath for rpmlint
chrpath -d %{buildroot}{%{_bindir}/gst-{inspect,launch,typefind,xmlinspect,xmllaunch}-0.10,%{_libdir}/{*.so,%{oname}-%{api}/*.so}}

%files tools -f %{oname}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%dir %{_var}/cache/%{oname}-%{api}
%{_bindir}/gst-feedback-%{api}
%{_bindir}/gst-inspect-%{api}
%{_bindir}/gst-launch-%{api}
%{_bindir}/gst-typefind-%{api}
%{_bindir}/gst-xmlinspect-%{api}
%{_bindir}/gst-xmllaunch-%{api}
%dir %{_libdir}/%{oname}-%{api}
%{_libdir}/%{oname}-%{api}/gst-plugin-scanner
%{_libdir}/%{oname}-%{api}/libgstcoreelements.so
%{_libdir}/%{oname}-%{api}/libgstcoreindexers.so
%{_mandir}/man1/gst-feedback-%{api}.1*
%{_mandir}/man1/gst-inspect-%{api}.1*
%{_mandir}/man1/gst-launch-%{api}.1*
%{_mandir}/man1/gst-typefind-%{api}.1*
%{_mandir}/man1/gst-xmlinspect-%{api}.1*
%{_mandir}/man1/gst-xmllaunch-%{api}.1*

%files -n %{libname}
%{_libdir}/libgstreamer-%{api}.so.%{major}*

%files -n %{libgstbase}
%{_libdir}/libgstbase-%{api}.so.%{major}*

%files -n %{libgstcheck}
%{_libdir}/libgstcheck-%{api}.so.%{major}*

%files -n %{libgstcontroller}
%{_libdir}/libgstcontroller-%{api}.so.%{major}*

%files -n %{libgstdataprocol}
%{_libdir}/libgstdataprotocol-%{api}.so.%{major}*

%files -n %{libgstnet}
%{_libdir}/libgstnet-%{api}.so.%{major}*

%if !%{with bootstrap}
%files -n %{girname}
%{_libdir}/girepository-1.0/Gst-%{api}.typelib
%{_libdir}/girepository-1.0/GstBase-%{api}.typelib
%{_libdir}/girepository-1.0/GstCheck-%{api}.typelib
%{_libdir}/girepository-1.0/GstController-%{api}.typelib
%{_libdir}/girepository-1.0/GstNet-%{api}.typelib
%endif

%files -n %{devname}
%doc ChangeLog
%if %{with docs}
%doc %{_datadir}/doc/%{oname}-%{api}
%endif
%dir %{_includedir}/%{oname}-%{api}
%dir %{_includedir}/%{oname}-%{api}/gst
%{_includedir}/%{oname}-%{api}/gst/*.h
%dir %{_includedir}/%{oname}-%{api}/gst/base/
%{_includedir}/%{oname}-%{api}/gst/base/*.h
%{_includedir}/%{oname}-%{api}/gst/check/
%dir %{_includedir}/%{oname}-%{api}/gst/controller/
%{_includedir}/%{oname}-%{api}/gst/controller/*.h
%dir %{_includedir}/%{oname}-%{api}/gst/dataprotocol/
%{_includedir}/%{oname}-%{api}/gst/dataprotocol/*.h
%{_includedir}/%{oname}-%{api}/gst/net/
%{_libdir}/libgstbase-%{api}.so
%{_libdir}/libgstcheck-%{api}.so
%{_libdir}/libgstdataprotocol-%{api}.so
%{_libdir}/libgstreamer-%{api}.so
%{_libdir}/libgstnet-%{api}.so
%{_libdir}/libgstcontroller-%{api}.so
%{_libdir}/pkgconfig/gstreamer-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-base-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-check-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-dataprotocol-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-net-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{api}.pc
%{_datadir}/aclocal/gst-element-check-%{api}.m4
%{_datadir}/gtk-doc/html/%{oname}-%{api}/
%{_datadir}/gtk-doc/html/%{oname}-libs-%{api}/
%{_datadir}/gtk-doc/html/%{oname}-plugins-%{api}
%if !%{with bootstrap}
%{_datadir}/gir-1.0/Gst-%{api}.gir
%{_datadir}/gir-1.0/GstBase-%{api}.gir
%{_datadir}/gir-1.0/GstCheck-%{api}.gir
%{_datadir}/gir-1.0/GstController-%{api}.gir
%{_datadir}/gir-1.0/GstNet-%{api}.gir
%endif
