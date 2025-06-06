# seo-wp-automation
==================================================
 TOOL TẠO BÀI VIẾT SEO TỰ ĐỘNG VÀ ĐĂNG LÊN WORDPRESS
==================================================

📌 MÔ TẢ DỰ ÁN
--------------------------------------------------
Ứng dụng web đơn giản giúp tạo bài viết chuẩn SEO tự động dựa trên danh sách từ khóa người dùng nhập vào.
Nội dung được tạo thông qua Google Generative AI và đăng lên website WordPress dưới dạng bản nháp để chờ duyệt.

--------------------------------------------------
🛠️ CÔNG NGHỆ SỬ DỤNG
--------------------------------------------------
- Python 3.x
- Flask (Web Server)
- Google Generative AI API
- WordPress REST API
- HTML + CSS (Frontend đơn giản)

--------------------------------------------------
📁 CÀI ĐẶT & KHỞI CHẠY
--------------------------------------------------

1. Tạo và kích hoạt môi trường ảo:

   # Trên Windows:
   python -m venv .venv
   .venv\Scripts\activate

   # Trên macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate

2. Cài đặt thư viện phụ thuộc:

   pip install -r requirements.txt

3. Tạo file `config.py` và thêm thông tin sau:

   WORDPRESS_URL = "https://your-wordpress-site.com"
   WORDPRESS_USERNAME = "tên người dùng WordPress"
   WORDPRESS_APP_PASSWORD = "mật khẩu ứng dụng WordPress"

4. Chạy ứng dụng:

   python main.py

5. Truy cập trình duyệt:

   http://127.0.0.1:5000

--------------------------------------------------
📝 HƯỚNG DẪN SỬ DỤNG
--------------------------------------------------
1. Nhập danh sách từ khóa (mỗi dòng một từ).
2. Nhấn nút "Tạo bài viết".
3. Ứng dụng sẽ:
   - Gửi từ khóa tới Google Generative AI để tạo bài viết.
   - Tự động đăng bài viết lên WordPress ở dạng bản nháp.
   - Hiển thị tiêu đề và đường dẫn bài viết trên màn hình.

--------------------------------------------------
📌 LƯU Ý QUAN TRỌNG
--------------------------------------------------
- Cần tạo **App Password** trong WordPress để có thể sử dụng REST API.
- Đảm bảo API key của Google Generative AI còn hiệu lực.
- Bài viết được tạo ra là bản nháp và cần được duyệt thủ công trước khi xuất bản.

--------------------------------------------------
📧 LIÊN HỆ HỖ TRỢ
--------------------------------------------------
- Email: 22520040@gm.uit.edu.vn
- Github: https://github.com/VanAnh2240
--------------------------------------------------
© BẢN QUYỀN
--------------------------------------------------
Copyright © 2025 Đinh Vân Anh

Toàn bộ mã nguồn và tài liệu thuộc quyền sở hữu của tác giả.
Không được sao chép, chỉnh sửa, phân phối hoặc sử dụng lại dưới bất kỳ hình thức nào nếu không có sự cho phép bằng văn bản.
