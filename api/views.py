from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Article
from api.serializers import ArticleSerializer
import json
# Create your views here.

@api_view()
def articleApi(request):
    articles = Article.objects.all()
    response = ArticleSerializer(articles, many=True)
    return Response(response.data)

@api_view(['POST'])
def createArticleApi(request):
    body = json.loads(request.body)
    response = ArticleSerializer(data=body)
    if response.is_valid():
        inst = response.save()
        response = ArticleSerializer(inst)
        return Response(response.data)
    return Response(response.errors)