#!/bin/bash

mkdir -p unique
for file in *; do
    echo "Summarizing ${file}."
    cat "${file}" | cut -f2 -d: | sed 's/^ //' | sort | uniq -c | sort -nr > "unique/${file}"
done
