from team import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout')

]