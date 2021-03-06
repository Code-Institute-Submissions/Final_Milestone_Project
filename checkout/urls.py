from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>',
        views.checkout_success, name='checkout_success'),
    path('cache_data/', views.cache_data, name='cache_data'),
    path('wh/', webhook, name='webhook'),
    path(
        'rate/<order_number>/<image_id>',
        views.leave_rating, name='leave_rating')
]
