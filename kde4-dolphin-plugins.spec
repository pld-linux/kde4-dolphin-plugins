#
# TODO:
# - add man files
#
%define		orgname		dolphin-plugins
%define		_state		stable
%define		qtver		4.8.1

Summary:	Dolphin VCS plugins
Name:		kde4-dolphin-plugins
Version:	4.14.3
Release:	1
License:	GPL
Group:		X11/Applications
Group:		X11/Development/Tools
Requires:	kde4-dolphin
Obsoletes:	kde-kio-git
Obsoletes:	kde4-kdesdk-dolphin-plugins
Conflicts:	kde-kio-svn < 4.9.3
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b5c3537e2f1064a5c74a57461dd2c7a3
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
# required for dolphin plugins
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libxslt-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	subversion-devel >= 0.37.0
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gimpdir	%{_datadir}/gimp/2.0
%define		_appdefsdir	%{_datadir}/X11/app-defaults
%define		_emacspkgdir	/usr/share/emacs/%(rpm -q --qf %{V} emacs-common | tr -d '[a-z]')
%define		_xemacspkgdir	/usr/share/xemacs-packages
%define		_zshfcdir	/usr/share/zsh/latest/functions

%description
This package contains plugins that offer integration of various
version control systems in Dolphin.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/fileviewbazaarplugin.so
%attr(755,root,root) %{_libdir}/kde4/fileviewdropboxplugin.so
%attr(755,root,root) %{_libdir}/kde4/fileviewgitplugin.so
%attr(755,root,root) %{_libdir}/kde4/fileviewhgplugin.so
%attr(755,root,root) %{_libdir}/kde4/fileviewsvnplugin.so
%{_datadir}/config.kcfg/fileviewgitpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewhgpluginsettings.kcfg
%{_datadir}/config.kcfg/fileviewsvnpluginsettings.kcfg
%{_datadir}/kde4/services/fileviewbazaarplugin.desktop
%{_datadir}/kde4/services/fileviewdropboxplugin.desktop
%{_datadir}/kde4/services/fileviewgitplugin.desktop
%{_datadir}/kde4/services/fileviewhgplugin.desktop
%{_datadir}/kde4/services/fileviewsvnplugin.desktop
