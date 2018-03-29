from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.place_list, name='place_list'), #list of places
	url(r'^visited$', views.places_visited, name='places_visited'), #places that have been visited
	url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
]