from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""
    """define application logic for url endpoint and django calls appropriate function"""
    
    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        """request passed in by django rest framework"""
        an_apiview = [
            'Use HTTP methods as a function (get, post, put, patch, delete',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})