# 通过添加STATICFILES_DIRS

# 在 django_test\django_test\settings.py 下配置jpg文件存放的文件夹
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),  # 静态文件路径
    'C:/Users/admin/Desktop/jpg_data',  # dicom文件存放的文件夹
)

# 在 django_test\templates\show_jpg.html 下用 /static/ 可以访问到
        "/static/jpg (1).jpg",
        "/static/jpg (2).jpg",
        "/static/jpg (3).jpg",
