from django.shortcuts import render, redirect
from django.views.generic import View
from . import models
from .forms import CreateCommentForm
from django.http import JsonResponse
from django.core.paginator import Paginator
from blog.models import Blog


class TeamView(View):
    def get(self, request):
        trainers = models.Trainer.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(trainers, 6)
        object_list = paginator.get_page(page_number)
        context = {
            'trainers': object_list
        }
        return render(request, 'team/team.html', context)

class TrainerDetail(View):
    def get(self, request, pk):
        form = CreateCommentForm()
        trainer = models.Trainer.objects.get(pk=pk)
        comments = trainer.comments.all()
        five_recents = Blog.objects.all().order_by('-updated_at', '-published_at')[0:5]
        context = {
            'trainer': trainer,
            'comments': comments,
            'form': form,
            'five_recents': five_recents,
        }
        return render(request, 'team/trainer_detail.html', context)


class CreateComment(View):
    def post(self, request, trainer_pk):
        form = CreateCommentForm(request.POST)
        trainer = models.Trainer.objects.get(pk=trainer_pk)
        comments = trainer.comments.all()
        count = comments.count()



        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.trainer = trainer
            if request.POST.get('comment_parent_id'):
                parent_id = request.POST.get('comment_parent_id')
                parent_comment = models.TrainerComment.objects.get(pk=int(parent_id))
                instance.parent = parent_comment

                instance.save()
                return redirect('team:trainer_detail', trainer.pk)

            instance.save()

            return redirect('team:trainer_detail', trainer.pk)

        return render(request, 'team/trainer_detail.html', {'form': form})

        # user_comment = request.user.username
        # return JsonResponse({'count': count, 'user': user_comment, })



