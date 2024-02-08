from django.apps import AppConfig


class UnitTestsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.unit_tests"
    label = "apps_unit_tests"
