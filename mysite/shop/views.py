from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils import timezone
from blog.models import Post, Color

from django.shortcuts import redirect


# Create your views here.
def shop(request):
	posts = Post.objects.all()

	return render(request, 'shop/shop.html')
	