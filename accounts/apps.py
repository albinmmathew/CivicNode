from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
	
    def ready(self):  # When the accounts app starts, load signals.
        import accounts.signals