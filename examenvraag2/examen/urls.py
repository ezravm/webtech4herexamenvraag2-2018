from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'filldb',views.set_data, name='set_data'),
]
