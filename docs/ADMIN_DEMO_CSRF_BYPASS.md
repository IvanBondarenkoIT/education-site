# CSRF на Railway (штатный режим)

Временный обход `ADMIN_DEMO_BYPASS_CSRF` **удалён** из проекта: падение деплоя было из‑за **`requirements.txt` в кодировке UTF-16**; после исправления на UTF-8 образ собирается, на Railway работают обычные настройки CSRF.

## Текущая конфигурация (`education_site/settings.py`)

- **`SECURE_PROXY_SSL_HEADER`** — если заданы `RAILWAY_ENVIRONMENT`, `RAILWAY` или `RAILWAY_PUBLIC_DOMAIN` (типичный Railway).
- **`CSRF_TRUSTED_ORIGINS`** — в т.ч. `https://*.railway.app`, `https://*.up.railway.app`, явный URL и опционально `DJANGO_CSRF_TRUSTED_ORIGINS` из Variables.

Дополнительно: ветка деплоя на Railway должна совпадать с веткой, куда пушите фиксы.
