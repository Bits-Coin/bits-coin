%define bdbv 4.8.30
%global selinux_variants mls strict targeted

%if 0%{?_no_gui:1}
%define _buildqt 0
%define buildargs --with-gui=no
%else
%define _buildqt 1
%if 0%{?_use_qt4}
%define buildargs --with-qrencode --with-gui=qt4
%else
%define buildargs --with-qrencode --with-gui=qt5
%endif
%endif

Name:		bitscoin
Version:	0.12.0
Release:	2%{?dist}
Summary:	Peer to Peer Cryptographic Currency

Group:		Applications/System
License:	MIT
URL:		https://bitscoin.org/
Source0:	https://bitscoin.org/bin/bitscoin-core-%{version}/bitscoin-%{version}.tar.gz
Source1:	http://download.oracle.com/berkeley-db/db-%{bdbv}.NC.tar.gz

Source10:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/contrib/debian/examples/bitscoin.conf

#man pages
Source20:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/doc/man/bitscoind.1
Source21:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/doc/man/bitscoin-cli.1
Source22:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/doc/man/bitscoin-qt.1

#selinux
Source30:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/contrib/rpm/bitscoin.te
# Source31 - what about bitscoin-tx and bench_bitscoin ???
Source31:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/contrib/rpm/bitscoin.fc
Source32:	https://raw.githubusercontent.com/bitscoin/bitscoin/v%{version}/contrib/rpm/bitscoin.if

Source100:	https://upload.wikimedia.org/wikipedia/commons/4/46/BitsCoin.svg

%if 0%{?_use_libressl:1}
BuildRequires:	libressl-devel
%else
BuildRequires:	openssl-devel
%endif
BuildRequires:	boost-devel
BuildRequires:	miniupnpc-devel
BuildRequires:	autoconf automake libtool
BuildRequires:	libevent-devel


Patch0:		bitscoin-0.12.0-libressl.patch


%description
BitsCoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitscoins is carried out collectively by the network.

%if %{_buildqt}
%package core
Summary:	Peer to Peer Cryptographic Currency
Group:		Applications/System
Obsoletes:	%{name} < %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
%if 0%{?_use_qt4}
BuildRequires:	qt-devel
%else
BuildRequires:	qt5-qtbase-devel
# for /usr/bin/lrelease-qt5
BuildRequires:	qt5-linguist
%endif
BuildRequires:	protobuf-devel
BuildRequires:	qrencode-devel
BuildRequires:	%{_bindir}/desktop-file-validate
# for icon generation from SVG
BuildRequires:	%{_bindir}/inkscape
BuildRequires:	%{_bindir}/convert

%description core
BitsCoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitscoins is carried out collectively by the network.

This package contains the Qt based graphical client and node. If you are looking
to run a BitsCoin wallet, this is probably the package you want.
%endif


%package libs
Summary:	BitsCoin shared libraries
Group:		System Environment/Libraries

%description libs
This package provides the bitscoinconsensus shared libraries. These libraries
may be used by third party software to provide consensus verification
functionality.

Unless you know need this package, you probably do not.

%package devel
Summary:	Development files for bitscoin
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the header files and static library for the
bitscoinconsensus shared library. If you are developing or compiling software
that wants to link against that library, then you need this package installed.

Most people do not need this package installed.

%package server
Summary:	The bitscoin daemon
Group:		System Environment/Daemons
Requires:	bitscoin-utils = %{version}-%{release}
Requires:	selinux-policy policycoreutils-python
Requires(pre):	shadow-utils
Requires(post):	%{_sbindir}/semodule %{_sbindir}/restorecon %{_sbindir}/fixfiles %{_sbindir}/sestatus
Requires(postun):	%{_sbindir}/semodule %{_sbindir}/restorecon %{_sbindir}/fixfiles %{_sbindir}/sestatus
BuildRequires:	systemd
BuildRequires:	checkpolicy
BuildRequires:	%{_datadir}/selinux/devel/Makefile

%description server
This package provides a stand-alone bitscoin-core daemon. For most users, this
package is only needed if they need a full-node without the graphical client.

Some third party wallet software will want this package to provide the actual
bitscoin-core node they use to connect to the network.

If you use the graphical bitscoin-core client then you almost certainly do not
need this package.

%package utils
Summary:	BitsCoin utilities
Group:		Applications/System

%description utils
This package provides several command line utilities for interacting with a
bitscoin-core daemon.

The bitscoin-cli utility allows you to communicate and control a bitscoin daemon
over RPC, the bitscoin-tx utility allows you to create a custom transaction, and
the bench_bitscoin utility can be used to perform some benchmarks.

