easy-parallel
=============

Parallel wrapper for easy multi-threading.

Installation
------------

From package root, run:

.. code-block:: console

    $ make requirements

Usage
-----

In python session:

.. code-block:: python

    def foo(x, y):
      return x + y

    num_threads = 10
    inputs = [(x * x, x) for x in range(10)]

    import parallel as par
    results = par.submit_jobs(foo, inputs, num_threads)
    print results
