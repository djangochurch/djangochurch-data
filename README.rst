Django Church Data
==================

Sample content for Django Church sites.


Installation
------------

.. _pip: http://www.pip-installer.org/

Install the package with pip_::

    pip install djangochurch-data

Add ``djangochurch_data`` to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'djangochurch_data',
    )

Run the following commands::

    python manage.py loaddata djangochurch_pages djangochurch_assets djangochurch_events djangochurch_news
    python manage.py djangochurchimages


Images
------

.. _Unsplash: https://unsplash.com/
.. _Creative Commons Zero license: https://unsplash.com/license

All images used in this project are provided by Unsplash_, who provide their
images under a `Creative Commons Zero license`_.
