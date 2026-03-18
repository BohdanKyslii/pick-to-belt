RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> accounts\forms.py:47:19
   |
45 |               "password2",
46 |           )
47 |           widgets = {
   |  ___________________^
48 | |             "username": forms.TextInput(
49 | |                 attrs={"placeholder": _("Username"), "autocomplete": "username"}
50 | |             ),
51 | |         }
   | |_________^
52 |
53 |       def __init__(self, *args, **kwargs):
   |

D107 Missing docstring in `__init__`
  --> accounts\forms.py:53:9
   |
51 |         }
52 |
53 |     def __init__(self, *args, **kwargs):
   |         ^^^^^^^^
54 |         super().__init__(*args, **kwargs)
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> accounts\forms.py:100:18
    |
 98 |     class Meta:
 99 |         model = User
100 |         fields = ["username", "email", "first_name", "last_name"]
    |                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
101 |         widgets = {
102 |             "username": forms.TextInput(attrs={"class": "form-control"}),
    |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> accounts\forms.py:101:19
    |
 99 |           model = User
100 |           fields = ["username", "email", "first_name", "last_name"]
101 |           widgets = {
    |  ___________________^
102 | |             "username": forms.TextInput(attrs={"class": "form-control"}),
103 | |             "first_name": forms.TextInput(attrs={"class": "form-control"}),
104 | |             "last_name": forms.TextInput(attrs={"class": "form-control"}),
105 | |         }
    | |_________^
    |

E501 Line too long (94 > 90)
  --> accounts\views.py:55:91
   |
53 |                 next_url = request.GET.get("next") or request.POST.get("next")
54 |
55 |                 # If next is not specified, or it leads to a profile, or it is empty - go home
   |                                                                                           ^^^^
56 |                 if not next_url or "/profile/" in next_url or next_url == "/":
57 |                     next_url = "home"
   |

D400 First line should end with a period
   --> common\templatetags\custom_filters.py:273:5
    |
271 | @register.filter
272 | def floatformat(value, decimal_places=2):
273 |     """Форматує число з заданою кількістю десяткових знаків"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
274 |     try:
275 |         return format(float(value), f".{decimal_places}f")
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> common\templatetags\custom_filters.py:273:5
    |
271 | @register.filter
272 | def floatformat(value, decimal_places=2):
273 |     """Форматує число з заданою кількістю десяткових знаків"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
274 |     try:
275 |         return format(float(value), f".{decimal_places}f")
    |
help: Add closing punctuation

D400 First line should end with a period
   --> common\templatetags\custom_filters.py:282:5
    |
280 | @register.filter
281 | def cut(value, arg):
282 |     """Видаляє всі значення аргументу з рядка"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
283 |     try:
284 |         return str(value).replace(arg, "")
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> common\templatetags\custom_filters.py:282:5
    |
280 | @register.filter
281 | def cut(value, arg):
282 |     """Видаляє всі значення аргументу з рядка"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
283 |     try:
284 |         return str(value).replace(arg, "")
    |
help: Add closing punctuation

D400 First line should end with a period
   --> common\templatetags\custom_filters.py:291:5
    |
289 | @register.filter
290 | def get_category_class(category):
291 |     """Повертає CSS клас для категорії витрат"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
292 |     category_map = {
293 |         "rent": "rent",
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> common\templatetags\custom_filters.py:291:5
    |
289 | @register.filter
290 | def get_category_class(category):
291 |     """Повертає CSS клас для категорії витрат"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
292 |     category_map = {
293 |         "rent": "rent",
    |
help: Add closing punctuation

D400 First line should end with a period
  --> data_to_import\import_data.py:15:5
   |
14 | def restore_json_to_table(json_file, db_table):
15 |     """Проста функція для відновлення одного файлу в одну таблицю"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |     try:
17 |         with open(json_file, "r", encoding="utf-8") as f:
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> data_to_import\import_data.py:15:5
   |
14 | def restore_json_to_table(json_file, db_table):
15 |     """Проста функція для відновлення одного файлу в одну таблицю"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |     try:
17 |         with open(json_file, "r", encoding="utf-8") as f:
   |
help: Add closing punctuation

UP015 [*] Unnecessary mode argument
  --> data_to_import\import_data.py:17:30
   |
15 |     """Проста функція для відновлення одного файлу в одну таблицю"""
16 |     try:
17 |         with open(json_file, "r", encoding="utf-8") as f:
   |                              ^^^
18 |             data = json.load(f)
   |
help: Remove mode argument

F541 [*] f-string without any placeholders
  --> data_to_import\import_data.py:22:19
   |
20 |         records = data.get("data", [])
21 |         if not records:
22 |             print(f"  Файл порожній")
   |                   ^^^^^^^^^^^^^^^^^^
23 |             return 0
   |
help: Remove extraneous `f` prefix

W291 Trailing whitespace
  --> data_to_import\import_data.py:38:62
   |
36 |                         # SQL запит для вставки або заміни
37 |                         sql = f"""
38 |                             INSERT OR REPLACE INTO {db_table}
   |                                                              ^
39 |                             ({", ".join(keys)})
40 |                             VALUES ({", ".join(placeholders)})
   |
help: Remove trailing whitespace

W291 Trailing whitespace
  --> data_to_import\import_data.py:39:48
   |
37 |                         sql = f"""
38 |                             INSERT OR REPLACE INTO {db_table}
39 |                             ({", ".join(keys)})
   |                                                ^
40 |                             VALUES ({", ".join(placeholders)})
41 |                         """
   |
help: Remove trailing whitespace

D202 [*] No blank lines allowed after function docstring (found 1)
  --> data_to_import\import_data.py:59:5
   |
58 | def main():
59 |     """Основний скрипт з чітким списком файлів і таблиць"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
60 |
61 |     # СПИСОК ФАЙЛІВ І ТАБЛИЦЬ
   |
help: Remove blank line(s) after function docstring

D400 First line should end with a period
  --> data_to_import\import_data.py:59:5
   |
58 | def main():
59 |     """Основний скрипт з чітким списком файлів і таблиць"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
60 |
61 |     # СПИСОК ФАЙЛІВ І ТАБЛИЦЬ
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> data_to_import\import_data.py:59:5
   |
58 | def main():
59 |     """Основний скрипт з чітким списком файлів і таблиць"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
60 |
61 |     # СПИСОК ФАЙЛІВ І ТАБЛИЦЬ
   |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> shipment\admin.py:156:15
    |
154 |     raw_id_fields = ("shop", "warehouse")
155 |     date_hierarchy = "date"
156 |     inlines = [ExpenseInvoiceItemInline]
    |               ^^^^^^^^^^^^^^^^^^^^^^^^^^
157 |     readonly_fields = ("created_at", "updated_at", "sum_price", "sum_prod")
    |

D400 First line should end with a period
  --> shipment\forms.py:17:5
   |
16 | class ExpenseInvoiceForm(forms.ModelForm):
17 |     """Форма для створення та редагування видаткових накладних"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
18 |
19 |     class Meta:
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> shipment\forms.py:17:5
   |
16 | class ExpenseInvoiceForm(forms.ModelForm):
17 |     """Форма для створення та редагування видаткових накладних"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
18 |
19 |     class Meta:
   |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:21:18
   |
19 |       class Meta:
20 |           model = ExpenseInvoice
21 |           fields = [
   |  __________________^
22 | |             "source",
23 | |             "invoice",
24 | |             "date",
25 | |             "shop",
26 | |             "warehouse",
27 | |             "sum_price",
28 | |             "sum_prod",
29 | |             "description",
30 | |         ]
   | |_________^
31 |           widgets = {
32 |               "date": forms.DateInput(attrs={"type": "date", "class": "datepicker"}),
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:31:19
   |
29 |               "description",
30 |           ]
31 |           widgets = {
   |  ___________________^
32 | |             "date": forms.DateInput(attrs={"type": "date", "class": "datepicker"}),
33 | |             "description": forms.Textarea(attrs={"rows": 3, "cols": 40}),
34 | |             "source": forms.Select(attrs={"class": "form-select"}),
35 | |         }
   | |_________^
36 |           labels = {
37 |               "invoice": _("Номер документа"),
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:36:18
   |
34 |               "source": forms.Select(attrs={"class": "form-select"}),
35 |           }
36 |           labels = {
   |  __________________^
37 | |             "invoice": _("Номер документа"),
38 | |             "date": _("Дата документа"),
39 | |             "source": _("Джерело даних"),
40 | |         }
   | |_________^
41 |           help_texts = {
42 |               "source": _("Виберіть організацію (ESP, OPT, RUB)"),
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:41:22
   |
39 |               "source": _("Джерело даних"),
40 |           }
41 |           help_texts = {
   |  ______________________^
42 | |             "source": _("Виберіть організацію (ESP, OPT, RUB)"),
43 | |             "invoice": _("Унікальний номер документа"),
44 | |         }
   | |_________^
   |

D400 First line should end with a period
  --> shipment\forms.py:48:5
   |
47 | class ExpenseInvoiceItemForm(forms.ModelForm):
48 |     """Форма для позицій видаткової накладної"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
49 |
50 |     class Meta:
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> shipment\forms.py:48:5
   |
47 | class ExpenseInvoiceItemForm(forms.ModelForm):
48 |     """Форма для позицій видаткової накладної"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
49 |
50 |     class Meta:
   |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:52:18
   |
50 |       class Meta:
51 |           model = ExpenseInvoiceItem
52 |           fields = [
   |  __________________^
53 | |             "invoice",
54 | |             "line_number",
55 | |             "product",
56 | |             "quantity",
57 | |             "price",
58 | |             "sum_price",
59 | |             "sum_prod",
60 | |             "warehouse",
61 | |             "description",
62 | |         ]
   | |_________^
63 |           widgets = {
64 |               "quantity": forms.NumberInput(attrs={"step": "0.001", "min": "0.001"}),
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:63:19
   |
61 |               "description",
62 |           ]
63 |           widgets = {
   |  ___________________^
64 | |             "quantity": forms.NumberInput(attrs={"step": "0.001", "min": "0.001"}),
65 | |             "price": forms.NumberInput(attrs={"step": "0.01", "min": "0.01"}),
66 | |             "sum_price": forms.NumberInput(attrs={"step": "0.01", "min": "0.00"}),
67 | |             "sum_prod": forms.NumberInput(attrs={"step": "0.01", "min": "0.00"}),
68 | |             "description": forms.Textarea(attrs={"rows": 2, "cols": 40}),
69 | |         }
   | |_________^
70 |
71 |       def clean(self):
   |

D400 First line should end with a period
  --> shipment\forms.py:87:5
   |
86 | class ExpenseInvoiceFilterForm(forms.Form):
87 |     """Форма для фільтрації видаткових накладних"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
88 |
89 |     SOURCE_CHOICES = [
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> shipment\forms.py:87:5
   |
86 | class ExpenseInvoiceFilterForm(forms.Form):
87 |     """Форма для фільтрації видаткових накладних"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
88 |
89 |     SOURCE_CHOICES = [
   |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> shipment\forms.py:89:22
   |
87 |       """Форма для фільтрації видаткових накладних"""
88 |
89 |       SOURCE_CHOICES = [
   |  ______________________^
90 | |         ("", "Всі джерела"),
91 | |         ("ESP", "ESP"),
92 | |         ("OPT", "OPT"),
93 | |         ("RUB", "RUB"),
94 | |     ]
   | |_____^
95 |
96 |       source = forms.ChoiceField(
   |

D400 First line should end with a period
   --> shipment\forms.py:135:5
    |
134 | class ImportExpenseInvoiceForm(forms.Form):
135 |     """Форма для імпорту видаткових накладних"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
136 |
137 |     SOURCE_CHOICES = [
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> shipment\forms.py:135:5
    |
134 | class ImportExpenseInvoiceForm(forms.Form):
135 |     """Форма для імпорту видаткових накладних"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
136 |
137 |     SOURCE_CHOICES = [
    |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> shipment\forms.py:137:22
    |
135 |       """Форма для імпорту видаткових накладних"""
136 |
137 |       SOURCE_CHOICES = [
    |  ______________________^
138 | |         ("ESP", "ESP"),
139 | |         ("OPT", "OPT"),
140 | |         ("RUB", "RUB"),
141 | |     ]
    | |_____^
142 |
143 |       source = forms.ChoiceField(
    |

D400 First line should end with a period
   --> shipment\forms.py:163:5
    |
162 | class ProductSearchForm(forms.Form):
163 |     """Форма для пошуку товарів"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
164 |
165 |     search = forms.CharField(
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> shipment\forms.py:163:5
    |
162 | class ProductSearchForm(forms.Form):
163 |     """Форма для пошуку товарів"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
164 |
165 |     search = forms.CharField(
    |
help: Add closing punctuation

E501 Line too long (100 > 90)
   --> shipment\models.py:287:91
    |
285 |         verbose_name=_("Items per intermediate package"),
286 |         help_text=_(
287 |             "Number of individual items in one intermediate package (e.g., 12 items per inner box)."
    |                                                                                           ^^^^^^^^^^
288 |         ),
289 |     )
    |

D401 First line of docstring should be in imperative mood: "String representation for product packaging."
   --> shipment\models.py:315:9
    |
314 |     def __str__(self):
315 |         """String representation for product packaging."""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
316 |         name = self.product.name if hasattr(self.product, "name") else self.product_id
317 |         return f"{_('Packaging for')}: {name}"
    |

E501 Line too long (92 > 90)
   --> shipment\models.py:365:91
    |
363 |                     {
364 |                         "items_per_intermediate": _(
365 |                             "This field is required when intermediate packaging is enabled."
    |                                                                                           ^^
366 |                         )
367 |                     }
    |

E501 Line too long (92 > 90)
   --> shipment\models.py:373:91
    |
371 |                     {
372 |                         "intermediate_package_weight": _(
373 |                             "This field is required when intermediate packaging is enabled."
    |                                                                                           ^^
374 |                         )
375 |                     }
    |

E501 Line too long (103 > 90)
   --> shipment\models.py:378:91
    |
376 |                 )
377 |
378 |             # Checking that the quantity in the intermediate package is less than or equal to the total
    |                                                                                           ^^^^^^^^^^^^^
379 |             if self.items_per_intermediate > self.items_per_package:
380 |                 raise ValidationError(
    |

E501 Line too long (99 > 90)
   --> shipment\models.py:383:91
    |
381 |                     {
382 |                         "items_per_intermediate": _(
383 |                             "Items per intermediate package cannot exceed total items per package."
    |                                                                                           ^^^^^^^^^
384 |                         )
385 |                     }
    |

E501 Line too long (96 > 90)
   --> shipment\models.py:392:91
    |
390 |                 {
391 |                     "items_per_intermediate": _(
392 |                         "Items per package must be divisible by items per intermediate package."
    |                                                                                           ^^^^^^
393 |                     )
394 |                 }
    |

D401 First line of docstring should be in imperative mood: "String representation of the expense invoice item."
   --> shipment\models.py:607:9
    |
606 |     def __str__(self):
607 |         """String representation of the expense invoice item."""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
608 |         product_name = self.product.name if self.product else "No product"
609 |         return f"{self.invoice.invoice} - {product_name} - {self.quantity}"
    |

D401 First line of docstring should be in imperative mood: "Main page of the shipment application."
  --> shipment\views.py:45:5
   |
43 | @login_required
44 | def dashboard(request):
45 |     """Main page of the shipment application."""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
46 |     context = {
47 |         "title": "Shipment Management",
   |

D400 First line should end with a period
   --> shipment\views.py:452:5
    |
450 | # API в'юшки для AJAX запитів
451 | def get_shop_details(request, shop_id):
452 |     """Отримання деталей магазину через AJAX"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
453 |     shop = get_object_or_404(Shop, id=shop_id)
454 |     data = {
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> shipment\views.py:452:5
    |
450 | # API в'юшки для AJAX запитів
451 | def get_shop_details(request, shop_id):
452 |     """Отримання деталей магазину через AJAX"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
453 |     shop = get_object_or_404(Shop, id=shop_id)
454 |     data = {
    |
help: Add closing punctuation

D400 First line should end with a period
   --> shipment\views.py:466:5
    |
465 | def get_product_details(request, product_id):
466 |     """Отримання деталей товару через AJAX"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
467 |     product = get_object_or_404(Product, id=product_id)
468 |     data = {
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> shipment\views.py:466:5
    |
465 | def get_product_details(request, product_id):
466 |     """Отримання деталей товару через AJAX"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
467 |     product = get_object_or_404(Product, id=product_id)
468 |     data = {
    |
help: Add closing punctuation

D400 First line should end with a period
   --> shipment\views.py:479:5
    |
478 | def search_products(request):
479 |     """Пошук товарів через AJAX"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
480 |     query = request.GET.get("q", "")
481 |     if query:
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> shipment\views.py:479:5
    |
478 | def search_products(request):
479 |     """Пошук товарів через AJAX"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
480 |     query = request.GET.get("q", "")
481 |     if query:
    |
help: Add closing punctuation

D400 First line should end with a period
   --> shipment\views.py:501:5
    |
500 | def export_invoices_csv(request):
501 |     """Експорт видаткових накладних у CSV"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
502 |     # Створюємо HTTP-відповідь з типом вмісту CSV
503 |     response = HttpResponse(content_type="text/csv")
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> shipment\views.py:501:5
    |
500 | def export_invoices_csv(request):
501 |     """Експорт видаткових накладних у CSV"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
502 |     # Створюємо HTTP-відповідь з типом вмісту CSV
503 |     response = HttpResponse(content_type="text/csv")
    |
help: Add closing punctuation

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `get_absolute_url` method should come before custom method
   --> transport\models.py:706:5
    |
704 |           }
705 |
706 | /     def get_absolute_url(self):
707 | |         """Return URL to car detail page."""
708 | |         from django.urls import reverse
709 | |
710 | |         return reverse("transport:car_detail", args=[self.car.id])
    | |__________________________________________________________________^
711 |
712 |       def save(self, *args, **kwargs) -> None:
    |

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `save` method should come before custom method
   --> transport\models.py:712:5
    |
710 |           return reverse("transport:car_detail", args=[self.car.id])
711 |
712 | /     def save(self, *args, **kwargs) -> None:
713 | |         """Save method with calculations."""
714 | |         # Calculate fuel consumption (l/100km)
715 | |         if self.mileage > 0 and self.fuel_liters > 0:
716 | |             self.fuel_consumption = (self.fuel_liters / self.mileage) * 100
717 | |         else:
718 | |             self.fuel_consumption = Decimal("0")
719 | |
720 | |         # Total expenses
721 | |         self.total_expenses = (
722 | |             self.fuel_cost
723 | |             + self.repair_cost
724 | |             + self.rent_cost
725 | |             + self.salary_cost
726 | |             + self.insurance
727 | |             + self.washing
728 | |             + self.parking
729 | |             + self.fines
730 | |             + self.other
731 | |         )
732 | |
733 | |         # Cost per km
734 | |         if self.mileage > 0:
735 | |             self.cost_per_km = self.total_expenses / self.mileage
736 | |         else:
737 | |             self.cost_per_km = Decimal("0")
738 | |
739 | |         super().save(*args, **kwargs)
    | |_____________________________________^
    |

F811 [*] Redefinition of unused `render` from line 8
  --> transport\views.py:8:30
   |
 6 | from django.contrib import messages
 7 | from django.contrib.auth.decorators import login_required
 8 | from django.shortcuts import render
   |                              ------ previous definition of `render` here
 9 | from django.core.paginator import Paginator
10 | from django.db.models import Q, Sum
11 | from django.http import HttpResponse, JsonResponse
12 | from django.shortcuts import get_object_or_404, redirect, render
   |                                                           ^^^^^^ `render` redefined here
13 | from django.utils import timezone
   |
help: Remove definition: `render`

D200 One-line docstring should fit on one line
 --> update_ai_context.py:2:1
  |
1 |   #!/usr/bin/env python3
2 | / """
3 | | Скрипт для оновлення AI контексту проекту
4 | | """
  | |___^
5 |
6 |   import os
  |
help: Reformat to one line

D400 First line should end with a period
 --> update_ai_context.py:2:1
  |
1 |   #!/usr/bin/env python3
2 | / """
3 | | Скрипт для оновлення AI контексту проекту
4 | | """
  | |___^
5 |
6 |   import os
  |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
 --> update_ai_context.py:2:1
  |
1 |   #!/usr/bin/env python3
2 | / """
3 | | Скрипт для оновлення AI контексту проекту
4 | | """
  | |___^
5 |
6 |   import os
  |
help: Add closing punctuation

D400 First line should end with a period
  --> update_ai_context.py:13:5
   |
12 | def get_project_info():
13 |     """Збирає інформацію про проект"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
14 |     project_root = Path(__file__).parent
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> update_ai_context.py:13:5
   |
12 | def get_project_info():
13 |     """Збирає інформацію про проект"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
14 |     project_root = Path(__file__).parent
   |
help: Add closing punctuation

UP015 [*] Unnecessary mode argument
  --> update_ai_context.py:63:33
   |
61 |     if req_file.exists():
62 |         try:
63 |             with open(req_file, "r", encoding="utf-8") as f:
   |                                 ^^^
64 |                 lines = f.readlines()
65 |                 # Беремо перші 20 непустих рядків
   |
help: Remove mode argument

UP015 [*] Unnecessary mode argument
  --> update_ai_context.py:88:39
   |
86 |     if env_file_found:
87 |         try:
88 |             with open(env_file_found, "r", encoding="utf-8") as f:
   |                                       ^^^
89 |                 for line in f:
90 |                     line = line.strip()
   |
help: Remove mode argument

D400 First line should end with a period
   --> update_ai_context.py:105:5
    |
104 | def generate_ai_context():
105 |     """Генерує оновлений AI_CONTEXT.md"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
106 |     info = get_project_info()
107 |     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> update_ai_context.py:105:5
    |
104 | def generate_ai_context():
105 |     """Генерує оновлений AI_CONTEXT.md"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
106 |     info = get_project_info()
107 |     now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    |
help: Add closing punctuation

invalid-syntax: Cannot use an escape sequence (backslash) in f-strings on Python 3.11 (syntax was added in Python 3.12)
   --> update_ai_context.py:124:7
    |
123 | ## 📦 КЛЮЧОВІ ЗАЛЕЖНОСТІ
124 |     {"\n".join(info["requirements"][:15])}
    |       ^
125 | ## 🌍 ЗМІННІ СЕРЕДОВИЩА
126 |     {"\n".join(info["env_vars"][:10])}
    |

invalid-syntax: Cannot use an escape sequence (backslash) in f-strings on Python 3.11 (syntax was added in Python 3.12)
   --> update_ai_context.py:126:7
    |
124 |     {"\n".join(info["requirements"][:15])}
125 | ## 🌍 ЗМІННІ СЕРЕДОВИЩА
126 |     {"\n".join(info["env_vars"][:10])}
    |       ^
127 | ## 🎯 СТИЛЬ КОДУ
128 | 1. **Код:** Англійська (змінні, функції, класи)
    |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
 --> warehouse\admin.py:7:20
  |
5 | @admin.register(Warehouse)
6 | class WarehouseAdmin(admin.ModelAdmin):
7 |     list_display = ["name"]
  |                    ^^^^^^^^
8 |     search_fields = ["name"]
  |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
 --> warehouse\admin.py:8:21
  |
6 | class WarehouseAdmin(admin.ModelAdmin):
7 |     list_display = ["name"]
8 |     search_fields = ["name"]
  |                     ^^^^^^^^
  |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:13:20
   |
11 | @admin.register(Category)
12 | class CategoryAdmin(admin.ModelAdmin):
13 |     list_display = ["name"]
   |                    ^^^^^^^^
14 |     search_fields = ["name"]
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:14:21
   |
12 | class CategoryAdmin(admin.ModelAdmin):
13 |     list_display = ["name"]
14 |     search_fields = ["name"]
   |                     ^^^^^^^^
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:19:20
   |
17 | @admin.register(Subcategory)
18 | class SubcategoryAdmin(admin.ModelAdmin):
19 |     list_display = ["name", "category"]
   |                    ^^^^^^^^^^^^^^^^^^^^
20 |     list_filter = ["category"]
21 |     search_fields = ["name", "category__name"]
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:20:19
   |
18 | class SubcategoryAdmin(admin.ModelAdmin):
19 |     list_display = ["name", "category"]
20 |     list_filter = ["category"]
   |                   ^^^^^^^^^^^^
21 |     search_fields = ["name", "category__name"]
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:21:21
   |
19 |     list_display = ["name", "category"]
20 |     list_filter = ["category"]
21 |     search_fields = ["name", "category__name"]
   |                     ^^^^^^^^^^^^^^^^^^^^^^^^^^
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:26:20
   |
24 | @admin.register(CostType)
25 | class CostTypeAdmin(admin.ModelAdmin):
26 |     list_display = ["name"]
   |                    ^^^^^^^^
27 |     search_fields = ["name"]
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:27:21
   |
25 | class CostTypeAdmin(admin.ModelAdmin):
26 |     list_display = ["name"]
27 |     search_fields = ["name"]
   |                     ^^^^^^^^
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:32:20
   |
30 | @admin.register(ExpenseObject)
31 | class ExpenseObjectAdmin(admin.ModelAdmin):
32 |     list_display = ["name", "warehouse", "category", "subcategory", "cost_type"]
   |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
33 |     list_filter = ["warehouse", "category", "cost_type"]
34 |     search_fields = ["name", "warehouse__name"]
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:33:19
   |
31 | class ExpenseObjectAdmin(admin.ModelAdmin):
32 |     list_display = ["name", "warehouse", "category", "subcategory", "cost_type"]
33 |     list_filter = ["warehouse", "category", "cost_type"]
   |                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
34 |     search_fields = ["name", "warehouse__name"]
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\admin.py:34:21
   |
32 |     list_display = ["name", "warehouse", "category", "subcategory", "cost_type"]
33 |     list_filter = ["warehouse", "category", "cost_type"]
34 |     search_fields = ["name", "warehouse__name"]
   |                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |

D400 First line should end with a period
  --> warehouse\forms.py:15:5
   |
14 | class ExpenseRecordStepForm(forms.Form):
15 |     """Спрощена форма з поступовим вибором для додавання витрат"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |
17 |     # Крок 1: Вибір складу
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> warehouse\forms.py:15:5
   |
14 | class ExpenseRecordStepForm(forms.Form):
15 |     """Спрощена форма з поступовим вибором для додавання витрат"""
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
16 |
17 |     # Крок 1: Вибір складу
   |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\forms.py:42:20
   |
40 |     # Крок 5: Дані витрати
41 |     current_year = datetime.datetime.now().year
42 |     YEAR_CHOICES = [(year, year) for year in range(current_year - 2, current_year + 2)]
   |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
43 |
44 |     year = forms.ChoiceField(
   |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\forms.py:103:17
    |
101 |                 return Category.objects.get(id=category_id)
102 |             except Category.DoesNotExist:
103 |                 raise ValidationError("Обрана категорія не існує")
    |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
104 |         return None
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\forms.py:112:17
    |
110 |                 return Subcategory.objects.get(id=subcategory_id)
111 |             except Subcategory.DoesNotExist:
112 |                 raise ValidationError("Обрана підкатегорія не існує")
    |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
113 |         return None
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\forms.py:121:17
    |
119 |                 return ExpenseObject.objects.get(id=expense_object_id)
120 |             except ExpenseObject.DoesNotExist:
121 |                 raise ValidationError("Обраний об'єкт витрат не існує")
    |                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
122 |         return None
    |

D202 [*] No blank lines allowed after function docstring (found 1)
 --> warehouse\management\commands\create_sample_csvs.py:6:5
  |
5 | def create_sample_csvs():
6 |     """Create sample CSV files for each model"""
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7 |
8 |     # Sample Region data
  |
help: Remove blank line(s) after function docstring

D400 First line should end with a period
 --> warehouse\management\commands\create_sample_csvs.py:6:5
  |
5 | def create_sample_csvs():
6 |     """Create sample CSV files for each model"""
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7 |
8 |     # Sample Region data
  |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
 --> warehouse\management\commands\create_sample_csvs.py:6:5
  |
5 | def create_sample_csvs():
6 |     """Create sample CSV files for each model"""
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
7 |
8 |     # Sample Region data
  |
help: Add closing punctuation

F841 Local variable `files` is assigned to but never used
  --> warehouse\management\commands\import_json.py:29:9
   |
27 |         }
28 |
29 |         files = [f for f in os.listdir(dir_path) if f.endswith(".json")]
   |         ^^^^^
30 |
31 |         # Визначаємо черговість (спочатку об'єкти, потім записи)
   |
help: Remove assignment to unused variable `files`

UP015 [*] Unnecessary mode argument
  --> warehouse\management\commands\import_json.py:48:34
   |
46 |             self.stdout.write(f"Обробка файлу: {filename}")
47 |
48 |             with open(file_path, "r", encoding="utf-8") as f:
   |                                  ^^^
49 |                 try:
50 |                     data_wrapper = json.load(f)
   |
help: Remove mode argument

RUF010 [*] Use explicit conversion flag
  --> warehouse\management\commands\import_json.py:78:73
   |
76 |                 except Exception as e:
77 |                     self.stdout.write(
78 |                         self.style.ERROR(f"Помилка у файлі {filename}: {str(e)}")
   |                                                                         ^^^^^^
79 |                     )
   |
help: Replace with conversion flag

E501 Line too long (128 > 90)
  --> warehouse\management\commands\load_csv_data.py:24:91
   |
22 |             "model",
23 |             type=str,
24 |             help="Name of the model to load data into (Region, CategoryShop, Shop, CategoryProduct, Product, ProductPackaging)",
   |                                                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
25 |         )
26 |         parser.add_argument("csv_file", type=str, help="Path to the CSV file")
   |

E501 Line too long (102 > 90)
  --> warehouse\management\commands\load_csv_data.py:64:91
   |
62 |             self.stderr.write(
63 |                 self.style.ERROR(
64 |                     f"Model '{model_name}' not found. Available models: {', '.join(model_map.keys())}"
   |                                                                                           ^^^^^^^^^^^^
65 |                 )
66 |             )
   |

UP015 [*] Unnecessary mode argument
  --> warehouse\management\commands\load_csv_data.py:77:33
   |
76 |         try:
77 |             with open(csv_file, "r", encoding=encoding) as file:
   |                                 ^^^
78 |                 reader = csv.DictReader(file, delimiter=delimiter)
   |
help: Remove mode argument

RUF010 [*] Use explicit conversion flag
  --> warehouse\management\commands\load_csv_data.py:95:68
   |
93 |                         self.stderr.write(
94 |                             self.style.WARNING(
95 |                                 f"Error processing row {row_num}: {str(e)}"
   |                                                                    ^^^^^^
96 |                             )
97 |                         )
   |
help: Replace with conversion flag

E501 Line too long (99 > 90)
   --> warehouse\management\commands\load_csv_data.py:118:91
    |
116 |                         self.stdout.write(
117 |                             self.style.SUCCESS(
118 |                                 f"Successfully created {len(created_objects)} {model_name} objects"
    |                                                                                           ^^^^^^^^^
119 |                             )
120 |                         )
    |

F541 [*] f-string without any placeholders
   --> warehouse\management\commands\load_csv_data.py:125:21
    |
123 |             self.stderr.write(
124 |                 self.style.ERROR(
125 |                     f"Encoding error. Try a different encoding like 'utf-8-sig', 'cp1251', or 'iso-8859-1'"
    |                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
126 |                 )
127 |             )
    |
help: Remove extraneous `f` prefix

E501 Line too long (107 > 90)
   --> warehouse\management\commands\load_csv_data.py:125:91
    |
123 |             self.stderr.write(
124 |                 self.style.ERROR(
125 |                     f"Encoding error. Try a different encoding like 'utf-8-sig', 'cp1251', or 'iso-8859-1'"
    |                                                                                           ^^^^^^^^^^^^^^^^^
126 |                 )
127 |             )
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:129:70
    |
127 |             )
128 |         except Exception as e:
129 |             self.stderr.write(self.style.ERROR(f"Error loading CSV: {str(e)}"))
    |                                                                      ^^^^^^
130 |
131 |     def create_object_from_row(self, model_class, row, row_num):
    |
help: Replace with conversion flag

D202 [*] No blank lines allowed after function docstring (found 1)
   --> warehouse\management\commands\load_csv_data.py:132:9
    |
131 |     def create_object_from_row(self, model_class, row, row_num):
132 |         """Create model object from CSV row based on model type"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
133 |
134 |         # Clean row data - strip whitespace
    |
help: Remove blank line(s) after function docstring

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:132:9
    |
131 |     def create_object_from_row(self, model_class, row, row_num):
132 |         """Create model object from CSV row based on model type"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
133 |
134 |         # Clean row data - strip whitespace
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:132:9
    |
131 |     def create_object_from_row(self, model_class, row, row_num):
132 |         """Create model object from CSV row based on model type"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
133 |
134 |         # Clean row data - strip whitespace
    |
help: Add closing punctuation

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:151:9
    |
150 |     def create_region(self, row, row_num):
151 |         """Create Region object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^
152 |         try:
153 |             return Region(
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:151:9
    |
150 |     def create_region(self, row, row_num):
151 |         """Create Region object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^
152 |         try:
153 |             return Region(
    |
help: Add closing punctuation

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:159:13
    |
157 |             )
158 |         except (ValueError, KeyError) as e:
159 |             raise Exception(f"Invalid Region data in row {row_num}: {str(e)}")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
160 |
161 |     def create_category_shop(self, row, row_num):
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:159:70
    |
157 |             )
158 |         except (ValueError, KeyError) as e:
159 |             raise Exception(f"Invalid Region data in row {row_num}: {str(e)}")
    |                                                                      ^^^^^^
160 |
161 |     def create_category_shop(self, row, row_num):
    |
help: Replace with conversion flag

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:162:9
    |
161 |     def create_category_shop(self, row, row_num):
162 |         """Create CategoryShop object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
163 |         try:
164 |             return CategoryShop(
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:162:9
    |
161 |     def create_category_shop(self, row, row_num):
162 |         """Create CategoryShop object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
163 |         try:
164 |             return CategoryShop(
    |
help: Add closing punctuation

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:170:13
    |
168 |             )
169 |         except (ValueError, KeyError) as e:
170 |             raise Exception(f"Invalid CategoryShop data in row {row_num}: {str(e)}")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
171 |
172 |     def create_shop(self, row, row_num):
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:170:76
    |
168 |             )
169 |         except (ValueError, KeyError) as e:
170 |             raise Exception(f"Invalid CategoryShop data in row {row_num}: {str(e)}")
    |                                                                            ^^^^^^
171 |
172 |     def create_shop(self, row, row_num):
    |
help: Replace with conversion flag

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:173:9
    |
172 |     def create_shop(self, row, row_num):
173 |         """Create Shop object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^
174 |         try:
175 |             # Get related objects
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:173:9
    |
172 |     def create_shop(self, row, row_num):
173 |         """Create Shop object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^
174 |         try:
175 |             # Get related objects
    |
help: Add closing punctuation

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:193:13
    |
191 |             )
192 |         except CategoryShop.DoesNotExist:
193 |             raise Exception(f"CategoryShop with id {category_id} not found")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
194 |         except Region.DoesNotExist:
195 |             raise Exception(f"Region with id {region_id} not found")
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:195:13
    |
193 |             raise Exception(f"CategoryShop with id {category_id} not found")
194 |         except Region.DoesNotExist:
195 |             raise Exception(f"Region with id {region_id} not found")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
196 |         except (ValueError, KeyError) as e:
197 |             raise Exception(f"Invalid Shop data in row {row_num}: {str(e)}")
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:197:13
    |
195 |             raise Exception(f"Region with id {region_id} not found")
196 |         except (ValueError, KeyError) as e:
197 |             raise Exception(f"Invalid Shop data in row {row_num}: {str(e)}")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
198 |
199 |     def create_category_product(self, row, row_num):
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:197:68
    |
195 |             raise Exception(f"Region with id {region_id} not found")
196 |         except (ValueError, KeyError) as e:
197 |             raise Exception(f"Invalid Shop data in row {row_num}: {str(e)}")
    |                                                                    ^^^^^^
198 |
199 |     def create_category_product(self, row, row_num):
    |
help: Replace with conversion flag

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:200:9
    |
199 |     def create_category_product(self, row, row_num):
200 |         """Create CategoryProduct object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
201 |         try:
202 |             parent_id = row.get("parent_id")
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:200:9
    |
199 |     def create_category_product(self, row, row_num):
200 |         """Create CategoryProduct object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
201 |         try:
202 |             parent_id = row.get("parent_id")
    |
help: Add closing punctuation

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:214:13
    |
212 |             )
213 |         except CategoryProduct.DoesNotExist:
214 |             raise Exception(f"Parent CategoryProduct with id {parent_id} not found")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
215 |         except (ValueError, KeyError) as e:
216 |             raise Exception(f"Invalid CategoryProduct data in row {row_num}: {str(e)}")
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:216:13
    |
214 |             raise Exception(f"Parent CategoryProduct with id {parent_id} not found")
215 |         except (ValueError, KeyError) as e:
216 |             raise Exception(f"Invalid CategoryProduct data in row {row_num}: {str(e)}")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
217 |
218 |     def create_product(self, row, row_num):
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:216:79
    |
214 |             raise Exception(f"Parent CategoryProduct with id {parent_id} not found")
215 |         except (ValueError, KeyError) as e:
216 |             raise Exception(f"Invalid CategoryProduct data in row {row_num}: {str(e)}")
    |                                                                               ^^^^^^
217 |
218 |     def create_product(self, row, row_num):
    |
help: Replace with conversion flag

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:219:9
    |
218 |     def create_product(self, row, row_num):
219 |         """Create Product object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
220 |         try:
221 |             category_id = int(row.get("category_id", 0))
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:219:9
    |
218 |     def create_product(self, row, row_num):
219 |         """Create Product object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
220 |         try:
221 |             category_id = int(row.get("category_id", 0))
    |
help: Add closing punctuation

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:247:13
    |
245 |             )
246 |         except CategoryProduct.DoesNotExist:
247 |             raise Exception(f"CategoryProduct with id {category_id} not found")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
248 |         except (ValueError, KeyError) as e:
249 |             raise Exception(f"Invalid Product data in row {row_num}: {str(e)}")
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:249:13
    |
247 |             raise Exception(f"CategoryProduct with id {category_id} not found")
248 |         except (ValueError, KeyError) as e:
249 |             raise Exception(f"Invalid Product data in row {row_num}: {str(e)}")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
250 |
251 |     def create_product_packaging(self, row, row_num):
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:249:71
    |
247 |             raise Exception(f"CategoryProduct with id {category_id} not found")
248 |         except (ValueError, KeyError) as e:
249 |             raise Exception(f"Invalid Product data in row {row_num}: {str(e)}")
    |                                                                       ^^^^^^
250 |
251 |     def create_product_packaging(self, row, row_num):
    |
help: Replace with conversion flag

D400 First line should end with a period
   --> warehouse\management\commands\load_csv_data.py:252:9
    |
251 |     def create_product_packaging(self, row, row_num):
252 |         """Create ProductPackaging object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
253 |         try:
254 |             product_id = int(row.get("product_id", 0))
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\management\commands\load_csv_data.py:252:9
    |
251 |     def create_product_packaging(self, row, row_num):
252 |         """Create ProductPackaging object"""
    |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
253 |         try:
254 |             product_id = int(row.get("product_id", 0))
    |
help: Add closing punctuation

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:264:13
    |
262 |             )
263 |         except Product.DoesNotExist:
264 |             raise Exception(f"Product with id {product_id} not found")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
265 |         except (ValueError, KeyError) as e:
266 |             raise Exception(f"Invalid ProductPackaging data in row {row_num}: {str(e)}")
    |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
   --> warehouse\management\commands\load_csv_data.py:266:13
    |
264 |             raise Exception(f"Product with id {product_id} not found")
265 |         except (ValueError, KeyError) as e:
266 |             raise Exception(f"Invalid ProductPackaging data in row {row_num}: {str(e)}")
    |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |

RUF010 [*] Use explicit conversion flag
   --> warehouse\management\commands\load_csv_data.py:266:80
    |
264 |             raise Exception(f"Product with id {product_id} not found")
265 |         except (ValueError, KeyError) as e:
266 |             raise Exception(f"Invalid ProductPackaging data in row {row_num}: {str(e)}")
    |                                                                                ^^^^^^
    |
help: Replace with conversion flag

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `Meta` class should come before Magic method
  --> warehouse\models.py:12:5
   |
10 |           return self.name
11 |
12 | /     class Meta:
13 | |         verbose_name = "Склад"
14 | |         verbose_name_plural = "Склади"
   | |______________________________________^
   |

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `Meta` class should come before Magic method
  --> warehouse\models.py:23:5
   |
21 |           return self.name
22 |
23 | /     class Meta:
24 | |         verbose_name = "Категорія"
25 | |         verbose_name_plural = "Категорії"
   | |_________________________________________^
   |

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `Meta` class should come before Magic method
  --> warehouse\models.py:37:5
   |
35 |           return f"{self.category} - {self.name}"
36 |
37 | /     class Meta:
38 | |         verbose_name = "Підкатегорія"
39 | |         verbose_name_plural = "Підкатегорії"
   | |____________________________________________^
   |

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `Meta` class should come before Magic method
  --> warehouse\models.py:48:5
   |
46 |           return self.name
47 |
48 | /     class Meta:
49 | |         verbose_name = "Тип витрат"
50 | |         verbose_name_plural = "Типи витрат"
   | |___________________________________________^
   |

DJ012 Order of model's inner classes, methods, and fields does not follow the Django Style Guide: `Meta` class should come before Magic method
  --> warehouse\models.py:71:5
   |
69 |           return f"{self.warehouse} - {self.name}"
70 |
71 | /     class Meta:
72 | |         verbose_name = "Об'єкт витрат"
73 | |         verbose_name_plural = "Об'єкти витрат"
74 | |         unique_together = ["warehouse", "category", "subcategory", "name"]
   | |__________________________________________________________________________^
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\models.py:74:27
   |
72 |         verbose_name = "Об'єкт витрат"
73 |         verbose_name_plural = "Об'єкти витрат"
74 |         unique_together = ["warehouse", "category", "subcategory", "name"]
   |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
  --> warehouse\models.py:78:21
   |
77 |   class ExpenseRecord(models.Model):
78 |       MONTH_CHOICES = [
   |  _____________________^
79 | |         (1, "Січень"),
80 | |         (2, "Лютий"),
81 | |         (3, "Березень"),
82 | |         (4, "Квітень"),
83 | |         (5, "Травень"),
84 | |         (6, "Червень"),
85 | |         (7, "Липень"),
86 | |         (8, "Серпень"),
87 | |         (9, "Вересень"),
88 | |         (10, "Жовтень"),
89 | |         (11, "Листопад"),
90 | |         (12, "Грудень"),
91 | |     ]
   | |_____^
92 |
93 |       expense_object = models.ForeignKey(
   |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> warehouse\models.py:123:27
    |
121 |         verbose_name = "Запис витрат"
122 |         verbose_name_plural = "Записи витрат"
123 |         unique_together = ["expense_object", "year", "month"]
    |                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
124 |         ordering = ["-year", "-month"]
    |

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> warehouse\models.py:124:20
    |
122 |         verbose_name_plural = "Записи витрат"
123 |         unique_together = ["expense_object", "year", "month"]
124 |         ordering = ["-year", "-month"]
    |                    ^^^^^^^^^^^^^^^^^^^
125 |
126 |     def __str__(self):
    |

D400 First line should end with a period
   --> warehouse\models.py:134:5
    |
133 | class FixedExpenseHistory(models.Model):
134 |     """Історія змін фіксованих витрат"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
135 |
136 |     expense_object = models.ForeignKey(
    |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
   --> warehouse\models.py:134:5
    |
133 | class FixedExpenseHistory(models.Model):
134 |     """Історія змін фіксованих витрат"""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
135 |
136 |     expense_object = models.ForeignKey(
    |
help: Add closing punctuation

RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
   --> warehouse\models.py:153:20
    |
151 |         verbose_name = "Історія фіксованих витрат"
152 |         verbose_name_plural = "Історія фіксованих витрат"
153 |         ordering = ["-start_date", "-created_at"]
    |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
154 |
155 |     def __str__(self):
    |

D205 1 blank line required between summary line and description
  --> warehouse\utils.py:7:5
   |
 6 |   def copy_fixed_expenses_to_month(year, month):
 7 | /     """
 8 | |     Автоматичне копіювання фіксованих витрат для вказаного місяця
 9 | |     з урахуванням актуальних сум з історії
10 | |     """
   | |_______^
11 |       from .models import ExpenseRecord, ExpenseObject, FixedExpenseHistory
12 |       import datetime
   |
help: Insert single blank line

D400 First line should end with a period
  --> warehouse\utils.py:7:5
   |
 6 |   def copy_fixed_expenses_to_month(year, month):
 7 | /     """
 8 | |     Автоматичне копіювання фіксованих витрат для вказаного місяця
 9 | |     з урахуванням актуальних сум з історії
10 | |     """
   | |_______^
11 |       from .models import ExpenseRecord, ExpenseObject, FixedExpenseHistory
12 |       import datetime
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> warehouse\utils.py:7:5
   |
 6 |   def copy_fixed_expenses_to_month(year, month):
 7 | /     """
 8 | |     Автоматичне копіювання фіксованих витрат для вказаного місяця
 9 | |     з урахуванням актуальних сум з історії
10 | |     """
   | |_______^
11 |       from .models import ExpenseRecord, ExpenseObject, FixedExpenseHistory
12 |       import datetime
   |
help: Add closing punctuation

E501 Line too long (95 > 90)
  --> warehouse\utils.py:45:91
   |
43 |                 month=month,
44 |                 amount=current_history.amount,
45 |                 comment=f"Автоматично створено. Актуальна сума з {current_history.start_date}",
   |                                                                                           ^^^^^
46 |                 is_auto_generated=True,
47 |             )
   |

D200 One-line docstring should fit on one line
  --> warehouse\utils.py:55:5
   |
54 |   def update_fixed_expense(expense_object, new_amount, start_year, start_month, comment=""):
55 | /     """
56 | |     Оновлення фіксованої витрати з певного місяця
57 | |     """
   | |_______^
58 |       from .models import ExpenseRecord  # Імпорт всередині функції
   |
help: Reformat to one line

D400 First line should end with a period
  --> warehouse\utils.py:55:5
   |
54 |   def update_fixed_expense(expense_object, new_amount, start_year, start_month, comment=""):
55 | /     """
56 | |     Оновлення фіксованої витрати з певного місяця
57 | |     """
   | |_______^
58 |       from .models import ExpenseRecord  # Імпорт всередині функції
   |
help: Add period

D415 First line should end with a period, question mark, or exclamation point
  --> warehouse\utils.py:55:5
   |
54 |   def update_fixed_expense(expense_object, new_amount, start_year, start_month, comment=""):
55 | /     """
56 | |     Оновлення фіксованої витрати з певного місяця
57 | |     """
   | |_______^
58 |       from .models import ExpenseRecord  # Імпорт всередині функції
   |
help: Add closing punctuation

F541 [*] f-string without any placeholders
  --> warehouse\utils.py:67:58
   |
65 |     if current_record:
66 |         current_record.amount = new_amount
67 |         current_record.comment = comment if comment else f"Оновлено фіксовану витрату"
   |                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
68 |         current_record.is_auto_generated = False
69 |         current_record.save()
   |
help: Remove extraneous `f` prefix

F841 Local variable `current_year` is assigned to but never used
  --> warehouse\utils.py:83:5
   |
82 |     # Оновлюємо наступні місяці (якщо вони автоматично згенеровані)
83 |     current_year = datetime.datetime.now().year
   |     ^^^^^^^^^^^^
84 |     current_month = datetime.datetime.now().month
   |
help: Remove assignment to unused variable `current_year`

F841 Local variable `current_month` is assigned to but never used
  --> warehouse\utils.py:84:5
   |
82 |     # Оновлюємо наступні місяці (якщо вони автоматично згенеровані)
83 |     current_year = datetime.datetime.now().year
84 |     current_month = datetime.datetime.now().month
   |     ^^^^^^^^^^^^^
85 |
86 |     future_records = (
   |
help: Remove assignment to unused variable `current_month`

D401 First line of docstring should be in imperative mood: "Fixed expenses management page."
   --> warehouse\views.py:394:5
    |
393 | def fixed_expenses_management(request):
394 |     """Fixed expenses management page."""
    |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
395 |     fixed_objects = ExpenseObject.objects.filter(cost_type__name="Фіксована")
    |

RUF059 Unpacked variable `record` is never used
   --> warehouse\views.py:744:29
    |
742 |                         # Знаходимо або створюємо запис
743 |                         if amount > 0:
744 |                             record, created = ExpenseRecord.objects.update_or_create(
    |                             ^^^^^^
745 |                                 expense_object=obj,
746 |                                 year=year,
    |
help: Prefix it with an underscore or any other dummy variable pattern
