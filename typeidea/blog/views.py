from datetime import date

from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from django.db.models import Q, F
from django.core.cache import cache

from .models import Category, Tag, Post
from config.models import SideBar
from comment.models import Comment

from comment.forms import CommentForm


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'sidebars': self.get_sidebars(),
            }
        )
        context.update(self.get_navs())
        return context

    def get_sidebars(self):
        return SideBar.objects.filter(status=SideBar.STATUS_SHOW)

    def get_navs(self):
        categories = Category.objects.filter(status=Category.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return {
            'navs': nav_categories,
            'categories': normal_categories
        }


class IndexView(CommonViewMixin, ListView):
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update(
            {
                'category': category,
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update(
            {
                'tag': tag,
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts(cls=Post)
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # self.handle_visited()
        return response

    # def handle_visited(self):
    #     increase_pv = False
    #     increase_uv = False
    #     uid = self.request.uid
    #     pv_key = 'pv:%s:%s' % (uid, self.request.path)
    #     if not cache.get(pv_key):
    #         increase_pv = True
    #         cache.set(pv_key, 1, 1*60)  # 1????????????
    #
    #     uv_key = 'uv:%s:%s:%s' % (uid, str(date.today()), self.request.path)
    #     if not cache.get(uv_key):
    #         increase_uv = True
    #         cache.set(uv_key, 1, 24*60*60)  # 24????????????
    #
    #     if increase_pv and increase_uv:
    #         Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
    #     elif increase_pv:
    #         Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
    #     elif increase_uv:
    #         Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)


class SearchView(IndexView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update(
            {
                'keyword': self.request.GET.get('keyword', '')
            }
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)
