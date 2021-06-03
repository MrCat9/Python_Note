# -*- coding: utf-8 -*-
# 图片转pdf
# 将图片放在 img_dir 目录下，将输出名为 pdf_name 的 pdf 文件


from PIL import Image
import os


def gen_pdf(img_dir, pdf_name):
    allow_file_format_list = ['.jpg', '.jpeg']

    file_list = os.listdir(img_dir)
    for f in file_list:
        tmp_index = f.rfind('.')
        file_format = f[tmp_index:]
        file_format = file_format.lower()
        # file_name = f[:tmp_index]

        if file_format in allow_file_format_list:
            continue
        elif file_format == 'png':  # png转jpg
            file_path = os.path.join(img_dir, f)
            file_name = f[:tmp_index]

            img = Image.open(file_path)
            r, g, b, a = img.split()
            img = Image.merge('RGB', (r, g, b))
            to_save_path = os.path.join(img_dir, file_name + '.jpg')
            print('保存', to_save_path)
            img.save(to_save_path)
            print('删除', file_path)
            os.remove(file_path)
        else:  # 删除未知格式文件
            file_path = os.path.join(img_dir, f)
            print('删除', file_path)
            os.remove(file_path)

    file_list = os.listdir(img_dir)
    im1 = Image.open(os.path.join(img_dir, file_list.pop(0)))
    im_list = []
    for i in file_list:
        img = Image.open(os.path.join(img_dir, i))
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            img = Image.merge('RGB', (r, g, b))
            img = img.convert('RGB')
        im_list.append(img)

    im1.save(pdf_name, 'PDF', resolution=100.0, save_all=True, append_images=im_list)
    print('输出文件名称：', pdf_name)


if __name__ == '__main__':
    test_input_img_dir = 'image'
    test_output_pdf_name = 'test_output_pdf_name.pdf'
    if not test_output_pdf_name.endswith('.pdf'):
        test_output_pdf_name = test_output_pdf_name + '.pdf'
    gen_pdf(img_dir=test_input_img_dir, pdf_name=test_output_pdf_name)
