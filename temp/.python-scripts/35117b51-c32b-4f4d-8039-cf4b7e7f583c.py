
import os
from PIL import Image

base = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output"

# Check large PNGs
large_pngs = [
    "1780994954802-80df6302-853e-45f5-a5d7-375f3bf954bb.png",
    "1780994965979-1c2c2527-ccd5-429d-86d1-cd5600fe9f12.png",
    "1780994972242-a24934d7-4b6e-419e-8ca6-7be5f89d4fa1.png",
    "1780994977158-ece1c71e-9431-4662-84d2-b01fdafe48cb.png",
    "1780994982482-eba8d537-d37c-427a-bf81-d3bde8fe90b1.png",
    "1780994588259-f495f9cd-0317-4b47-9022-ff506f792bd6.png",
    "1781260268419-c4e6c596-f26b-45fd-aca6-b40991a73fc8.png",
]

for fname in large_pngs:
    path = os.path.join(base, fname)
    if os.path.exists(path):
        img = Image.open(path)
        size_kb = os.path.getsize(path) / 1024
        print(f"{fname}: {img.size[0]}x{img.size[1]}  {img.mode}  {size_kb:.1f}KB")

# Check files that were converted PNG->JPG
converted = [
    "1781096608773-a51c1b87-8613-43b5-a9b0-53f30b86c71b.jpg",
    "1781096613747-0b14610d-9b87-4d2f-92b9-a5a89f57bbca.jpg",
    "1781096618143-340e3db9-69aa-4b8e-a8f3-3de096b760e4.jpg",
    "1781248912995-63f188f7-d149-4dba-9217-70fc09688263.jpg",
]
print("\nConverted PNG->JPG:")
for fname in converted:
    path = os.path.join(base, fname)
    if os.path.exists(path):
        img = Image.open(path)
        size_kb = os.path.getsize(path) / 1024
        print(f"{fname}: {img.size[0]}x{img.size[1]}  {img.mode}  {size_kb:.1f}KB")
