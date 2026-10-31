# Tổng quan dự án

Website giới thiệu **mẫu thiệp cưới online** (bản demo). Khách vào xem một thiệp mẫu hoàn chỉnh, có thể chia sẻ link cho khách mời.

- Mẫu tham chiếu: https://chungdoi.com/vi/mau-thiep/minimalism-nau/demo
- Ảnh tham chiếu trong thư mục gốc:
  - `s1.png`: màn hình mở thiệp gốc (cover).
  - `s2.png`: toàn trang thiệp gốc sau khi mở (ảnh rất nhỏ, phóng to để xem bố cục).
  - `s3.png`: ảnh chụp bản demo của chính dự án này, **không phải** mẫu gốc.
- Phong cách: **tối giản, hiện đại, chuyên nghiệp**, tông be/nâu ấm, hoa khô trang trí ở góc.
- Ngôn ngữ giao diện: **tiếng Việt** (có dấu đầy đủ). Định dạng ngày kiểu Việt: `3 tháng 1, 2026`, giờ 24h.
- Ưu tiên **mobile-first**: phần lớn khách mời mở thiệp trên điện thoại qua Zalo/Messenger.

Khi phân vân về bố cục hay chi tiết, mở lại 2 ảnh tham chiếu (`s1.png`, `s2.png`) và bám theo chúng.

## Bản quyền

Không sao chép mã nguồn, ảnh hay logo của chungdoi.com: chỉ lấy cảm hứng bố cục và phong cách, mọi asset phải tự làm hoặc có giấy phép.

## Trạng thái hiện tại

Bản demo đầu tiên là **một file `index.html` độc lập** (HTML + CSS + JS thuần, font Google, ảnh cưới thật trong `images/photos/`). Hiệu ứng cuộn dùng `IntersectionObserver` với class `.reveal` (thêm `style="--d:.1s"` để xuất hiện lần lượt). Mở `index.html#open` sẽ bỏ qua màn hình cover. Khi chuyển sang Next.js (xem `tech-stack.md`), giữ nguyên giao diện và token màu của file này.

## Ảnh của cô dâu chú rể

- Ảnh gốc nằm trong `ảnh/` (mỗi ảnh 7–18 MB, 4565×6847): **không đưa thẳng lên web**. Dùng bản WebP nhẹ trong `images/photos/` (`<tên>-900.webp` cho album và ảnh bìa, `<tên>-1600.webp` cho ảnh xem lớn). Thêm ảnh mới vào `ảnh/` rồi chạy `python optimize_photos.py`.
- Ảnh bìa ("The wedding of") là `BEE08701`. Album gồm các ảnh trong `ảnh/` (bỏ `BEE08708`), đúng thứ tự tên file. `images/og.jpg` (1200×630) là ảnh chia sẻ; khi có tên miền phải đổi `og:image` thành URL tuyệt đối.
- Không áp bộ lọc màu (sepia…) lên ảnh thật, giữ nguyên màu thợ ảnh đã chỉnh.

