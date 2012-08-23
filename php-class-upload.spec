%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.2.0
%define		pkgname	class-upload
Summary:	PHP Class to manager file uploads
Name:		php-class-upload
Version:	0.29
Release:	3
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://www.verot.net/download/class.upload.php/class.upload.tar.gz
# Source0-md5:	62ca1de1543dc5a197652b3409a1315e
URL:		http://www.verot.net/php_class_upload.htm
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.533
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php(pcre)
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}
%define		_phpdocdir		%{_docdir}/phpdoc

%description
This PHP script uploads files and manipulates images very easily.

The perfect script to generate thumbnails or create a photo gallery!
It can convert, resize and work on uploaded images in many ways, add
labels, watermarks and reflections and other image editing features.
You can use it for files uploaded through an HTML form, a Flash
uploader, or on local files.

%package phpdoc
Summary:	Online manual for class.upload.php
Summary(pl.UTF-8):	Dokumentacja online do class.upload.php
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for class.upload.php.

%description phpdoc -l pl.UTF-8
Dokumentacja do class.upload.php.

%prep
%setup -q -n class.upload_%{version}

rm lang/class.upload.xx_XX.php

%undos lang/*.php *.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a class.upload.php $RPM_BUILD_ROOT%{_appdir}
cp -a lang $RPM_BUILD_ROOT%{_appdir}/lang

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a test.png watermark.png bg.gif index.html test $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}
cp -a sources/* $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/class.upload.php
# XXX: maybe dedicated dir needed
%dir %{php_data_dir}/lang
%lang(ca) %{php_data_dir}/lang/class.upload.ca_CA.php
%lang(cs) %{php_data_dir}/lang/class.upload.cs_CS.php
%lang(de) %{php_data_dir}/lang/class.upload.de_DE.php
%lang(el) %{php_data_dir}/lang/class.upload.el_GR.php
%lang(es) %{php_data_dir}/lang/class.upload.es_ES.php
%lang(et) %{php_data_dir}/lang/class.upload.et_EE.php
%lang(fr) %{php_data_dir}/lang/class.upload.fr_FR.php
%lang(he) %{php_data_dir}/lang/class.upload.he_IL.php
%lang(hr) %{php_data_dir}/lang/class.upload.hr_HR.php
%lang(id) %{php_data_dir}/lang/class.upload.id_ID.php
%lang(it) %{php_data_dir}/lang/class.upload.it_IT.php
%lang(nl) %{php_data_dir}/lang/class.upload.nl_NL.php
%lang(nb) %{php_data_dir}/lang/class.upload.no_NO.php
%lang(pl) %{php_data_dir}/lang/class.upload.pl_PL.php
%lang(pt) %{php_data_dir}/lang/class.upload.pt_BR.php
%lang(ro) %{php_data_dir}/lang/class.upload.ro_RO.php
%lang(ru) %{php_data_dir}/lang/class.upload.ru_RU.php
%lang(ru) %{php_data_dir}/lang/class.upload.ru_RU.windows-1251.php
%lang(sk) %{php_data_dir}/lang/class.upload.sk_SK.php
%lang(sv) %{php_data_dir}/lang/class.upload.sv_SE.php
%lang(tr) %{php_data_dir}/lang/class.upload.tr_TR.php
%lang(uk) %{php_data_dir}/lang/class.upload.uk_UA.php
%lang(uk) %{php_data_dir}/lang/class.upload.uk_UA.windows-1251.php
%lang(vn) %{php_data_dir}/lang/class.upload.vn_VN.php
%lang(zh_CN) %{php_data_dir}/lang/class.upload.zh_CN.gb-2312.php
%lang(zh_CN) %{php_data_dir}/lang/class.upload.zh_CN.php
%lang(zh_TW) %{php_data_dir}/lang/class.upload.zh_TW.php
%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{pkgname}
