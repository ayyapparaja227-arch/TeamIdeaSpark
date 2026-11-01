import re

with open('/Users/ayyapparaja/Documents/SIH/orca_dump/index.js') as f:
    code = f.read()

pos = code.find('ocean-statement')
if pos != -1:
    snippet = code[pos-300:pos+500]
    # find all strings
    strings = re.findall(r'[`\x27"]([^`\x27"]{15,200})[`\x27"]', snippet)
    for s in strings:
        print("->", s)
