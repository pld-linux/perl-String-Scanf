%include	/usr/lib/rpm/macros.perl
Summary:	String-Scanf perl module
Summary(pl):	Modu� perla String-Scanf
Name:		perl-String-Scanf
Version:	1.2
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-Scanf-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-Scanf emulates the sscanf() of the C stdio library.

%description -l pl
String-Scanf emuluje funkcj� sscanf() pochodz�c� z biblioteki C stdio.

%prep
%setup -q -n String-Scanf-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/String/Scanf
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/String/Scanf.pm
%{perl_sitearch}/auto/String/Scanf

%{_mandir}/man3/*
