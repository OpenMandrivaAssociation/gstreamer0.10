%define oname	gst-plugins-base
%define bname	gstreamer%{api}
%define api	0.10
%define major	0
%define libapp %mklibname gstapp %{api} %{major}
%define girapp %mklibname gstapp-gir %{api}
%define libaudio %mklibname gstaudio %{api} %{major}
%define giraudio %mklibname gstaudio-gir %{api}
%define libcdda	%mklibname gstcdda %{api} %{major}
%define libfft %mklibname gstfft %{api} %{major}
%define girfft %mklibname gstfft-gir %{api}
%define libinterfaces	%mklibname gstinterfaces %{api} %{major}
%define girinterfaces	%mklibname gstinterfaces-gir %{api}
%define libnetbuffer	%mklibname gstnetbuffer %{api} %{major}
%define girnetbuffer	%mklibname gstnetbuffer-gir %{api}
%define libpbutils %mklibname gstpbutils %{api} %{major}
%define girpbutils %mklibname gstpbutils-gir %{api}
%define libriff %mklibname gstriff %{api} %{major}
%define girriff %mklibname gstriff-gir %{api}
%define librtp %mklibname gstrtp %{api} %{major}
%define girrtp %mklibname gstrtp-gir %{api}
%define librtsp %mklibname gstrtsp %{api} %{major}
%define girrtsp %mklibname gstrtsp-gir %{api}
%define libsdp %mklibname gstsdp %{api} %{major}
%define girsdp %mklibname gstsdp-gir %{api}
%define libtag %mklibname gsttag %{api} %{major}
%define girtag %mklibname gsttag-gir %{api}
%define libvideo %mklibname gstvideo %{api} %{major}
%define girvideo %mklibname gstvideo-gir %{api}

%define libname %mklibname gstreamer-plugins-base %{api} %{major}
%define devname %mklibname gstreamer-plugins-base %{api} -d
%define girname %mklibname gstreamer-plugins-base-gir %{api}
%define rosalib %mklibname gstreamer-plugins-base %{api}

%define build_libvisual 1
%define build_docs 0
%define build_qtexamples 0
%define enable_check 0

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-base
Version:	0.10.36
Release:	9
License:	LGPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gst-plugins-base/%{api}/%{oname}-%{version}.tar.xz
Patch0:	align.patch

BuildRequires:	%{bname}-tools < 1.0
BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.36
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xv)
%if %{build_libvisual}
BuildRequires:	pkgconfig(libvisual-0.4) >= 0.4
%endif
%ifarch %ix86
BuildRequires:	nasm => 0.90
%endif
%ifnarch %arm %mips
BuildRequires:	valgrind
%endif
%if %{build_qtexamples}
BuildRequires:	qt4-devel
%endif
%if %{build_docs}
BuildRequires:	gtk-doc
%endif
%if %{enable_check}
#gw we need some fonts for the tests
BuildRequires:	fonts-ttf-dejavu
%endif

# md legacy provides, do_not remove until everything 
# that requires the provide is cleaned up
Provides:	%{bname}-plugins
Suggests:	gst-install-plugins-helper
Conflicts:	%{bname}-plugins-bad < 0.10.10

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of reference plugins, base classes for other
plugins, and helper libraries:
 * device plugins:	x(v)imagesink, alsa, v4lsrc, cdparanoia
 * containers:	ogg
 * codecs:	vorbis, theora
 * text:	textoverlay, subparse
 * sources:	audiotestsrc, videotestsrc, gnomevfssrc
 * network:	tcp
 * typefind
 * audio processing:	audioconvert, adder, audiorate, audioscale, volume
 * visualisation:	libvisual
 * video processing:	ffmpegcolorspace
 * aggregate elements:	decodebin, playbin

%package -n %{libapp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8
Obsoletes:	%mklibname gstreamer-plugins-base0.10
%rename		%{rosalib}

%description -n %{libapp}
This package contain a shared library for %{name}.

%package -n %{girapp}
Summary:	GObject Introspection interface libraries for %{libapp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8
Conflicts:	%mklibname gstreamer-plugins-base 0.10 < 0.10.35-2

%description -n %{girapp}
GObject Introspection interface libraries for %{libapp}.

%package -n %{libaudio}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libaudio}
This package contain a shared library for %{name}.

%package -n %{giraudio}
Summary:	GObject Introspection interface libraries for %{libaudio}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{giraudio}
GObject Introspection interface libraries for %{libaudio}.

%package -n %{libcdda}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libcdda}
This package contain a shared library for %{name}.

