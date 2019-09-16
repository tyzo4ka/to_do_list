from django.contrib import admin
from django.urls import path
from webapp.views import index_view, task_create_view, task_view,task_update_view, task_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view, name="index"),
    path("article/<int:pk>/", task_view, name="task_view"),
    path('task/add/', task_create_view, name='task_add'),
    path("task/<int:pk>/edit", task_update_view, name='task_update'),
    path("task/<int:pk>/delete", task_delete_view, name="task_delete")
]
