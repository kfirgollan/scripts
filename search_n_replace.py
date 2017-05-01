#!/usr/bin/env python
import sys
import os

patterns = sys.argv[1].split(',')

if len(patterns) % 2 != 0:
    print "Invalid patterns list! you must provided search/replace patterns"
    sys.exit(0)

for idx in range(0, len(patterns), 2):
    search_pat = patterns[idx]
    replace_pat = patterns[idx+1]

    val = raw_input("replacing %s with %s, ok? " % (search_pat, replace_pat))
    if val != 'y':
        print "skipping..."
        continue

    os.system("ag -l '%s' | xargs sed -i 's/%s/%s/g'" % (search_pat, search_pat, replace_pat))
