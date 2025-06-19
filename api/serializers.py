from rest_framework import serializers
from todo.models import  Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.CharField( read_only=True)
    class Meta:

        model = Todo
        fields = ['id','title','memo','created','datecompleted','important','username','user']




class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','memo','created','datecompleted','important']