smb3-router
==============

.. image:: https://badge.fury.io/py/smb3-router.png
    :target: https://badge.fury.io/py/smb3-router

.. image:: https://travis-ci.org/narfman0/smb3-router.png?branch=master
    :target: https://travis-ci.org/narfman0/smb3-router

Create a DAG for smb3 for use with routing

Installation
------------

Install via pip::

    pip install smb3-router

Development
-----------

Run test suite to ensure everything works::

    make test

Release
-------

To publish your plugin to pypi, sdist and wheels are registered, created and uploaded with::

    make release-test

For test. After ensuring the package works, run the prod target and win::

    make release-prod

License
-------

Copyright (c) 2021 Jon Robison

See LICENSE for details
