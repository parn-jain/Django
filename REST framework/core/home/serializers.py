from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['name','age']
        # exclude = ['id','fathers_name']


    def validate(self,data):
        if 'age' in data and data['age']<18:
            raise serializers.ValidationError({'error':"Age is less then 18"})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':"name must not contain digit"})
        return data 