%package -n %{libfft}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libfft}
This package contain a shared library for %{name}.

%package -n %{girfft}
Summary:	GObject Introspection interface libraries for %{libfft}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girfft}
GObject Introspection interface libraries for %{libfft}.

%package -n %{libinterfaces}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libinterfaces}
This package contain a shared library for %{name}.

%package -n %{girinterfaces}
Summary:	GObject Introspection interface libraries for %{libfft}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girinterfaces}
GObject Introspection interface libraries for %{libinterfaces}.

%package -n %{libnetbuffer}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libnetbuffer}
This package contain a shared library for %{name}.

%package -n %{girnetbuffer}
Summary:	GObject Introspection interface libraries for %{libfft}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girnetbuffer}
GObject Introspection interface libraries for %{libnetbuffer}.

%package -n %{libpbutils}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libpbutils}
This package contain a shared library for %{name}.

%package -n %{girpbutils}
Summary:	GObject Introspection interface libraries for %{libpbutils}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girpbutils}
GObject Introspection interface libraries for %{libpbutils}.

%package -n %{libriff}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libriff}
This package contain a shared library for %{name}.

%package -n %{girriff}
Summary:	GObject Introspection interface libraries for %{libriff}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girriff}
GObject Introspection interface libraries for %{libriff}.

%package -n %{librtp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{librtp}
This package contain a shared library for %{name}.

%package -n %{girrtp}
Summary:	GObject Introspection interface libraries for %{librtp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girrtp}
GObject Introspection interface libraries for %{librtp}.

%package -n %{librtsp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{librtsp}
This package contain a shared library for %{name}.

%package -n %{girrtsp}
Summary:	GObject Introspection interface libraries for %{librtsp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girrtsp}
GObject Introspection interface libraries for %{librtsp}.

%package -n %{libsdp}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libsdp}
This package contain a shared library for %{name}.

%package -n %{girsdp}
Summary:	GObject Introspection interface libraries for %{libsdp}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girsdp}
GObject Introspection interface libraries for %{libsdp}.

%package -n %{libtag}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libtag}
This package contain a shared library for %{name}.

%package -n %{girtag}
Summary:	GObject Introspection interface libraries for %{libtag}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base-gir0.10 < 0.10.36-8

%description -n %{girtag}
GObject Introspection interface libraries for %{libtag}.

%package -n %{libvideo}
Group:		System/Libraries
Summary:	GStreamer plugin libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{libvideo}
This package contain a shared library for %{name}.

%package -n %{girvideo}
Summary:	GObject Introspection interface libraries for %{libvideo}
Group:		System/Libraries
Obsoletes:	%{_lib}gstreamer-plugins-base0.10_0 < 0.10.36-8

%description -n %{girvideo}
GObject Introspection interface libraries for %{libvideo}.

%package -n %{devname}
Summary:	GStreamer Plugin Library Headers
Group:		Development/C
Requires:   %{libapp} = %{version}-%{release}
Requires:   %{girapp} = %{version}-%{release}
Requires:   %{libaudio} = %{version}-%{release}
Requires:   %{giraudio} = %{version}-%{release}
Requires:   %{libcdda} = %{version}-%{release}
Requires:   %{libfft} = %{version}-%{release}
Requires:   %{girfft} = %{version}-%{release}
Requires:   %{libinterfaces} = %{version}-%{release}
Requires:   %{girinterfaces} = %{version}-%{release}
Requires:   %{libnetbuffer} = %{version}-%{release}
Requires:   %{girnetbuffer} = %{version}-%{release}
Requires:   %{libpbutils} = %{version}-%{release}
Requires:   %{girpbutils} = %{version}-%{release}
Requires:   %{libriff} = %{version}-%{release}
Requires:   %{girriff} = %{version}-%{release}
Requires:   %{librtp} = %{version}-%{release}
Requires:   %{girrtp} = %{version}-%{release}
Requires:   %{librtsp} = %{version}-%{release}
Requires:   %{girrtsp} = %{version}-%{release}
Requires:   %{libsdp} = %{version}-%{release}
Requires:   %{girsdp} = %{version}-%{release}
Requires:   %{libtag} = %{version}-%{release}
Requires:   %{girtag} = %{version}-%{release}
Requires:   %{girvideo} = %{version}-%{release}
Requires:   %{libvideo} = %{version}-%{release}
%if %{enable_check}
# gw is required at build time for make check
Requires:	%{name} = %{version}-%{release}
%endif
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%package -n %{bname}-gnomevfs
Summary:	GStreamer plug-ins for GNOME VFS input and output
Group:		System/Libraries
Requires:	gnome-vfs2 > 1.9.4.00
Requires:	%{name} = %{version}-%{release}

