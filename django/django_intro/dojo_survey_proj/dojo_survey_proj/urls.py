from django.urls import path, include           # import include
urlpatterns = [
    path('', include('dojo_survey.urls')),
]