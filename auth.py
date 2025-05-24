"""
Модуль для работы с аутентификацией пользователей.
Предоставляет функции регистрации и входа в систему.
"""

from typing import Dict, Tuple


# Хранилище пользователей (в реальном приложении следует использовать базу данных)
_users: Dict[str, str] = {}


def register_user(username: str, password: str) -> Tuple[bool, str]:
    """
    Регистрирует нового пользователя в системе.

    Args:
        username: Имя пользователя для регистрации
        password: Пароль пользователя

    Returns:
        Кортеж (успешность операции, сообщение)
    """
    if not username or not password:
        return False, "Имя пользователя и пароль не могут быть пустыми"

    if len(username) < 3:
        return False, "Имя пользователя должно быть не менее 3 символов"

    if len(password) < 6:
        return False, "Пароль должен быть не менее 6 символов"

    if username in _users:
        return False, "Пользователь с таким именем уже существует"

    _users[username] = password
    return True, "Пользователь успешно зарегистрирован"


def login(username: str, password: str) -> Tuple[bool, str]:
    """
    Проверяет учетные данные пользователя.

    Args:
        username: Имя пользователя
        password: Пароль пользователя

    Returns:
        Кортеж (успешность аутентификации, сообщение)
    """
    if not username or not password:
        return False, "Имя пользователя и пароль не могут быть пустыми"

    if username not in _users:
        return False, "Пользователь не найден"

    if _users[username] != password:
        return False, "Неверный пароль"

    return True, "Аутентификация прошла успешно"


def get_user_count() -> int:
    """Возвращает количество зарегистрированных пользователей. Используется для тестирования."""
    return len(_users)


def clear_users():
    """Очищает хранилище пользователей. Используется для тестирования."""
    global _users
    _users = {}