%define upstream_name    X11-GUITest
%define upstream_version 0.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provides GUI testing/interaction facilities
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/X11/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: libx11-devel
BuildRequires: perl-devel
BuildRequires: x11-proto-devel
BuildRequires: libxtst-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl package is intended to facilitate the testing of GUI applications
by means of user emulation. It can be used to test/interact with GUI
applications; which have been built upon the X library or toolkits (i.e.,
GTK+, Xt, Qt, Motif, etc.) that "wrap" the X library's functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
if [ x${DISPLAY} != 'x' ]; then 
    make test
else
    exit 0
fi

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*


