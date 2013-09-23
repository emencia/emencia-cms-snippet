.. _DjangoCMS: https://www.django-cms.org
.. _djangocodemirror: https://github.com/sveetch/djangocodemirror

snippet
=======

This is a "cms.plugins.snippet" (from djangocms) cloned to extend it with some facilities.

Original code is from the original `DjangoCMS`_ plugin.

Changes from original code
--------------------------

This clone try to change as few orignal code as possible, actually the differences are :

* Adding a template tag to directly use snippet fragments in the templates, not only from CMS pages;
* Add usage of `djangocodemirror`_ for the HTML editor;

Requires
--------

* `DjangoCMS`_ version >= 2.3 (tested with 2.3.6) (should not work with >= 3.x);
* `djangocodemirror`_ 0.9.x;

In the admin, the HTML content will be edited with the `djangocodemirror`_ editor.

Install
-------

The only thing needed is to replace the ``cms.plugins.snippet`` in your `DjangoCMS`_ settings, like this : ::

    INSTALLED_APPS = (
        'cms',
        # Plugins
        ...
        #'cms.plugins.snippet',
        'snippet', # the snippet plugin clone
        'djangocodemirror', # the editor
        ...
    )

Then add : ::

    CODEMIRROR_SETTINGS = {
        'cms_snippet': {
            'mode': {'name': "jinja2", 'htmlMode': True},
            'lineWrapping': True,
            'lineNumbers': True,
            'search_enabled': True,
            'embed_settings': True,
            'add_jquery': True,
            'lib_buttons_path': 'djangocodemirror/snippet_buttons.js',
        },
    }


Because the code is cloned from the original plugin with just a few changes, all CMS stuff should work as with the original plugin, you should even add it in an existing install without loss in database and without any syncdb.

Usage
-----

Template tags
.............

Use the template tags in your templates : ::

    {% load snippet_tags %}
    {% snippet_fragment [Snippet ID or instance] %}

Like this : ::

    {% load snippet_tags %}
    {% snippet_fragment 42 %}
    
The required argument is for the Snippet ID or a Snippet instance if you want.
