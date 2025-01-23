import os
from PIL import Image

# 遍历当前文件夹
for filename in os.listdir('.'):
    # 检查文件是否为webp格式
    if filename.lower().endswith('.webp'):
        try:
            # 打开webp图片
            with Image.open(filename) as img:
                # 构建转换后的png文件名
                new_filename = os.path.splitext(filename)[0] + '.png'
                # 保存为png格式
                img.save(new_filename, 'PNG')
                print(f'{filename} 已转换为 {new_filename}')
        except Exception as e:
            print(f'转换 {filename} 时出错: {e}')