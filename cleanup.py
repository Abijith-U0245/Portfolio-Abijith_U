import re

with open('c:/Users/abiji/portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove base64 data after the profile.png img tag
pattern = r'(<img src="profile\.png" style="width:100%;display:block;object-fit:contain;">)[A-Za-z0-9+/=]+'
content = re.sub(pattern, r'\1', content)

with open('c:/Users/abiji/portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup complete")
