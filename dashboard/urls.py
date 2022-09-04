from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('branches', views.branches, name="branches"),
    path('feedbacks', views.feedbacks, name="feedbacks"),
    path('branches/rm/<int:id>', views.deleteBranch),
    path('branches/edit/<int:id>', views.editBranch),
    path('feedbacks/rm/<int:id>', views.deleteFeedBack),
    path('printer', views.printer, name="printer"),
    path('api/queue/', views.queue),
]
