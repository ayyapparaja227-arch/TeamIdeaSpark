import re

with open('/Users/ayyapparaja/Documents/SIH/orca_dump/index.js') as f:
    code = f.read()

# Let's find all objects with {name: ..., body: ...} or {id: ..., title: ...}
matches = re.findall(r'(\b[a-zA-Z0-9_$]{1,4})\s*=\s*(\[\s*\{[^\n]{20,2000}\}\s*\])', code)
print(f"Matched variable arrays: {len(matches)}")

for var_name, content in matches:
    if any(k in content for k in ['name:', 'title:', 'body:', 'role:', 'source:', 'agency:', 'step:', 'domain:']):
        print(f"\n>>> VAR {var_name} (length {len(content)}):")
        print(content[:500] + ("..." if len(content) > 500 else ""))
