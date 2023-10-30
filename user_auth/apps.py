from django.apps import AppConfig

class UserAuthConfig(AppConfig):
    """
    AppConfig class for the 'user_auth' app.

    This class represents the configuration for the 'user_auth' app. It defines app-specific settings
    and configurations, such as the default auto field and the app's name.

    Attributes:
        default_auto_field (str): The name of the default auto field for models in the app.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_auth'
