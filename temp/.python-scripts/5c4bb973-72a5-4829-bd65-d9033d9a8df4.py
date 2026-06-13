
import os

file_path = r"C:\Users\Administrator\AppData\Roaming\Tencent\Marvis\User\oAN1i2TIPZU4jdXjuXy26Kkhaw-k\workspace\conv_19ec034636f_cda3115e48bb\output\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the after-sales section boundaries
start_marker = "\n<!-- After-Sales -->"
end_marker = "</section>\n\n<!-- Contact -->"

start_idx = content.find(start_marker)
if start_idx == -1:
    print("ERROR: start marker not found!")
    # Try alternative
    start_idx = content.find("<!-- After-Sales -->")
    print(f"Found '<!-- After-Sales -->' at {start_idx}")
else:
    print(f"Found start marker at {start_idx}")

# Find end marker after start
end_idx = content.find(end_marker, start_idx)
if end_idx == -1:
    print("ERROR: end marker not found!")
else:
    end_idx += len(end_marker) - len("<!-- Contact -->")
    print(f"End marker found at {end_idx}")
    
    # Verify what we're removing
    to_remove = content[start_idx:end_idx]
    print(f"\nRemoving {len(to_remove)} chars from index {start_idx} to {end_idx}")
    print(f"First 100 chars: {to_remove[:100]}")
    print(f"Last 100 chars: {to_remove[-100:]}")
    
    # Do the removal, keeping only "<!-- Contact -->"
    new_content = content[:start_idx] + "\n<!-- Contact -->" + content[end_idx + len(end_marker) - len("<!-- Contact -->"):]
    
    # Verify
    if "after-sales" in new_content.lower():
        # Check if remaining references are only in CSS (should be removed already) or nav
        remaining = new_content.lower().count("after-sales")
        print(f"\nWARNING: {remaining} 'after-sales' references remain!")
        # Show where
        for line_no, line in enumerate(new_content.split('\n'), 1):
            if 'after-sales' in line.lower():
                print(f"  Line {line_no}: {line.strip()}")
    else:
        print("\nSUCCESS: All 'after-sales' references removed from file.")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("\nFile written successfully.")
