#main/urls.py
from django.shortcuts import redirect  
from django.urls import path, re_path  
from . import views  

# Funktio, joka ohjaa käyttäjän feed-sivulle
def redirect_to_feed(request):
    return redirect('feed')  

urlpatterns = [
    
    path('', redirect_to_feed),  # Tyhjä reitti (etusivu) ohjaa feed-sivulle
    path('signup/', views.signup, name='signup'),  # Käyttäjän rekisteröitymissivu
    path('login/', views.login_view, name='login'),  # Kirjautumissivu
    path('logout/', views.feed, name='logout'),  # Uloskirjautumissivu, joka ohjaa feed-sivulle (tarkistettava, onko tämä oikea logout-toiminto)
    path('feed/', views.feed, name='feed'),  # Sivusto, jossa näytetään kaikki julkaisut (feed)
    path('post/create/', views.post_create, name='post_create'),  # Julkaisun luontisivu
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),  # Tietyn julkaisun poistaminen sen id-tunnisteen perusteella
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),  # Kommentin luontisivu tietylle julkaisulle id-tunnisteen perusteella
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),  # Kommentin poistaminen id-tunnisteen perusteella
    path('post/<int:pk>/like/', views.like, name='like'),  # Tykkäystoiminto tietylle julkaisulle id-tunnisteen perusteella
    re_path(r'^profile/(?!change-username/)(?P<username>\w+)/$', views.user_profile, name='user_profile'),  # regex.Profiilisivu käyttäjän käyttäjänimen perusteella, mutta ohittaa change-username-polun
    path('guest/profile/<str:username>/', views.guest_profile, name='guest_profile'),  # Vierailijaprofiilisivu tietyn käyttäjän käyttäjänimen perusteella
    path('profile/change-username/', views.change_username, name='change_username'),  # Käyttäjänimen vaihtosivu
    path('search/', views.search_users, name='search_users'),  # Käyttäjähaun sivu
]



#ok