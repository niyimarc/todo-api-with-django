from rest_framework.serializers import ModelSerializer
from todolist.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model= Todo
        fields = ('title', 'desc', 'is_complete',)