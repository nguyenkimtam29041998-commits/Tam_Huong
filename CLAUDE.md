# CLAUDE.md

Hướng dẫn cho Claude Code khi làm việc trong dự án này.

## Quy tắc bắt buộc

Các quy tắc này áp dụng cho mọi thay đổi, không có ngoại lệ.

1. **Screenshot và so sánh sau mỗi thay đổi lớn.** Thay đổi lớn là: thêm hoặc sửa một section, đổi bố cục, đổi màu/font/token, đổi hiệu ứng. Sau khi làm xong:
   - Chạy `python screenshot.py <tên-phiên-bản>` (Playwright + Chrome có sẵn). Script chụp màn hình mở thiệp và toàn trang ở khổ **375px** (mobile) và **1440px** (desktop), lưu vào `screenshots/`, đồng thời báo có thanh cuộn ngang hay không. Ảnh toàn trang khá dài, nên cắt thành từng đoạn để xem.
   - Mở 2 ảnh design gốc và so sánh: màu, font, cỡ chữ, khoảng cách, thứ tự, vị trí hoa trang trí.
   - Ghi ngắn những chỗ còn lệch và sửa trước khi báo xong. Không báo "đã giống design" khi chưa chụp và so sánh.
2. **Mobile-friendly.**
   - Thiết kế mobile-first; kiểm tra tối thiểu ở 360px, 375px, 414px và 768px.
   - Không có thanh cuộn ngang; chữ nội dung tối thiểu 14px; nút và vùng bấm tối thiểu 44×44px.
   - Có thẻ `<meta name="viewport" content="width=device-width, initial-scale=1">`; không chặn người dùng phóng to.
   - Ảnh co giãn theo khung (`max-width: 100%`), form dễ nhập trên bàn phím điện thoại (đúng `type`/`inputmode`).
3. **Mọi section có animation khi scroll.**
   - Mỗi section xuất hiện bằng hiệu ứng khi cuộn tới (fade + trượt lên nhẹ 16–24px, 0.6–0.8s, `ease-out`), dùng `whileInView` của Framer Motion với `viewport={{ once: true, amount: 0.2 }}`.
   - Dùng chung một component bọc (ví dụ `<Reveal>`) để mọi section đồng nhất; các phần tử con (ảnh album, mục timeline, lời chúc) xuất hiện lần lượt (stagger 0.08–0.12s).
   - Chỉ animate `opacity` và `transform` để mượt trên điện thoại; khi `prefers-reduced-motion` bật thì hiện ngay, không chuyển động.
   - Section mới thêm mà chưa có animation thì chưa được coi là xong.

## Dự án

Website giới thiệu **mẫu thiệp cưới online** (bản demo). Khách vào xem một thiệp mẫu hoàn chỉnh, có thể chia sẻ link cho khách mời.

- Mẫu tham chiếu: https://chungdoi.com/vi/mau-thiep/minimalism-nau/demo
- Ảnh tham chiếu trong thư mục gốc:
  - `chungdoi.com_vi_mau-thiep_minimalism-nau_demo.png`: màn hình mở thiệp (cover).
  - `chungdoi.com_vi_mau-thiep_minimalism-nau_demo (1).png`: toàn trang thiệp sau khi mở.
- Phong cách: **tối giản, hiện đại, chuyên nghiệp**, tông be/nâu ấm, hoa khô trang trí ở góc.
- Ngôn ngữ giao diện: **tiếng Việt** (có dấu đầy đủ). Định dạng ngày kiểu Việt: `3 tháng 1, 2026`, giờ 24h.
- Ưu tiên **mobile-first**: phần lớn khách mời mở thiệp trên điện thoại qua Zalo/Messenger.

Khi phân vân về bố cục hay chi tiết, mở lại 2 ảnh tham chiếu và bám theo chúng. Không sao chép mã nguồn, ảnh hay logo của chungdoi.com: chỉ lấy cảm hứng bố cục và phong cách, mọi asset phải tự làm hoặc có giấy phép.

