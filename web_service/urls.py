from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.finish_order, name='finish_order'),
]