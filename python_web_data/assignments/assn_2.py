#! /usr/bin/env python3
import re
print(sum([ int(w) for w in re.findall('[0-9]+', open("../class_files/regex_sum_225350.txt", "r").read()) ]))
