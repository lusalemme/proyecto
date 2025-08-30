from django.urls import path
from usuarios.views import iniciar_sesion, registro, perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout')
]