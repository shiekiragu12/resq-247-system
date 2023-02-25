from django import template
import json
from datetime import date
from django.utils import timezone

from django.urls import reverse
from django.utils.text import slugify

from facilities.serializers import ConditionSerializer

register = template.Library()


@register.filter
def to_json(obj, target):
    serializer = None
    if target == 'condition':
        serializer = ConditionSerializer(obj, many=False)
    return json.dumps(serializer.data if serializer else serializer)


@register.filter
def get_full_url(url_name):
    return reverse(url_name)


@register.filter
def get_first_letter(username):
    if username:
        return username[0:1]
    return 'N/A'


@register.filter
def calculate_age(date_of_birth):
    today = timezone.now().date()
    if date_of_birth:
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age
    return "N/A"


@register.filter
def get_range(count):
    return range(0, count)


@register.filter
def custom_slugify(text):
    return slugify(text)
