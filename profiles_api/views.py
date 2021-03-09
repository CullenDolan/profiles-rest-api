from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # list of http status codes
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer 

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial+update",
            "Automatically maps to URLS using Routers",
            "Provides more functionality with less code",
        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
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
            
    def retrieve(self, request, pk=None):
        """Handle getting an object by ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """handle updating object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """handle parital updating object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """handle removing object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creatig and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() #django already knows all the http requests
    authentication_classes = (TokenAuthentication,) # comma creates this as a tuple
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handles creating reading and updating items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)