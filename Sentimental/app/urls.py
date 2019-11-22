from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^submit/',views.index1,name='submit'),
    url(r'^home/',views.index2,name='home'),
    url(r'^home1/',views.index,name='home1'),
    url(r'^submit1/',views.index4,name='submit1'),
    url(r'^submit2/',views.index5,name='submit2'),
    url(r'^submit3/',views.index6,name='submit3'),
    url(r'^submit4/',views.index7,name='submit4'),
    url(r'^submit5/',views.index8,name='submit5'),
    url(r'^submit6/',views.index9,name='submit6'),
    url(r'^submit7/',views.index10,name='submit7'),
    url(r'^submit8/',views.index11,name='submit8')




]