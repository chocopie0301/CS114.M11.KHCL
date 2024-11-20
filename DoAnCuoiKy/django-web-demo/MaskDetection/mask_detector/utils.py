# mask_detector/utils.py

import torch
from pathlib import Path

def detect_mask(image_path):
    # Đường dẫn tới mô hình YOLOv5 đã huấn luyện (best.pt)
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

    # Chạy mô hình nhận diện trên ảnh
    results = model(image_path)

    # Lưu ảnh kết quả vào thư mục runs/detect*
    save_dir = Path('runs/detect')  # Thư mục mặc định nơi YOLOv5 lưu ảnh nhận diện
    results.save(save_dir=str(save_dir))  # Lưu ảnh vào thư mục chạy YOLOv5

    # Lấy tất cả các thư mục detect (detect, detect2, detect3, v.v.)
    detect_folders = [f for f in Path('runs').iterdir() if f.is_dir() and f.name.startswith('detect')]
    
    if not detect_folders:
        return None, "No detect folder found."

    # Lấy thư mục 'detect' mới nhất
    latest_detect_folder = max(detect_folders, key=lambda f: f.stat().st_ctime)
    # print('last_detect_folder:', latest_detect_folder)

    # Lấy tên ảnh gốc từ image_path
    image_name = Path(image_path).name  # Lấy tên ảnh từ đường dẫn đầy đủ

    # Lấy đường dẫn tới ảnh kết quả trong thư mục detect mới nhất
    result_image_path = latest_detect_folder / image_name  # Dùng tên ảnh gốc để lấy ảnh kết quả

    # Kiểm tra xem ảnh có tồn tại trong thư mục detect không
    if not result_image_path.exists():
        return None, "Detected image not found in the folder."

    # Trả về đường dẫn của ảnh kết quả để hiển thị trên web
    return f'/runs/{latest_detect_folder.name}/{result_image_path.name}'
