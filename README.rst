==============
pytest-xmlcomp
==============

Version: 0.3.0

.. image:: https://img.shields.io/pypi/v/pytest-xmlcomp.svg
    :target: https://pypi.org/project/pytest-xmlcomp
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-xmlcomp.svg
    :target: https://pypi.org/project/pytest-xmlcomp
    :alt: Python versions

.. image:: https://travis-ci.org/openSUSE/pytest-xmlcomp.svg?branch=develop
    :target: https://travis-ci.org/openSUSE/pytest-xmlcomp
    :alt: See Build Status on Travis CI


.. Hmn, I think this is a bit too vague.

.. A simple plugin comparing XML files against XPath expressions.
   -OR-
   pytest-xmlcomp is a plugin for testing XML files with the pytest framework.
   The input XML file is transformed and the result is checked against XPath expressions.


A simple plugin comparing XML files. Work in progress.

----

.. Maybe move this paragraph into the one of the following sections.

pytest-xmlcomp is a plugin for `pytest`, which takes a XML file and modifies it with a user-defined function in a hook.
Then it takes user-expected XPath expressions from a JSON file and checks if they are available in the modified XML file.

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

.. I think, this is a bit misleading. Although you have two XML files
   (input and result), you compare only the result file against your XPath expressions.
   => Better rephrase it so it is clear what you mean

- compares two XML files based on XPath expressions
- XPath expressions can be retrieved from a JSON file


Requirements
------------

.. The following list isn't really correct. You need all the requirements
   if you *develop* the plugin, but not to actually run/use it.
   Remove everything after lxml.

* pytest
* lxml
* tox
* bumpversion
* check-manifest
* flake8
* isort
* wheel


Installation
------------

You can install `pytest-xmlcomp` via `pip install` from the GitHub repository::

    $ pip install git+https://github.com/openSUSE/pytest-xmlcomp.git@develop


Purpose
-------

.. It would be helpful, if you make a list what you need. Maybe something like this:
   Make sure you have:
   * a input XML file
   * a hook which modifies/transforms your XML file into another XML file ("result XML")
   * a JSON file which contains XPath expressions you want to check against your result XML.
   All the requirements are explained in the following sections.

First of all ensure, that you have an input XML file, a hook which modifies your input XML file and a valid JSON file, which contains the XPath
expressions you want to check. 


Hooks
-----

.. I have some issues:
   1. Well, actually you can't define your own hook in pytest_xmlcomp/hooks.py.
      You need to define it in conftest.py
   2. "will be called", better use "is called" or "pytest calls ..."
   3. Remove "in order to..."

In pytest_xmlcomp/hooks.py, you can define a custom hook, which will be called in order to modify your XML input file.
This is absolutely important in order to run pytest-xmlcomp properly.


Generating XPath Expressions
----------------------------

.. Replace "You can define..." with "Define your XPath..."

You can define the XPath expressions in a JSON file, which can be found in the data directory.

.. Don't say "please". :) You only say that, if you want something from
   your readers. Start with "Make sure..."
   Maybe add an example.

Please make sure that the JSON file has the same basename as the XML file.
A introduction to the JSON file format can be found here: `www.json.org`_

.. You can't "validate" a JSON file, you can only check if it adheres
   to its syntax.

You can also validate your JSON file before running pytest-xmlcomp. Just run::

    $ python3 -m json.tool foo.json


.. I would suggest to add an example *how* you can integrate it into your own project


Contributing
------------

Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `GNU GPL v3.0`_ license, "pytest-xmlcomp" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/Lightlace/pytest-xmlcomp/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
