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
* Add a slug field;

Requires
--------

* Django 1.4 to 1.6;
* `DjangoCMS`_ version 2.3.6 to 3.0.x;
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
    {% snippet_fragment [Snippet ID or slug or instance] %}

Like this : ::

    {% load snippet_tags %}
    {% snippet_fragment 42 %}

Or with the slug : ::

    {% load snippet_tags %}
    {% snippet_fragment 'my-snippet' %}
    
The first argument is required, you can use either 

* The Snippet ID;
* The Snippet slug;
* The Snippet instance.

Use as a template block with fallback : ::

    {% snippet_fragment 'my-snippet' or %}
        ... clumsy safe ...
    {% endsnippet_fragment %}

In case there is no snippet instance/id/slug, fallback template will be rendered.
