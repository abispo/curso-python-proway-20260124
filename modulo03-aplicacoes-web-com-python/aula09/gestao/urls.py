from django.urls import path

from . import views

app_name = "gestao"

urlpatterns = [
    path('', views.index, name="index"),
    path('nova-os/', views.nova_ordem_de_servico, name="nova_ordem_de_servico")
]
