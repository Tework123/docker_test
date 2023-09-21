from rest_framework import serializers


class TimeSecond5AggSerializer(serializers.Serializer):
    minutes = serializers.DateTimeField()
    avg_value = serializers.FloatField()