%description -n %{bname}-gnomevfs
Plug-Ins for reading and writing through GNOME VFS.

%package -n %{bname}-cdparanoia
Summary:	Gstreamer plugin for CD audio input using CDParanoia IV
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description -n %{bname}-cdparanoia
Plugin for ripping audio tracks using cdparanoia under GStreamer

%if %{build_libvisual}
%package -n %{bname}-libvisual
Summary:	GStreamer visualisations plug-in based on libvisual
Group:		Video
Requires:	%{name} = %{version}-%{release}

%description -n %{bname}-libvisual
This plugin makes visualisations based on libvisual available for
GStreamer applications.
%endif

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-experimental \
	--with-package-name='%{vendor} %{name} package' \
	--with-package-origin='%{disturl}' \
	--enable-libvisual

%make

%if %{enable_check}
%check
cd tests/check
#gw check fail with a gconf error in 0.10.21
%make check
%endif

%install
%makeinstall_std

%find_lang %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS README NEWS
%{_bindir}/gst-discoverer-%{api}
%{_bindir}/gst-visualise-%{api}
%dir %{_datadir}/gst-plugins-base
%{_datadir}/gst-plugins-base/license-translations.dict
%{_mandir}/man1/gst-visualise-%{api}.1*
%{_libdir}/gstreamer-%{api}/libgstffmpegcolorspace.so
# non-core plugins without external dependencies
%{_libdir}/gstreamer-%{api}/libgstapp.so
%{_libdir}/gstreamer-%{api}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{api}/libgstaudiorate.so
%{_libdir}/gstreamer-%{api}/libgstaudioresample.so
%{_libdir}/gstreamer-%{api}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{api}/libgstdecodebin.so
%{_libdir}/gstreamer-%{api}/libgstdecodebin2.so
%{_libdir}/gstreamer-%{api}/libgstencodebin.so
%{_libdir}/gstreamer-%{api}/libgstgdp.so
%{_libdir}/gstreamer-%{api}/libgstgio.so
%{_libdir}/gstreamer-%{api}/libgstpango.so
%{_libdir}/gstreamer-%{api}/libgstplaybin.so
%{_libdir}/gstreamer-%{api}/libgstsubparse.so
%{_libdir}/gstreamer-%{api}/libgsttcp.so
%{_libdir}/gstreamer-%{api}/libgstvolume.so
%{_libdir}/gstreamer-%{api}/libgstadder.so
%{_libdir}/gstreamer-%{api}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{api}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{api}/libgsttheora.so
%{_libdir}/gstreamer-%{api}/libgstogg.so
%if %mdkversion < 201100
%{_libdir}/gstreamer-%{api}/libgstvideo4linux.so
%endif
%{_libdir}/gstreamer-%{api}/libgstvideorate.so
%{_libdir}/gstreamer-%{api}/libgstvideoscale.so
%{_libdir}/gstreamer-%{api}/libgstvorbis.so
%{_libdir}/gstreamer-%{api}/libgstximagesink.so
%{_libdir}/gstreamer-%{api}/libgstxvimagesink.so
%{_libdir}/gstreamer-%{api}/libgstalsa.so

%files -n %{libapp}
%{_libdir}/libgstapp-%{api}.so.%{major}*

%files -n %{libaudio}
%{_libdir}/libgstaudio-%{api}.so.%{major}*

%files -n %{libcdda}
%{_libdir}/libgstcdda-%{api}.so.%{major}*

%files -n %{libfft}
%{_libdir}/libgstfft-%{api}.so.%{major}*

%files -n %{libinterfaces}
%{_libdir}/libgstinterfaces-%{api}.so.%{major}*

%files -n %{libnetbuffer}
%{_libdir}/libgstnetbuffer-%{api}.so.%{major}*

%files -n %{libpbutils}
%{_libdir}/libgstpbutils-%{api}.so.%{major}*

%files -n %{libriff}
%{_libdir}/libgstriff-%{api}.so.%{major}*

%files -n %{librtp}
%{_libdir}/libgstrtp-%{api}.so.%{major}*

%files -n %{librtsp}
%{_libdir}/libgstrtsp-%{api}.so.%{major}*

%files -n %{libsdp}
%{_libdir}/libgstsdp-%{api}.so.%{major}*

%files -n %{libtag}
%{_libdir}/libgsttag-%{api}.so.%{major}*

%files -n %{libvideo}
%{_libdir}/libgstvideo-%{api}.so.%{major}*

