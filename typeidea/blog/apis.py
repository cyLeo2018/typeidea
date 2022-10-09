from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    serializer_class = PostSerializer
