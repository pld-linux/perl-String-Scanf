%include	/usr/lib/rpm/macros.perl
Summary:	String-Scanf perl module
Summary(pl):	Modu³ perla String-Scanf
Name:		perl-String-Scanf
Version:	1.4
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-Scanf-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-Scanf emulates the sscanf() of the C stdio library.

%description -l pl
String-Scanf emuluje funkcjê sscanf() pochodz±c± z biblioteki C stdio.

%prep
%setup -q -n String-Scanf-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/String/Scanf.pm
%{_mandir}/man3/*
