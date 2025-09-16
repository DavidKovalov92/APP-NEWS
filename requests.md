# Керівництво по тестуванню Django API в Postman

## Підготовка до тестування

### 1. Налаштування середовища
Перед тестуванням переконайтеся, що ваш Django сервер запущений:
```bash
python manage.py runserver
```

### 2. Налаштування Postman
1. Відкрийте Postman
2. Створіть нову колекцію "Django Auth API"
3. Налаштуйте змінні середовища:
   - `base_url`: `http://127.0.0.1:8000`
   - `access_token`: (буде встановлено після логіну)
   - `refresh_token`: (буде встановлено після логіну)

## Тестування ендпоінтів

### 1. Реєстрація користувача (POST)

**URL:** `{{base_url}}/api/v1/auth/register/`

**Метод:** POST

**Headers:**
```
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "SecurePass123!",
    "password_confirm": "SecurePass123!",
    "first_name": "Test",
    "last_name": "User"
}
```

**Очікувана відповідь (201 Created):**
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "full_name": "Test User",
        "avatar": null,
        "bio": "",
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-01-01T10:00:00Z",
        "posts_count": 0,
        "comments_count": 0
    },
    "refresh": "refresh_token_here",
    "access": "access_token_here",
    "message": "User registered successfully"
}
```

**Тести для перевірки в Postman:**
```javascript
// Tests tab
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Response has required fields", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("user");
    pm.expect(responseJson).to.have.property("access");
    pm.expect(responseJson).to.have.property("refresh");
});

// Зберігаємо токени для подальшого використання
const responseJson = pm.response.json();
pm.environment.set("access_token", responseJson.access);
pm.environment.set("refresh_token", responseJson.refresh);
```

### 2. Вхід користувача (POST)

**URL:** `{{base_url}}/api/v1/auth/login/`

**Метод:** POST

**Headers:**
```
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "email": "test@example.com",
    "password": "SecurePass123!"
}
```

**Очікувана відповідь (200 OK):**
```json
{
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "full_name": "Test User",
        "avatar": null,
        "bio": "",
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-01-01T10:00:00Z",
        "posts_count": 0,
        "comments_count": 0
    },
    "refresh": "new_refresh_token_here",
    "access": "new_access_token_here",
    "message": "User login successfully"
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Login successful", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.message).to.include("login successfully");
});

// Оновлюємо токени
const responseJson = pm.response.json();
pm.environment.set("access_token", responseJson.access);
pm.environment.set("refresh_token", responseJson.refresh);
```

### 3. Отримання профілю користувача (GET)

**URL:** `{{base_url}}/api/v1/auth/profile/`

**Метод:** GET

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Очікувана відповідь (200 OK):**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User",
    "full_name": "Test User",
    "avatar": null,
    "bio": "",
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z",
    "posts_count": 0,
    "comments_count": 0
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Profile data is correct", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("id");
    pm.expect(responseJson).to.have.property("email");
    pm.expect(responseJson).to.have.property("username");
});
```

### 4. Оновлення профілю користувача (PUT/PATCH)

**URL:** `{{base_url}}/api/v1/auth/profile/`

**Метод:** PUT або PATCH

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "first_name": "Updated Test",
    "last_name": "Updated User",
    "bio": "This is my updated bio"
}
```

**Очікувана відповідь (200 OK):**
```json
{
    "first_name": "Updated Test",
    "last_name": "Updated User",
    "bio": "This is my updated bio",
    "avatar": null
}
```

### 5. Зміна паролю (POST)

**URL:** `{{base_url}}/api/v1/auth/change-password/`

**Метод:** POST

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "old_password": "SecurePass123!",
    "new_password": "NewSecurePass456!",
    "new_password_confirm": "NewSecurePass456!"
}
```

**Очікувана відповідь (200 OK):**
```json
{
    "message": "Password changed successfully"
}
```

### 6. Оновлення токена (POST)

**URL:** `{{base_url}}/api/v1/auth/token/refresh/`

**Метод:** POST

**Headers:**
```
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "refresh": "{{refresh_token}}"
}
```

**Очікувана відповідь (200 OK):**
```json
{
    "access": "new_access_token_here"
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("New access token received", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("access");
});

// Зберігаємо новий access токен
const responseJson = pm.response.json();
pm.environment.set("access_token", responseJson.access);
```

### 7. Вихід користувача (POST)

**URL:** `{{base_url}}/api/v1/auth/logout/`

**Метод:** POST

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "refresh_token": "{{refresh_token}}"
}
```

**Очікувана відповідь (200 OK):**
```json
{
    "message": "Logout succesful"
}
```

## Сценарії тестування

### Позитивні тести

1. **Повний цикл користувача:**
   - Реєстрація → Логін → Перегляд профілю → Оновлення профілю → Вихід

2. **Оновлення токенів:**
   - Логін → Використання access токена → Оновлення через refresh токен

### Негативні тести

1. **Реєстрація з невалідними даними:**
   ```json
   {
       "username": "",
       "email": "invalid-email",
       "password": "123",
       "password_confirm": "456"
   }
   ```
   Очікувана відповідь: 400 Bad Request

2. **Логін з невірними даними:**
   ```json
   {
       "email": "wrong@example.com",
       "password": "wrongpassword"
   }
   ```
   Очікувана відповідь: 400 Bad Request

3. **Доступ без токена:**
   - Спроба отримати профіль без Authorization header
   - Очікувана відповідь: 401 Unauthorized

4. **Використання недійсного токена:**
   - Використання неправильного або прострочeного токена
   - Очікувана відповідь: 401 Unauthorized

## Налаштування колекції в Postman

### Pre-request Scripts для всієї колекції:
```javascript
// Встановлюємо базовий URL якщо він не встановлений
if (!pm.environment.get("base_url")) {
    pm.environment.set("base_url", "http://127.0.0.1:8000");
}
```

### Collection Variables:
- `base_url`: `http://127.0.0.1:8000`
- `test_email`: `test@example.com`
- `test_password`: `SecurePass123!`

## Виправлення помилок в коді

Я помітив кілька помилок у вашому коді, які потрібно виправити:

### 1. В `apps/accounts/urls.py`:
```python
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views  # Виправлено: додано крапку

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 2. В `apps/accounts/serializers.py`:
```python
# Виправити назву методу
def validate(self, attrs):  # було valifate
```

### 3. В `apps/accounts/views.py`:
```python
# Видалити дублікат класу ProfileView і виправити помилки
class ChangePasswordView(generics.UpdateAPIView):  # Було ProfileView
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Виправлено raise_exceptions
        serializer.save()

        return Response({
            'message': 'Password changed successfully'
        }, status=status.HTTP_200_OK)
```

### 4. В `config/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include  # Додано include
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('apps.accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## Поради по тестуванню

1. **Використовуйте змінні середовища** для зберігання токенів та базової URL
2. **Створіть тести для кожного ендпоінта** щоб автоматично перевіряти відповіді
3. **Тестуйте як позитивні, так і негативні сценарії**
4. **Зберігайте колекцію** для повторного використання
5. **Використовуйте Collection Runner** для запуску всіх тестів одразу

Це керівництво допоможе вам повноцінно протестувати ваш Django REST API використовуючи Postman!