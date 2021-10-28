from django.urls import path
from .views import ActivityView, Registration, ActivityViewById, SubmissionView, AllSubmissions

urlpatterns = [
    path('activities/', ActivityView.as_view()),
    path('activities/<int:activity_id>/', ActivityViewById.as_view()),
    path('activities/<int:activity_id>/submissions/', Registration.as_view()),
    path('submissions/<int:submission_id>/', SubmissionView.as_view()),
    path('submissions/', AllSubmissions.as_view()),
]
