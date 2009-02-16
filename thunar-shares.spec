Summary:	Samba support for Thunar filemanager
Name:		thunar-shares
Version:	0.16
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://code.google.com/p/thunar-shares/
Source0:	http://thunar-shares.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:	thunar-devel
Requires:	samba-common
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
%dir %{_datadir}/thunar-shares
%{_libdir}/thunarx-1/thunar-shares.la
%{_libdir}/thunarx-1/thunar-shares.so
%{_datadir}/thunar-shares/*.xml
