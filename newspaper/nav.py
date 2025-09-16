from newspaper.models import Category

def navigation(request):
    categories = Category.objects.all()[:4]
    return {"categories": categories}