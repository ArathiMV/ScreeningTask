# Remind-Me-Later

This is a simple Django-based reminder project.

## Features

* Create and manage reminders
* Store reminder details in the database
* Basic project setup with virtual environment

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ArathiMV/ScreeningTask.git
```

### 2. Navigate to the Project Folder

```bash
cd rem_project
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 3.1 Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### 3.2 Activate Virtual Environment (Mac/Linux)

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Now open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser

## Testing with Postman

You can test the Remind-Me-Later API using Postman.

### 1. Create a Reminder (POST)

**Endpoint:**

```
POST http://127.0.0.1:8000/rem-me-later/create-reminder/
```

**Headers:**

```
Content-Type: application/json
```

**Body (raw JSON):**

```json
{
  "date": "2025-08-25",
  "time": "15:30",
  "message": "Screening Task Scheduled",
  "reminder_type": "EMAIL"
}
```

**Response:**

```json
{
  "id": 1,
  "message": "Screening Task Scheduled",
  "date": "2025-08-25",
  "time": "15:30:00",
  "reminder_type": "EMAIL",
  "created_at": "2025-08-23 00:19",
  "updated_at": "2025-08-23 00:19"
}
```

### 2. Get All Reminders (GET)

**Endpoint:**

```
GET http://127.0.0.1:8000/rem-me-later/get-reminders/
```

**Response:**

```json
[
  {
    "id": 1,
    "message": "Screening Task Scheduled",
    "date": "2025-08-25",
    "time": "15:30:00",
    "reminder_type": "EMAIL",
    "created_at": "2025-08-23 00:19",
    "updated_at": "2025-08-23 00:19"
  }
]
```