## Trạng thái hiện tại

Bản demo đầu tiên là **một file `index.html` độc lập** (HTML + CSS + JS thuần, font Google, ảnh mẫu từ Unsplash). Hiệu ứng cuộn dùng `IntersectionObserver` với class `.reveal` (thêm `style="--d:.1s"` để xuất hiện lần lượt). Mở `index.html#open` sẽ bỏ qua màn hình cover. Khi chuyển sang Next.js theo phần dưới, giữ nguyên giao diện và token màu của file này.

## Công nghệ (mặc định, đổi được nếu chủ dự án yêu cầu)

- **Next.js (App Router) + TypeScript**, xuất tĩnh (`output: 'export'`) để host trên Vercel/Netlify.
- **Tailwind CSS** cho style; màu và font khai báo thành token trong `tailwind.config` / CSS variables, không viết mã màu rời rạc trong component.
- **Framer Motion** cho hiệu ứng; `next/font` cho Google Fonts; `next/image` cho ảnh.
- Không thêm thư viện UI nặng (MUI, Ant…). Lịch, đồng hồ đếm ngược, form tự viết.

Lệnh thường dùng:

```bash
npm install
npm run dev      # chạy local tại http://localhost:3000
npm run build    # build + xuất tĩnh
npm run lint
```

## Cấu trúc thư mục đề xuất

```
src/
  app/
    page.tsx                 # trang chủ / danh sách mẫu
    mau-thiep/[slug]/demo/   # trang demo từng mẫu
  components/
    invitation/              # mỗi section thiệp là 1 component
    ui/                      # Button, Card, SectionTitle, Divider...
  data/
    invitations/minimalism-nau.ts   # toàn bộ nội dung thiệp
  lib/                       # format ngày, countdown, helpers
  styles/globals.css
public/
  images/  decor/  music/
```

**Nội dung thiệp tách khỏi giao diện**: tên cô dâu chú rể, ngày giờ, địa điểm, ảnh, lịch trình, tài khoản mừng cưới… nằm trong file `data/`, có kiểu TypeScript (`InvitationData`). Component chỉ đọc dữ liệu, không hard-code tên hay ngày. Như vậy thêm mẫu mới chỉ cần thêm file data + theme.

## Hệ thống thiết kế

### Màu sắc (lấy theo ảnh mẫu)

| Token | Giá trị | Dùng cho |
|---|---|---|
| `bg` | `#EFE3D6` → `#E3CFBC` (gradient) | nền trang |
| `paper` | `#FCF8F3` | thẻ/card nội dung |
| `primary` | `#7A665C` | nút, icon tròn, điểm nhấn |
| `primary-dark` | `#5E4D44` | hover nút |
| `ink` | `#6B5A50` | tiêu đề, tên |
| `muted` | `#A39488` | chữ phụ, ngày tháng |
| `line` | `#D9C8B8` | đường kẻ, viền mảnh |

Không dùng màu bão hòa mạnh (xanh, đỏ tươi). Đen thuần `#000` và trắng thuần làm nền đều tránh.

### Typography

- Tên cô dâu chú rể, tiêu đề lớn: serif cổ điển (**EB Garamond** hoặc **Cormorant Garamond**), weight 400–500.
- Nội dung, nút: **Lora** (serif dễ đọc).
- Nhãn section nhỏ: chữ in hoa, `letter-spacing` rộng (0.2em), cỡ 11–12px.
- Mọi font phải hỗ trợ **subset `vietnamese`**; kiểm tra dấu (ả, ỹ, ặ…) hiển thị đúng.

### Bố cục và chi tiết

- Nội dung nằm trong cột hẹp, `max-w` khoảng **420–480px**, căn giữa; desktop vẫn giữ dạng "thiệp dọc" với nền gradient hai bên.
- Card: nền `paper`, bo góc nhỏ (8–12px), shadow mềm, nhiều khoảng trắng.
- Nút: dạng viên thuốc (`rounded-full`), nền `primary`, chữ trắng.
- Phân cách: đường kẻ mảnh hai bên + họa tiết nhỏ ở giữa (❦).
- Hoa khô/cành lá: ảnh PNG nền trong, đặt ở góc card, không che chữ.
- Hiệu ứng nhẹ nhàng: lá rơi chậm ở nền, fade/slide-up khi cuộn tới section. Tôn trọng `prefers-reduced-motion`.

