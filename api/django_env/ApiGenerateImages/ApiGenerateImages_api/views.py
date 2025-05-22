from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import TodoSerializer
import os

class apiGenerateView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        # Abre la imagen en modo binario ('rb')
            img_path = './imgprueba.jpg'  # Cambia esto por la ruta de tu imagen
            if not os.path.exists(img_path):
                return Response(
                    {"error": "Imagen no encontrada"},
                    status=status.HTTP_404_NOT_FOUND
                )
        
            with open(img_path, 'rb') as img:
                response = Response(img.read(), content_type='image/jpeg')
                # Opcional: Agregar cabeceras para descarga
                # response['Content-Disposition'] = 'attachment; filename="imagen.jpg"'
                return response