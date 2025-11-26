Namesti vse pakete z pip install -r requirements.txt


Za html strani bi rabil

te strani grejo v templates od store razen contact.html

templates/home.html
templates/categories.html
templates/products.html
templates/cart.html
templates/contact.html  <- ta gre v templates ki je v contact
templates/checkout.html

Vsi statični elementi kot so css in js grejo v file 
/static/
css/
js/
img/

Za uporabo CSS/JS ali slik v templatu moraš dodati:

```html
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/app.js' %}"></script>
<img src="{% static 'img/logo.png' %}" alt="logo">





Kako zagnati:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


za logiranje je
marketzone1
marketzone12345


stran deluje na http://127.0.0.1:8000/ oziroma bo delovala ko bodo htmlji not