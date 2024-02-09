
from django.urls import path
from recipe import views

urlpatterns = [
    path('register/',views.register_user),
    path('login/',views.login_user),
    path('home/',views.home),
    path('logout/',views.user_logout),
     path('index/',views.index),
    path('filter/<category_value>',views.filter_by_category),
    path('sort/<sort_value>',views.sort_by_time),
    path('rating/<rating_value>',views.filter_by_rating),
    ]