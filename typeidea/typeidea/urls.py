"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import links
from comment.views import CommentView

from blog.apis import PostViewSet
from rest_framework.routers import DefaultRouter
import blog

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')


urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # 首页
    path('category/<category_id>/', CategoryView.as_view(), name='category_list'),  # 分类列表页
    path('tag/<tag_id>/', TagView.as_view(), name='tag_list'),  # 标签列表页
    path('post/<post_id>/', PostDetailView.as_view(), name='post_detail'),  # 文章详情页
    path('search/', SearchView.as_view(), name='search'),  # 搜索
    path('comment/', CommentView.as_view(), name='comment'),  # 评论
    path('author/<owner_id>/', AuthorView.as_view(), name='author'),  # 作者
    path('links/', links, name='links'),  # 友链展示页
    path('api-auth/', include('rest_framework.urls')),  # restful api auth
    # path('api/', include(router.urls)),  # restful api
    path('admin/', admin.site.urls, name='admin')  # 管理后台
]