This package contains utilities needed by the bitscoin-server package.


%prep
%setup -q
%patch0 -p1 -b .libressl
cp -p %{SOURCE10} ./bitscoin.conf.example
tar -zxf %{SOURCE1}
cp -p db-%{bdbv}.NC/LICENSE ./db-%{bdbv}.NC-LICENSE
mkdir db4 SELinux
cp -p %{SOURCE30} %{SOURCE31} %{SOURCE32} SELinux/


%build
CWD=`pwd`
cd db-%{bdbv}.NC/build_unix/
../dist/configure --enable-cxx --disable-shared --with-pic --prefix=${CWD}/db4
make install
cd ../..

./autogen.sh
%configure LDFLAGS="-L${CWD}/db4/lib/" CPPFLAGS="-I${CWD}/db4/include/" --with-miniupnpc --enable-glibc-back-compat %{buildargs}
make %{?_smp_mflags}

pushd SELinux
for selinuxvariant in %{selinux_variants}; do
	make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile
	mv bitscoin.pp bitscoin.pp.${selinuxvariant}
	make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile clean
done
popd


%install
make install DESTDIR=%{buildroot}

mkdir -p -m755 %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/bitscoind %{buildroot}%{_sbindir}/bitscoind

# systemd stuff
mkdir -p %{buildroot}%{_tmpfilesdir}
cat <<EOF > %{buildroot}%{_tmpfilesdir}/bitscoin.conf
d /run/bitscoind 0750 bitscoin bitscoin -
EOF
touch -a -m -t 201504280000 %{buildroot}%{_tmpfilesdir}/bitscoin.conf

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cat <<EOF > %{buildroot}%{_sysconfdir}/sysconfig/bitscoin
# Provide options to the bitscoin daemon here, for example
# OPTIONS="-testnet -disable-wallet"

OPTIONS=""

# System service defaults.
# Don't change these unless you know what you're doing.
CONFIG_FILE="%{_sysconfdir}/bitscoin/bitscoin.conf"
DATA_DIR="%{_localstatedir}/lib/bitscoin"
PID_FILE="/run/bitscoind/bitscoind.pid"
EOF
touch -a -m -t 201504280000 %{buildroot}%{_sysconfdir}/sysconfig/bitscoin

mkdir -p %{buildroot}%{_unitdir}
cat <<EOF > %{buildroot}%{_unitdir}/bitscoin.service
[Unit]
Description=BitsCoin daemon
After=syslog.target network.target

[Service]
Type=forking
ExecStart=%{_sbindir}/bitscoind -daemon -conf=\${CONFIG_FILE} -datadir=\${DATA_DIR} -pid=\${PID_FILE} \$OPTIONS
EnvironmentFile=%{_sysconfdir}/sysconfig/bitscoin
User=bitscoin
Group=bitscoin

Restart=on-failure
PrivateTmp=true
TimeoutStopSec=120
TimeoutStartSec=60
StartLimitInterval=240
StartLimitBurst=5

[Install]
WantedBy=multi-user.target
EOF
touch -a -m -t 201504280000 %{buildroot}%{_unitdir}/bitscoin.service
#end systemd stuff

mkdir %{buildroot}%{_sysconfdir}/bitscoin
mkdir -p %{buildroot}%{_localstatedir}/lib/bitscoin

#SELinux
for selinuxvariant in %{selinux_variants}; do
	install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
	install -p -m 644 SELinux/bitscoin.pp.${selinuxvariant} %{buildroot}%{_datadir}/selinux/${selinuxvariant}/bitscoin.pp
done

