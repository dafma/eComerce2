from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Variation
from carts.models import Cart, CartItem


class CartView(SingleObjectMixin, View):
    model = Cart
    template_name = "carts/carts.html"

    def get_object(self, *args, **kwargs):
        # 5 min
        self.request.session.set_expiry(300)
        cart_id = self.request.session.get("cart_id")
        if None == cart_id:
            cart = Cart()
            cart.save()
            cart_id = cart.id
            self.request.session["cart_id"] = cart_id
        cart = Cart.objects.get(id=cart_id)
        if self.request.user.is_authenticated():
            cart.user = self.request.user
            cart.save()
        return cart

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        item_id = request.GET.get("item")
        delete_item = request.GET.get("delete")
        if item_id:
            item_instance = get_object_or_404(Variation, id=item_id)
            qty = request.GET.get("qty")
            cart_item = CartItem.objects.get_or_create(cart=cart, item=item_instance)[0]
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
        context = {
            "object": self.get_object(),
        }
        template = self.template_name

        return render(request, template, context)
