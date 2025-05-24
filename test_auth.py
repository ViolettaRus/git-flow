from auth import clear_users, get_user_count, login, register_user


class TestAuthModule:
    """Тесты для модуля аутентификации."""

    def setup_method(self, method):
        """Очистка данных перед каждым тестом."""
        clear_users()

    def test_register_user_success(self):
        """Тест успешной регистрации пользователя."""
        result, msg = register_user("testuser", "password123")
        assert result is True
        assert msg == "Пользователь успешно зарегистрирован"
        assert get_user_count() == 1

    def test_register_user_empty_credentials(self):
        """Тест регистрации с пустыми учетными данными."""
        for username, password in [("", ""), ("user", ""), ("", "pass")]:
            result, msg = register_user(username, password)
            assert result is False
            assert msg == "Имя пользователя и пароль не могут быть пустыми"
            assert get_user_count() == 0

    def test_register_user_short_username(self):
        """Тест регистрации с коротким именем пользователя."""
        result, msg = register_user("ab", "password123")
        assert result is False
        assert msg == "Имя пользователя должно быть не менее 3 символов"
        assert get_user_count() == 0

    def test_register_user_short_password(self):
        """Тест регистрации с коротким паролем."""
        result, msg = register_user("testuser", "12345")
        assert result is False
        assert msg == "Пароль должен быть не менее 6 символов"
        assert get_user_count() == 0

    def test_register_user_already_exists(self):
        """Тест регистрации уже существующего пользователя."""
        register_user("testuser", "password123")
        result, msg = register_user("testuser", "newpassword")
        assert result is False
        assert msg == "Пользователь с таким именем уже существует"
        assert get_user_count() == 1

    def test_login_success(self):
        """Тест успешного входа в систему."""
        register_user("testuser", "password123")
        result, msg = login("testuser", "password123")
        assert result is True
        assert msg == "Аутентификация прошла успешно"

    def test_login_empty_credentials(self):
        """Тест входа с пустыми учетными данными."""
        for username, password in [("", ""), ("user", ""), ("", "pass")]:
            result, msg = login(username, password)
            assert result is False
            assert msg == "Имя пользователя и пароль не могут быть пустыми"

    def test_login_user_not_found(self):
        """Тест входа несуществующего пользователя."""
        result, msg = login("unknown", "password123")
        assert result is False
        assert msg == "Пользователь не найден"

    def test_login_wrong_password(self):
        """Тест входа с неверным паролем."""
        register_user("testuser", "password123")
        result, msg = login("testuser", "wrongpassword")
        assert result is False
        assert msg == "Неверный пароль"