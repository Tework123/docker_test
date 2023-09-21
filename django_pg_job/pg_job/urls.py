from django.urls import path

from pg_job.views import TimeSecond5AggView

urlpatterns = [

    path('time_second_5/', TimeSecond5AggView.as_view()),
]