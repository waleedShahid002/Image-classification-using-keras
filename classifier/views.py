from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings


import numpy as np
from keras.models import load_model
from keras.utils import img_to_array
import os
from PIL import Image

# Load your Keras model

model_path = os.path.join(os.path.dirname(__file__), 'model.h5')

model = load_model(model_path)


IMAGE_SIZE = (180, 180)

# @csrf_exempt

@csrf_exempt

def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if not image_file:
            return render(request, 'index.html', {'error': 'No image provided'})
        
        file_name = default_storage.save(f"uploads/{image_file.name}", image_file)
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)


        try:
            image = Image.open(file_path)
            
            img = image.resize(IMAGE_SIZE)
            img_array = img_to_array(img)  # Normalize pixel values
            img_array = np.expand_dims(img_array, axis=0)
            


            predictions = model.predict(img_array)
            score = float(predictions[0][0])

        

            

         


            if score >= 0.5:
                result = {
                    'label': 'Dog',
                    'confidence': f"{10 * score :.2f}%"


                }
            
            else:
                result = {
                    'label': 'Cat',
                    'confidence': f"{10 * (1 - score):.2f}%"

                }

            return render(request, 'index.html',{
                'result': result,
                # 'image_url': file_name
                'image_url': f"{settings.MEDIA_URL}{file_name}"
            })
        except Exception as e:
            return render(request, 'index.html', {'error': f"An error occured: {str(e)}"})
    
    return render(request, 'index.html')







