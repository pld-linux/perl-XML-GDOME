#
# Conditional build:
%bcond_with tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	GDOME
Summary:	XML::GDOME - interface to Level 2 DOM gdome2 library
Summary(pl):	XML::GDOME - interfejs do biblioteki DOM Level 2 gdome2
Name:		perl-XML-GDOME
Version:	0.85
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6210b865524ff27ca4cb8a66a72f5ecd
BuildRequires:	gdome2-devel >= 0.7.2
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML-Common
BuildRequires:	perl-XML-SAX
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::GDOME is a Perl module that provides the DOM Level 2 Core API
for accessing XML documents. It uses a XS wrapper around the gdome2
library.

%description -l pl
XML::GDOME to modu³ Perla dostarczaj±cy podstawowe API DOM Level 2 do
dostêpu do dokumentów XML. U¿ywa wrappera XS do biblioteki gdome2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/XML/GDOME.pm
%dir %{perl_vendorarch}/XML/GDOME
%{perl_vendorarch}/XML/GDOME/SAX
%{perl_vendorarch}/auto/XML/*
%{_mandir}/man3/*
