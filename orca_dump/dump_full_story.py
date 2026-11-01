import re

with open('/Users/ayyapparaja/Documents/SIH/orca_dump/index.js') as f:
    code = f.read()

# Let's search for large string blocks or JSON data arrays
arrays = re.findall(r'\[\{[^{}\]]{100,5000}\}\]', code)
print(f"Large data arrays found: {len(arrays)}")

# Let's inspect each array
for i, arr in enumerate(arrays[:8]):
    print(f"\n--- ARRAY {i+1} (len {len(arr)}) ---")
    print(arr[:400], "...\n")
