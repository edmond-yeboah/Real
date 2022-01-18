from django.apps import AppConfig


class BossConfig(AppConfig):
    name = 'boss'

    def ready(self):
        import boss.signals

