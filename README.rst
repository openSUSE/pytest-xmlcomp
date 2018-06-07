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


A simple plugin for comparing XML files with the pytest framework.
The input XML file is modified with a user-defined function and the result is checked against XPath expressions.

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

pytest-xmlcomp is a plugin for `pytest`, which takes a XML file and transforms it with a user-defined hook named `pytest_xmlcomp_transform_xml`.
Then it takes user-expected XPath expressions from a JSON file and checks if they are available in the transformed XML file.


Requirements
------------

* pytest
* lxml


Installation
------------

You can install `pytest-xmlcomp` via `pip install` from the GitHub repository::

    $ pip install git+https://github.com/openSUSE/pytest-xmlcomp.git@develop


Purpose
-------

Make sure you have:

* a input XML file
* a hook which modifies your input XML file into a 'result' XML file
* a valid JSON file, which contains the XPath expressions you want to check against.


Using Hooks
-----------

Overwite the custom hook ``pytest_xmlcomp_transform_xml`` in ``test/conftest.py`` to modify or transform your input XML file.


Generating XPath Expressions
----------------------------

Define your XPath expressions in a JSON file, which can be found in the data directory.
Example:

* first column: XPath expression
* second column: expected result)

.. code-block:: json

    [   
        ["/doc",        ["<doc>"]],
        ["/doc/foo",    ["<foo>"]],
        ["/doc/bar",    ["<bar>"]]
    ]


Make sure that the JSON file has the same basename as the XML file.
A introduction to the JSON file format can be found here: `www.json.org`.

You can also check if your JSON file adheres to its syntax before running pytest-xmlcomp. Just run::

    $ python3 -m json.tool foo.json
    
Example Setup
--------------

Here is an example for a directory structure:

* ``tests/conftest.py`` (define your custom hook here)
* ``tests/data/foo`` (you can place you input XML file and your JSON file here)

The hook can look like this:

.. code-block:: python
    
    # give the input XML file to the hook with "xmlfile"
    def pytest_xmlcomp_transform_xml(xmlfile):
        """
        Hook for transforming XML
        :param xmlfile: Input XML file which will be modified
        :type xmlfile: str | :class:`py.path.local`
        :returns: The modified XML file.
        """
        #try to get the tree of the XML file
        try:
            tree = etree.parse(source=str(xmlfile))
        except etree.XMLSyntaxError as error:
            print("XML Syntax Error in file %s:\n%s" % (xmlfile, error),
            file=sys.stderr)
        return None
    # --- tree modification here ---
    # return the modified XML tree
    return tree
  
Here is an example for the input XML and the accompanying JSON file:

.. code-block:: xml
    
    <doc>
        <foo/>
        <bar/>
    </doc>
    
.. code-block:: json

    [   
        ["/doc", ["<doc>"]],
        ["/doc/foo", ["<foo>"]],
        ["/doc/bar", ["<bar>"]]
    ]

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
