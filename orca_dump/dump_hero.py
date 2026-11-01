import re

with open('/Users/ayyapparaja/Documents/SIH/orca_dump/index.js') as f:
    code = f.read()

# Look for hero section or top section
pos = code.find('ocean-statement')
if pos != -1:
    print("Found ocean-statement at:", pos)
    print(code[pos-200:pos+1000])

# Look for opening h1 / hero title
pos_top = code.find('id:`top`')
if pos_top == -1:
    pos_top = code.find('id:"top"')
if pos_top != -1:
    print("\nFound top section at:", pos_top)
    print(code[pos_top:pos_top+1200])
