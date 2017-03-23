from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.contrib import messages
from django.core.urlresolvers import reverse


from products.models import Variation
from .models import Cart, CartItem
# Create your views here.


class ItemCountView(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse({"count": 3})
        else:
            raise Http404


class CartView(SingleObjectMixin, View):
    model = Cart
    template_name = "carts/cart_view.html"

    def get_cart_object(self, *args, **kwargs):
        cart_id = self.request.session.get("cart_id")
        if cart_id == None:
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
        cart = self.get_cart_object()
        item_id = request.GET.get("item")
        delete_item = request.GET.get("delete", False)
        if item_id:
            item_instance = get_object_or_404(Variation, id=item_id)
            qty = request.GET.get("qty", 1)
            try:
                if int(qty) < 1:
                    delete_item = True
            except:
                raise Http404

            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item_instance)
            if delete_item:
                cart_item.delete()
            else:
                cart_item.quantity = qty
                cart_item.save()
                messages.success(self.request, "Your cart has been updated")

        context = {
            "object": self.get_cart_object()
        }
        template = self.template_name

        return render(request, template, context)



