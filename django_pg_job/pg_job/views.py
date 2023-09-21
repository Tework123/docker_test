from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from pg_job.models import TimeSecond5
from pg_job.serializers import TimeSecond5AggSerializer


class TimeSecond5AggView(generics.ListAPIView):
    """Показывает поминутно агрегированные данные из таблицы TimeSecond5"""
    serializer_class = TimeSecond5AggSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        times = TimeSecond5.objects.all()
        # агрегировать по минутам(сумма?)
        # соединить таблицы на локале, проверить поля со временем
        # переходить на докер, поднять джанго в докере,
        # наверное придется создавать таблицы в джанго,
        # а потом на их основе писать тригеры и функции в пгадмине
        return times
