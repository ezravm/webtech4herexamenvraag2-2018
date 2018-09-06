from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'filldb',views.set_data, name='set_data'),
        url(r'get_movies',views.get_movies, name='get_movies'),
        url(r'search_movie', views.search_movie, name='search_movie'),
]
