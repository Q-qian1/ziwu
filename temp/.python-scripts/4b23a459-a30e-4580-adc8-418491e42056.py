
import re
import os
import urllib.request
import urllib.error

output_dir = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"
html_path = os.path.join(output_dir, "index.html")

# Read HTML
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all cdn.nlark.com URLs in src attributes
pattern = re.compile(r'src="(https://cdn\.nlark\.com/[^"]+)"')
matches = pattern.findall(content)
print(f"Found {len(matches)} CDN images")

# Deduplicate by filename
urls = list(dict.fromkeys(matches))  # preserve order
print(f"Unique URLs: {len(urls)}")

# Download and replace
success = 0
failed = 0
for url in urls:
    # Extract filename from URL
    filename = url.split('/')[-1]
    filepath = os.path.join(output_dir, filename)
    
    # Download if not exists
    if not os.path.exists(filepath):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                with open(filepath, 'wb') as f:
                    f.write(data)
            print(f"  Downloaded: {filename} ({len(data)} bytes)")
            success += 1
        except Exception as e:
            print(f"  FAILED: {filename} - {e}")
            failed += 1
            continue
    else:
        print(f"  Already exists: {filename}")
        success += 1
    
    # Replace in content
    content = content.replace(url, filename)

# Write back HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify no CDN URLs remain
remaining = re.findall(pattern, content)
print(f"\nRemaining CDN URLs in HTML: {len(remaining)}")
if remaining:
    for r in remaining:
        print(f"  {r}")

print(f"\nDone: {success} downloaded/existing, {failed} failed")
