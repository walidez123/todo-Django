from django.urls import path
from . import views
urlpatterns = [
    path('',views.index , name='main'),
    path('update/<task_id>',views.update,name='update-task'),
    path('delete/<task_id>',views.delete,name='delete-task'),
    path('finish/<task_id>',views.finish,name='finish-task'),
]
