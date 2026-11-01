import re

with open('/Users/ayyapparaja/Documents/SIH/orca_dump/index.js') as f:
    code = f.read()

# Let's search for the chapter index array
# Something like [{ num: '01', id: 'ocean', title: ... }]
idx_start = code.find('chapter-index')
if idx_start != -1:
    print("Found chapter-index around:", idx_start)
    print(code[idx_start-200:idx_start+800])

# Let's inspect the sections: 'ocean', 'reasoning', 'evidence', 'decision', 'system', 'crew'
for sec_id in ['ocean', 'reasoning', 'evidence', 'decision', 'system', 'crew']:
    pos = code.find(f'id:`{sec_id}`')
    if pos == -1:
        pos = code.find(f'id:"{sec_id}"')
    if pos != -1:
        print(f"\n================ SECTION: {sec_id} ================")
        print(code[pos:pos+1500])
