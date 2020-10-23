from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from points import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    url(r'^login/$', views.login_app, name = 'login'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^profile/preview/$', views.preview_html, name = 'preview_html'),
    url(r'^logout/$', views.logout_app, name = 'logout_app'),
    url(r'^profile/points_history/$', views.history, name = 'history'),
    url(r'^profile/points_table/$', views.table, name = 'table'),
    url(r'^profile/rewards/$', views.rewards, name = 'rewards'),
    url(r'^profile/requests/$', views.requests, name = 'requests'),
    path('profile/requests/<int:req_id>', views.req_detail, name='req_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
