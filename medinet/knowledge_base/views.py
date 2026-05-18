from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def article_list(request):
    article = Article.objects.all().order_by('-create_at')

    return render(request, 'knowledge_base/article_list.html', {
        'articles': article
    })

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form =ArticleForm()

    return render(request, 'knowledge_base/article_create.html', {'form': form

    })
