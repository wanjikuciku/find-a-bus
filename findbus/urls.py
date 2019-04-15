from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    url(r'^$',views.index, name='index'),
    url(r'^search/$', views.search_category,name ='search_category'),
    url(r"^accounts/profile/$", views.my_profile, name = "my_profile"),
    url(r"^message/$", views.message, name = "message")

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
