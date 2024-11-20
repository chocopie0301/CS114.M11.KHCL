# 
_Mình có thêm chút "gia vị" về giao diện bằng html/css_
Để tránh conflict (xung đột) khi cài đặt thư viện, cần sử dụng python python ver 3.9

1. Cài đặt môi trường ảo để chạy dự án, cài đặt các thư viện cần thiết trong môi trường

pip install pipenv

cd path/to/your/project

pipenv install django
pipenv install torch torchvision pillow opencv-python
pipenv install yolov5

Kích hoạt môi trường ảo:

pipenv shell

2. Runserver
python manage.py migrate
python manage.py runserver


