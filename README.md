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
