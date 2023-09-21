import random
from datetime import datetime

from django.db.models import Avg, Count
from django.db.models.functions import TruncMinute
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from pg_job.models import TimeSecond5
from pg_job.serializers import TimeSecond5AggSerializer


class TimeSecond5AggView(generics.ListCreateAPIView):
    """Показывает поминутно агрегированные данные из таблицы TimeSecond5"""

    serializer_class = TimeSecond5AggSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        times = TimeSecond5.objects.annotate(minutes=TruncMinute('time')).values('minutes').annotate(
            avg_value=Avg('value')).order_by('minutes')

        serializer = TimeSecond5AggSerializer(times, many=True)

        return serializer.data

    def post(self, request, *args, **kwargs):
        TimeSecond5.objects.create(time=datetime.now(), value=random.randrange(0, 10))
        return Response(status=status.HTTP_201_CREATED, data='Time created')
