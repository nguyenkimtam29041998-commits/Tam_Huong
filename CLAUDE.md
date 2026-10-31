# CLAUDE.md

Hướng dẫn cho Claude Code khi làm việc trong dự án này: website **thiệp cưới online (bản demo)**, phong cách tối giản, hiện đại, chuyên nghiệp, tiếng Việt, ưu tiên điện thoại.

Chi tiết nằm trong [.claude/rules/](.claude/rules/), mỗi file một chủ đề. Các rule không có `paths` luôn được nạp; rule có `paths` chỉ nạp khi Claude làm việc với file khớp.

| File | Chủ đề | Nạp khi |
|---|---|---|
| `project-overview.md` | Mục tiêu, ảnh tham chiếu, bản quyền, trạng thái hiện tại | luôn |
| `visual-verification.md` | **Bắt buộc**: chụp screenshot và so sánh sau mỗi thay đổi lớn | luôn |
| `mobile-first.md` | **Bắt buộc**: mobile-friendly | luôn |
| `scroll-animation.md` | **Bắt buộc**: mọi section có animation khi cuộn | luôn |
| `auto-scroll.md` | Trang tự cuộn như phim, trang chạy lại sau 30 giây yên lặng, album chạy độc lập (3 giây/ảnh), cờ tắt khi chụp screenshot | luôn |
| `tech-stack.md` | Công nghệ, lệnh, cấu trúc thư mục, tách nội dung khỏi giao diện | luôn |
| `definition-of-done.md` | Checklist trước khi báo xong | luôn |
| `design-system.md` | Màu, font, bố cục | khi sửa HTML/CSS/TSX |
| `invitation-sections.md` | Danh sách và thứ tự các section thiệp | khi sửa HTML, component, data |
| `code-conventions.md` | Quy ước code, ảnh, nhạc, SEO, dữ liệu demo | khi sửa HTML/JS/TS/CSS |
