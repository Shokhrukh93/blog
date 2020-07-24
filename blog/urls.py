from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.IndexView.as_view(), name='post_list'),
    path('<int:pk>', views.DetailView.as_view(), name='post_detail'),
]
