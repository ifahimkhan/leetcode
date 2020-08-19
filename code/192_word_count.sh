#!/bin/bash
# Read from the file words.txt and output the word frequency list to stdout.
# tr -s               : replace space by newline
# sort                : sort according to lexicographical order asc
# uniq -c             : print val with count of consectuive occurrences
# sort -nr            : sort according to numerical order dsc
# awk '{print $2 $1}' : split line into fields 
filepath=${1:-words.txt}   
cat $filepath | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2" "$1}'
