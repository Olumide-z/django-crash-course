from django.urls import path
from . import views

# the path hello leads to hello world view
urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('', views.hello_python, name='hello_python'),
    path('html', views.hello_html_view, name='hello_html'),
    path('hello_query', views.hello_query, name='hello_query'),
    path('special', views.special_view, name='special_view'),
    path('postendpoint', views.post_example, name='post_example'),
    path('submitexample', views.submit_example, name='submit_example'),
    path('submit', views.submit_django_form, name='submit_django_form'),
    path('helloname/<str:name>', views.hello_name_html_view, name='hello_name_html'),
    path('template', views.template_view, name='template_view'),
    path('todos', views.todos_view, name='todos_view'),
    path('person_details/<int:person_id>',
         views.person_details, name='person_details'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('toggle_todo_done/<int:todo_id>',
         views.toggle_todo_done, name='toggle_todo_done')
]
