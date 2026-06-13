
import os

base = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"
backup_dir = os.path.join(base, "backup")
exts = ('.jpg', '.jpeg', '.png')

curr_files = [f for f in os.listdir(base) if f.lower().endswith(exts)]
bak_files = [f for f in os.listdir(backup_dir) if f.lower().endswith(exts)]

print("=" * 80)
print(f"{'文件':<55s} {'原始':>8s} {'压缩后':>8s} {'压缩率':>7s}")
print("-" * 80)

for fname in sorted(curr_files):
    curr_path = os.path.join(base, fname)
    bak_path = os.path.join(backup_dir, fname)
    curr_sz = os.path.getsize(curr_path)
    bak_sz = os.path.getsize(bak_path) if os.path.exists(bak_path) else curr_sz
    pct = (1 - curr_sz / bak_sz) * 100
    print(f"{fname:<55s} {bak_sz/1024:>7.1f}K {curr_sz/1024:>7.1f}K {pct:>6.1f}%")

curr_total = sum(os.path.getsize(os.path.join(base, f)) for f in curr_files)
bak_total = sum(os.path.getsize(os.path.join(backup_dir, f)) for f in bak_files if f.lower().endswith(exts))

print("-" * 80)
print(f"{'TOTAL':<55s} {bak_total/1024/1024:>7.2f}M {curr_total/1024/1024:>7.2f}M {(1-curr_total/bak_total)*100:>6.1f}%")
print("=" * 80)

# Verify no leftovers
leftover_png = [f for f in curr_files if f in ['1781096608773-a51c1b87-8613-43b5-a9b0-53f30b86c71b.png',
    '1781096613747-0b14610d-9b87-4d2f-92b9-a5a89f57bbca.png',
    '1781096618143-340e3db9-69aa-4b8e-a8f3-3de096b760e4.png',
    '1781248912995-63f188f7-d149-4dba-9217-70fc09688263.png']]
if leftover_png:
    print(f"\nWARNING: leftover .png files: {leftover_png}")
else:
    print("\n无残留旧 .png 文件，一切正常。")
