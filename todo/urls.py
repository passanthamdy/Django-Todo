from unicodedata import name
from django.urls import path 
from . import views

app_name='todo'

urlpatterns=[
    path('',views.index ,name= 'list'),
    path('details/<int:id>',views.todo_details ,name= 'details'),
    path('done/<int:id>', views.todo_done, name='done'),
    path('update/<int:id>',views.update_todo, name='update'), 
    path('delete/<int:id>', views.delete_task, name='delete'),
    path('finished', views.finished_tasks, name='finished'),
    path('unfinished', views.unfinished_tasks, name='unfinished'),
    # path('home/json',todo_json_home ,name= 'home-json'),
    # path('home/<str:todo_name>', todo_home, name='home')

]