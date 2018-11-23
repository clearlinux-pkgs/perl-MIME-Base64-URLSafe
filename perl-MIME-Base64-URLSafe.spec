#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MIME-Base64-URLSafe
Version  : 0.01
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/MIME-Base64-URLSafe-0.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/MIME-Base64-URLSafe-0.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmime-base64-urlsafe-perl/libmime-base64-urlsafe-perl_0.01-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-MIME-Base64-URLSafe-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
MIME-Base64-URLSafe version 0.01
================================
MIME::Base64::URLSafe is an URL-safe base64 encoder / decoder, compatible with python's urlsafe_b64encode / urlsafe_b64decode.  The codec uses '-' and '/' instead of '+' and '/', which have special meanings when embedded in URL.

%package dev
Summary: dev components for the perl-MIME-Base64-URLSafe package.
Group: Development
Provides: perl-MIME-Base64-URLSafe-devel = %{version}-%{release}

%description dev
dev components for the perl-MIME-Base64-URLSafe package.


%package license
Summary: license components for the perl-MIME-Base64-URLSafe package.
Group: Default

%description license
license components for the perl-MIME-Base64-URLSafe package.


%prep
%setup -q -n MIME-Base64-URLSafe-0.01
cd ..
%setup -q -T -D -n MIME-Base64-URLSafe-0.01 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/MIME-Base64-URLSafe-0.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MIME-Base64-URLSafe
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-MIME-Base64-URLSafe/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/MIME/Base64/URLSafe.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MIME::Base64::URLSafe.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MIME-Base64-URLSafe/deblicense_copyright
