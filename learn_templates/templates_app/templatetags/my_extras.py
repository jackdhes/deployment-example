
##  CUSTOM TEMPLATE TAGS  ##

from django import template

register = template.Library()

# Note these functions ALWAYS take in the 'value' parameter, as they have to take
# in the value being fed to the html file...
@register.filter(name='cutter')
def cut(value,arg):
    # Cuts out all values of 'arg' from the string
    return value.replace(arg,'WOOOW')

# register.filter('cutter',cut)
# Registering the filter function, we give it a name 'cutter' which is what we
# reference when using the function. Followed by the function its self^^^
