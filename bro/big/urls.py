from django.urls import path
from . import views
urlpatterns=[
    path('',views.new,name='new'),
    path('ok',views.asd,name='dsa'),
    path("lm",views.wtd,name="lm"),
    path("mm", views.register_request, name="mm"),
    path("yo", views.login_request, name='yo'),
    path("logout",views.logout_request,name='logout'),
]