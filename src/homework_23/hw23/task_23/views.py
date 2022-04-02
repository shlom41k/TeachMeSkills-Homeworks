from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework import generics, viewsets
from .serializers import CommentSerializer
from .models import Comment


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")


# 1-st variant
def api_comments(request):
    if request.method == "GET":
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)


# 2-nd variant
# С использованием декораторов
@api_view(["GET", "POST"])
def api_comments_2(request):
    if request.method == "GET":
        comments = Comment.objects.filter()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# Получение инфы об одном объекте
@api_view(["GET", "PUT", "DELETE"])
def api_comment_detail(request, pk: int):
    comment = Comment.objects.get(pk=pk)

    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        comment.delete()
    return Response(status=HTTP_204_NO_CONTENT)


# 3-rd variant
# Контроллеры класса
class APIComments(APIView):
    def get(self, request):
        comments = Comment.objects.filter()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# Получение инфы об одном объекте
class APICommentDetail(APIView):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# 4-th variant
# Контроллеры-классы высокого уровня
class APICommentsHL(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Получение инфы об одном объекте
class APICommentDetailHL(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# 5-th variant
# Метаконтроллеры
class APICommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
