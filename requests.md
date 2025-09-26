# Керівництво по тестуванню Django API в Postman

## Підготовка до тестування

### 1. Налаштування середовища
Перед тестуванням переконайтеся, що ваш Django сервер запущений:
```bash
python manage.py runserver
```

### 2. Налаштування Postman
1. Відкрийте Postman
2. Створіть нову колекцію "Django Blog API"
3. Налаштуйте змінні середовища:
   - `base_url`: `http://127.0.0.1:8000`
   - `access_token`: (буде встановлено після логіну)
   - `refresh_token`: (буде встановлено після логіну)

---

## ТЕСТУВАННЯ ДОДАТКУ ACCOUNTS

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

---

## ТЕСТУВАННЯ ДОДАТКУ MAIN (КАТЕГОРІЇ ТА ПОСТИ)

### КАТЕГОРІЇ

### 1. Отримання списку категорій (GET)

**URL:** `{{base_url}}/api/v1/posts/categories/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Query параметри (опційно):**
- `search`: пошук за назвою або описом
- `ordering`: сортування (`name`, `created_at`, `-name`, `-created_at`)

**Приклад з параметрами:** `{{base_url}}/api/v1/posts/categories/?search=tech&ordering=-created_at`

**Очікувана відповідь (200 OK):**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Technology",
            "slug": "technology",
            "description": "All about technology",
            "posts_count": 5,
            "created_at": "2024-01-01T10:00:00Z"
        }
    ]
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has pagination structure", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("count");
    pm.expect(responseJson).to.have.property("results");
});
```

### 2. Створення нової категорії (POST)

**URL:** `{{base_url}}/api/v1/posts/categories/`

**Метод:** POST

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "name": "Technology",
    "description": "All about technology and innovation"
}
```

**Очікувана відповідь (201 Created):**
```json
{
    "id": 1,
    "name": "Technology",
    "slug": "technology",
    "description": "All about technology and innovation",
    "posts_count": 0,
    "created_at": "2024-01-01T10:00:00Z"
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Category created successfully", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("slug");
    pm.expect(responseJson.name).to.eql("Technology");
});

// Зберігаємо ID категорії для подальших тестів
const responseJson = pm.response.json();
pm.environment.set("category_id", responseJson.id);
pm.environment.set("category_slug", responseJson.slug);
```

### 3. Отримання деталей категорії (GET)

**URL:** `{{base_url}}/api/v1/posts/categories/{{category_slug}}/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Очікувана відповідь (200 OK):**
```json
{
    "id": 1,
    "name": "Technology",
    "slug": "technology",
    "description": "All about technology and innovation",
    "posts_count": 0,
    "created_at": "2024-01-01T10:00:00Z"
}
```

### 4. Оновлення категорії (PUT/PATCH)

**URL:** `{{base_url}}/api/v1/posts/categories/{{category_slug}}/`

**Метод:** PUT або PATCH

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "name": "Updated Technology",
    "description": "Updated description about technology"
}
```

### 5. Видалення категорії (DELETE)

**URL:** `{{base_url}}/api/v1/posts/categories/{{category_slug}}/`

**Метод:** DELETE

**Headers:**
```
Authorization: Bearer {{access_token}}
```

**Очікувана відповідь (204 No Content)**

### 6. Отримання постів по категорії (GET)

**URL:** `{{base_url}}/api/v1/posts/categories/{{category_slug}}/posts/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Очікувана відповідь (200 OK):**
```json
{
    "category": {
        "id": 1,
        "name": "Technology",
        "slug": "technology",
        "description": "All about technology",
        "posts_count": 1,
        "created_at": "2024-01-01T10:00:00Z"
    },
    "posts": [
        {
            "id": 1,
            "title": "First Tech Post",
            "slug": "first-tech-post",
            "content": "This is a technology post...",
            "image": null,
            "category": "Technology",
            "author": "testuser",
            "status": "published",
            "created_at": "2024-01-01T11:00:00Z",
            "updated_at": "2024-01-01T11:00:00Z",
            "views_count": 0,
            "comments_count": 0
        }
    ]
}
```

### ПОСТИ

### 1. Отримання списку постів (GET)

