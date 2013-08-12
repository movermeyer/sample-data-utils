.. include:: globals
.. _index:

==================
Sample Data Utils
==================

Overview
========

.. image:: https://secure.travis-ci.org/saxix/django-sample_data_utils.png?branch=master
   :target: http://travis-ci.org/saxix/sample_data_utils/

.. image:: https://coveralls.io/repos/saxix/sample_data_utils/badge.png
   :target: https://coveralls.io/r/saxix/sample_data_utils


Set of utilities to create consistent and "reasonable" test data.

Sometime is not not possible use fully random generated data, the validation logic
could expects consistent and properly linked data to pass, here is where |app| can help us

These utilities can be used where the validity check of of your code is too restrictive
to be used with full random data generator and or to create demo dataset with



Table Of Contents
=================

.. toctree::
    :maxdepth: 1

    text
    numeric
    geo
    net
    money
    people
    utils
    changes
