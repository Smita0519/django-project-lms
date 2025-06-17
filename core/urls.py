from django.urls import path
from core.views import HomePageView, TeacherCreateView, TeacherListView

urlpatterns =  [
    path('', HomePageView.as_view, name = 'home'),    # '' no name means takes base url
    path('teacher/list/', TeacherListView.as_view(), name='teacher.index'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher.create')
]