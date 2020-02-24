#!/bin/bash

TITLE="$@"
SLUG=$(echo -n "${TITLE}" | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
OUT=content/drafts/${SLUG}.markdown
DATE=$(date +"%Y-%m-%d %H:%M")

if [ "${TITLE}" != "" ]; then
    echo "Title: ${TITLE}" > ${OUT}
    echo "Author: gozar" >> ${OUT}
    echo "Date: ${DATE}" >> ${OUT}
    echo "Slug: ${SLUG}" >> ${OUT}
    echo -e "Category: \nTags: \nStatus: draft\n\n" >> ${OUT}

    vim ${OUT}

    read -p "Add file to git? " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        git add ${OUT}
    fi

else
    echo "I need a title"
fi


