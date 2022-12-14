#!/bin/sh

script=$(readlink -f "$0")
scriptdir=`dirname "$script"`
cd "$scriptdir"

CLASSPATH=
for FILE in `ls ./lib/*.jar`
do
   CLASSPATH=${CLASSPATH}:${FILE}
done

export SWT_GTK3=0

java -enableassertions -Xmx1g -Xss2m -cp ".:${CLASSPATH}" -Djava.library.path="lib" net.sourceforge.docfetcher.Main "$@"
