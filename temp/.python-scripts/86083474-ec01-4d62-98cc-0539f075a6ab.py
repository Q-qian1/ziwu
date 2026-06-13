
import os

file_path = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove nav link
old_nav = '      <li><a href="#after-sales">售后</a></li>\n'
content = content.replace(old_nav, '')

# 2. Remove phone responsive after-sales rules
old_phone = '\n  .after-sales-grid { grid-template-columns: 1fr; gap: 14px; }\n  .as-card { padding: 24px 20px; }'
content = content.replace(old_phone, '')

# 3. Remove small phone responsive after-sales rules
old_small = '\n  .as-card { padding: 18px 14px; border-radius: 14px; }\n  .as-number { width: 34px; height: 34px; font-size: 0.95rem; border-radius: 10px; }\n  .as-content h3 { font-size: 0.88rem; }\n  .as-content p { font-size: 0.78rem; line-height: 1.65; }'
content = content.replace(old_small, '')

# Final check
remaining = content.lower().count("after-sales") + content.lower().count(".as-card") + content.lower().count(".as-number") + content.lower().count(".as-content")
if remaining > 0:
    print(f"WARNING: {remaining} after-sales references remain!")
    for line_no, line in enumerate(content.split('\n'), 1):
        lower = line.lower()
        if any(x in lower for x in ['after-sales', '.as-card', '.as-number', '.as-content']):
            print(f"  Line {line_no}: {line.strip()}")
else:
    print("SUCCESS: All after-sales references cleaned.")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("File written.")
