from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from .forms import CreateBlogCommentForm
from django.core.paginator import Paginator

class BlogListView(View):
    def get(self, request):
        tags = models.Tag.objects.all()
        categories = models.Category.objects.all()
        try:
            category_title = request.GET.get('category')
            category = models.Category.objects.get(title=category_title)
            blogs = category.blogs.all()
            try:
                tag_t = request.GET.get('tag')
                tag = models.Tag.objects.get(tag_title=tag_t)
                blogs = tag.blogs.all()
            except:
                pass


        except:
            blogs = models.Blog.objects.all()
            try:
                tag_t = request.GET.get('tag')
                tag = models.Tag.objects.get(tag_title=tag_t)
                blogs = tag.blogs.all()
            except:
                pass


        five_revent_blogs = models.Blog.objects.all().order_by('-updated_at', '-published_at')
        page_number = request.GET.get('page')
        paginator = Paginator(blogs, 6)
        object_list = paginator.get_page(page_number)
        context = {
            'blogs': object_list,
            'categories': categories,
            'recents': five_revent_blogs,
            'tags': tags,
        }
        return render(request, 'blog/blog_list_view.html', context)

class BlogDetailView(View):
    def get(self, request, pk):

        form = CreateBlogCommentForm()
        blog = models.Blog.objects.get(pk=pk)
        tags = blog.tags.all()
        categories = blog.category.all()
        comments = blog.comments.all()
        context = {
            'blog': blog,
            'tags': tags,
            'form': form,
            'comments': comments,
            'categories': categories,
        }
        return render(request, 'blog/blog_detail.html', context)

class CreateCommentView(View):
    def post(self, request, pk):
        blog = models.Blog.objects.get(pk=pk)
        form = CreateBlogCommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.blog = blog
            if request.POST.get('parent_id'):
                parent_id = request.POST.get('parent_id')
                parent_comment = models.BlogComment.objects.get(pk=int(parent_id))
                instance.parent = parent_comment
                instance.save()
                return redirect('blog:blog_detail', blog.pk)

            instance.save()
            return redirect('blog:blog_detail', blog.pk)

        return render(request, 'blog/blog_detail.html', {'form': form})

