from django.urls import path
from .views import Home, About, Login, Feedback, Queue, Dashboard

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('login/', Login.as_view(), name='login'),
    path('queue/', Queue.as_view(), name='queue'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('', Home.as_view(), name='home'),
]
