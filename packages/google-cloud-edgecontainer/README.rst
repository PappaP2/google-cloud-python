Python Client for Distributed Cloud Edge Container
==================================================

|preview| |pypi| |versions|

`Distributed Cloud Edge Container`_: Google Distributed Cloud Edge allows you to run Kubernetes clusters on dedicated hardware provided and maintained by Google that is separate from the Google Cloud data center.

- `Client Library Documentation`_
- `Product Documentation`_

.. |preview| image:: https://img.shields.io/badge/support-preview-orange.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-edgecontainer.svg
   :target: https://pypi.org/project/google-cloud-edgecontainer/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-edgecontainer.svg
   :target: https://pypi.org/project/google-cloud-edgecontainer/
.. _Distributed Cloud Edge Container: https://cloud.google.com/distributed-cloud/edge
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/edgecontainer/latest
.. _Product Documentation:  https://cloud.google.com/distributed-cloud/edge

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Distributed Cloud Edge Container.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Distributed Cloud Edge Container.:  https://cloud.google.com/distributed-cloud/edge
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Code samples and snippets
~~~~~~~~~~~~~~~~~~~~~~~~~

Code samples and snippets live in the `samples/` folder.


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Our client libraries are compatible with all current `active`_ and `maintenance`_ versions of
Python.

Python >= 3.7

.. _active: https://devguide.python.org/devcycle/#in-development-main-branch
.. _maintenance: https://devguide.python.org/devcycle/#maintenance-branches

Unsupported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.6

If you are using an `end-of-life`_
version of Python, we recommend that you update as soon as possible to an actively supported version.

.. _end-of-life: https://devguide.python.org/devcycle/#end-of-life-branches

Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-edgecontainer


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-edgecontainer

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Distributed Cloud Edge Container
   to see other available methods on the client.
-  Read the `Distributed Cloud Edge Container Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Distributed Cloud Edge Container Product documentation:  https://cloud.google.com/distributed-cloud/edge
.. _README: https://github.com/googleapis/google-cloud-python/blob/main/README.rst
