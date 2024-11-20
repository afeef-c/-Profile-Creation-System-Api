from django.urls import path
from .views import CreateStudentProfileView

urlpatterns = [
    path('create-profile/', CreateStudentProfileView.as_view(), name='create-profile'),
]
