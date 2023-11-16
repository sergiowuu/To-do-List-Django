from todo.models import Todo

from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'is_done', 'created_at', 'updated_at', 'user']
    