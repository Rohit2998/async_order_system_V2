# 🛒 Async Order Processing System

This is a Django-based REST API for processing orders asynchronously using **Celery** and **RabbitMQ**. It handles tasks like verifying stock, calculating prices, and updating order status in the background for better performance and scalability.

---

## ⚙️ Tech Stack

| Component        | Technology              |
|------------------|--------------------------|
| Backend API      | Django + DRF             |
| Database         | PostgreSQL               |
| Task Queue       | Celery                   |
| Message Broker   | RabbitMQ                 |
| Monitoring       | Flower                   |
| Containerization | Docker + Docker Compose  |

---

## 🚀 Features

- Place orders via API
- Asynchronous task handling with Celery
- Stock validation and deduction
- Atomic DB transactions for consistency
- Order status: `pending`, `confirmed`, `failed`
- Task queue monitoring with Flower

---
## 🚀 Start the Project
```
docker-compose build 
```
## 📦 API Endpoints

### ➕ Create an Order

```http
POST /api/orders/
Content-Type: application/json

{
  "items": [
    { "product": 1, "quantity": 2 },
    { "product": 2, "quantity": 1 }
  ]
}
```
### List Orders
```
GET /api/orders/
```
### Add Products
```
POST /api/products/
{
  "name": "Widget",
  "stock": 100,
  "price": 19.99
}
```

