"""refugiomascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from apps.adopcion.views import index

from django.views.generic import TemplateView

urlpatterns = [
    # Urls Vue.js
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path(r'nosotros/', TemplateView.as_view(template_name='index.html')),
    path(r'dashboard/', TemplateView.as_view(template_name='index.html')),
    re_path(r'dashboard/presolicitud=(?P<pk>\d+)', TemplateView.as_view(template_name='index.html')),
    path(r'login/', TemplateView.as_view(template_name='index.html')),
    path(r'prueba/', TemplateView.as_view(template_name='index.html')),
    path(r'mascotas/', TemplateView.as_view(template_name='index.html')),
    path(r'mascotas/solicitud', TemplateView.as_view(template_name='index.html')),
    path(r'mascotas/solicitud=(?P<pk>\d+)', TemplateView.as_view(template_name='index.html')),
    path(r'noticia/', TemplateView.as_view(template_name='index.html')),
    path(r'noticias-comunidad/', TemplateView.as_view(template_name='index.html')),
    re_path(r'noticias-comunidad/(?P<pk>\d+)', TemplateView.as_view(template_name='index.html')),
    # /Vue.js

    # Urls Apps
    path(r'admin/', admin.site.urls),
    path(r'api/v1.0/', include('apps.api.urls', namespace="api")),

    # Urls Users
    path(r'rest-auth/', include('rest_auth.urls')),
    path(r'rest-auth/registration/', include('rest_auth.registration.urls')),
    path(r'refresh-token/', refresh_jwt_token),
    # path(r'usuario/', include('apps.usuario.urls', namespace="usuario")),
    # path(r'accounts/login/', LoginView.as_view(), {'template_name':'indexbk.html'}, name='login'),
    # path(r'logout/', logout_then_login, name='logout'),
    # path(r'reset/password_reset', PasswordResetView, {'template_name':'registration/password_reset_form.html', 'email_template_name':'registration/password_reset_email.html'}, name='password_reset'),
    # path(r'reset/password_reset_done', PasswordResetDoneView, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    # re_path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/', PasswordResetConfirmView, {'template_name': 'registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    # path(r'reset/done', PasswordResetCompleteView, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
] + static( '/static/', document_root=settings.STATIC_ROOT, show_indexes=True ) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)