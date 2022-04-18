from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _

import re

class PasswordValidator:
    def __init__(self, min_digits=10):
        self.min_digits = min_digits

    def validate(self, password, user=None):
        if not len(re.findall('\d', password)) >= self.min_digits:
            raise ValidationError(
                _("The password must contain at least %(min_digits)d digit(s), 0-9."),
                code='password_no_number',
                params={'min_digits': self.min_digits},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_digits)d digit(s), 0-9." % {'min_digits': self.min_digits}
        )

def validate_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        raise ValidationError(
            _('CPF inválido, o CPF deve conter 11 numeros.'),
            params={'cpf': cpf},
        )

    firts_nine_of_cpf = cpf[:-2]
    reverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(firts_nine_of_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            firts_nine_of_cpf += str(d)

    sequence = firts_nine_of_cpf == str(firts_nine_of_cpf[0]) * len(cpf)

    if cpf != firts_nine_of_cpf or sequence:
        raise ValidationError(
            _('%(cpf)s não e um CPF válido.'),
            params={'cpf': cpf},
        )
