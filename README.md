# turklang-datatables

## Description

This is a Django app using Django REST Framework and Datatables.js for [Turkic morpheme](http://modmorph.turklang.net/ru/) pivot tables.

## Native Application Development

* Install [Python](https://www.python.org/downloads/)

Running Django applications has been simplified with a `manage.py` file to avoid dealing with configuring environment variables to run your app. From your project root, you can download the project dependencies with:

```bash
pipenv install
```

Then, activate this app's virtualenv:

```bash
pipenv shell
```

To run your application locally, run this inside the virtualenv:

```bash
python manage.py runserver
```

![Example of datatable](/example-datatable.png)
