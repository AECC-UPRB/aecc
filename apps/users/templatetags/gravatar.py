from django import template
from django.conf import settings

import urllib
import hashlib

register = template.Library()


@register.filter(name='gravatar_url')
def gravatar_url(instance, email):
    size = 40
    hash = hashlib.md5(email.lower()).hexdigest()
    params = urllib.urlencode({'d': "identicon", 's': str(size)})

    return "{}://www.gravatar.com/avatar/{}?".format(
        settings.PROTOCOL, hash, params)
