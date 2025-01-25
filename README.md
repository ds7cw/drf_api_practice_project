# drf_api_practice_project

**Django Custom Management Commands**

To execute the `populate_db.py` script:
```bash
python manage.py populate_db
```
https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/

---
**Django UML Diagrams**

To create a class diagram based on the models from the `api` app and save the graphs into `models.dot` file:
```bash
python manage.py graph_models api > models.dot
```
https://django-extensions.readthedocs.io/en/latest/graph_models.html

---
**Django REST Framework Formats**

By default, the API will return the format specified by the headers, which in the case of the browser is HTML. The format can be specified using `?format=` in the request, so you can look at the raw JSON response in a browser by adding `?format=json` to the URL.

https://www.django-rest-framework.org/topics/browsable-api/#formats

---

**Django Silk**

Silk is a *live* profiling and *inspection tool* for the Django framework. Silk intercepts and *stores HTTP requests and database queries* before presenting them in a user interface for further inspection.

https://pypi.org/project/django-silk/

---

**prefetch_related**

`prefetch_related` is designed to stop the deluge of database queries that is caused by accessing related objects. It returns a `QuerySet` that will automatically retrieve, in a single batch, related objects for each of the specified lookups.

`prefetch_related` does a separate lookup for each relationship, and does the ‘joining’ in Python. This allows it to prefetch many-to-many, many-to-one, and `GenericRelation` objects which cannot be done using `select_related`, in addition to the foreign key and one-to-one relationships that are supported by select_related.

https://docs.djangoproject.com/en/5.1/ref/models/querysets/#prefetch-related

---

**DRF Generic Views**

The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.

```python
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

https://www.django-rest-framework.org/api-guide/generic-views/#generic-views

---
