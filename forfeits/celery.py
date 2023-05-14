import os
from celery import Celery

# Устанавливаем переменную окружения, указывающую на настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forfeits.settings')
app = Celery('forfeits')

# Загружаем настройки из файла настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи из приложений Django
app.autodiscover_tasks()

# Запускаем Celery Worker
if __name__ == '__main__':
    app.start()
