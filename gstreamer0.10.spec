%define name gstreamer0.10
%define oname gstreamer
%define version 0.10.21
%define release %mkrel 1
%define vname %{oname}10

%define major 0.10
%define majorminor 0.10
%define libname %mklibname %{name}_ %{major}
%define libnamedev %mklibname -d %{name}
%define 	_glib2		2.2.0
%define 	_libxml2	2.4.0
%define build_docs 0

Name: 		%name
Summary: 	GStreamer Streaming-media framework runtime
Version: 	%version
Release: 	%release
License: 	LGPL
Group: 		Sound
URL:            http://gstreamer.freedesktop.org/
Source0: 	http://gstreamer.freedesktop.org/src/gstreamer/%{oname}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
BuildRequires: 	glib2-devel >= %_glib2
BuildRequires: 	libxml2-devel >= %_libxml2
BuildRequires:	popt-devel
BuildRequires:	gettext-devel
BuildRequires:  libcheck-devel
BuildRequires:  valgrind
BuildRequires:  chrpath
%ifarch %ix86 
BuildRequires: 	nasm => 0.90
%endif
BuildRequires: 	bison
BuildRequires:  flex
%if %build_docs
BuildRequires: 	gtk-doc >= 0.7
BuildRequires: 	transfig
BuildRequires:  docbook-dtd42-xml
BuildRequires:  ghostscript
BuildRequires:  python-pyxml
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package tools
Summary: GStreamer Streaming-media framework runtime
Group: 	Sound
Provides: %vname-tools = %version-%release
Provides: gstreamer
Obsoletes: gstreamer

%description tools
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package -n %libname
Summary: Libraries for GStreamer streaming-media framework
Group: System/Libraries
Requires: %name-tools >= %version-%release
Provides: libgstreamer%{majorminor} = %version-%release

%description -n %libname
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %libnamedev
Summary: Libraries and include files for GStreamer streaming-media framework
Group: Development/C
Requires: %{libname} = %{version}
Requires: libglib2-devel
Requires: libxml2-devel
Provides: libgstreamer-devel = %version-%release
Provides: gstreamer%{majorminor}-devel = %version-%release
Obsoletes: %mklibname -d %{name}_ 0.10

%description -n %libnamedev
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %oname-%version

%build
%configure2_5x  --enable-debug --disable-dependency-tracking \
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \
  --with-cachedir=%{_var}/cache/%{oname}-%{majorminor} \
  --with-configdir=%{_sysconfdir}/%{oname} \
  --disable-tests --disable-examples --disable-rpath \
%if %build_docs
  --enable-docbook --enable-gtk-doc \
%else	
  --disable-docbook --disable-gtk-doc \
%endif
 --with-html-dir=%_datadir/gtk-doc/html

make

%check
cd tests/check
make check

