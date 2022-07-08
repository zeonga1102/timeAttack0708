from django.contrib import admin
from django.urls import path, include
from .views import SkillView, JobView, ApplyingUserView

urlpatterns = [
    path('', SkillView.as_view()),

    path('job', JobView.as_view()),

    path('apply', ApplyingUserView.as_view())
]
