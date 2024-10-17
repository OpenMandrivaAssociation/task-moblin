Name:    	task-moblin
Version: 	2.1
Release: 	%mkrel 8
Summary: 	Metapackage for the Moblin experience
Group:   	Graphical desktop/Other
License:	Various
URL:		https://www.moblin.org
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

# moblin stuff
Requires:	moblin-bookmarks
Requires:       moblin-ux-settings
Requires:	moblin-cursor-theme
Requires:	moblin-mutter
Requires:	moblin-session
Requires:	moblin-user-skel
Requires:	moblin-web-browser
Requires:	connman
Requires:	bisho
Requires:	carrick-ng
Requires:	dalston
Requires:	hornsey

# extra
Requires:	dates
Requires:	contacts
Requires:	empathy
Requires:	bluez-pin

Suggests:	gdm
Suggests:	halevt-user

%description
Moblin is an open source project focused on building a Linux-based
platform optimized for the next generation of mobile devices including
Netbooks, Mobile Internet Devices, and In-vehicle infotainment systems.

This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Moblin environment.

%package devel
Summary:	Moblin development metapackage
Group:		Development/Other
Url:		https://www.moblin.org

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Moblin development environment.

%files

%files devel


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1-8mdv2011.0
+ Revision: 615112
- the mass rebuild of 2010.1 packages

* Mon Dec 21 2009 Olivier Blin <oblin@mandriva.com> 2.1-7mdv2010.1
+ Revision: 480569
- use halevt-user for removable automount

* Fri Nov 13 2009 Caio Begotti <caio1982@mandriva.org> 2.1-6mdv2010.1
+ Revision: 465783
- fix requires for teuf

* Tue Nov 10 2009 Caio Begotti <caio1982@mandriva.org> 2.1-5mdv2010.1
+ Revision: 464256
- fix requires for dams <3

* Wed Oct 21 2009 Olivier Blin <oblin@mandriva.com> 2.1-4mdv2010.0
+ Revision: 458519
- suggest gdm

* Tue Oct 13 2009 Olivier Blin <oblin@mandriva.com> 2.1-3mdv2010.0
+ Revision: 457123
- do not require unused libgconnman0
  (and the name was invalid on x86_64, #54536)

* Thu Oct 08 2009 Olivier Blin <oblin@mandriva.com> 2.1-2mdv2010.0
+ Revision: 456091
- remove incorrect epoch
- require empathy

* Wed Oct 07 2009 Caio Begotti <caio1982@mandriva.org> 1:2.1-1mdv2010.0
+ Revision: 455736
- imported package task-moblin


