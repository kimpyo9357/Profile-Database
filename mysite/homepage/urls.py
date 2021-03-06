from django.urls import path

from . import views

app_name = "homepage"
urlpatterns = [
    path('', views.login, name='login'),
    path('Author/', views.author, name='author'),
    path('AuthorLogin/', views.authorlogin),
    path('Message/', views.message, name="message"),
    path('SignUp/', views.signup, name="signup"),
    path('Information', views.information, name='information'),
    path('Delete/', views.delete, name="delete"),
]