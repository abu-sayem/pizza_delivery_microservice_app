
from django.urls import include, path
from . import views

urlpatterns = [

    #path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', views.UserListView.as_view()),
]
