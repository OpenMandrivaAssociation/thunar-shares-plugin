Summary:	Samba support for Thunar filemanager
Name:		thunar-shares-plugin
Version:	0.2.0
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel
Requires:	samba-common
Obsoletes:	thunar-shares < 0.2.0
Provides:	thunar-shares
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Thunar file manager extension to share files using Samba.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog NEWS TODO
%{_libdir}/thunarx-1/thunar-shares-plugin.la
%{_libdir}/thunarx-1/thunar-shares-plugin.so
