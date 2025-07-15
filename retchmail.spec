Summary:	Retchmail - fast replacement for Fetchmail
Summary(pl.UTF-8):	Retchmail - szybki zamiennik Fetchmaila
Name:		retchmail
Version:	1.1.1
Release:	1
License:	LGPL v2.1+
Group:		Networking/Utilities
Source0:	http://wvstreams.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	5f12436f8d59b715c2bb84745b4ce91c
Patch0:		%{name}-c++.patch
URL:		http://alumnit.ca/wiki/index.php?page=RetchMail
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	wvstreams-devel >= 4.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Retchmail is a fast POP3 retriever. It supports simultaneous POP3 and
POP3S mail retrieval from multiple sites to multiple mailboxes.
Retchmail is good for quick retrieval of e-mail if you do not need the
features of other, more comprehensive, retrievers like Fetchmail.

%description -l pl.UTF-8
Retchmail to szybki klient POP3. Obsługuje jednoczesne pobieranie
wiadomości poprzez POP3 i POP3S z wielu serwerów do wielu skrzynek.
Jest dobry do szybkiego ściągania poczty, jeśli nie są wymagane
możliwości innych, pełniejszych klientów, takich jak Fetchmail.

%prep
%setup -q
%patch -P0 -p1

%build
# not autoconf generated, no arguments used
./configure
%{__make} -j1 \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CPPOPTS="%{rpmcppflags}" \
	COPTS="%{rpmcflags}" \
	CXXOPTS="%{rpmcppflags}" \
	VERBOSE=1 \
	enable_debug=no

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/retchmail
%{_mandir}/man1/retchmail.1*
%{_mandir}/man5/retchmail.conf.5*
