"""
Временные middleware для отладки/демо. Не использовать в продакшене без крайней необходимости.
"""
import os


class AdminDemoBypassCsrfMiddleware:
    """
    ТОЛЬКО ДЛЯ КРАТКОВРЕМЕННОГО ДЕМО.

    Если задана переменная окружения ADMIN_DEMO_BYPASS_CSRF=1, отключает проверку CSRF
    для POST на страницу входа в админку (/admin/login/).

    Django проверяет request._dont_enforce_csrf_checks в CsrfViewMiddleware ДО проверки
    Origin/Referer — поэтому это обходит и 403 «Origin checking failed».

    После демо: удалить переменную из Railway и этот middleware из MIDDLEWARE (или оставить
    middleware — без переменной он ничего не делает).

    Риск: любой может отправить POST на /admin/login/ без CSRF-токена, пока флаг включён.
    Усильте пароль админа и отключите флаг сразу после показа.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self._should_bypass(request):
            request._dont_enforce_csrf_checks = True
        return self.get_response(request)

    def _should_bypass(self, request):
        if os.environ.get("ADMIN_DEMO_BYPASS_CSRF", "").strip() not in ("1", "true", "yes"):
            return False
        if request.method != "POST":
            return False
        path = request.path.rstrip("/")
        return path.endswith("/admin/login")
