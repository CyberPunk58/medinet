from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404

def article_list(request):
    article = Article.objects.all().order_by('-create_at')

    return render(request, 'knowledge_base/article_list.html', {
        'articles': article
    })

def article_detail(request, article_id):
    article = get_object_or_404(
        Article,
        id=article_id
    )

    return render(request, 'knowledge_base/article_detail.html', {
        'article': article
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
