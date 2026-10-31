---
paths:
  - "**/*.html"
  - "**/*.{js,ts,tsx,jsx}"
  - "**/*.css"
---

# Quy tắc khi viết code

- Component nhỏ, mỗi section một file, đặt tên tiếng Anh (`WeddingInfo`, `Countdown`, `GiftBox`); chữ hiển thị là tiếng Việt.
- Ngày giờ xử lý theo múi giờ `Asia/Ho_Chi_Minh`; dùng `Intl.DateTimeFormat('vi-VN')`.
- Ảnh: dùng WebP/AVIF, có `alt` tiếng Việt, lazy-load mọi ảnh dưới màn hình đầu. Ảnh hero nặng tối đa ~300KB.
- Nhạc nền: MP3 nhỏ hơn 3MB, chỉ tải khi người dùng bấm "Mở thiệp".
- Accessibility: tương phản chữ đủ đọc trên nền be, nút bấm tối thiểu 44×44px, focus hiển thị rõ.
- SEO và chia sẻ: đặt `title`, `description`, ảnh **Open Graph** (1200×630) cho từng thiệp để link hiện đẹp khi gửi qua Zalo/Facebook.
- Thiệp này dùng thông tin thật (số điện thoại, số tài khoản, địa chỉ) do chủ đám cưới cung cấp: chỉ sửa theo yêu cầu của họ, không tự bịa hay thay bằng dữ liệu giả.
