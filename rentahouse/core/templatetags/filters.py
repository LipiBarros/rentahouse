from django import template


register = template.Library()


@register.filter(is_safe=True)
def add_error_msg_in_label(value):
    errors = ', '.join(value.errors)
    return value.label_tag(attrs={'data-error': errors})


@register.filter(is_safe=True)
def add_validate_invalid_class_in_input(value):
    return value.as_widget(attrs={'class': 'validate invalid'})
