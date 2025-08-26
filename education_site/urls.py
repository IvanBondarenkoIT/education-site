"""
URL configuration for education_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.views import page_not_found, server_error, permission_denied, bad_request

# Настройка обработчиков ошибок
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'
handler400 = 'core.views.bad_request'

# URL patterns для всех языков
urlpatterns = i18n_patterns(
    # Главная страница и основные страницы сайта
    path('', include('core.urls')),
    
    # Админка
    path('admin/', admin.site.urls),
    
    # Префикс для каждого языка
    prefix_default_language=False,
)

# URL patterns без языкового префикса
urlpatterns += [
    # Статические файлы в режиме разработки
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

# Добавляем отладочные URL в режиме разработки
if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
    except ImportError:
        pass
