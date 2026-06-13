
import os
import shutil
from PIL import Image

base = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"
backup_dir = os.path.join(base, "backup")
os.makedirs(backup_dir, exist_ok=True)

exts = ('.jpg', '.jpeg', '.png')
MAX_W = 1200
JPEG_QUALITY = 85

files = [f for f in os.listdir(base) if f.lower().endswith(exts)]
print(f"共找到 {len(files)} 张图片\n")

total_before = 0
total_after = 0
results = []

for fname in sorted(files):
    src = os.path.join(base, fname)
    ext = fname.rsplit('.', 1)[-1].lower()
    size_before = os.path.getsize(src)
    total_before += size_before

    # Backup original
    shutil.copy2(src, os.path.join(backup_dir, fname))

    img = Image.open(src)
    orig_mode = img.mode
    has_alpha = orig_mode in ('RGBA', 'LA', 'PA') or (orig_mode == 'P' and 'transparency' in img.info)

    # Resize if width > MAX_W
    w, h = img.size
    if w > MAX_W:
        ratio = MAX_W / w
        img = img.resize((MAX_W, int(h * ratio)), Image.LANCZOS)

    # Determine output format
    if ext == 'png' and has_alpha:
        # Keep as PNG with alpha
        # Convert to RGB temporarily for save if mode has alpha, but save as PNG keeps alpha
        if img.mode == 'RGBA':
            # Optimize PNG: convert to palette if possible, else save with optimization
            img.save(src, 'PNG', optimize=True)
        elif img.mode == 'P':
            img.save(src, 'PNG', optimize=True)
        else:
            img.save(src, 'PNG', optimize=True)
        out_fmt = 'PNG'
    else:
        # Convert to JPEG
        if img.mode in ('RGBA', 'LA', 'PA', 'P'):
            # Handle alpha/transparency: composite on white background
            if img.mode in ('RGBA', 'LA'):
                bg = Image.new('RGB', img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else img.split()[1] if img.mode == 'LA' else None)
                img = bg
            elif img.mode == 'P':
                img = img.convert('RGBA')
                bg = Image.new('RGB', img.size, (255, 255, 255))
                bg.paste(img, mask=img.split()[-1])
                img = bg
            else:
                img = img.convert('RGB')
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # If original was PNG, rename to .jpg
        if ext == 'png':
            new_fname = fname.rsplit('.', 1)[0] + '.jpg'
            new_src = os.path.join(base, new_fname)
            # Remove old PNG (already backed up)
            img.save(new_src, 'JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
            os.remove(src)
            fname = new_fname
            src = new_src
            out_fmt = 'JPEG (from PNG)'
        else:
            img.save(src, 'JPEG', quality=JPEG_QUALITY, optimize=True, progressive=True)
            out_fmt = 'JPEG'

    size_after = os.path.getsize(src)
    total_after += size_after
    pct = (1 - size_after / size_before) * 100
    results.append((fname, size_before, size_after, pct, out_fmt, f"{w}x{h}"))
    print(f"{fname:<50s} {size_before:>8d}B -> {size_after:>8d}B  ({pct:5.1f}%)  [{out_fmt}]")

print(f"\n{'='*80}")
print(f"原始总大小: {total_before:>12,d} B  ({total_before/1024/1024:.2f} MB)")
print(f"压缩后总大小: {total_after:>12,d} B  ({total_after/1024/1024:.2f} MB)")
print(f"压缩率:       {(1-total_after/total_before)*100:>11.1f}%")
print(f"节省空间:     {total_before-total_after:>12,d} B  ({(total_before-total_after)/1024/1024:.2f} MB)")
print(f"备份目录:     {backup_dir}")
