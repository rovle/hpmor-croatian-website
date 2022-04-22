#!/bin/bash
for filename in Poglavlja/*.docx; do
    name=${filename##*/}
    name=${name%.*}
    pandoc --wrap=none -f docx -t markdown "${filename}" -o "Poglavlja_markdown/${name}.md"
done
