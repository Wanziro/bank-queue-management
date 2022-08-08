from audioop import add
from django.urls import path
from .views import Home, About, Login, Feedback, Queue, AddClientToTheQueue, GetClientsOnTheQueue, UpdateClient, GetChartData

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('feedback/', Feedback.as_view(), name='feedback'),
    path('login/', Login.as_view(), name='login'),
    path('queue/', Queue.as_view(), name='queue'),
    path('api/addclient/', AddClientToTheQueue.as_view(), name='api_add_client'),
    path('api/removeclient/', UpdateClient.as_view(), name='api_remove_client'),
    path('api/getclients/', GetClientsOnTheQueue.as_view(), name='api_get_clients'),
    path('api/chart/', GetChartData.as_view(), name='api_get_chart_data'),
    path('', Home.as_view(), name='home'),
]