%if %{_buildqt}
# qt icons
install -D -p share/pixmaps/bitscoin.ico %{buildroot}%{_datadir}/pixmaps/bitscoin.ico
install -p share/pixmaps/nsis-header.bmp %{buildroot}%{_datadir}/pixmaps/
install -p share/pixmaps/nsis-wizard.bmp %{buildroot}%{_datadir}/pixmaps/
install -p %{SOURCE100} %{buildroot}%{_datadir}/pixmaps/bitscoin.svg
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/bitscoin16.png -w16 -h16
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/bitscoin32.png -w32 -h32
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/bitscoin64.png -w64 -h64
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/bitscoin128.png -w128 -h128
%{_bindir}/inkscape %{SOURCE100} --export-png=%{buildroot}%{_datadir}/pixmaps/bitscoin256.png -w256 -h256
%{_bindir}/convert -resize 16x16 %{buildroot}%{_datadir}/pixmaps/bitscoin256.png %{buildroot}%{_datadir}/pixmaps/bitscoin16.xpm
%{_bindir}/convert -resize 32x32 %{buildroot}%{_datadir}/pixmaps/bitscoin256.png %{buildroot}%{_datadir}/pixmaps/bitscoin32.xpm
%{_bindir}/convert -resize 64x64 %{buildroot}%{_datadir}/pixmaps/bitscoin256.png %{buildroot}%{_datadir}/pixmaps/bitscoin64.xpm
%{_bindir}/convert -resize 128x128 %{buildroot}%{_datadir}/pixmaps/bitscoin256.png %{buildroot}%{_datadir}/pixmaps/bitscoin128.xpm
%{_bindir}/convert %{buildroot}%{_datadir}/pixmaps/bitscoin256.png %{buildroot}%{_datadir}/pixmaps/bitscoin256.xpm
touch %{buildroot}%{_datadir}/pixmaps/*.png -r %{SOURCE100}
touch %{buildroot}%{_datadir}/pixmaps/*.xpm -r %{SOURCE100}

# Desktop File - change the touch timestamp if modifying
mkdir -p %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/bitscoin-core.desktop
[Desktop Entry]
Encoding=UTF-8
Name=BitsCoin
Comment=BitsCoin P2P Cryptocurrency
Comment[fr]=BitsCoin, monnaie virtuelle cryptographique pair à pair
Comment[tr]=BitsCoin, eşten eşe kriptografik sanal para birimi
Exec=bitscoin-qt %u
Terminal=false
Type=Application
Icon=bitscoin128
MimeType=x-scheme-handler/bitscoin;
Categories=Office;Finance;
EOF
# change touch date when modifying desktop
touch -a -m -t 201511100546 %{buildroot}%{_datadir}/applications/bitscoin-core.desktop
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/bitscoin-core.desktop

# KDE protocol - change the touch timestamp if modifying
mkdir -p %{buildroot}%{_datadir}/kde4/services
cat <<EOF > %{buildroot}%{_datadir}/kde4/services/bitscoin-core.protocol
[Protocol]
exec=bitscoin-qt '%u'
protocol=bitscoin
input=none
output=none
helper=true
listing=
reading=false
writing=false
makedir=false
deleting=false
EOF
# change touch date when modifying protocol
touch -a -m -t 201511100546 %{buildroot}%{_datadir}/kde4/services/bitscoin-core.protocol
%endif

# man pages
install -D -p %{SOURCE20} %{buildroot}%{_mandir}/man1/bitscoind.1
install -p %{SOURCE21} %{buildroot}%{_mandir}/man1/bitscoin-cli.1
%if %{_buildqt}
install -p %{SOURCE22} %{buildroot}%{_mandir}/man1/bitscoin-qt.1
%endif

# nuke these, we do extensive testing of binaries in %%check before packaging
rm -f %{buildroot}%{_bindir}/test_*

%check
make check
srcdir=src test/bitscoin-util-test.py
test/functional/test_runner.py --extended

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%pre server
getent group bitscoin >/dev/null || groupadd -r bitscoin
getent passwd bitscoin >/dev/null ||
	useradd -r -g bitscoin -d /var/lib/bitscoin -s /sbin/nologin \
	-c "BitsCoin wallet server" bitscoin
exit 0

%post server
%systemd_post bitscoin.service
# SELinux
if [ `%{_sbindir}/sestatus |grep -c "disabled"` -eq 0 ]; then
for selinuxvariant in %{selinux_variants}; do
	%{_sbindir}/semodule -s ${selinuxvariant} -i %{_datadir}/selinux/${selinuxvariant}/bitscoin.pp &> /dev/null || :
done
%{_sbindir}/semanage port -a -t bitscoin_port_t -p tcp 8332
%{_sbindir}/semanage port -a -t bitscoin_port_t -p tcp 8333
%{_sbindir}/semanage port -a -t bitscoin_port_t -p tcp 18332
%{_sbindir}/semanage port -a -t bitscoin_port_t -p tcp 18333
%{_sbindir}/semanage port -a -t bitscoin_port_t -p tcp 18443
%{_sbindir}/semanage port -a -t bitscoin_port_t -p tcp 18444
%{_sbindir}/fixfiles -R bitscoin-server restore &> /dev/null || :
%{_sbindir}/restorecon -R %{_localstatedir}/lib/bitscoin || :
fi

%posttrans server
%{_bindir}/systemd-tmpfiles --create

%preun server
%systemd_preun bitscoin.service

%postun server
%systemd_postun bitscoin.service
# SELinux
if [ $1 -eq 0 ]; then
	if [ `%{_sbindir}/sestatus |grep -c "disabled"` -eq 0 ]; then
	%{_sbindir}/semanage port -d -p tcp 8332
	%{_sbindir}/semanage port -d -p tcp 8333
	%{_sbindir}/semanage port -d -p tcp 18332
	%{_sbindir}/semanage port -d -p tcp 18333
	%{_sbindir}/semanage port -d -p tcp 18443
	%{_sbindir}/semanage port -d -p tcp 18444
	for selinuxvariant in %{selinux_variants}; do
		%{_sbindir}/semodule -s ${selinuxvariant} -r bitscoin &> /dev/null || :
	done
	%{_sbindir}/fixfiles -R bitscoin-server restore &> /dev/null || :
	[ -d %{_localstatedir}/lib/bitscoin ] && \
		%{_sbindir}/restorecon -R %{_localstatedir}/lib/bitscoin &> /dev/null || :
	fi
fi

%clean
rm -rf %{buildroot}

%if %{_buildqt}
%files core
%defattr(-,root,root,-)
%license COPYING db-%{bdbv}.NC-LICENSE
%doc COPYING bitscoin.conf.example doc/README.md doc/bips.md doc/files.md doc/multiwallet-qt.md doc/reduce-traffic.md doc/release-notes.md doc/tor.md
%attr(0755,root,root) %{_bindir}/bitscoin-qt
%attr(0644,root,root) %{_datadir}/applications/bitscoin-core.desktop
%attr(0644,root,root) %{_datadir}/kde4/services/bitscoin-core.protocol
%attr(0644,root,root) %{_datadir}/pixmaps/*.ico
%attr(0644,root,root) %{_datadir}/pixmaps/*.bmp
%attr(0644,root,root) %{_datadir}/pixmaps/*.svg
%attr(0644,root,root) %{_datadir}/pixmaps/*.png
%attr(0644,root,root) %{_datadir}/pixmaps/*.xpm
%attr(0644,root,root) %{_mandir}/man1/bitscoin-qt.1*
%endif

%files libs
%defattr(-,root,root,-)
%license COPYING
%doc COPYING doc/README.md doc/shared-libraries.md
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%license COPYING
%doc COPYING doc/README.md doc/developer-notes.md doc/shared-libraries.md
%attr(0644,root,root) %{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%attr(0644,root,root) %{_libdir}/pkgconfig/*.pc

%files server
%defattr(-,root,root,-)
%license COPYING db-%{bdbv}.NC-LICENSE
%doc COPYING bitscoin.conf.example doc/README.md doc/REST-interface.md doc/bips.md doc/dnsseed-policy.md doc/files.md doc/reduce-traffic.md doc/release-notes.md doc/tor.md
%attr(0755,root,root) %{_sbindir}/bitscoind
%attr(0644,root,root) %{_tmpfilesdir}/bitscoin.conf
%attr(0644,root,root) %{_unitdir}/bitscoin.service
%dir %attr(0750,bitscoin,bitscoin) %{_sysconfdir}/bitscoin
%dir %attr(0750,bitscoin,bitscoin) %{_localstatedir}/lib/bitscoin
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/sysconfig/bitscoin
%attr(0644,root,root) %{_datadir}/selinux/*/*.pp
%attr(0644,root,root) %{_mandir}/man1/bitscoind.1*

%files utils
%defattr(-,root,root,-)
%license COPYING
%doc COPYING bitscoin.conf.example doc/README.md
%attr(0755,root,root) %{_bindir}/bitscoin-cli
%attr(0755,root,root) %{_bindir}/bitscoin-tx
%attr(0755,root,root) %{_bindir}/bench_bitscoin
%attr(0644,root,root) %{_mandir}/man1/bitscoin-cli.1*



%changelog
* Fri Feb 26 2016 Alice Wonder <buildmaster@librelamp.com> - 0.12.0-2
- Rename Qt package from bitscoin to bitscoin-core
- Make building of the Qt package optional
- When building the Qt package, default to Qt5 but allow building
-  against Qt4
- Only run SELinux stuff in post scripts if it is not set to disabled

* Wed Feb 24 2016 Alice Wonder <buildmaster@librelamp.com> - 0.12.0-1
- Initial spec file for 0.12.0 release

# This spec file is written from scratch but a lot of the packaging decisions are directly
# based upon the 0.11.2 package spec file from https://www.ringingliberty.com/bitscoin/
