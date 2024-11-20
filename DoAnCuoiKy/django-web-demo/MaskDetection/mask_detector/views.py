# mask_detector/views.py

from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import detect_mask

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):  # Check if there's an uploaded image
        # Get the uploaded image file
        image = request.FILES['image']
        
        # Save the uploaded image to the 'media/uploads/' folder for further processing
        image_path = f'media/uploads/{image.name}'
        with open(image_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # Call the mask detection function
        result_image_path = detect_mask(image_path)

        if result_image_path:  # If a result image is found
            return render(request, 'detection/result.html', {
                'original_image_path': f'/media/uploads/{image.name}',  # Path to the original image
                'result_image_path': result_image_path,  # Path to the detected image
            })
        else:  # If no result image is found
            return render(request, 'detection/error.html', {
                'error_message': "No image found in detect folder.",  # Error message
            })
    return render(request, 'detection/upload.html')  # Render the upload page for GET request
