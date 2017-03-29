#!/bin/bash

percent() {
    if [[ "$1" -eq "0" ]]; then
        echo "0"
        return
    fi
    echo "$(($1 * 100 / $2))"
}

total_matching=
total_total=
for code in $(cat ../ordered_sets.txt); do
    file="unique/${code}"
    if [[ ! -e "${file}" ]]; then
        continue
    fi
    matching="$(grep -Ef ../target_patterns.grep "${file}" | sed 's/[^0-9]//g' | paste -s -d+ - | bc)"
    if [[ -z "${matching}" ]]; then
        matching="0"
    fi
    total=$(wc -l "${file}" | sed 's/ .*//')
    ((total_matching+=$matching))
    ((total_total+=$total))
    percent="$(percent ${matching} ${total})"
    echo "${code}: ${matching}/${total} (${percent}%)"
done
percent="$(percent ${total_matching} ${total_total})"
echo
echo "Total: ${total_matching}/${total_total} (${percent}%)"
