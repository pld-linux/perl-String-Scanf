#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	String
%define		pnam	Scanf
Summary:	String::Scanf - emulates the sscanf() of the C stdio library
Summary(pl.UTF-8):	String::Scanf - emulacja funkcji sscanf() pochodzącej z biblioteki C stdio
Name:		perl-String-Scanf
Version:	2.1
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6fe49bcefcf7dcc58ad9fea207277552
URL:		http://search.cpan.org/dist/String-Scanf/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Scanf supports scanning strings for data using formats similar
to the libc/stdio sscanf().

%description -l pl.UTF-8
Moduł String::Scanf pozwala na skanowanie łańcuchów poprzez łańcuchy
formatujące podobne do tych używanych w funkcji sscanf() libc/stdio.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/String/Scanf.pm
%{_mandir}/man3/*
