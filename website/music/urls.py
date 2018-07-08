from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^albums/$', views.AblumListView.as_view()),
url(r'^albums/create11/$',  views.UsersCreate.as_view()),

url(r'^albums/(?P<title>[\w-]+)/$',views.AblumdetailView.as_view(),name="detail"),
url(r'^albums/(?P<title>[\w-]+)/edit/$',views.AblumUpdateView.as_view()),
url(r'^albums/(?P<title>[\w-]+)/delete/$',views.AblumDeleteView.as_view()),
url(r'^register/$',views.UsersCreate.as_view()) # creates users


]
