#define URL route for index() view
# from . import views
from django.urls import path
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    # path('', views.index, name='index')
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]
