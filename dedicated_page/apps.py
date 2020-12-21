from django.apps import AppConfig

class DedicatedPageConfig(AppConfig):
    name = 'dedicated_page'

    def ready(self):
        import dedicated_page.signals