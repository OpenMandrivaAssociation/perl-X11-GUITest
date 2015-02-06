%define upstream_name X11-GUITest
%define upstream_version 0.28

%define debug_package %{nil}

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

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


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.250.0-2
+ Revision: 773706
- add pkgconfig(xi) to buildrequires
- use pkgconfig() deps for buildsrequires
- clean out spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1
+ Revision: 685757
- new version

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1
+ Revision: 672883
- update to new version 0.24

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1
+ Revision: 660024
- update to new version 0.23

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 629522
- update to new version 0.22

* Wed Jul 21 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 556563
- adding missing buildrequires:

* Tue Jun 30 2009 Olivier Thauvin <nanardon@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 390985
- don't run test if no X11 detected
- buildrequires
- import perl-X11-GUITest


* Tue Jun 30 2009 cpan2dist 0.21-1mdv
- initial mdv release, generated with cpan2dist



