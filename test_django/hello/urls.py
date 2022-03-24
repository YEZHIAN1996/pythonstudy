from django.urls import path
from hello.views import is_odd
urlpatterns = [
    path('<int:num>/', is_odd, name='is_odd')
]