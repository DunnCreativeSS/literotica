for f in ./* ./**/* ; do
html2text  "$f" "utf-8" >> "$f.txt"
done;
