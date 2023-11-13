from django.urls import path 
from . import views 


urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("task/<int:pk>/update", views.task_update, name="task-update"),
    path("task/<int:pk>/delete", views.task_delete, name="task-delete")
    
]
