Name:    	task-moblin
Version: 	2.1
Release: 	%mkrel 2
Epoch:		1
Summary: 	Metapackage for the Moblin experience
Group:   	Graphical desktop/Other
License:	Various
URL:		http://www.moblin.org
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
Requires:	libgconnman0
Requires:	connman
Requires:	bisho
Requires:	carrick-ng
Requires:	dalston
Requires:	hornsey

# extra
Requires:	dates
Requires:	contacts
Requires:	empathy

%description
Moblin is an open source project focused on building a Linux-based
platform optimized for the next generation of mobile devices including
Netbooks, Mobile Internet Devices, and In-vehicle infotainment systems.

This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal Moblin environment.

%package devel
Summary:	Moblin development metapackage
Group:		Development/Other
Url:		http://www.moblin.org

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for Moblin development environment.

%files

%files devel
