"""Tạo ảnh web nhẹ từ ảnh gốc trong thư mục ảnh/ (giữ nguyên ảnh gốc).

Dùng: python optimize_photos.py
Mỗi ảnh BEExxxx.jpg tạo ra 2 file WebP trong images/photos/:
  BEExxxx-900.webp   cho album và ảnh bìa
  BEExxxx-1600.webp  cho ảnh xem lớn (lightbox)
Cần: pip install pillow
"""
import glob
import os
from PIL import Image, ImageOps

SRC, OUT = "ảnh", "images/photos"
SIZES = ((900, 80), (1600, 80))  # (chiều rộng, chất lượng WebP)

os.makedirs(OUT, exist_ok=True)
for f in sorted(glob.glob(f"{SRC}/*.jpg") + glob.glob(f"{SRC}/*.jpeg") + glob.glob(f"{SRC}/*.png")):
    name = os.path.splitext(os.path.basename(f))[0]
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")  # xoay đúng chiều theo EXIF
    for w, q in SIZES:
        out = f"{OUT}/{name}-{w}.webp"
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(out, "WEBP", quality=q, method=6)
        print(f"{out}  {os.path.getsize(out) / 1024:.0f}KB")
