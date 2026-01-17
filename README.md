# 📰 APP-NEWS
**A high-performance news platform with subscription-based monetization and dynamic content management.**

![GitHub Repo Size](https://img.shields.io/github/repo-size/DavidKovalov92/APP-NEWS?style=for-the-badge)
![GitHub Language Count](https://img.shields.io/github/languages/count/DavidKovalov92/APP-NEWS?style=for-the-badge)
![License](https://img.shields.io/github/license/DavidKovalov92/APP-NEWS?style=for-the-badge)

---

## 📝 Overview
**APP-NEWS** — це сучасна платформа для агрегації новин, розроблена на базі **Django**. Проєкт поєднує в собі функціонал класичного блогу з просунутими механіками монетизації через підписки та інструментами для просування контенту користувачів.

Основна мета проєкту — забезпечити безпечне та швидке середовище для споживання контенту з можливістю персоналізації стрічки новин.

---

## ✨ Key Features

* 💳 **Monetization:** Повна інтеграція **Stripe API** для управління циклами підписки. Користувачі можуть купувати преміум-доступ до ексклюзивних новин з автоматизованою обробкою платежів.
* 🔒 **Security:** Впроваджено надійну аутентифікацію за допомогою **JWT (JSON Web Tokens)**. Це забезпечує безпечну роботу в режимі stateless між бекендом та фронтендом.
* 🚀 **User Interaction:** Реалізовано функціонал **"Pin Posts"**, що дозволяє користувачам закріплювати свої записи у топі стрічки після придбання відповідних послуг.
* 📂 **Content Management:** Гнучка система категорій та фільтрації новин, що дозволяє легко знаходити потрібний контент.

---

## 🛠️ Technical Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white) ![DRF](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white) |
| **Security** | ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) ![OAuth2](https://img.shields.io/badge/OAuth2-blue?style=for-the-badge) |
| **Payments** | ![Stripe](https://img.shields.io/badge/stripe-%235433FF.svg?style=for-the-badge&logo=stripe&logoColor=white) |
| **Database** | ![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) |
| **DevOps** | ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) |

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* Docker & Docker Compose
* Stripe Account (API Keys)

### Installation
1. **Клонуйте репозиторій:**
   ```bash
   git clone [https://github.com/DavidKovalov92/APP-NEWS.git](https://github.com/DavidKovalov92/APP-NEWS.git)
   cd APP-NEWS
