---
paths:
  - "**/*.html"
  - "**/*.css"
  - "**/*.{tsx,jsx}"
  - "tailwind.config.*"
---

# Hệ thống thiết kế

## Màu sắc (lấy theo ảnh mẫu)

| Token | Giá trị | Dùng cho |
|---|---|---|
| `bg` | `#EFE3D6` → `#E3CFBC` (gradient) | nền trang |
| `paper-2` | `#F5EEE9` | nền cột thiệp |
| `card` | `#ECE1D5` | thẻ nội dung (lễ cưới, tiệc, lịch trình) |
| `paper` | `#FCF8F3` | thẻ mở thiệp, ô nhập liệu |
| `gold` | `#B8864E` | icon nét trong lịch trình |
| `primary` | `#7A665C` | nút, icon tròn, điểm nhấn |
| `primary-dark` | `#5E4D44` | hover nút |
| `ink` | `#6B5A50` | tiêu đề, tên |
| `muted` | `#A39488` | chữ phụ, ngày tháng |
| `line` | `#D9C8B8` | đường kẻ, viền mảnh |

Không dùng màu bão hòa mạnh (xanh, đỏ tươi). Đen thuần `#000` và trắng thuần làm nền đều tránh. Màu và font khai báo thành token (CSS variables), không viết mã màu rời rạc.

## Typography

- Tên cô dâu chú rể, tiêu đề lớn: serif cổ điển (**EB Garamond** hoặc **Cormorant Garamond**), weight 400–500.
- Nội dung, nút: **Lora** (serif dễ đọc).
- Nhãn section nhỏ: chữ in hoa, `letter-spacing` rộng (0.2em), cỡ 11–12px.
- Mọi font phải hỗ trợ **subset `vietnamese`**; kiểm tra dấu (ả, ỹ, ặ…) hiển thị đúng.

## Bố cục và chi tiết

- Nội dung nằm trong cột rộng bằng màn hình điện thoại: **375–414px** (token `--page-w: 414px`), căn giữa; desktop vẫn giữ dạng "thiệp dọc" với nền gradient hai bên. Màn hình mở thiệp giữ đúng tỉ lệ như `s1.png`.
- Card: nền `paper`, bo góc nhỏ (8–12px), shadow mềm, nhiều khoảng trắng.
- Nút: dạng viên thuốc (`rounded-full`), nền `primary`, chữ trắng.
- Phân cách: đường kẻ mảnh hai bên + họa tiết nhỏ ở giữa (❦).
- Hoa khô/cành lá: ảnh PNG nền trong (hoặc SVG), đặt ở góc card, không che chữ.
- Hiệu ứng nhẹ nhàng: lá rơi chậm ở nền, fade/slide-up khi cuộn tới section (xem `scroll-animation.md`).
