# Animation khi cuộn (bắt buộc)

Mọi section đều có animation khi cuộn tới. Section mới thêm mà chưa có animation thì chưa được coi là xong.

- Hiệu ứng: fade + trượt lên nhẹ 16–24px, 0.6–0.8s, `ease-out`.
  - Bản Next.js: `whileInView` của Framer Motion với `viewport={{ once: true, amount: 0.2 }}`.
  - Bản `index.html` hiện tại: class `.reveal` + `IntersectionObserver`.
- Dùng chung một component bọc (ví dụ `<Reveal>`) để mọi section đồng nhất.
- Các phần tử con (ảnh album, mục timeline, lời chúc) xuất hiện lần lượt (stagger 0.08–0.12s).
- Chỉ animate `opacity` và `transform` để mượt trên điện thoại.
- Khi `prefers-reduced-motion` bật thì hiện ngay, không chuyển động (kể cả lá rơi ở nền).
