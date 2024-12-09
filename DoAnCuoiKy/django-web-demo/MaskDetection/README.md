# MASK Detection Testing

**Phần demo này mình xây dựng một app chạy local với django, để hiển thị chức năng `choose`, `upload` image và `show` image_detected. _Mình có thêm chút "gia vị" về giao diện bằng html/css_ nên đây là một trang cơ bản về chức năng và cả giao diện.**



![](https://github.com/chocopie0301/CS114.M11.KHCL/blob/main/DoAnCuoiKy/django-web-demo/MaskDetection/image/demo/MaskDetection.gif)

## 1 Đầu tiên, sau khi git clone repo này về máy, thì bạn cần phải chuyển hướng đến đúng thư mục MaskDetection.
## 2 Sau đó cài đặt các thư viện hỗ trợ cần thiết. 
- Chú ý: Để tránh conflict (xung đột) khi cài đặt thư viện, cần sử dụng python ver 3.9.

### (SbS) Cài đặt môi trường ảo để chạy dự án, cài đặt các thư viện cần thiết trong môi trường

`pip install pipenv`

`cd path/to/your/project`

`pipenv install django`

`pipenv install torch torchvision pillow opencv-python`

`pipenv install yolov5`

## 3 Kích hoạt môi trường ảo và runserver
### 3.1 Kích hoạt môi trường ảo

pipenv shell

### 3.2 Runserver
`python manage.py migrate`

`python manage.py runserver`

Cuối cùng, truy cập và trải nghiệm: `http://127.0.0.1:8000/`

### Chi tiết đồ án trong ![Mask Detection](https://github.com/chocopie0301/CS114.M11.KHCL/edit/main/DoAnCuoiKy)