**URL:** `{{base_url}}/api/v1/posts/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Query параметри (опційно):**
- `category`: фільтр за категорією
- `author`: фільтр за автором
- `status`: фільтр за статусом (`draft`, `published`)
- `search`: пошук за заголовком і контентом
- `ordering`: сортування (`created_at`, `updated_at`, `views_count`, `title`)

**Приклад з параметрами:** `{{base_url}}/api/v1/posts/?category=1&status=published&search=tech&ordering=-created_at`

**Очікувана відповідь (200 OK):**
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "My First Blog Post",
            "slug": "my-first-blog-post",
            "content": "This is the content of my first blog post. It's quite interesting and informative...",
            "image": null,
            "category": "Technology",
            "author": "testuser",
            "status": "published",
            "created_at": "2024-01-01T10:00:00Z",
            "updated_at": "2024-01-01T10:00:00Z",
            "views_count": 0,
            "comments_count": 0
        }
    ]
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Posts list structure is correct", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("results");
    if (responseJson.results.length > 0) {
        pm.expect(responseJson.results[0]).to.have.property("title");
        pm.expect(responseJson.results[0]).to.have.property("slug");
    }
});
```

### 2. Створення нового поста (POST)

**URL:** `{{base_url}}/api/v1/posts/`

**Метод:** POST

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "title": "My Amazing Blog Post",
    "content": "This is the full content of my amazing blog post. It contains lots of interesting information about various topics. The content should be engaging and informative for the readers.",
    "category": 1,
    "status": "published"
}
```

**Очікувана відповідь (201 Created):**
```json
{
    "title": "My Amazing Blog Post",
    "content": "This is the full content of my amazing blog post...",
    "image": null,
    "category": 1,
    "status": "published"
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Post created successfully", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.title).to.eql("My Amazing Blog Post");
    pm.expect(responseJson.status).to.eql("published");
});

// Зберігаємо дані поста для подальших тестів
// Примітка: slug генерується автоматично на бекенді
pm.environment.set("post_slug", "my-amazing-blog-post");
```

### 3. Отримання деталей поста (GET)

**URL:** `{{base_url}}/api/v1/posts/{{post_slug}}/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Очікувана відповідь (200 OK):**
```json
{
    "id": 1,
    "title": "My Amazing Blog Post",
    "slug": "my-amazing-blog-post",
    "content": "This is the full content of my amazing blog post. It contains lots of interesting information about various topics. The content should be engaging and informative for the readers.",
    "image": null,
    "category": 1,
    "category_info": {
        "id": 1,
        "name": "Technology",
        "slug": "technology"
    },
    "author": 1,
    "author_info": {
        "id": 1,
        "username": "testuser",
        "full_name": "Test User",
        "avatar": null
    },
    "status": "published",
    "created_at": "2024-01-01T10:00:00Z",
    "updated_at": "2024-01-01T10:00:00Z",
    "views_count": 1,
    "comments_count": 0
}
```

**Тести для перевірки:**
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Post details are correct", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson).to.have.property("author_info");
    pm.expect(responseJson).to.have.property("category_info");
    pm.expect(responseJson.views_count).to.be.at.least(1);
});
```

### 4. Оновлення поста (PUT/PATCH)

**URL:** `{{base_url}}/api/v1/posts/{{post_slug}}/`

**Метод:** PUT або PATCH

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "title": "Updated Amazing Blog Post",
    "content": "This is the updated content of my blog post with new and improved information.",
    "status": "published"
}
```

**Очікувана відповідь (200 OK):**
```json
{
    "title": "Updated Amazing Blog Post",
    "content": "This is the updated content of my blog post with new and improved information.",
    "image": null,
    "category": 1,
    "status": "published"
}
```

### 5. Видалення поста (DELETE)

**URL:** `{{base_url}}/api/v1/posts/{{post_slug}}/`

**Метод:** DELETE

**Headers:**
```
Authorization: Bearer {{access_token}}
```

**Очікувана відповідь (204 No Content)**

### 6. Отримання моїх постів (GET)

**URL:** `{{base_url}}/api/v1/posts/my-posts/`

**Метод:** GET

**Headers:**
```
Authorization: Bearer {{access_token}}
Content-Type: application/json
```

**Query параметри (опційно):**
- `category`: фільтр за категорією
- `status`: фільтр за статусом
- `search`: пошук
- `ordering`: сортування

**Очікувана відповідь (200 OK):**
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "My First Post",
            "slug": "my-first-post",
            "content": "Content preview...",
            "image": null,
            "category": "Technology",
            "author": "testuser",
            "status": "published",
            "created_at": "2024-01-01T10:00:00Z",
            "updated_at": "2024-01-01T10:00:00Z",
            "views_count": 5,
            "comments_count": 2
        }
    ]
}
```

### 7. Популярні пости (GET)

**URL:** `{{base_url}}/api/v1/posts/popular/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Очікувана відповідь (200 OK):**
```json
[
    {
        "id": 1,
        "title": "Most Popular Post",
        "slug": "most-popular-post",
        "content": "This post has the most views...",
        "image": null,
        "category": "Technology",
        "author": "testuser",
        "status": "published",
        "created_at": "2024-01-01T10:00:00Z",
        "updated_at": "2024-01-01T10:00:00Z",
        "views_count": 1000,
        "comments_count": 25
    }
]
```

