# TODO:
# - use system PEAR [ done, needs tests]
# - add lang packs from http://sourceforge.net/projects/dotmods/
# - check if it works at all...
#
Summary:	PHP web-based project management framework
Summary(pl):	Oparte na PHP i WWW ¶rodowisko do zarz±dzania projektami
Name:		dotproject
Version:	1.0.1
Release:	0.2
License:	BSD
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/dotproject/%{name}_%{version}.tar.gz
# Source0-md5:	7387852573613bb6d4fc4e592b76c69a
Patch0:		%{name}-system_PEAR.patch
URL:		http://sourceforge.net/projects/dotproject/
Requires:	php(gd)
Requires:	php(mysql)
Requires:	php-pear-Date
Requires:	webserver
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir		/usr/share/dotproject

%description
PHP web-based project management framework that includes modules for
companies, projects, tasks (with Gantt charts), forums, files,
calendar, contacts, tickets/helpdesk, multi-language support,
user/module permissions and themes.

%description -l pl
Oparte na PHP i WWW ¶rodowisko do zarz±dzania projektami zawieraj±ce
modu³y dla firm, projektów, zadañ (z wykresami Gantta), forum, plików,
kalendarza, kontaktów, biletów/helpdesku, obs³ugê wielu jêzyków,
uprawnienia u¿ytkowników do modu³ów oraz motywy.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpdir}/{classes,db,files/temp,functions,images,includes,lib,locales,misc,modules,style} \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd/%{name}

install *.php $RPM_BUILD_ROOT%{_phpdir}
install classes/* $RPM_BUILD_ROOT%{_phpdir}/classes
install functions/* $RPM_BUILD_ROOT%{_phpdir}/functions
install includes/* $RPM_BUILD_ROOT%{_phpdir}/includes
install locales/*.{php,html} $RPM_BUILD_ROOT%{_phpdir}/locales

cp -R images/* $RPM_BUILD_ROOT%{_phpdir}/images
cp -R lib/* $RPM_BUILD_ROOT%{_phpdir}/lib
cp -R misc/* $RPM_BUILD_ROOT%{_phpdir}/misc
cp -R modules/* $RPM_BUILD_ROOT%{_phpdir}/modules
cp -R style/* $RPM_BUILD_ROOT%{_phpdir}/style

# Locale:
install -d $RPM_BUILD_ROOT%{_phpdir}/locales/en
install locales/en/* $RPM_BUILD_ROOT%{_phpdir}/locales/en

# play with config - it should be writeable and shouldn't be in /usr:
rm $RPM_BUILD_ROOT%{_phpdir}/includes/config-dist.php
install includes/config-dist.php $RPM_BUILD_ROOT%{_sysconfdir}/httpd/%{name}/config.php
ln -s %{_sysconfdir}/httpd/%{name}/config.php $RPM_BUILD_ROOT%{_phpdir}/includes/config.php

# and remove PEAR's Date class that comes with the archive
rm -rf $RPM_BUILD_ROOT%{_phpdir}/lib/PEAR

%clean
rm -rf $RPM_BUILD_ROOT

#%triggerpostun  -- %{name} <= %{version}
#echo "You have to install %{name}-install package to prepare upgrade!!!"
#echo "For upgrade: http://<your.site.address>/<path>/install/upgrade.php"

%files
%defattr(644,root,root,755)
%doc ChangeLog docs/* db/*.sql
%attr(755,root,http) %dir %{_sysconfdir}/httpd/%{name}
%attr(640,root,http) %config(noreplace) %{_sysconfdir}/httpd/%{name}/config.php
%attr(750,root,http) %dir %{_phpdir}
%attr(640,root,http) %{_phpdir}/*.php
%attr(750,root,http) %dir %{_phpdir}/classes
%attr(640,root,http) %{_phpdir}/classes/*.php
%attr(640,root,http) %{_phpdir}/classes/*.html
%attr(750,root,http) %dir %{_phpdir}/functions
%attr(640,root,http) %{_phpdir}/functions/*
%attr(750,root,http) %dir %{_phpdir}/includes
%attr(640,root,http) %{_phpdir}/includes/*
%attr(750,root,http) %dir %{_phpdir}/images
%attr(640,root,http) %{_phpdir}/images/*.gif
%attr(750,root,http) %dir %{_phpdir}/images/icons
%attr(640,root,http) %{_phpdir}/images/icons/*.gif
%attr(640,root,http) %{_phpdir}/images/icons/*.png
%attr(750,root,http) %dir %{_phpdir}/images/obj
%attr(640,root,http) %{_phpdir}/images/obj/*.gif
%attr(750,root,http) %dir %{_phpdir}/lib
%attr(640,root,http) %{_phpdir}/lib/*
%attr(750,root,http) %dir %{_phpdir}/misc
%attr(640,root,http) %{_phpdir}/misc/*
%attr(750,root,http) %dir %{_phpdir}/modules
%attr(640,root,http) %{_phpdir}/modules/*
%attr(750,root,http) %dir %{_phpdir}/style
%attr(640,root,http)  %{_phpdir}/style/*.html
%attr(750,root,http) %dir %{_phpdir}/style/classic
%attr(750,root,http) %dir %{_phpdir}/style/classic/images
%attr(750,root,http) %dir %{_phpdir}/style/default
%attr(750,root,http) %dir %{_phpdir}/style/default/images
%attr(750,root,http) %dir %{_phpdir}/style/default/images/obj
%attr(640,root,http) %{_phpdir}/style/*/*.php
%attr(640,root,http) %{_phpdir}/style/*/*.html
%attr(640,root,http) %{_phpdir}/style/*/*.css
%attr(640,root,http) %{_phpdir}/style/*/images/*.gif
%attr(640,root,http) %{_phpdir}/style/*/images/*.html
%attr(640,root,http) %{_phpdir}/style/*/images/*.ico
%attr(640,root,http) %{_phpdir}/style/*/images/*.jpg
%attr(640,root,http) %{_phpdir}/style/*/images/*.png
%attr(640,root,http) %{_phpdir}/style/*/images/obj/*
%attr(750,root,http) %dir %{_phpdir}/locales
%attr(640,root,http) %{_phpdir}/locales/*.php
%attr(640,root,http) %{_phpdir}/locales/*.html
%attr(750,root,http) %dir %{_phpdir}/locales/en
%lang(en) %attr(640,root,http) %{_phpdir}/locales/en/*

#%lang(pl) %{_phpdir}/language/lang_polish
#%lang(pl) %{_phpdir}/templates/subSilver/images/lang_polish

#%lang(de) %{_phpdir}/language/lang_german
#%lang(de) %{_phpdir}/templates/subSilver/images/lang_german

#%lang(fr) %{_phpdir}/language/lang_french
#%lang(fr) %{_phpdir}/templates/subSilver/images/lang_french
