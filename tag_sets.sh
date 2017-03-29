#!/bin/bash

mkdir -p tagged_sets
for file in sets/*; do
    code="$(basename -s ".json" ${file})"
    echo "Tagging ${code}."
    ./creature_names.py <"${file}" | ./parse_names.py > "tagged_sets/${code}"
done
