#!/bin/bash

for code in $(cat ordered_sets.txt); do
    if [[ ! -e "tagged_sets/unique/${code}" ]]; then
        echo "Skipping ${code}." >&2
        continue
    fi
    echo "Summarizing ${code}." >&2
    echo "--------------------------------------------------"
    echo "${code}"
    echo "--------------------------------------------------"
    head -n 10 "tagged_sets/unique/${code}" | while read format; do
        count="$(echo "${format}" | cut -d ' ' -f 1)"
        format="$(echo "${format}" | cut -d ' ' -f 2-)"
        example="$(grep ": ${format}$" tagged_sets/${code} | head -n 1)"
        example="$(echo "${example}" | sed 's/:.*//')"
        if echo "${format}" | grep -qEf target_patterns.grep; then
            format="* ${format}"
        fi
        echo -e "${count}\t${format} (\"${example}\")"
    done
    echo
done