## Các section của thiệp (theo thứ tự)

1. **Màn hình mở thiệp (cover)**: icon tim tròn, tên "Hoàng Nam & Thảo Vy", ngày, "Thân mời", nút **Mở thiệp**. Bấm nút thì mở thiệp và bắt đầu phát nhạc (trình duyệt chặn autoplay nên nhạc chỉ phát sau thao tác này).
2. **Hero**: ảnh cưới khung polaroid, nhãn nhỏ "Save the date", tên hai người.
3. **Thông tin lễ cưới**: tên bố mẹ hai họ, tên cô dâu chú rể, thứ / ngày / giờ, ngày âm lịch, địa điểm.
4. **Album ảnh**: lưới/carousel ảnh, bấm để xem lớn (lightbox).
5. **Thông tin tiệc cưới**: giờ đón khách, giờ khai tiệc, **lịch tháng** đánh dấu ngày cưới, **đồng hồ đếm ngược**, nút "Xem bản đồ" (mở Google Maps).
6. **Dress code**: các chấm màu gợi ý trang phục.
7. **Lịch trình ngày cưới**: timeline giờ + icon + hoạt động.
8. **Xác nhận tham dự (RSVP)**: họ tên, số người, tham dự hay không, lời nhắn.
9. **Sổ lời chúc**: danh sách lời chúc của khách (tên, thời gian, nội dung).
10. **Hộp quà mừng cưới**: thông tin chuyển khoản + mã QR của cô dâu và chú rể, nút sao chép số tài khoản.
11. **Nút nổi**: bật/tắt nhạc. Không dùng nút Messenger của mẫu gốc trừ khi được yêu cầu.

Bản demo dùng dữ liệu mẫu (tên, ảnh, ngân hàng giả). Form RSVP và lời chúc ở bản demo chỉ lưu tạm phía client hoặc hiển thị thông báo "đã gửi"; chưa nối backend trừ khi được yêu cầu.

## Quy tắc khi viết code

- Component nhỏ, mỗi section một file, đặt tên tiếng Anh (`WeddingInfo`, `Countdown`, `GiftBox`); chữ hiển thị là tiếng Việt.
- Ngày giờ xử lý theo múi giờ `Asia/Ho_Chi_Minh`; dùng `Intl.DateTimeFormat('vi-VN')`.
- Ảnh: dùng WebP/AVIF, có `alt` tiếng Việt, lazy-load mọi ảnh dưới màn hình đầu. Ảnh hero nặng tối đa ~300KB.
- Nhạc nền: MP3 nhỏ hơn 3MB, chỉ tải khi người dùng bấm "Mở thiệp".
- Accessibility: tương phản chữ đủ đọc trên nền be, nút bấm tối thiểu 44×44px, focus hiển thị rõ.
- SEO và chia sẻ: đặt `title`, `description`, ảnh **Open Graph** (1200×630) cho từng thiệp để link hiện đẹp khi gửi qua Zalo/Facebook.
- Không để lộ thông tin cá nhân thật (số tài khoản, số điện thoại) trong dữ liệu demo.

## Kiểm tra trước khi coi là xong

- Đã chụp screenshot 375px và 1440px, so với design gốc và sửa các chỗ lệch.
- Không có thanh cuộn ngang ở mọi khổ từ 360px trở lên.
- Mọi section đều có animation khi scroll và tắt đúng khi bật `prefers-reduced-motion`.
- Dấu tiếng Việt hiển thị đúng ở mọi font.
- `npm run build` và `npm run lint` chạy không lỗi.
- Lighthouse mobile: Performance và Accessibility từ 90 trở lên.
