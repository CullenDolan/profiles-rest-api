from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # list of http status codes
from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    """define application logic for url endpoint and django calls appropriate function"""
    serializer_class = serializers.HelloSerializer 

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

    def post(self, request):
        """Create hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
                )

        
    def put(self, request, pk=None):
        """Handle updating an object by replacing the entire thing"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial update of object by only replacing the specific field"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})