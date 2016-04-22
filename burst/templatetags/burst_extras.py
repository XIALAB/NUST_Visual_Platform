from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    print 'dic=', dictionary
    print 'key=', key
    return dictionary.get(key)
