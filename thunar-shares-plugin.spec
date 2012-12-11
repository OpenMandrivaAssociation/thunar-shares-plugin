Summary:	Samba support for Thunar filemanager
Name:		thunar-shares-plugin
Version:	0.2.0
Release:	6
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
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


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-4mdv2010.1
+ Revision: 543283
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.2.0-3mdv2010.0
+ Revision: 445423
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-2mdv2009.1
+ Revision: 349182
- rebuild whole xfce

* Mon Feb 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 340735
- update to new version 0.2.0
- adapt to new name
- upstream has changed name

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.16-2mdv2009.1
+ Revision: 294893
- rebuild for new Thunar  (Xfce4.6 beta1)

* Mon Oct 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.16-1mdv2009.1
+ Revision: 293344
- add source and spec files
- Created package structure for thunar-shares.

