from django.conf.urls import url
from weather_control_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.SignUpFormView.as_view(), name='signup'),
    url(r'^home/', views.home, name='home'),
    url(r'^login/', views.login_or_logout, name='login'),
    url(r'^logout/', views.LogoutFormView.as_view(), name='logout'),

]