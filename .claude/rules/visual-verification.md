# Screenshot và so sánh với design gốc (bắt buộc)

Áp dụng sau mỗi thay đổi lớn, không có ngoại lệ. Thay đổi lớn là: thêm hoặc sửa một section, đổi bố cục, đổi màu/font/token, đổi hiệu ứng.

1. Chạy `python screenshot.py <tên-phiên-bản>` (Playwright + Chrome có sẵn). Script chụp màn hình mở thiệp và toàn trang ở khổ **375px**, **414px** (mobile) và **1440px** (desktop), lưu vào `screenshots/`, đồng thời báo có thanh cuộn ngang hay không.
2. Khi chỉ sửa một section, chụp riêng section đó: `python screenshot.py <tên> --el ".party"` (khổ 414px).
3. Mở 2 ảnh design gốc (`s1.png`, `s2.png`) và so sánh: màu, font, cỡ chữ, khoảng cách, thứ tự, vị trí hoa trang trí.
4. Ghi ngắn những chỗ còn lệch và sửa trước khi báo xong.

Không báo "đã giống design" khi chưa chụp và so sánh. Ảnh toàn trang rất dài: cắt thành từng đoạn để xem.