### 8. Останні пости (GET)

**URL:** `{{base_url}}/api/v1/posts/recent/`

**Метод:** GET

**Headers:**
```
Content-Type: application/json
```

**Очікувana відповідь (200 OK):**
```json
[
    {
        "id": 2,
        "title": "Latest Blog Post",
        "slug": "latest-blog-post",
        "content": "This is the most recent post...",
        "image": null,
        "category": "News",
        "author": "testuser",
        "status": "published",
        "created_at": "2024-01-01T15:00:00Z",
        "updated_at": "2024-01-01T15:30:00Z",
        "views_count": 10,
        "comments_count": 1
    }
]
```

## Сценарії тестування для Main App

### Позитивні тести

1. **Повний CRUD для категорій:**
   - Створення категорії → Отримання списку → Отримання деталей → Оновлення → Видалення

2. **Повний CRUD для постів:**
   - Створення поста → Отримання списку → Отримання деталей → Оновлення → Видалення

3. **Фільтрація та пошук:**
   - Пошук постів за ключовими словами
   - Фільтрація за категорією
   - Фільтрація за автором
   - Сортування за різними полями

4. **Тестування без авторизації:**
   - Перегляд публічних постів
   - Перегляд категорій
   - Популярні та останні пости

### Негативні тести

1. **Створення контенту без авторизації:**
   ```json
   {
       "title": "Test Post",
       "content": "Test content"
   }
   ```
   Очікувана відповідь: 401 Unauthorized

2. **Створення поста з невалідними даними:**
   ```json
   {
       "title": "",
       "content": "",
       "category": 999
   }
   ```
   Очікувана відповідь: 400 Bad Request

3. **Доступ до неіснуючого контенту:**
   - GET `/api/v1/posts/nonexistent-slug/`
   - Очікувана відповідь: 404 Not Found

4. **Спроба редагування чужого поста:**
   - Авторизуйтесь як інший користувач
   - Спробуйте редагувати пост іншого автора
   - Очікувана відповідь: 403 Forbidden

## Тестування з файлами (Multipart)

### Створення поста з зображенням

**URL:** `{{base_url}}/api/v1/posts/`

**Метод:** POST

**Headers:**
```
Authorization: Bearer {{access_token}}
```

**Body (form-data):**
```
title: "Post with Image"
content: "This post contains an image"
category: 1
status: published
image: [Виберіть файл зображення]
```

### Оновлення аватара користувача

**URL:** `{{base_url}}/api/v1/auth/profile/`

**Метод:** PATCH

**Headers:**
```
Authorization: Bearer {{access_token}}
```

**Body (form-data):**
```
avatar: [Виберіть файл зображення]
```

## Автоматичні тести для колекції

### Collection Variables:
- `base_url`: `http://127.0.0.1:8000`
- `test_email`: `test@example.com`
- `test_password`: `SecurePass123!`
- `category_slug`: `technology`
- `post_slug`: `my-first-post`

### Pre-request Script для колекції:
```javascript
// Встановлюємо базовий URL якщо він не встановлений
if (!pm.environment.get("base_url")) {
    pm.environment.set("base_url", "http://127.0.0.1:8000");
}

// Автоматично додаємо токен до заголовків для захищених ендпоінтів
const token = pm.environment.get("access_token");
if (token && pm.request.url.toString().includes("/api/v1/")) {
    pm.request.headers.add({
        key: "Authorization",
        value: `Bearer ${token}`
    });
}
```

### Загальні тести для відповідей:
```javascript
// Тест для перевірки часу відповіді
pm.test("Response time is less than 2000ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});

// Тест для перевірки Content-Type
pm.test("Content-Type is application/json", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});

// Тест для перевірки відсутності помилок сервера
pm.test("No server errors", function () {
    pm.expect(pm.response.code).to.be.below(500);
});
```

## Порядок тестування

Рекомендується виконувати тести в такому порядку:

### Етап 1: Аутентифікація
1. Реєстрація користувача
2. Логін користувача
3. Отримання профілю

### Етап 2: Категорії
1. Створення категорії
2. Отримання списку категорій
3. Отримання деталей категорії
4. Оновлення категорії