%files -n %{girapp}
%{_libdir}/girepository-1.0/GstApp-%{api}.typelib

%files -n %{giraudio}
%{_libdir}/girepository-1.0/GstAudio-%{api}.typelib

%files -n %{girfft}
%{_libdir}/girepository-1.0/GstFft-%{api}.typelib

%files -n %{girinterfaces}
%{_libdir}/girepository-1.0/GstInterfaces-%{api}.typelib

%files -n %{girnetbuffer}
%{_libdir}/girepository-1.0/GstNetbuffer-%{api}.typelib

%files -n %{girpbutils}
%{_libdir}/girepository-1.0/GstPbutils-%{api}.typelib

%files -n %{girriff}
%{_libdir}/girepository-1.0/GstRiff-%{api}.typelib

%files -n %{girrtp}
%{_libdir}/girepository-1.0/GstRtp-%{api}.typelib

%files -n %{girrtsp}
%{_libdir}/girepository-1.0/GstRtsp-%{api}.typelib

%files -n %{girsdp}
%{_libdir}/girepository-1.0/GstSdp-%{api}.typelib

%files -n %{girtag}
%{_libdir}/girepository-1.0/GstTag-%{api}.typelib

%files -n %{girvideo}
%{_libdir}/girepository-1.0/GstVideo-%{api}.typelib

%files -n %{devname}
%doc docs/libs/html docs/plugins/html
%{_includedir}/gstreamer-%{api}/gst/app/
%{_includedir}/gstreamer-%{api}/gst/audio
%{_includedir}/gstreamer-%{api}/gst/cdda/
%{_includedir}/gstreamer-%{api}/gst/fft
%{_includedir}/gstreamer-%{api}/gst/interfaces
%{_includedir}/gstreamer-%{api}/gst/netbuffer
%{_includedir}/gstreamer-%{api}/gst/pbutils
%{_includedir}/gstreamer-%{api}/gst/riff
%{_includedir}/gstreamer-%{api}/gst/rtsp
%{_includedir}/gstreamer-%{api}/gst/sdp
%{_includedir}/gstreamer-%{api}/gst/tag/
%{_includedir}/gstreamer-%{api}/gst/video/
%{_includedir}/gstreamer-%{api}/gst/floatcast/
%{_includedir}/gstreamer-%{api}/gst/rtp
%{_libdir}/pkgconfig/gstreamer-app-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-audio-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-cdda-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-fft-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-floatcast-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-interfaces-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-netbuffer-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-pbutils-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-base-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-riff-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-rtp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-rtsp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-sdp-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-tag-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-video-%{api}.pc
%{_libdir}/libgstaudio-%{api}.so
%{_libdir}/libgstapp-%{api}.so
%{_libdir}/libgstcdda-%{api}.so
%{_libdir}/libgstfft-%{api}.so
%{_libdir}/libgstinterfaces-%{api}.so
%{_libdir}/libgstnetbuffer-%{api}.so
%{_libdir}/libgstpbutils-%{api}.so
%{_libdir}/libgstriff-%{api}.so
%{_libdir}/libgstrtp-%{api}.so
%{_libdir}/libgstrtsp-%{api}.so
%{_libdir}/libgsttag-%{api}.so
%{_libdir}/libgstsdp-%{api}.so
%{_libdir}/libgstvideo-%{api}.so
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/GstApp-%{api}.gir
%{_datadir}/gir-1.0/GstAudio-%{api}.gir
%{_datadir}/gir-1.0/GstFft-%{api}.gir
%{_datadir}/gir-1.0/GstInterfaces-%{api}.gir
%{_datadir}/gir-1.0/GstNetbuffer-%{api}.gir
%{_datadir}/gir-1.0/GstPbutils-%{api}.gir
%{_datadir}/gir-1.0/GstRiff-%{api}.gir
%{_datadir}/gir-1.0/GstRtp-%{api}.gir
%{_datadir}/gir-1.0/GstRtsp-%{api}.gir
%{_datadir}/gir-1.0/GstSdp-%{api}.gir
%{_datadir}/gir-1.0/GstTag-%{api}.gir
%{_datadir}/gir-1.0/GstVideo-%{api}.gir

%files -n %{bname}-gnomevfs
%{_libdir}/gstreamer-%{api}/libgstgnomevfs.so

%files -n %{bname}-cdparanoia
%{_libdir}/gstreamer-%{api}/libgstcdparanoia.so

%if %{build_libvisual}
%files -n %{bname}-libvisual
%{_libdir}/gstreamer-%{api}/libgstlibvisual.so
%endif

