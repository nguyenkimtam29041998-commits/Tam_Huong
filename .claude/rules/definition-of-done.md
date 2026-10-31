# Kiểm tra trước khi coi là xong

- Đã chụp screenshot 375px, 414px và 1440px, so với design gốc và sửa các chỗ lệch (xem `visual-verification.md`).
- Không có thanh cuộn ngang ở mọi khổ từ 360px trở lên.
- Mọi section đều có animation khi scroll và tắt đúng khi bật `prefers-reduced-motion`.
- Dấu tiếng Việt hiển thị đúng ở mọi font.
- `npm run build` và `npm run lint` chạy không lỗi (khi dự án đã chuyển sang Next.js).
- Lighthouse mobile: Performance và Accessibility từ 90 trở lên.
