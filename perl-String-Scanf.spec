# $revision: 1.19 $, $date: 2002/07/10 08:48:48 $
#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Scanf
Summary:	String::Scanf emulates the sscanf() of the C stdio library
Summary(pl):	String::Scanf emuluje funkcjê sscanf() pochodz±c± z biblioteki C stdio
Name:		perl-String-Scanf
Version:	2.0
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Scanf supports scanning strings for data using formats similar
to the libc/stdio sscanf().

%description -l pl
Modu³ String::Scanf pozwala na skanowanie ³añcuchów poprzez ³añcuchy
formatuj±ce podobne do tych u¿ywanych w funkcji sscanf() libc/stdio.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/String/Scanf.pm
%{_mandir}/man3/*
