# -*- coding: utf-8 -*-
"""
Common templates tags for porticus
"""
from django import template
from django.utils.safestring import mark_safe

from cms.plugins.snippet.models import Snippet

register = template.Library()

class SnippetFragment(template.Node):
    """
    Get a snippet HTML fragment
    """
    def __init__(self, snippet_id_varname):
        """
        :type insert_instance_varname: string or object ``django.db.models.Model``
        :param insert_instance_varname: Instance variable name or a string slug
        """
        self.snippet_id_varname = template.Variable(snippet_id_varname)
    
    def render(self, context):
        """
        :type context: object ``django.template.Context``
        :param context: Context tag object
        
        :rtype: string
        :return: the HTML for the snippet
        """
        # Default assume this is directly an instance
        snippet_instance = self.snippet_id_varname.resolve(context)
        # Assume this is slug
        if isinstance(snippet_instance, basestring) or isinstance(snippet_instance, int):
            snippet_instance = Snippet.objects.get(pk=snippet_instance)
        
        return mark_safe( self.get_content_render(context, snippet_instance) )

    def get_content_render(self, context, instance):
        """
        Render the snippet HTML, using a template if defined in its instance
        """
        context.update({
            'object': instance,
        })
        try:
            if instance.template:
                t = template.loader.get_template(instance.template)
                context.update({'html': mark_safe(instance.html)})
                content = t.render(template.Context(context))
            else:
                t = template.Template(instance.html)
                content = t.render(template.Context(context))
        except template.TemplateDoesNotExist, e:
            content = _('Template %(template)s does not exist.') % {'template': instance.template}
        except Exception, e:
            content = str(e)
        return content

@register.tag(name="snippet_fragment")
def do_snippet_fragment(parser, token):
    """
    Display a snippet HTML fragment
    
    Usage : ::
    
        {% snippet_fragment [Snippet ID or instance] %}
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError, "You need to specify at less an \"Snippet\" ID or instance"
    else:
        return SnippetFragment(*args[1:])

do_snippet_fragment.is_safe = True
