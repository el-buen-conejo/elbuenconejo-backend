from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "apps.users"
    # label = "apps_users"

    def ready(self):
        import apps.users.signals

    class Meta:
        verbose_name = "Usuarios"
