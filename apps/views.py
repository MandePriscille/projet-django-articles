from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.models import Article

def get(request):
    articles = Article.objects.all() # Récupération des articles
    paginator = Paginator(articles, 5) # 5 articles par page
    
    page_number = request.GET.get('page', 1)  # Récupération de la page demandée ou de la première par défaut

    try:
        page_obj = paginator.get_page(page_number)

    except PageNotAnInteger:        # Affiche la première page si le numéro de page n'est pas valide
        page_obj = paginator.page(1)

    except EmptyPage:   # Affiche la dernière page si le numéro de page est hors limite
        page_obj = paginator.page(paginator.page_number)    

    return render(request, 'paginations/page.html',{'page_obj':page_obj})