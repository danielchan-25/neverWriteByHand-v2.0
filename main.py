import random
import base64
import io
from PIL import ImageFont, Image, ImageDraw
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="static")

size = 4  # 整齐度
font_path = r"fonts/STLITI.TTF"     # 字体文件
background_path = r"static/background.png"  # 背景图片


def generate_image(size, content, ttf_path):
    FONT = ImageFont.truetype(ttf_path, 25)  # 设置字体

    LENGSTR = len(content)
    FLAG = 0

    img = Image.open(background_path)  # 背景图片
    draw = ImageDraw.Draw(img)

    while FLAG < LENGSTR:
        for i in range(28):
            for j in range(38):
                if FLAG >= LENGSTR:
                    break
                if content[FLAG] == "\n":
                    FLAG += 1
                    break
                draw.text((70 + random.random() * size / 2 + 25 * j, 83 + random.random() * size + i * 48),
                          content[FLAG], (0, 0, 0),
                          font=FONT)
                FLAG += 1
            if FLAG >= LENGSTR:
                break

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    img_base64 = base64.b64encode(img_byte_arr.getvalue())
    return img_base64


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        user_input = request.form["content"]
        img_base64 = generate_image(size=size, content=user_input, ttf_path=font_path)
        return f"<img src='data:image/png;base64,{img_base64.decode('utf-8')}'/>"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
