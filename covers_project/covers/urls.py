from django.urls import path
from covers import views 


urlpatterns = [
	path('', views.home, name='covers-home'),
	path('about/', views.about, name="covers-about")
]