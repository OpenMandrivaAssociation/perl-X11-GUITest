%define upstream_name X11-GUITest
%define upstream_version 0.25

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Provides GUI testing/interaction facilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/X11/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	pkgconfig(xextproto)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xi)

%description
This Perl package is intended to facilitate the testing of GUI applications
by means of user emulation. It can be used to test/interact with GUI
applications; which have been built upon the X library or toolkits (i.e.,
GTK+, Xt, Qt, Motif, etc.) that "wrap" the X library's functionality.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
if [ x${DISPLAY} != 'x' ]; then 
    make test
else
    exit 0
fi

%install
%makeinstall_std

%files
%doc docs/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
