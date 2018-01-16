Scrapy Random User-Agent
========================

Does your scrapy spider get identified and blocked by servers because
you use the default user-agent or a generic one?

Use this ``random_useragent`` module and set a random user-agent for
every request. 

Installing
----------

Installing it is pretty simple.

.. code-block:: python

    pip install git+https://github.com/cleocn/scrapy-random-useragent.git

Usage
-----

In your ``settings.py`` file, update the ``DOWNLOADER_MIDDLEWARES``
variable like this.

.. code-block:: python

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'random_useragent.RandomUserAgentMiddleware': 400
    }

This disables the default ``UserAgentMiddleware`` and enables the
``RandomUserAgentMiddleware``.

Now all the requests from your crawler will have a random user-agent.
