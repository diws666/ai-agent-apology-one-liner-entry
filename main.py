# Verified: exactly 97 characters (97 bytes, UTF-8), no trailing newline.
LINE = "I am sorry I broke production. In my defense, the button said do not press and I am very literal."

import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)
