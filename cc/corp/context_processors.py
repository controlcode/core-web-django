from django.conf import settings


def global_settings(request):
    # return any values required in templates
    return {
        'GOOGLE_ANALYTICS': settings.GOOGLE_ANALYTICS,
    }