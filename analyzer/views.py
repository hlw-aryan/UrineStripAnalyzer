from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile

from .image_processing import extract_colors

class AnalyzeImageView(APIView):
    def post(self, request):
        # Get the uploaded image data
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:

            # Process the image
            colors = extract_colors(image_file)

            # Return the colors as JSON response
            return Response(
                {
                    "success": "true",
                    "code": 200,
                    "result": {
                        'URO': colors[0],
                        'BIL': colors[1],
                        'KET': colors[2],
                        'BLD': colors[3],
                        'PRO': colors[4],
                        'NIT': colors[5],
                        'LEU': colors[6],
                        'GLU': colors[7],
                        'SG': colors[8],
                        'PH': colors[9]
                    }
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