%install  
rm -rf $RPM_BUILD_ROOT  installed-docs
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_var}/cache/%{oname}-%{majorminor}
#clean the files we don't want to install 
rm -f $RPM_BUILD_ROOT%{_libdir}/%{oname}-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/%{oname}-%{majorminor}/*.a
rm -f %buildroot/%_libdir/*a 
rm -f %buildroot/%{_bindir}/gst-feedback
rm -f %buildroot/%{_bindir}/gst-inspect
rm -f %buildroot/%{_bindir}/gst-launch
rm -f %buildroot/%{_bindir}/gst-md5sum
rm -f %buildroot/%{_bindir}/gst-typefind
rm -f %buildroot/%{_bindir}/gst-xmlinspect
rm -f %buildroot/%{_bindir}/gst-xmllaunch


%find_lang %oname-%majorminor
%if %build_docs
mv %buildroot%_datadir/doc/%oname-%majorminor/ installed-docs
%endif

#gw really remove rpath for rpmlint
chrpath -d %buildroot{%_bindir/gst-{inspect,launch,typefind,xmlinspect,xmllaunch}-0.10,%_libdir/{*.so,%{oname}-%{majorminor}/*.so}}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files tools -f %oname-%majorminor.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS
%dir %{_var}/cache/%{oname}-%{majorminor}
%{_bindir}/gst-feedback-%majorminor
%{_bindir}/gst-inspect-%majorminor
%{_bindir}/gst-launch-%majorminor
%{_bindir}/gst-typefind-%majorminor
%{_bindir}/gst-xmlinspect-%majorminor
%{_bindir}/gst-xmllaunch-%majorminor
%{_mandir}/man1/gst-feedback-%majorminor.1.*
%{_mandir}/man1/gst-inspect-%majorminor.1.*
%{_mandir}/man1/gst-launch-%majorminor.1.*
%{_mandir}/man1/gst-typefind-%majorminor.1.*
%{_mandir}/man1/gst-xmlinspect-%majorminor.1.*
%{_mandir}/man1/gst-xmllaunch-%majorminor.1.*
# gw this must always be in a package named gstreamer-tools
#%files -n gstreamer-tools
#%defattr(-, root, root, -)
#%{_bindir}/gst-feedback
#%{_bindir}/gst-inspect
#%{_bindir}/gst-launch
#%{_bindir}/gst-md5sum
#%{_bindir}/gst-typefind
#%{_bindir}/gst-xmlinspect
#%{_bindir}/gst-xmllaunch


%files -n %libname
%defattr(-, root, root)
%dir %{_libdir}/%{oname}-%{majorminor}
%{_libdir}/libgstbase-%majorminor.so.*
%{_libdir}/libgstcheck-%majorminor.so.*
%{_libdir}/libgstdataprotocol-%majorminor.so.*
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/%{oname}-%{majorminor}/libgstcoreelements.so
%{_libdir}/%{oname}-%{majorminor}/libgstcoreindexers.so

%files -n %libnamedev
%defattr(-, root, root)
%doc ChangeLog
%if %build_docs
%doc installed-docs/*
%endif
%dir %{_includedir}/%{oname}-%{majorminor}
%dir %{_includedir}/%{oname}-%{majorminor}/gst
%{_includedir}/%{oname}-%{majorminor}/gst/*.h
%dir %{_includedir}/%{oname}-%{majorminor}/gst/base/
%{_includedir}/%{oname}-%{majorminor}/gst/base/*.h
%{_includedir}/%{oname}-%{majorminor}/gst/check/
%dir %{_includedir}/%{oname}-%{majorminor}/gst/controller/
%{_includedir}/%{oname}-%{majorminor}/gst/controller/*.h
%dir %{_includedir}/%{oname}-%{majorminor}/gst/dataprotocol/
%{_includedir}/%{oname}-%{majorminor}/gst/dataprotocol/*.h
%{_includedir}/%{oname}-%{majorminor}/gst/net/
%{_libdir}/libgstbase-%majorminor.so
%{_libdir}/libgstcheck-%majorminor.so
%{_libdir}/libgstdataprotocol-%majorminor.so
%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstnet-%{majorminor}.so
%{_libdir}/libgstcontroller-%{majorminor}.so
%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-base-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-check-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-dataprotocol-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-net-%majorminor.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{majorminor}.pc
%if 1
## we specify the API docs as regular files since %docs doesn't fail when
#  files aren't found anymore for RPM >= 4
#  we list all of the files we really need to trap incomplete doc builds
#  then we catch the rest with *, you can safely ignore the errors from this
## gstreamer API
%dir %{_datadir}/gtk-doc/html/%{oname}-%{majorminor}
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/%{oname}-%{majorminor}.devhelp
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/GstBin.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/GstClock.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/GstObject.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/GstPipeline.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/GstPluginFeature.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/%{oname}.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/%{oname}-support.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/GstXML.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/index.html
%{_datadir}/gtk-doc/html/%{oname}-%{majorminor}/index.sgml
## gstreamer-libs API
%dir %{_datadir}/gtk-doc/html/%{oname}-libs-%{majorminor}
%{_datadir}/gtk-doc/html/%{oname}-libs-%{majorminor}/%{oname}-libs-%{majorminor}.devhelp
%{_datadir}/gtk-doc/html/%{oname}-libs-%{majorminor}/%{oname}-libs.html
%{_datadir}/gtk-doc/html/%{oname}-libs-%{majorminor}/index.html
%{_datadir}/gtk-doc/html/%{oname}-libs-%{majorminor}/index.sgml
## this catches all of the rest of the docs we might have forgotten
%{_datadir}/gtk-doc/html/*
%endif


