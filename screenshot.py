"""Chụp screenshot index.html ở khổ mobile và desktop.

Dùng:
  python screenshot.py <tên>                 -> cover + toàn trang ở 375, 414, 1440px
  python screenshot.py <tên> --el ".album"   -> chỉ chụp phần tử đó ở 414px (nhanh, để soi từng section)
Ảnh lưu vào screenshots/. Cần: pip install playwright (dùng Chrome đã cài sẵn).
"""
import sys
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
OUT = ROOT / "screenshots"
OUT.mkdir(exist_ok=True)
args = sys.argv[1:]
EL = None
if "--el" in args:
    i = args.index("--el"); EL = args[i + 1]; del args[i:i + 2]
TAG = args[0] if args else datetime.now().strftime("%Y%m%d-%H%M")
URL = (ROOT / "index.html").resolve().as_uri()

SIZES = {"375": (375, 812, True), "414": (414, 896, True), "1440": (1440, 900, False)}
if EL:
    SIZES = {"414": SIZES["414"]}

REVEAL_ALL = """async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 300) { scrollTo({top: y, behavior: 'instant'}); await new Promise(r => setTimeout(r, 80)); }
    scrollTo({top: 0, behavior: 'instant'});
}"""

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    for name, (w, h, mobile) in SIZES.items():
        page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2 if mobile else 1,
                                is_mobile=mobile, has_touch=mobile)
        page.add_init_script("window.__noAutoScroll = true")  # tắt tự cuộn để ảnh chụp ổn định
        page.goto(URL, wait_until="networkidle")
        page.wait_for_timeout(1200)
        if not EL:
            page.screenshot(path=OUT / f"{TAG}-cover-{name}.png")
        page.click("#openBtn")
        page.evaluate(REVEAL_ALL)
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1300)
        if EL:
            for k, loc in enumerate(page.locator(EL).all()):
                f = OUT / f"{TAG}-{EL.strip('.#').replace(' ', '_')}{'-' + str(k) if k else ''}.png"
                loc.screenshot(path=f); print("Đã lưu", f.name)
        else:
            page.screenshot(path=OUT / f"{TAG}-page-{name}.png", full_page=True)
        overflow = page.evaluate("document.documentElement.scrollWidth > innerWidth")
        print(f"{name}px: thanh cuộn ngang = {overflow}")
        page.close()
    browser.close()
