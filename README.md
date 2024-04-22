# neverWriteByHand v2.0

![效果展示]()

本项目在 [https://github.com/SAI-24-me/neverWriteByHand](https://github.com/SAI-24-me/neverWriteByHand) 基础上二次开发。

新增了以下功能：

1. 代码优化
2. 新增 `requirement.txt` 
3. 多字体生成

# 使用方法

1. 安装环境
```shell
pip install -r requirement.txt
```

2. 在 [方正字库官网](http://www.foundertype.com) 挑选汉字手写字体

3. 将下载的 ttf 字体文件存放至 `fonts` 目录

4. 将需要转手写的文字写进 `content.txt`

5. 执行程序：`python main.py`

6. 生成的图片将会存放在 `output` 目录中
