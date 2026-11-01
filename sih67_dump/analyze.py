import re

with open('/Users/ayyapparaja/Documents/SIH/sih67_dump/index.js', 'r') as f:
    code = f.read()

# Find meaningful UI text strings
matches = re.findall(r'[\x27\x22\x60]([^\x27\x22\x60\n\r]{10,120})[\x27\x22\x60]', code)
ui_strings = set()
for m in matches:
    m_clean = m.strip()
    if ' ' in m_clean and len(m_clean) > 12:
        if not any(ch in m_clean for ch in ['{', '}', ';', '(', ')', '=', '<', '>', '+', '*', '\\', '$', 'return', 'function', 'import', 'export']):
            ui_strings.add(m_clean)

sorted_strings = sorted(list(ui_strings))
print(f"Total UI strings: {len(sorted_strings)}")
for s in sorted_strings[:50]:
    print("->", s)

# Search for component section titles or navigation items
nav = re.findall(r'\{[^{}]*name:[^{}]*href:[^{}]*\}', code)
print("\nNav items found:", nav)

# Search for section tags or IDs
sections = re.findall(r'id:[\x27\x22]([a-z0-9\-]+)[\x27\x22]', code)
print("\nSection IDs:", set(sections))
