import os
import random
import time
from PIL import ImageFont, Image, ImageDraw
from flask import Flask, request, render_template, send_file

app = Flask(__name__, template_folder="static")

SIZE = 4  # 整齐度
FONT_PATH = r"fonts/"
SAVE_PATH = r"output/"


# 获取文字内容
def get_content(txt_path):
    with open(txt_path, "r", encoding="UTF-8") as f:
        content = f.read()
    return content


def generate_image(size, content, ttf_path, save_path):
    FONT = ImageFont.truetype(ttf_path, 25)  # 设置字体

    LENGSTR = len(content)
    FLAG = 0

    while FLAG < LENGSTR:
        img = Image.open("background.png")
        draw = ImageDraw.Draw(img)
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
        img_path = os.path.join(save_path, f"{int(time.time())}.png")
        img.save(img_path)
    return img_path


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        user_input = request.form["content"]
        img_path = generate_image(size=SIZE, content=user_input,
                                  ttf_path=os.path.join(FONT_PATH, "STLITI.TTF"),
                                  save_path=SAVE_PATH
                                  )
        return send_file(img_path, mimetype="image/png")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
