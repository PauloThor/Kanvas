from django.urls import path
from .views import CourseView, CourseViewById, Registration

urlpatterns = [
    path('courses/', CourseView.as_view()),
    path('courses/<int:course_id>/', CourseViewById.as_view()),
    path('courses/<int:course_id>/registrations/', Registration.as_view()),
]
