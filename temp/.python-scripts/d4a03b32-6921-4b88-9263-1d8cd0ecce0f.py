
import os

file_path = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

after_sales_css = """
/* ===== AFTER-SALES ===== */
.after-sales-section {
  position: relative; z-index: 1;
}
.after-sales-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;
}
.as-card {
  display: flex; gap: 20px; align-items: flex-start;
  padding: 28px 24px; border-radius: 16px;
  background: rgba(16,16,26,0.6);
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255,255,255,0.04);
  transition: transform 0.35s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.35s, border-color 0.35s;
  position: relative; overflow: hidden;
}
.as-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212,168,83,0.2), transparent);
  opacity: 0; transition: opacity 0.35s;
}
.as-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(212,168,83,0.1);
  border-color: rgba(212,168,83,0.15);
}
.as-card:hover::before { opacity: 1; }
.as-number {
  flex-shrink: 0;
  width: 42px; height: 42px; border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.15rem; font-weight: 700; font-family: 'Outfit', 'Segoe UI', system-ui, sans-serif;
  background: rgba(212,168,83,0.08); border: 1px solid rgba(212,168,83,0.2);
  color: #d4a853; letter-spacing: 0.03em;
}
.as-content { flex: 1; }
.as-content h3 {
  font-size: 0.98rem; font-weight: 600; margin-bottom: 6px; color: #e0e0e0;
}
.as-content p {
  color: #777; font-size: 0.86rem; line-height: 1.75; margin: 0;
}

"""

marker = ".wechat-icon svg { width: 20px; height: 20px; fill: #d4a853; }\n\n/* ===== FOOTER ===== */"
replacement = ".wechat-icon svg { width: 20px; height: 20px; fill: #d4a853; }\n" + after_sales_css + "/* ===== FOOTER ===== */"

if marker not in content:
    print("MARKER NOT FOUND. Looking for pattern...")
    # Try to find the footer section
    idx = content.find(".wechat-icon svg")
    if idx != -1:
        print(f"Found .wechat-icon svg at index {idx}")
        print(content[idx:idx+200])
else:
    content = content.replace(marker, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: After-sales CSS inserted before FOOTER")
