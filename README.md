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

**The get_queryset() method**

`get_queryset(self)` returns the queryset that should be used for list views, and that should be used as the base for lookups in detail views. Defaults to returning the queryset specified by the `queryset` attribute.

This method should always be used rather than accessing `self.queryset` directly, as `self.queryset` gets evaluated only once, and those results are cached for all subsequent requests.

May be overridden to provide dynamic behavior, such as returning a queryset, that is specific to the user making the request.

https://www.django-rest-framework.org/api-guide/generic-views/#methods

---

**Django InlineModelAdmin**

The admin interface has the ability to edit models on the same page as a parent model. These are called inlines.

https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.InlineModelAdmin

---

**Writing and Running Tests**

Django’s unit tests use a Python standard library module: `unittest`. This module defines tests using a class-based approach.
When you run your tests, the default behavior of the test utility is to find all the test case classes (that is, subclasses of `unittest.TestCase`) in any file whose name begins with `test`, automatically build a test suite out of those test case classes, and run that suite.

Once you’ve written tests, run them using the `test` command of your project’s `manage.py` utility:

```script
$ ./manage.py test
```

https://docs.djangoproject.com/en/5.1/topics/testing/overview/

---

**REST framework Class-based Views**

REST framework provides an `APIView` class, which subclasses Django's `View` class.
- Requests passed to the handler methods will be REST framework's `Request` instances, not Django's `HttpRequest` instances.
- Handler methods may return REST framework's `Response`, instead of Django's `HttpResponse`. The view will manage content negotiation and setting the correct renderer on the response.
- Any `APIException` exceptions will be caught and mediated into appropriate responses.
- Incoming requests will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.

https://www.django-rest-framework.org/api-guide/views/

---

**DRF ListCreateAPIView**

Used for read-write endpoints to represent a collection of model instances. Provides `get` and `post` method handlers.

Extends: `GenericAPIView`, `ListModelMixin`, `CreateModelMixin`

https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview

https://www.cdrf.co/3.14/rest_framework.generics/ListCreateAPIView.html

---

**Overview of access restriction methods**

REST framework offers three different methods to customize access restrictions on a case-by-case basis. These apply in different scenarios and have different effects and limitations.

- `queryset` / `get_queryset()`: Limits the general visibility of existing objects from the database. The queryset limits which objects will be listed and which objects can be modified or deleted. The `get_queryset()` method can apply different querysets based on the current action.
- `permission_classes` / `get_permissions()`: General permission checks based on the current action, request and targeted object. Object level permissions can only be applied to retrieve, modify and deletion actions. Permission checks for list and create will be applied to the entire object type. (In case of list: subject to restrictions in the queryset.)
- `serializer_class` / `get_serializer()`: Instance level restrictions that apply to all objects on input and output. The serializer may have access to the request context. The `get_serializer()` method can apply different serializers based on the current action.

https://www.django-rest-framework.org/api-guide/permissions/#overview-of-access-restriction-methods

---

**Simple JSON Web Token Authentication**

Simple JWT provides a `JSON` Web Token authentication backend for the `Django REST Framework`. It aims to cover the most common use cases of JWTs by offering a conservative set of default features. It also aims to be easily extensible in case a desired feature is not present.

Install via the package manager:
```script
$ pip install djangorestframework-simplejwt
```

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html

---

**RetrieveUpdateDestroyAPIView**

Used for **read-write-delete** endpoints to represent **a single model instance**.

Provides `get`, `put`, `patch` and `delete` method handlers.

Extends: `GenericAPIView`, `RetrieveModelMixin`, `UpdateModelMixin`, `DestroyModelMixin`

https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview

---

**DRF Spectacular**

**drf-spectacular** is an **OpenAPI 3** schema generation library with explicit focus on extensibility, customizability and client generation. It is the recommended way for generating and presenting OpenAPI schemas.

drf-spectacular has 3 goals:
- Extract as much schema information from DRF as possible.

- Provide flexibility to make the schema usable in the real world (not only toy examples).

- Generate a schema that works well with the most popular client generators.

Install drf-spectacular:
```script
$ pip install drf-spectacular
```

Generate schema:
```script
$ ./manage.py spectacular --color --file schema.yml
```

https://drf-spectacular.readthedocs.io/en/latest/readme.html#installation

---

**DRF Filtering & django-filter**

The `django-filter` library includes a `DjangoFilterBackend` class which supports highly customizable field filtering for REST framework.

To use `DjangoFilterBackend`, first install `django-filter`.

```script
$ pip install django-filter
```
https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering

https://django-filter.readthedocs.io/en/stable/guide/usage.html

```script
GET /products/?name__iexact=watch
```

---

**DRF SearchFilter**

The `SearchFilter` class supports simple single query parameter based searching, and is based on the Django admin's search functionality.

The `SearchFilter` class will only be applied if the view has a `search_fields` attribute set. The `search_fields` attribute should be a list of names of text type fields on the model, such as `CharField` or `TextField`.

```python
from rest_framework import filters

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
```

