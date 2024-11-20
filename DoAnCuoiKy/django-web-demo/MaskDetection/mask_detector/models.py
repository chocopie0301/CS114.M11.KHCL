# mask_detector/models.py

from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Lưu ảnh đã upload
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Thời gian upload

    def __str__(self):
        return f"Image uploaded on {self.uploaded_at}"

class DetectionResult(models.Model):
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)  # Liên kết với ảnh đã upload
    output_image = models.ImageField(upload_to='outputs/')  # Lưu ảnh kết quả nhận diện
    detection_details = models.TextField()  # Lưu thông tin về bounding box hoặc kết quả nhận diện

    def __str__(self):
        return f"Detection result for {self.uploaded_image.image.name}"
