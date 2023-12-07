#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v3
# autospec commit: c1050fe
#
Name     : cronie
Version  : 1.7.0
Release  : 29
URL      : https://github.com/cronie-crond/cronie/archive/cronie-1.7.0/cronie-1.7.0.tar.gz
Source0  : https://github.com/cronie-crond/cronie/archive/cronie-1.7.0/cronie-1.7.0.tar.gz
Source1  : cronie.service
Summary  : Cron daemon for executing programs at set times
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ ISC LGPL-2.1 MIT
Requires: cronie-bin = %{version}-%{release}
Requires: cronie-license = %{version}-%{release}
Requires: cronie-man = %{version}-%{release}
Requires: cronie-services = %{version}-%{release}
Requires: cronie-setuid = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Don-t-complain-about-missing-etc-cron.d.patch

%description
Cronie contains the standard UNIX daemon crond that runs specified programs at
scheduled times and related tools. It is a fork of the original vixie-cron and
has security and configuration enhancements like the ability to use pam and
SELinux.

%package bin
Summary: bin components for the cronie package.
Group: Binaries
Requires: cronie-setuid = %{version}-%{release}
Requires: cronie-license = %{version}-%{release}
Requires: cronie-services = %{version}-%{release}

%description bin
bin components for the cronie package.


%package license
Summary: license components for the cronie package.
Group: Default

%description license
license components for the cronie package.


%package man
Summary: man components for the cronie package.
Group: Default

%description man
man components for the cronie package.


%package services
Summary: services components for the cronie package.
Group: Systemd services
Requires: systemd

%description services
services components for the cronie package.


%package setuid
Summary: setuid components for the cronie package.
Group: Default

%description setuid
setuid components for the cronie package.


%prep
%setup -q -n cronie-cronie-1.7.0
cd %{_builddir}/cronie-cronie-1.7.0
%patch -P 1 -p1
pushd ..
cp -a cronie-cronie-1.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701946305
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701946305
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cronie
cp %{_builddir}/cronie-cronie-%{version}/COPYING %{buildroot}/usr/share/package-licenses/cronie/6261e3b944ea705753eeb12c7e6fb0ef3ba42bee || :
cp %{_builddir}/cronie-cronie-%{version}/COPYING.anacron %{buildroot}/usr/share/package-licenses/cronie/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/cronie-cronie-%{version}/COPYING.obstack %{buildroot}/usr/share/package-licenses/cronie/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/cronie.service
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name} --skip-path /usr/bin/crontab

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/anacron
/V3/usr/bin/crond
/V3/usr/bin/cronnext
/usr/bin/anacron
/usr/bin/crond
/usr/bin/cronnext

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cronie/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/cronie/6261e3b944ea705753eeb12c7e6fb0ef3ba42bee
/usr/share/package-licenses/cronie/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cronnext.1
/usr/share/man/man1/crontab.1
/usr/share/man/man5/anacrontab.5
/usr/share/man/man5/crontab.5
/usr/share/man/man8/anacron.8
/usr/share/man/man8/cron.8
/usr/share/man/man8/crond.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/cronie.service

%files setuid
%defattr(-,root,root,-)
%attr(4755,root,cron) /usr/bin/crontab
