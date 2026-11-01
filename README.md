# Diêm La Điện

Địa ngục điện online 2.5D cho TikTok LIVE, fork từ Chánh Điện Online của Kent Juno (MIT).
Người xem bình luận là bước vào điện, ngồi ghế xét xử, sám hối. Ai tặng quà sẽ được xướng tên xét nghiệp bằng giọng đọc tiếng Việt.

## Khác gì bản gốc
- Chủ đề: Diêm La Điện thay cho chánh điện. Diêm Vương ở giữa, hai Phán Quan hai bên.
- Lời tụng đổi thành lời sám hối và phán xét, không còn kinh Phật.
- Từ đổi skin đổi thành: diêm, phán, mạnh, tiểu quỷ, quỷ sai, nữ quỷ, nam quỷ.
- Quà đổi thành: Huyết Hoa, Đèn Địa Ngục, Trống Địa Ngục.
- Bảng Công Đức đổi thành Sổ Nghiệp.
- Asset vẽ lại bằng PIL trong `tools/generate-assets.py`, không dùng ảnh chánh điện gốc. Nhạc thiền gốc đã gỡ, bản này chưa có nhạc nền riêng — thay file trong `assets/music/` hoặc tắt nhạc ở bảng điều khiển.
- Cơ chế giữ nguyên bản gốc: tối đa 100 chỗ, chỗ tự mở rộng 24 → 36 → 64 → 100, server chỉ nghe 127.0.0.1, WebSocket chỉ nhận Origin localhost, file tĩnh có danh sách trắng, không dùng tài khoản TikTok.

## Chạy bộ LIVE
Cần Node.js 20 trở lên.

```bash
cd live
npm install
npm start
```

1. Mở `http://localhost:3000/live/control.html`.
2. Bấm **Mở màn hình overlay 9:16**, rồi bấm **Bật âm thanh** một lần trong cửa sổ đó.
3. OBS: Browser source trỏ tới `http://localhost:3000/live/overlay.html`, 1080×1920. TikTok LIVE Studio: Window capture cửa sổ overlay.
4. Bật LIVE trên TikTok, nhập `@username` vào bảng điều khiển, bấm **Kết nối**.

Chưa live vẫn thử được: **Thử tương tác**, **Đổ người mẫu 15/36/64/100** hoặc **Bot mô phỏng**.

## Giấy phép
Code gốc MIT của Kent Juno, xem `LICENSE`. Phần đổi mới cho Diêm La Điện cũng theo MIT. Asset vẽ lại bằng PIL là placeholder, thay bằng art hoàn chỉnh trước khi dùng công khai. `tiktok-live-connector` là thư viện cộng đồng, không phải API chính thức của TikTok.
