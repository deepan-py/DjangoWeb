from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all the 'arg' from string
    """
    return value.replace(arg,'')

# we can also use decorators
# this a one way of registering template tag
# register.filter('cut',cut)
