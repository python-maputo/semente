from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter
def first_word(value):
    list_value = value.split(" ")
    val = ""
    for v in list_value:
        if v != v.lower():
            val = val + v[0]
    return val


@register.filter
def spacing_no(value):
    list_value = value.split(" ")
    val = ""
    for v in list_value:
        val = val + v
    return val


@register.filter
def money_format(value):
    money = round(float(value), 2)
    return "$%s%s" % (intcomma(int(money)), ("%0.2f" % money)[-3:])
