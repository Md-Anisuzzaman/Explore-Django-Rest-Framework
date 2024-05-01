# from rest_framework import serializers

# class CategorySerilizer(serializers.Serializer):
#     id = serializers.IntegerField(primary_key=True, unique=True, null=False)
#     name = serializers.CharField(max_length=100)
#     created_date = serializers.DateTimeField(auto_now_add=True)
#     modified_date = serializers.DateTimeField(auto_now=True)


# from rest_framework import serializers

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     created_date = serializers.DateTimeField(read_only=True)
#     modified_date = serializers.DateTimeField(read_only=True)


from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','created_date','modified_date']