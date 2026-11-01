import re

with open('/Users/ayyapparaja/Documents/SIH/sih67_dump/index.js') as f:
    code = f.read()

sections = ['problem', 'solution', 'architecture', 'market', 'validation', 'team']
for s in sections:
    pos = code.find(f'id:"{s}"')
    if pos == -1:
        pos = code.find(f'id:`{s}`')
    print(f"\n================ SECTION: {s} (pos: {pos}) ================")
    if pos != -1:
        print(code[pos:pos+800])
