from rest_framework import serializers

from pg_job.models import TimeSecond5


class TimeSecond5AggSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSecond5
        fields = '__all__'
