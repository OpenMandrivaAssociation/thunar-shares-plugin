Summary:	Samba support for Thunar filemanager
Name:		thunar-shares-plugin
Version:	0.2.0
Release:	9
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		thunar-shares-plugin-0.2.0-rosa-thunarx-2.patch
BuildRequires:	pkgconfig(thunarx-2)
BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	intltool

# required for patch0
BuildRequires:	xfce4-dev-tools

Requires:	samba-common

%description
A Thunar file manager extension to share files using Samba.

%prep
%setup -q
%patch0 -p1

%build
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.in

# required for patch0
xdt-autogen

%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog NEWS TODO
%{_libdir}/thunarx-2/thunar-shares-plugin.so
