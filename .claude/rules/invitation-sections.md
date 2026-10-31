---
paths:
  - "**/*.html"
  - "src/components/invitation/**"
  - "src/data/**"
---

# Các section của thiệp (theo thứ tự)

1. **Màn hình mở thiệp (cover)**: icon tim tròn, tên "Kim Tâm & Lan Hương", ngày 29 tháng 11, 2026, "Thân mời", nút **Mở thiệp**. Bấm nút thì mở thiệp và bắt đầu phát nhạc (trình duyệt chặn autoplay nên nhạc chỉ phát sau thao tác này).
2. **Hero**: nhãn "The wedding of", tên hai người chữ nghiêng, ảnh polaroid (ảnh cưới BEE08701) nghiêng có băng dính giấy, con dấu sáp và bó hoa khô.
3. **Thông tin lễ cưới**: bố mẹ hai họ kèm địa chỉ (2 cột có vạch dọc), chú rể Nguyễn Kim Tâm, cô dâu Trần Lan Hương, hai buổi lễ trong cùng ngày Chủ nhật 29/11/2026 (âm lịch 21/10 Bính Ngọ): **Lễ Vu Quy 13:00** và **Lễ Thành Hôn 14:00**, khối ngày "THỨ | 29 | THÁNG".
4. **Album ảnh**: băng chuyền gồm các ảnh trong thư mục `ảnh/` **trừ `BEE08708`** (hiện 9 ảnh, khung 2:3), **xoay vòng vô tận** (nhân bản 2 ảnh ở mỗi đầu, hết ảnh cuối trượt liền sang ảnh đầu), ảnh ở giữa phóng to dần theo vị trí, chấm chỉ trang, bấm để xem lớn (lightbox). Không có nút ‹ ›. Mỗi 3 giây tự trượt sang ảnh kế tiếp (1 giây, easing mượt). Album chạy liên tục, không dừng theo trang. Chỉ khi người xem chạm hoặc vuốt đúng vào album thì tạm dừng để xem lại hoặc xem tiếp, yên lặng 3 giây thì tự chạy tiếp. Mở lightbox thì đứng yên. Không tự chạy khi `prefers-reduced-motion`. Chi tiết kỹ thuật trong `auto-scroll.md` (cuộn ngang bằng `scrollLeft`, không dùng `scrollIntoView`).
5. **Thông tin tiệc cưới**: tiệc nhà Trai và nhà Gái cùng 16:30 Thứ bảy 28/11/2026 (âm lịch 20/10), khối ngày, **lịch tháng 11/2026** (ngày 28 khoanh tròn, ngày 29 hình tim, có chú thích), **đồng hồ đếm ngược** tới Lễ Thành Hôn, link "Thêm vào lịch" (.ics có 4 sự kiện), nút "Xác nhận tham dự" (mở hộp thoại RSVP).
6. **Địa điểm**: hai nơi tổ chức tiệc, mỗi nơi có tên, địa chỉ, link "Chỉ đường" (Google Maps); cả hai nhà đều có số điện thoại bấm gọi được (nhà Trai 0333 356 886, nhà Gái 0363 438 617); tranh vẽ toà nhà mờ.
8. **Lịch trình ngày cưới**: icon nét vàng · giờ · chấm trên trục nét đứt · hoạt động. 13:00 Lễ Vu Quy · 13:30 Giao lưu chụp ảnh cùng nhà gái · 14:00 Lễ Thành Hôn · 14:50 Giao lưu chụp ảnh cùng nhà trai.
9. **Xác nhận tham dự (RSVP)**: hộp thoại gồm họ tên, số điện thoại, tham dự hay không, số người.
10. **Sổ lưu bút**: form tên + lời chúc, danh sách lời chúc bên dưới.
11. **Hộp quà mừng**: hình hộp quà bấm được, mở hộp thoại chuyển khoản với 2 tab chú rể / cô dâu. Dùng **ảnh QR ngân hàng thật** (`images/qr/groom.png`, `images/qr/bride.png`, cắt từ `QR/CR` và `QR/CD`) cùng ngân hàng, tên và số tài khoản khớp với mã QR (Techcombank: NGUYEN KIM TAM 1903 1555 0030 17; TRAN LAN HUONG 1907 3282 2880 18), nút sao chép số tài khoản. Đổi tài khoản thì phải cắt lại ảnh QR và sửa `BANKS` trong `index.html`.
12. **Nút nổi**: bật/tắt nhạc, giữa mép phải màn hình. Không dùng nút Messenger của mẫu gốc trừ khi được yêu cầu. Không có nút tạm dừng cho tự cuộn trang hay album.

## Dữ liệu demo

Bản demo dùng thông tin thật của đám cưới nhưng lời chúc mẫu trong sổ lưu bút là tên giả. Form RSVP và lời chúc chỉ lưu tạm phía client (`localStorage`, khoá `wishes-v2`; đổi khoá khi cần xoá lời chúc đã lưu trong trình duyệt) hoặc hiển thị thông báo "đã gửi"; chưa nối backend trừ khi được yêu cầu.
