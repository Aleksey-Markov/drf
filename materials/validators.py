from rest_framework.exceptions import ValidationError
import re


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('\Byoutube\B')

        tmp_val = dict(value).get(self.field)
        if not tmp_val:
            return

        first_match = re.search('youtube.com', tmp_val)

        if not first_match:
            raise ValidationError(f"Ошибка! Допустимы ссылки только на YouTube.")
