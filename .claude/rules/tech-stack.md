# Công nghệ và cấu trúc thư mục

Mặc định cho bản Next.js, đổi được nếu chủ dự án yêu cầu. Bản `index.html` hiện tại là HTML/CSS/JS thuần (xem `project-overview.md`).

## Công nghệ

- **Next.js (App Router) + TypeScript**, xuất tĩnh (`output: 'export'`) để host trên Vercel/Netlify.
- **Tailwind CSS** cho style; màu và font khai báo thành token trong `tailwind.config` / CSS variables, không viết mã màu rời rạc trong component.
- **Framer Motion** cho hiệu ứng; `next/font` cho Google Fonts; `next/image` cho ảnh.
- Không thêm thư viện UI nặng (MUI, Ant…). Lịch, đồng hồ đếm ngược, form tự viết.

## Lệnh thường dùng

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

## Nội dung tách khỏi giao diện

Tên cô dâu chú rể, ngày giờ, địa điểm, ảnh, lịch trình, tài khoản mừng cưới… nằm trong file `data/`, có kiểu TypeScript (`InvitationData`). Component chỉ đọc dữ liệu, không hard-code tên hay ngày. Như vậy thêm mẫu mới chỉ cần thêm file data + theme.
