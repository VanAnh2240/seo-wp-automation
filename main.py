import json
import google.generativeai as genai
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request, jsonify, render_template
from config import WORDPRESS_URL, WORDPRESS_USERNAME, WORDPRESS_APP_PASSWORD

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('models/gemini-2.0-flash')


def generate_seo_content(keywords):
    prompt = f"""
    Viết một bài viết chi tiết cho WordPress với ít nhất 2500 từ, 
    chứa thông tin hữu ích được tối ưu cho SEO, SEO ngữ nghĩa, EEAT và Rank Math SEO. 
    Bao gồm các trích dẫn từ nguồn uy tín ở cuối bài viết. 
    Chèn 1-2 liên kết nội bộ một cách tự nhiên bài viết đến trang web của tôi: https://dinhhuongtuonglai.id.vn. ở đầu và cuối bài viết
    Tập trung các từ khóa sau: {', '.join(keywords)}. 
    Vui lòng kết hợp tất cả các từ khóa trên một cách tự nhiên trong bài viết.
    Bài viết có đủ thẻ <meta charset> <meta description>,... để tối ưu SEO

    QUAN TRỌNG: Định dạng bài viết bằng các thẻ HTML chuẩn như sau:
    - Dùng thẻ <h1> cho tiêu đề chính của bài viết,
    - Dùng thẻ <h2> cho tiêu đề các phần chính,
    - Dùng thẻ <h3> cho tiêu đề các phần phụ nếu cần,
    - Dùng thẻ <p> cho đoạn văn,
    - Dùng thẻ <a href="URL">văn bản liên kết</a> cho các liên kết.

    Trả về toàn bộ nội dung bài viết dưới dạng HTML, có thể dán trực tiếp vào trình soạn thảo WordPress.
    Vui lòng không dùng cú pháp markdown, chỉ dùng thẻ HTML thuần túy.
    """
    try:
        response = model.generate_content(prompt)
        raw_content = response.text.strip()

        import re
        # Tách title từ <h1>
        match = re.search(r"<h1>(.*?)</h1>", raw_content, re.IGNORECASE | re.DOTALL)
        title = match.group(1).strip() if match else f"Bài viết về: {', '.join(keywords)}"

        # Xóa <h1> khỏi bài viết
        cleaned_content = re.sub(r"<h1>.*?</h1>", "", raw_content, flags=re.IGNORECASE | re.DOTALL)

        # Bắt đầu từ <!DOCTYPE html>
        start_index = cleaned_content.find("<!DOCTYPE html>")
        content = cleaned_content[start_index:] if start_index != -1 else cleaned_content

        return title, content

    except Exception as e:
        return None, f"Error: {e}"


def post_to_wordpress(title, content):
    data = {
        'title': title,
        'content': content,
        'status': 'draft'
    }
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.post(
            WORDPRESS_URL,
            headers=headers,
            auth=HTTPBasicAuth(WORDPRESS_USERNAME, WORDPRESS_APP_PASSWORD),
            json=data,
            timeout=10
        )
        if response.status_code == 201:
            link = response.json().get("link")
            return True, link
        else:
            return False, response.text
    except Exception as e:
        return False, str(e)


@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.get_json()
    keywords = data.get('keywords', [])
    if not keywords or not isinstance(keywords, list):
        return jsonify({'success': False, 'error': 'Keywords phải là danh sách và không được để trống'}), 400

    title, content = generate_seo_content(keywords)
    if title is None:
        return jsonify({'success': False, 'error': content}), 500

    with open("output_article.txt", "w", encoding="utf-8") as f_out:
        f_out.write(f"Title: {title}\n\n")
        f_out.write(content)

    success, resp = post_to_wordpress(title, content)
    if success:
        return jsonify({'success': True, 'title': title, 'link': resp})
    else:
        return jsonify({'success': False, 'error': resp}), 500


if __name__ == "__main__":
    app.run(debug=True)
