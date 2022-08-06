from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    # path('<int:id>', views.singleBlog),
    # path('create', views.create, name="create"),
]
