from rest_framework import serializers
from api.models import Article, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only= True)
    class Meta:
        model = Article
        fields = '__all__'

