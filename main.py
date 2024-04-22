import os
import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import time


# 获取文字内容
def get_content(txt_path):
    with open(txt_path, 'r', encoding='UTF-8') as f:
        content = f.read()
    f.close()
    return content


def main(content, ttf_path, save_path, size):
    font = ImageFont.truetype(ttf_path, 25)  # 设置字体

    lenstr = len(content)
    flag = 0

    while flag < lenstr:
        img = Image.open('background.png')
        draw = ImageDraw.Draw(img)
        for i in range(28):
            for j in range(38):
                if flag >= lenstr:
                    break
                if content[flag] == '\n':
                    flag += 1
                    break
                draw.text((70 + random.random() * size / 2 + 25 * j, 83 + random.random() * size + i * 48),
                          content[flag], (0, 0, 0),
                          font=font)
                flag += 1
            if flag >= lenstr:
                break
        img.save(save_path + str(int(time.time())) + ".png")
    print("success!")


if __name__ == "__main__":
    size = 4  # 整齐度
    ttf_path = ".\\fonts\\"
    save_path = ".\\output\\"
    content = get_content(txt_path='content.txt')

    for font in os.listdir(ttf_path):
        if font.endswith(".TTF") or font.endswith(".ttf"):
            main(content=content, ttf_path=f"{ttf_path}{font}", save_path=save_path, size=4)
