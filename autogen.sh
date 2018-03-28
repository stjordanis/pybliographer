#!/bin/sh

aclocal_extra="-I m4"

GNOMEDOC=`which yelp-build`
    if test -z $GNOMEDOC; then
        echo "*** The tools to build the documentation are not found,"
        echo "    please intall the yelp-tools package ***"
        exit 1
    fi

aclocal ${aclocal_extra}
autoreconf --verbose --force --install || exit 1

if [ -x ./config.status ] ; then
    ./config.status --recheck
    ./config.status
else
    ./configure "$@" || exit 1
fi
