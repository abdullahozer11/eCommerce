from django.urls import path

from commerce_app.views import IndexView, AboutView, ContactView, ProductView, TestimonialView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/', ProductView.as_view(), name='product'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
]