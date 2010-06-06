#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	GDOME
Summary:	XML::GDOME - interface to Level 2 DOM gdome2 library
Summary(pl.UTF-8):	XML::GDOME - interfejs do biblioteki DOM Level 2 gdome2
Name:		perl-XML-GDOME
Version:	0.86
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01ee59f686f9d409bdc316297942ea55
URL:		http://search.cpan.org/dist/XML-GDOME/
BuildRequires:	gdome2-devel >= 0.7.2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-LibXML-Common
BuildRequires:	perl-XML-SAX
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::GDOME is a Perl module that provides the DOM Level 2 Core API
for accessing XML documents. It uses a XS wrapper around the gdome2
library.

%description -l pl.UTF-8
XML::GDOME to moduł Perla dostarczający podstawowe API DOM Level 2 do
dostępu do dokumentów XML. Używa wrappera XS do biblioteki gdome2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/XML/*.pm
%dir %{perl_vendorarch}/XML/GDOME
%{perl_vendorarch}/XML/GDOME/SAX
%dir %{perl_vendorarch}/auto/XML/GDOME
%{perl_vendorarch}/auto/XML/GDOME/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/XML/GDOME/*.so
%{_mandir}/man3/*
