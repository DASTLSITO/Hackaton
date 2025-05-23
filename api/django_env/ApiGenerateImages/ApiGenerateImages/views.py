from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
import csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
from .Ploteo import generarImg
from .puntoSeleccionado import obtenerMapaPuntosEspecificos
from django.http import JsonResponse
import base64
from datetime import date
import keras 
#from keras.models import load_model


class apiGenerateView(APIView):
    def get(self, request, *args, **kwargs):
        # Abre la imagen en modo binario ('rb')

        buffer = generarImg()  # Buffer ya contiene PNG con RGBA
        return HttpResponse(buffer.getvalue(), content_type='image/png')
    

class apiSpecificPoint(APIView):
    def get(self, request):
        lat = request.GET.get('lat', 0)  
        lon = request.GET.get('lon', 0)  

        image_buffer, datos = obtenerMapaPuntosEspecificos(lat, lon)
        
        # Convertir imagen a base64 para incluirla en JSON
        image_base64 = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
        
        # Crear respuesta JSON con imagen y datos
        response_data = {
            "image": image_base64,
            "datos": datos
        }
        
        return JsonResponse(response_data)



# class apiProbabilidadDeEncontrarSardina(APIView):
#     def get(self, request):
#         lat = request.GET.get('lat', 0)  
#         lon = request.GET.get('lon', 0)  
#         fecha = request.GET.get('fecha', date.today())

#         datos_de_entrada = [[lat, lon,  fecha]]

#         modelo = load_model('/home/dastl/Documents/HACKATON/api/django_env/ApiGenerateImages/ApiGenerateImages/model.weights.h5')
#         predicciones = modelo.predict(datos_de_entrada)

#         return predicciones

#         # image_buffer, datos = obtenerMapaPuntosEspecificos(lat, lon)
        
#         # # Convertir imagen a base64 para incluirla en JSON
#         # image_base64 = base64.b64encode(image_buffer.getvalue()).decode('utf-8')
        
#         # # Crear respuesta JSON con imagen y datos
#         # response_data = {
#         #     "image": image_base64,
#         #     "datos": datos
#         # }
        
#         # return JsonResponse(response_data)
        

