
import os
from PIL import Image

base = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"
backup_dir = os.path.join(base, "backup")

large_pngs = [
    "1780994954802-80df6302-853e-45f5-a5d7-375f3bf954bb.png",
    "1780994965979-1c2c2527-ccd5-429d-86d1-cd5600fe9f12.png",
    "1780994972242-a24934d7-4b6e-419e-8ca6-7be5f89d4fa1.png",
    "1780994977158-ece1c71e-9431-4662-84d2-b01fdafe48cb.png",
    "1780994982482-eba8d537-d37c-427a-bf81-d3bde8fe90b1.png",
]

print("=== RGBA PNG quantize 降色压缩 ===\n")

for fname in large_pngs:
    backup = os.path.join(backup_dir, fname)
    src = os.path.join(base, fname)
    
    # Load from backup (original)
    img = Image.open(backup)
    size_before = os.path.getsize(src)  # current size on disk
    
    w, h = img.size
    MAX_W = 1200
    if w > MAX_W:
        ratio = MAX_W / w
        img = img.resize((MAX_W, int(h * ratio)), Image.LANCZOS)
    
    # Quantize RGBA to 256-color palette with alpha
    img_q = img.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG)
    img_q.save(src, 'PNG', optimize=True)
    
    size_after = os.path.getsize(src)
    pct = (1 - size_after / size_before) * 100
    kb_saved = (size_before - size_after) / 1024
    print(f"{fname}")
    print(f"  {size_before/1024:.1f}KB -> {size_after/1024:.1f}KB  ({pct:+.1f}% / {kb_saved:+.0f}KB)")

print("\nDone.")
