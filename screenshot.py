"""Chụp screenshot index.html ở khổ mobile và desktop.

Dùng: python screenshot.py [tên-ghi-chú]   -> lưu vào screenshots/
Cần: pip install playwright (dùng Chrome đã cài sẵn, không cần tải trình duyệt).
"""
import sys
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
OUT = ROOT / "screenshots"
OUT.mkdir(exist_ok=True)
TAG = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y%m%d-%H%M")
URL = (ROOT / "index.html").resolve().as_uri()

SIZES = {"375": dict(width=375, height=812, mobile=True), "1440": dict(width=1440, height=900, mobile=False)}

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    for name, s in SIZES.items():
        page = browser.new_page(viewport={"width": s["width"], "height": s["height"]},
                                device_scale_factor=2 if s["mobile"] else 1,
                                is_mobile=s["mobile"], has_touch=s["mobile"])
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(1200)
        page.screenshot(path=OUT / f"{TAG}-cover-{name}.png")

        page.click("#openBtn")
        # Cuộn hết trang để các section chạy animation, rồi chụp toàn trang.
        page.evaluate("""async () => {
            for (let y = 0; y < document.body.scrollHeight; y += 300) { scrollTo({top: y, behavior: 'instant'}); await new Promise(r => setTimeout(r, 80)); }
            scrollTo({top: 0, behavior: 'instant'});
        }""")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1200)
        page.screenshot(path=OUT / f"{TAG}-page-{name}.png", full_page=True)
        overflow = page.evaluate("document.documentElement.scrollWidth > innerWidth")
        print(f"{name}px: thanh cuộn ngang = {overflow}")
        page.close()
    browser.close()
print("Đã lưu vào", OUT)
