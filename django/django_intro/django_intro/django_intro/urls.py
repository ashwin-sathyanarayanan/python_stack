from django.urls import path, include           # import include
urlpatterns = [
    path('first_app/', include('my_first_app.urls')),
    path('second_app/', include('my_second_app.urls'))
]
