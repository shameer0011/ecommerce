import json
from . models import *

def cookieCart(request):
            try:
                cart=json.loads(request.COOKIES['cart'])
                print(cart)
            except:
                cart=[] #or {}

            #Create empty cart for now for non-logged in user
            items = []

            order={'get_cart_items':0,'get_cart_total':0,'shipping':False}
            # we may call 'get_cart_items' above..both situation have 'cart_items'
            cart_Items=order['get_cart_items']#total cart..
            #cart_total=order['get_cart_total']# total price

            for i in cart:
                print(i,"it is a product id")
                try:
                    product=Product.objects.get(id=i)
                    total=product.price* cart[i]['quantity_s']
                    order['get_cart_total']+=total# full total price..get from total loop to store a value..
                    order['get_cart_items']+=cart[i]['quantity_s']# full total cart..get from total loop to store a value..

                    cart_Items += cart[i]['quantity_s']# only for layout total cart..
                    cart_total= order['get_cart_total']

                    item={
                        'product':{
                            'id':product.id,
                            'name':product.name,
                            'price':product.price,
                            'imageUrl':product.imageUrl,
                            'digital':product.digital
                        },
                        'quantity':cart[i]['quantity_s'],
                        'get_total':total
                    }
                    items.append(item)
                except:# oru product ne cart lek maatti..pinne db il ninn athine kalanju..appo error varum..ath vraathirikan..
                    pass 
               
            return {'cart_Items':cart_Items,'items':items,'order':order,'cart_total':cart_total}