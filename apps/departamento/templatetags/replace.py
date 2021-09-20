from django import template
register = template.Library()

@register.filter
def replaceCod(value):
    return value.replace("Cod","Codigo")