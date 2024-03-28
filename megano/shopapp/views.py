from django.conf import settings
from django.core.cache import cache
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView

from .models import Seller, Discount, Review
from .forms import ReviewForm


def adding_review(request: HttpRequest):
    """Функция для обработки формы товара
    и отображения отзывов на странице"""
    error = ""
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Неправильно составлен отзыв!"

    form = ReviewForm
    context = {
        "reviews": Review.objects.all(),
        "count_rev": Review.objects.all().count(),
        "form": form,
        "error": error
    }
    return render(request, "shopapp/product_reviews.html", context=context)

@method_decorator(cache_page(60 * 60), name="dispatch")
class SellerDetailView(DetailView):
    model = Seller
    template_name = "shopapp/seller_detail.html"
    context_object_name = "seller"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seller = self.get_object()
        top_products = get_top_products(seller)
        context["top_products"] = top_products
        return context


def get_top_products(seller):
    pass


class DiscountListView(ListView):
    model = Discount
    template_name = "shopapp/discount_list.html"
