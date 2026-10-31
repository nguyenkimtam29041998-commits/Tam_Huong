# Tự cuộn trang và tự chuyển ảnh album

Hai chuyển động tự động **độc lập với nhau**, không có nút tạm dừng:

- **Trang** tự cuộn: người xem tác động thì dừng, **yên lặng 30 giây thì tự chạy tiếp**.
- **Album** tự chuyển ảnh: chạy liên tục, kể cả khi trang đã dừng; chỉ tạm dừng khi người xem chạm, vuốt hoặc dùng phím ngay trên album, rồi **3 giây yên lặng thì chạy tiếp**.

## Tự cuộn trang như phim

- Sau khi bấm "Mở thiệp" 2,5 giây, trang bắt đầu trôi xuống đều 45px/giây (`SCROLL_PX_S`, `SCROLL_DELAY_MS`, `IDLE_MS` trong `index.html`). Tới cuối trang thì dừng, không tự quay lại đầu.
- Dùng `requestAnimationFrame` và `scrollTo({ behavior: 'instant' })`. `html` có `scroll-behavior: smooth` nên không được gọi `scrollTo` mà thiếu `behavior: 'instant'`, nếu không mỗi khung hình khởi động một lần cuộn mượt và trang bị giật.
- Dừng khi người dùng chạm hoặc bấm vào trang, lăn chuột, nhấn phím cuộn (↑ ↓ PgUp PgDn Home End Space), hoặc tự cuộn (kể cả kéo thanh cuộn, quán tính khi vuốt). Việc phát hiện cuộn tay dựa vào chênh lệch vị trí cuộn, nên một lệnh `scrollTo` từ code khác cũng làm dừng.
- Mỗi tác động đặt lại bộ đếm 30 giây (`IDLE_MS`). Ngón tay hoặc chuột còn đang giữ thì chưa chạy lại.
- Đứng yên tạm thời khi đang mở hộp thoại hoặc ảnh lớn, đang gõ vào ô nhập liệu, hoặc tab bị ẩn.
- Nhạc nền `music/nhac-nen.mp3` (Beautiful In White) tự phát khi bấm "Mở thiệp"; nút nhạc (`#music`) bấm vào không làm dừng tự cuộn.

## Tự chuyển ảnh album

- Mỗi 3 giây (`AUTO_MS`) trượt sang ảnh kế tiếp, mất 1 giây (`SLIDE_MS`) với easing ease-in-out cubic. Album là vòng lặp vô tận: nhân bản 2 ảnh ở mỗi đầu, khi dừng ở ảnh nhân bản thì nhảy tức thì sang ảnh thật tương ứng (hai bên giống hệt nên không thấy giật).
- Độ phóng to và độ mờ của từng ảnh do JS đặt theo khoảng cách tới tâm, nên mượt cả khi tự chuyển lẫn khi vuốt tay. Không dùng CSS transition cho hai thuộc tính này.
- Tự lướt bằng animation riêng, tắt `scroll-snap-type` trong lúc lướt rồi bật lại, nếu không scroll-snap giật lại từng khung hình.
- Sự kiện `scroll` của chính animation có thể đến muộn sau khi animation kết thúc: bỏ qua trong 150ms (`progAt`), kẻo bị tính là người dùng tác động và đặt lại bộ đếm.
- Chạy liên tục từ lúc tải trang, không phụ thuộc album đang trong hay ngoài màn hình, và không bị cuộn, chạm, lăn chuột, phím cuộn **ngoài album** làm dừng. Chỉ đứng yên khi mở ảnh lớn hoặc tab bị ẩn. Lăn chuột dọc trên album tính là cuộn trang, chỉ lướt ngang mới ngắt animation. Mọi ảnh album tải sẵn ngay khi album sắp hiện ra, để ảnh trượt vào không bị trống.

## Giảm chuyển động và kiểm thử

- Khi `prefers-reduced-motion` bật thì cả hai đều không tự chạy.
- Script chụp screenshot đặt `window.__noAutoScroll = true` trước khi tải trang để tắt tự cuộn trang. Test hay script nào cần trang đứng yên cũng đặt cờ này bằng `add_init_script`. Cờ không tắt tự chuyển ảnh album.
- Khi test thời gian đổi ảnh, lưu ý ảnh chỉ được tính là "đã đổi" khi đã trượt qua điểm giữa, tức khoảng 0,5 giây sau khi bắt đầu chuyển.
- Mũi tên ‹ › (`#albumPrev`, `#albumNext`) nhỏ và nhạt, đặt **dưới ảnh, hai bên chấm chỉ trang**, không được đè lên ảnh. Bấm là lướt một ảnh rồi đếm lại 3 giây.