This will allow the client to filter the items in the list by making queries such as:

```
http://example.com/api/users?search=russell
```

https://www.django-rest-framework.org/api-guide/filtering/#searchfilter

---

**Custom Generic Filter**

You can provide your own generic filtering backend, or write an installable app for other developers to use.

To do so override `BaseFilterBackend`, and override the `.filter_queryset(self, request, queryset, view)` method. The method should return a new, filtered queryset.

As well as allowing clients to perform searches and filtering, generic filter backends can be useful for restricting which objects should be visible to any given request or user.

You might want to restrict users to only being able to see objects they created:
```python
class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
```

https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering

---

**Pagination**

REST framework includes support for customizable pagination styles. This allows you to modify how large result sets are split into individual pages of data.

Pagination is only performed automatically if you're using the generic views or viewsets. If you're using a regular `APIView`, you'll need to call into the pagination API yourself to ensure you return a paginated response. 

Pagination can be turned off by setting the pagination class to `None`.

The pagination style may be set globally, using the `DEFAULT_PAGINATION_CLASS` and `PAGE_SIZE` setting keys. For example, to use the built-in limit/offset pagination, you would do something like this:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```

https://www.django-rest-framework.org/api-guide/pagination/

---

**DRF Viewsets**

A `ViewSet` class is simply a type of class-based View, that does not provide any method handlers such as `.get()` or `.post()`, and instead provides actions such as `.list()` and `.create()`.

The method handlers for a `ViewSet` are only bound to the corresponding actions at the point of finalizing the view, using the `.as_view()` method.

Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a *router class*, that automatically determines the urlconf for you.

```python
from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
```

There are two main advantages of using a `ViewSet` class over using a `View` class.

- Repeated logic can be combined into a single class. We only need to specify the queryset once, and it'll be used across multiple views.
- By using routers, we no longer need to deal with wiring up the URL conf ourselves.

https://www.django-rest-framework.org/api-guide/viewsets/

---

**Mark Extra Actions for Routing**

If you have ad-hoc methods that should be routable, you can mark them as such with the `@action` decorator. Like regular actions, extra actions may be intended for either a single object, or an entire collection. To indicate this, set the `detail` argument to `True` or `False`. The router will configure its URL patterns accordingly. e.g., the `DefaultRouter` will configure detail actions to contain `pk` in their URL patterns.

The `action` decorator will route `GET` requests by default, but may also accept other HTTP methods by setting the `methods` argument. For example:

```python
 @action(detail=True, methods=['post', 'delete'])
    def unset_password(self, request, pk=None):
       ...
```

https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing

---

**Additional keyword arguments**

There is a shortcut allowing you to specify arbitrary additional keyword arguments on fields, using the `extra_kwargs` option. As in the case of `read_only_fields`, this means you do not need to explicitly declare the field on the serializer.

This option is a dictionary, mapping field names to a dictionary of keyword arguments. For example:
```python
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
```

If the field has already been explicitly declared on the serializer class, then the `extra_kwargs` option will be ignored.

https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments

---

**Writing .update() methods for nested representations**

For updates you'll want to think carefully about how to handle updates to relationships. For example if the data for the relationship is `None`, or not provided, which of the following should occur?

- Set the relationship to `NULL` in the database.
- Delete the associated instance.
- Ignore the data and leave the instance as it is.
- Raise a validation error.

Because the behavior of nested creates & updates can be ambiguous, and may require complex dependencies between related models, REST framework 3 requires you to always write these methods explicitly. The default `ModelSerializer` `.create()` and `.update()` methods do not include support for writable nested representations.

https://www.django-rest-framework.org/api-guide/serializers/#writing-update-methods-for-nested-representations

---

**Django TestCase class**

This is the most common class to use for writing tests in Django. It inherits from `TransactionTestCase` (and by extension `SimpleTestCase`). If your Django application doesn’t use a database, use `SimpleTestCase`.

The class:

- Wraps the tests within two nested `atomic()` blocks: one for the whole class and one for each test. Therefore, if you want to test some specific database transaction behavior, use `TransactionTestCase`.

- Checks deferrable database constraints at the end of each test.

Classmethod `TestCase.setUpTestData()`. The class-level `atomic` block described above allows the creation of initial data at the class level, once for the whole `TestCase`. This technique allows for faster tests as compared to using `setUp()`.

https://docs.djangoproject.com/en/5.1/topics/testing/tools/#django.test.TestCase

---

**Caching with Redis and Django**

To cache something is to save the result of an expensive calculation so that you don’t have to perform the calculation next time.

Redis is an in-memory database that can be used for caching. To begin you’ll need a Redis server running either locally or on a remote machine.

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
```

https://docs.djangoproject.com/en/5.1/topics/cache/

https://github.com/jazzband/django-redis

Django provides a `method_decorator` to use decorators with class based views. This can be used with other cache decorators such as `cache_page`, `vary_on_cookie` and `vary_on_headers`.

https://www.django-rest-framework.org/api-guide/caching/

---
