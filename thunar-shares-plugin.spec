%define _disable_rebuild_configure 1

Summary:	Samba support for Thunar filemanager
Name:		thunar-shares-plugin
Version:	0.3.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://archive.xfce.org/src/thunar-plugins/thunar-shares-plugin/0.3/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(thunarx-3)
#BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	intltool

Requires:	samba-common

%description
A Thunar file manager extension to share files using Samba.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%{_libdir}/thunarx-3/thunar-shares-plugin.so
