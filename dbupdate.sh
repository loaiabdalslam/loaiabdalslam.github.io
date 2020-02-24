#!/bin/bash

TOPOST=/Users/gozar/Dropbox/Elements/gtia.com/*.markdown
SITE=/Users/gozar/Development/gtia.com

shopt -s nullglob

YEAR=`date +%Y`
NOW=`date +"%Y-%m-%d %H:%M"`

for file in ${TOPOST}
do
    DATELINE=`cat "${file}" | grep "^Date: "`
    if [[ ${DATELINE#* } < ${NOW} ]]; then
        mv "${file}" "${SITE}/content/${YEAR}"
        POST=true
   fi
done

if [[ ${POST} ]]; then
    cd "${SITE}"
    git add "${SITE}/content/${YEAR}"
    make github
    git push
fi
