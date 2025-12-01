from django.contrib import admin
from django.urls import path
from store import views as store_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', store_views.home, name="home"),
    path("trgovina/", store_views.trgovina, name="trgovina"),
    path('categories/', store_views.categories, name="categories"),
    path('products/<int:category_id>/', store_views.products, name="products"),

    path('cart/', store_views.cart_view, name="cart_view"),
    path('cart/add/<int:product_id>/', store_views.add_to_cart, name="add_to_cart"),
    path('cart/update/<int:item_id>/', store_views.update_cart, name="update_cart"),
    path('cart/remove/<int:item_id>/', store_views.remove_from_cart, name="remove_from_cart"),

    path('checkout/', store_views.checkout_steps, name="checkout"),

    path('contact/', contact_views.contact_form, name="contact_form"),

    path('about/', store_views.about, name="about"),
    path('services/', store_views.services, name="services"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
