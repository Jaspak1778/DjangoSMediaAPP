# main/urls.py

from rest_framework.routers import DefaultRouter
from .api_views import PostViewSet, CommentViewSet, LikeViewSet
from django.urls import path, re_path, include
from . import views
from django.shortcuts import redirect

# REST API reititys
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

# Ohjataan käyttäjä syötteeseen
def redirect_to_feed(request):
    # Tarkistetaan, onko käyttäjä kirjautunut
    if request.user.is_authenticated:
        return redirect('feed')
    else:
        return redirect('login')
    
# URLS
urlpatterns = [
    # REST API reitit
    path('api/', include(router.urls)),

    # Ohjataan etusivulta syöte-sivulle
    path('', redirect_to_feed),

    # Käyttäjän kirjautumiseen liittyvät reitit
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Syötesivu ja postaukset
    path('feed/', views.feed, name='feed'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/like/', views.like, name='like'),

    # Käyttäjäprofiilit
    re_path(r'^profile/(?!change-username/)(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    path('guest/profile/<str:username>/', views.guest_profile, name='guest_profile'),
    path('profile/change-username/', views.change_username, name='change_username'),

    # Käyttäjien haku
    path('search/', views.search_users, name='search_users'),
]


#ok