from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()), # register an APIView
    path('login/', views.UserLoginApiView.as_view()), # register the login view
    path('', include(router.urls)) # register the ViewSet
]
