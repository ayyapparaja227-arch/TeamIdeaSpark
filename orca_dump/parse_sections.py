import re

with open('/Users/ayyapparaja/Documents/SIH/orca_dump/index.js') as f:
    code = f.read()

# Let's find the chapter index navigation items!
# In index.js, look for anchor links <a href="#..."> or navigation array
navs = re.findall(r'href:[\x27"`]#([a-z0-9\-]+)[\x27"`][^}]*children:[\x27"`]([^`\x27"]+)[\x27"`]', code)
print("Nav links found:", navs)

# Also search for <section id="...">
sections = re.findall(r'id:[\x27"`]([a-z0-9\-]+)[\x27"`]', code)
print("IDs found:", [s for s in sections if s not in ['root', 'chapter-index']])

# Let's find h2 elements
h2s = re.findall(r'jsx\([\x27"`]h2[\x27"`],[^}]*children:([^\)]+)\)', code)
print(f"H2 count: {len(h2s)}")
for h in h2s[:15]:
    print("H2 ->", h[:100])
