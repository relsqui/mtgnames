#!/bin/bash

for file in sets/*; do
    code="$(basename -s ".json" ${file})"
    ./creature_names.py <"${file}" | ./parse_names.py > "tagged_sets/${code}"
    file_size="$(wc -c "tagged_sets/${code}" | cut -d ' ' -f 1)"
    if [[ "${file_size}" -lt "10" ]]; then
        echo "Skipping ${code} (${file_size} bytes)."
        rm "tagged_sets/${code}"
    else
        echo "Tagging ${code} (${file_size} bytes)."
    fi
done
