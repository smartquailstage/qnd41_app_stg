from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .models import solutions, solutions_categories
from solutions_blog.models import BlogPage


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'webapp/products/smartbusinessmedia/index/smartbusinesmedia.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})





def blog_index(request):
    posts = BlogPage.objects.live().public().order_by('-date')
    return render(request, 'solutions/meet_solutions.html', {
        'posts': posts,
    })

def blog_post(request, slug):
    post = BlogPage.objects.live().public().get(slug=slug)
    return render(request, 'solutions/meet_solutions.html', {
        'post': post,
    })


def solution_items(request):
    solution = solutions_categories.objects.live().public().order_by('-date ')
    return render(request, 'solutions/solutions.html', {'solution':solution})

def solutions_items(request):
    solutions = solutions_categories.objects.live().public().order_by('category')
    return render(request, 'solutions/solutions.html', {'solutions':solutions})