### Етап 3: Пости
1. Створення поста
2. Отримання списку постів
3. Отримання деталей поста
4. Отримання моїх постів
5. Оновлення поста

### Етап 4: Публічні ендпоінти
1. Популярні пости
2. Останні пости
3. Пости за категорією

### Етап 5: Очищення
1. Видалення тестових постів
2. Видалення тестових категорій
3. Логаут користувача  

## Поради по оптимізації тестування

### 1. Використання змінних середовища
Створіть файл environment в Postman з такими змінними:
```json
{
  "base_url": "http://127.0.0.1:8000",
  "access_token": "",
  "refresh_token": "",
  "category_id": "",
  "category_slug": "",
  "post_id": "",
  "post_slug": "",
  "test_email": "test@example.com",
  "test_password": "SecurePass123!"
}
```

### 2. Створення тестових даних
Додайте Pre-request Script для автоматичного створення тестових даних:

```javascript
// Pre-request script для створення категорії перед створенням поста
if (pm.info.requestName === "Create Post" && !pm.environment.get("category_id")) {
    pm.sendRequest({
        url: pm.environment.get("base_url") + "/api/v1/posts/categories/",
        method: "POST",
        header: {
            "Authorization": "Bearer " + pm.environment.get("access_token"),
            "Content-Type": "application/json"
        },
        body: {
            mode: "raw",
            raw: JSON.stringify({
                "name": "Test Category",
                "description": "Test category for automated tests"
            })
        }
    }, function (err, response) {
        if (!err && response.code === 201) {
            const responseJson = response.json();
            pm.environment.set("category_id", responseJson.id);
            pm.environment.set("category_slug", responseJson.slug);
        }
    });
}
```

### 3. Очищення даних після тестування
Додайте Post-response Script для очищення:

```javascript
// Post-response script для видалення тестових даних
if (pm.info.requestName === "Delete Post" && pm.response.code === 204) {
    // Видаляємо категорію після видалення поста
    const categorySlug = pm.environment.get("category_slug");
    if (categorySlug) {
        pm.sendRequest({
            url: pm.environment.get("base_url") + "/api/v1/posts/categories/" + categorySlug + "/",
            method: "DELETE",
            header: {
                "Authorization": "Bearer " + pm.environment.get("access_token")
            }
        }, function (err, response) {
            if (!err && response.code === 204) {
                pm.environment.unset("category_id");
                pm.environment.unset("category_slug");
            }
        });
    }
}
```

### 4. Валідація відповідей
Загальні тести для всіх запитів:

```javascript
// Глобальний тест для колекції
pm.test("Status code is success", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 201, 204]);
});

pm.test("Response time is acceptable", function () {
    pm.expect(pm.response.responseTime).to.be.below(3000);
});

// Тест структури даних для GET запитів
if (pm.request.method === "GET" && pm.response.code === 200) {
    pm.test("Response has correct structure", function () {
        const responseJson = pm.response.json();
        
        // Для пагінованих відповідей
        if (responseJson.hasOwnProperty("results")) {
            pm.expect(responseJson).to.have.property("count");
            pm.expect(responseJson.results).to.be.an("array");
        }
        
        // Для детальних відповідей
        if (responseJson.hasOwnProperty("id")) {
            pm.expect(responseJson.id).to.be.a("number");
        }
    });
}
```

### 5. Тестування безпеки
Додайте тести для перевірки авторизації:

```javascript
// Тест для захищених ендпоінтів
pm.test("Authentication required", function () {
    if (pm.request.headers.get("Authorization")) {
        pm.expect(pm.response.code).to.not.eql(401);
    }
});

// Тест для CORS заголовків
pm.test("CORS headers present", function () {
    if (pm.response.headers.get("Access-Control-Allow-Origin")) {
        pm.expect(pm.response.headers.get("Access-Control-Allow-Origin")).to.not.be.undefined;
    }
});
```

### 6. Масове тестування
Для запуску всіх тестів використовуйте Collection Runner:
1. Клікніть на колекцію → "Run collection"
2. Виберіть environment
3. Встановіть затримку між запитами (500ms)
4. Увімкніть "Keep variable values"
5. Запустіть тести

### 7. Експорт та імпорт колекції
Збережіть вашу колекцію для подальшого використання:
1. Правий клік на колекцію → "Export"
2. Виберіть Collection v2.1
3. Збережіть JSON файл

Це керівництво забезпечить повне тестування всіх функцій вашого Django Blog API через Postman. Не забувайте регулярно оновлювати тести при внесенні змін до API.