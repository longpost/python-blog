
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post,Category,Tag


'''class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
'''
class DetailView(generic.DetailView):#option2
    model=Post
    template_name = 'blog/detail.html'

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'
    
    print(111111,Post.objects.order_by('-created_time')[:5])
    def get_queryset(self):
        """Return the last five published blogs."""
        return Post.objects.filter(
        created_time__lte=timezone.now()
    ).order_by('-created_time')[:5]
        #return Post.objects.order_by('-created_time')[:5]
    
'''def detail(request, post_id):#option1
    
    post = get_object_or_404(Post, pk=post_id)
    #post=Post.objects.get(pk=post_id)
    print(post,post.body,post.author)
    context={'post':post}
    return render(request,'blog/detail.html',context)
'''
'''def index(request):#option 1
    #print(222222)
    latest_post_list = Post.objects.order_by('-created_time')[:5]
    #print(111111,latest_post_list)
    
    output = ', '.join([q.title for q in latest_post_list])
    return HttpResponse(output)
'''

'''def index(request):#option 2
    #print(222222)
    latest_post_list = Post.objects.order_by('-created_time')[:5]
    #print(111111,latest_post_list)
    context={'latest_post_list':latest_post_list}
    
    return render(request,'blog/index.html',context)
'''
