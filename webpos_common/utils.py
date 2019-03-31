import pendulum
from django.conf import settings


def get_now() -> pendulum.DateTime:
    return pendulum.now(settings.TIME_ZONE)
