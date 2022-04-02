from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, api_comments, api_comments_2, api_comment_detail
from .views import APIComments, APICommentDetail, APICommentsHL, APICommentDetailHL, APICommentViewSet


router = DefaultRouter()
router.register('comments', APICommentViewSet)


urlpatterns = [
    path('', index, name='index'),

    path('comments/', api_comments, name='api_comments'),

    # Вьюхи используют декораторы
    path('comments2/', api_comments_2, name='api_comments_2'),
    path('comment/<int:pk>', api_comment_detail, name='api_comment_detail'),

    # Вьюхи используют контроллер класса
    path('api_comments/', APIComments.as_view(), name='api_comments_class'),
    path('api_comments/<int:pk>', APICommentDetail.as_view(), name="api_comment_detail_class"),

    # Вьюхи используют контроллер класса высокого уровня
    path('api_comments_hl/', APICommentsHL.as_view(), name='api_comments_hl_class'),
    path('api_comments_hl/<int:pk>', APICommentDetailHL.as_view(), name="api_comment_detail_hl_class"),

    # Вьюхи используют метаконтроллер
    path('api/', include(router.urls)),
]
