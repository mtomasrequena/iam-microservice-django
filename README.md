# IAM Microservice - Django REST API

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-092E20.svg)
![Django REST Framework](https://img.shields.io/badge/DRF-3.14+-red.svg)

A scalable Identity and Access Management (IAM) REST API built with Django REST Framework and JSON Web Tokens (JWT). This microservice acts as the foundational authentication and authorization layer, designed to support decoupled architectures (such as React/Flutter frontends or external AI models).

## 🚀 Key Features

* **Custom User Model:** Authentication is handled strictly via Email (bypassing Django's default username approach) to meet modern industry standards.
* **Role-Based Access Control (RBAC):** Built-in support for different user tiers (Admin, Client, Auditor).
* **Business-Ready Fields:** Includes specific data points for highly regulated sectors (e.g., Fintech, Healthtech), such as KYC (Know Your Customer) validation status and verified phone numbers.
* **Stateless Authentication:** Fully decoupled security using JWT.
* **Admin Backoffice:** Pre-configured Django Admin panel for rapid user auditing and management.

## 🛠️ Tech Stack

* **Backend Framework:** Django
* **API Toolkit:** Django REST Framework (DRF)
* **Authentication:** JWT (JSON Web Tokens)
* **Database:** SQLite (Development) / Ready for PostgreSQL (Production)

## 💻 Local Setup & Installation

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/iam-microservice-django.git](https://github.com/YOUR_USERNAME/iam-microservice-django.git)
cd iam-microservice-django