from django.conf.urls import url
from creative.views import home, add, display, analyze, wish_list, login, admin_view, logout

app_name = 'creative'
urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^admin$', admin_view, name="admin"),
    url(r'^add$', add, name="write"),
    url(r'^display/(\d+)/$', display, name="display"),
    url(r'^analyze$', analyze, name="think"),
    url(r'^list$', wish_list, name="wish"),
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
]
