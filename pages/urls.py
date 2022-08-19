from django.urls import path
from .views import home, GetAllBranches, About, login_request, logout_request, register, feedback, Queue, AddClientToTheQueue, GetClientsOnTheQueue, UpdateClient, GetChartData

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('feedback/', feedback, name='feedback'),
    path('register/', register, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('queue/', Queue.as_view(), name='queue'),
    path('api/addclient/', AddClientToTheQueue.as_view(), name='api_add_client'),
    path('api/removeclient/', UpdateClient.as_view(), name='api_remove_client'),
    path('api/getclients/', GetClientsOnTheQueue.as_view(), name='api_get_clients'),
    path('api/branches/', GetAllBranches.as_view(), name='api_all_branches'),
    path('api/chart/', GetChartData.as_view(), name='api_get_chart_data'),
    path('', home, name='home'),
]
