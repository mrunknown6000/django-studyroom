from django import template

register = template.Library()

@register.simple_tag
def callFunction(functionName, arguments=None):
	exec(f'base.views.{functionName}({arguments})')