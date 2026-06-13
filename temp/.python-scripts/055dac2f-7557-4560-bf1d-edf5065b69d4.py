
import os
from PIL import Image

base = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"
backup_dir = os.path.join(base, "backup")

# Large RGBA PNGs - restore from backup and re-compress with compress_level=9
large_pngs = [
    "1780994954802-80df6302-853e-45f5-a5d7-375f3bf954bb.png",
    "1780994965979-1c2c2527-ccd5-429d-86d1-cd5600fe9f12.png",
    "1780994972242-a24934d7-4b6e-419e-8ca6-7be5f89d4fa1.png",
    "1780994977158-ece1c71e-9431-4662-84d2-b01fdafe48cb.png",
    "1780994982482-eba8d537-d37c-427a-bf81-d3bde8fe90b1.png",
]

print("=== 大 PNG 重压缩 (compress_level=9) ===\n")
for fname in large_pngs:
    src = os.path.join(base, fname)
    backup = os.path.join(backup_dir, fname)
    
    size_before = os.path.getsize(src)
    
    if os.path.exists(backup):
        # Use original backup, not already-"optimized" version
        img = Image.open(backup)
    else:
        img = Image.open(src)
    
    w, h = img.size
    MAX_W = 1200
    if w > MAX_W:
        ratio = MAX_W / w
        img = img.resize((MAX_W, int(h * ratio)), Image.LANCZOS)
    
    # Save PNG with max compression
    img.save(src, 'PNG', optimize=True, compress_level=9)
    
    size_after = os.path.getsize(src)
    pct = (1 - size_after / size_before) * 100
    print(f"{fname}")
    print(f"  {size_before/1024:.1f}KB -> {size_after/1024:.1f}KB  ({pct:+.1f}%)  {img.size[0]}x{img.size[1]} {img.mode}")

print("\n=== 更新 HTML 引用 (.png -> .jpg) ===\n")
html_path = os.path.join(base, "index.html")
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '1781096608773-a51c1b87-8613-43b5-a9b0-53f30b86c71b.png': '1781096608773-a51c1b87-8613-43b5-a9b0-53f30b86c71b.jpg',
    '1781096613747-0b14610d-9b87-4d2f-92b9-a5a89f57bbca.png': '1781096613747-0b14610d-9b87-4d2f-92b9-a5a89f57bbca.jpg',
    '1781096618143-340e3db9-69aa-4b8e-a8f3-3de096b760e4.png': '1781096618143-340e3db9-69aa-4b8e-a8f3-3de096b760e4.jpg',
    '1781248912995-63f188f7-d149-4dba-9217-70fc09688263.png': '1781248912995-63f188f7-d149-4dba-9217-70fc09688263.jpg',
}

for old, new in replacements.items():
    count = html.count(old)
    html = html.replace(old, new)
    print(f"  {old.rsplit('.',1)[0]}.png -> .jpg  ({count}处)")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("\nHTML 已更新。")
