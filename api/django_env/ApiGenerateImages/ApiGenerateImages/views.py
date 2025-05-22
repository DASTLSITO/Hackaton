from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import os

class apiGenerateView(APIView):
    # add permission to check if user is authenticated
    
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        # Abre la imagen en modo binario ('rb')
            image = Image.open("/home/dastl/Documents/HACKATON/api/django_env/ApiGenerateImages/ApiGenerateImages_api/imgprueba.jpg")  # Cambia esto por la ruta de tu imagen
            # Create a BytesIO object to hold the image data
            buffer = BytesIO()

            # Save the image to the buffer in a specific format (e.g., JPEG, PNG)
            image.save(buffer, format='JPEG')

            # Get the image data from the buffer
            image_data = buffer.getvalue()

            # Create an HttpResponse object with the image data and Content-Type
            return HttpResponse(image_data, content_type='image/jpeg')
