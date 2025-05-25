
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('<int:todo_id>/', todo_vew),
    path('<int:todo_id>/delete', todo_delet_view),
]
