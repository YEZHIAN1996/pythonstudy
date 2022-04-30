from django.urls import path
from hello.views import is_odd, http_req
urlpatterns = [
    path('<int:num>/', is_odd, name='is_odd'),
    path('http/req/', http_req, name='http_req')
]

