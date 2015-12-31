from django.conf.urls import url
from creative import views

app_name = 'creative'
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^admin$', views.admin_view, name="admin"),
    url(r'^add$', views.add, name="write"),
    url(r'^display/(\d+)/$', views.display, name="display"),
    url(r'^analyze$', views.analyze, name="think"),
    url(r'^list$', views.wish_list, name="wish"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^get-entry$',  views.get_entry, name="get_entry"),
    url(r'^comment$', views.add_comment, name="comment"),
]
