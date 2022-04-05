from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('signin/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('add_product/',views.add_product,name='add_product'),
    path('view_product/',views.view_product,name='view_product'),
    path('edit_product/<int:pk>/',views.edit_product,name='edit_product'),
    path('delete_product/<int:pk>/',views.delete_product,name='delete_product'),
    path('collection_men/',views.collection_men,name='collection_men'),
    path('collection_women/',views.collection_women,name='collection_women'),
    path('collection_Kids/',views.collection_Kids,name='collection_Kids'),
    path('category_cloth/',views.category_cloth,name='category_cloth'),
    path('category_footware/',views.category_footware,name='category_footware'),
    path('category_watchs/',views.category_watchs,name='category_watchs'),
    path('category_accessoies/',views.category_accessoies,name='category_accessoies'),
    path('size_s/',views.size_s,name='size_s'),
    path('size_m/',views.size_m,name='size_m'),
    path('size_l/',views.size_l,name='size_l'),
    path('size_xl/',views.size_xl,name='size_xl'),
    path('shop_single/<int:pk>/',views.shop_single,name='shop_single'),
    path('whishlist/<int:pk>/',views.whishlist,name='whishlist'),
    path('whishlist2/',views.whishlist2,name='whishlist2'),
    path('delete_from_whishlist/<int:pk>/',views.delete_from_whishlist,name='delete_from_whishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('delete_from_cart/<int:pk>/',views.delete_from_cart,name='delete_from_cart'),
    path('change_qty/',views.change_qty,name='change_qty'),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/',views.callback, name='callback'),
    path('my_orders/',views.my_orders, name='my_orders'),
    path('ajax/validate_email/',views.validate_signup, name='validate_email'),
]


