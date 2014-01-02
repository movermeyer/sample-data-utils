.. include:: globals
.. _cookbook:


CookBook
========

Create user friendly unique sequences:


.. code-block:: python

    >>> from django.contrib.auth.models import User
    >>> from django_dynamic_fixture import G
    >>> from functools import partial
    >>> from sample_data_utils.utils import sequence
    >>> names = partial(sequence, 'Name', cache={})()
    >>> next(names)
    'User-0'
    >>> next(names)
    'User-1'
    >>> next(names)
    'User-2'
    >>> names2 = partial(sequence, 'Name', cache={})()
    >>> next(names2)
    'User-0'
    >>> next(names)
    'User-3'

Get unique country info
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from sample_data_utils import countries

    next(countries)
    next(countries)


Use SDU with django-dynamic-fixtures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create more user friendly DDF names:

.. code-block:: python

    from django.contrib.auth.models import User
    from django_dynamic_fixture import G
    from functools import partial
    from sample_data_utils.utils import sequence

    def user_factory(**kwargs):
        names = partial(sequence, 'User', cache={})()
        kwargs.setdefault('username', lambda x: next(names))

        country = G(User, **kwargs)

    # create superuser
    user_factory(username='admin', is_superuser=True)

    # create 10 users from User-0 to User-9
    user_factory(n=10)

