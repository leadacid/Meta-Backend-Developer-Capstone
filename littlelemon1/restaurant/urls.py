#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('index', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view(), name= 'menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('create-booking/', views.CreateBookingView.as_view(), name='create-booking'),
    path('create-booking/<int:pk>', views.SingleBookingView.as_view()),
]

