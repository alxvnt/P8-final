from django.urls import path
from users import views

urlpatterns = [
    path('enregistrement/', views.register, name="enregistrement"),
    path('connexion/', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('compte', views.mon_compte, name="compte"),
    path('mes_aliments', views.fav, name="fav"),
    path('suppression/', views.delete_product, name="suppression"),

]