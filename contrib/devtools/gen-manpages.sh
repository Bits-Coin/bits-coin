#!/usr/bin/env bash

export LC_ALL=C
TOPDIR=${TOPDIR:-$(git rev-parse --show-toplevel)}
BUILDDIR=${BUILDDIR:-$TOPDIR}

BINDIR=${BINDIR:-$BUILDDIR/src}
MANDIR=${MANDIR:-$TOPDIR/doc/man}

DIGIBYTED=${DIGIBYTED:-$BINDIR/bitscoind}
DIGIBYTECLI=${DIGIBYTECLI:-$BINDIR/bitscoin-cli}
DIGIBYTETX=${DIGIBYTETX:-$BINDIR/bitscoin-tx}
DIGIBYTEQT=${DIGIBYTEQT:-$BINDIR/qt/bitscoin-qt}

[ ! -x $DIGIBYTED ] && echo "$DIGIBYTED not found or not executable." && exit 1

# The autodetected version git tag can screw up manpage output a little bit
DGBVER=($($DIGIBYTECLI --version | head -n1 | awk -F'[ -]' '{ print $6, $7 }'))

# Create a footer file with copyright content.
# This gets autodetected fine for bitscoind if --version-string is not set,
# but has different outcomes for bitscoin-qt and bitscoin-cli.
echo "[COPYRIGHT]" > footer.h2m
$DIGIBYTED --version | sed -n '1!p' >> footer.h2m

for cmd in $DIGIBYTED $DIGIBYTECLI $DIGIBYTETX $DIGIBYTEQT; do
  cmdname="${cmd##*/}"
  help2man -N --version-string=${DGBVER[0]} --include=footer.h2m -o ${MANDIR}/${cmdname}.1 ${cmd}
  sed -i "s/\\\-${DGBVER[1]}//g" ${MANDIR}/${cmdname}.1
done

rm -f footer.h2m
