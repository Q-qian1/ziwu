
import os

base = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"
backup_dir = os.path.join(base, "backup")
exts = ('.jpg', '.jpeg', '.png')

# Current sizes
curr_files = [f for f in os.listdir(base) if f.lower().endswith(exts)]
curr_total = sum(os.path.getsize(os.path.join(base, f)) for f in curr_files)

# Backup (original) sizes
bak_files = [f for f in os.listdir(backup_dir) if f.lower().endswith(exts)]
bak_total = sum(os.path.getsize(os.path.join(backup_dir, f)) for f in bak_files)

print(f"当前图片数: {len(curr_files)}")
print(f"原始总大小: {bak_total/1024/1024:.2f} MB")
print(f"压缩后总大小: {curr_total/1024/1024:.2f} MB")
print(f"压缩率: {(1-curr_total/bak_total)*100:.1f}%")
print(f"节省空间: {(bak_total-curr_total)/1024/1024:.2f} MB")

# Check HTML references
html_path = os.path.join(base, "index.html")
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Verify no .png references remain for converted files
converted = ['1781096608773', '1781096613747', '1781096618143', '1781248912995']
for c in converted:
    if f'{c}.png' in html:
        print(f"WARNING: HTML still references {c}.png")
    elif f'{c}.jpg' in html:
        print(f"OK: HTML correctly references {c}.jpg")
    else:
        print(f"WARNING: HTML missing reference to {c}")
