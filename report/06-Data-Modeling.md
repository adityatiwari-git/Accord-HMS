# 6. Data Modeling

## 6.1 Department

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | CharField | Department name |
| description | TextField | Department description |

## 6.2 Doctor

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | CharField | Doctor name |
| department | ForeignKey | Related department |
| qualification | CharField | Qualification |
| experience | PositiveIntegerField | Years of experience |
| email | EmailField | Email address |
| phone | CharField | Phone number |
| available | BooleanField | Availability status |

## 6.3 Profile

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| user | OneToOneField | Related Django user |
| full_name | CharField | Patient name |
| phone | CharField | Patient phone |
| address | TextField | Patient address |

## 6.4 Appointment

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| patient | ForeignKey | Patient/User |
| doctor | ForeignKey | Doctor |
| appointment_date | DateField | Appointment date |
| appointment_time | TimeField | Appointment time |
| reason | TextField | Optional reason |
| status | CharField | Pending/Confirmed/Completed/Cancelled |
| created_at | DateTimeField | Creation time |

## 6.5 Gallery

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| title | CharField | Gallery title |
| description | TextField | Description |
| image_url | URLField | Image address |
| created_at | DateTimeField | Creation time |

## 6.6 ContactMessage

| Field | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| name | CharField | Sender name |
| email | EmailField | Sender email |
| subject | CharField | Subject |
| message | TextField | Enquiry |
| created_at | DateTimeField | Creation time |

## 6.7 Relationship Diagram

```text
                     ┌──────────────┐
                     │     User     │
                     └──────┬───────┘
                            1│
              ┌──────────────┴──────────────┐
              │                             │
             1│                             N│
      ┌───────▼───────┐             ┌───────▼────────┐
      │    Profile    │             │   Appointment  │
      └───────────────┘             └───────┬────────┘
                                            N│
                                             │1
                                      ┌──────▼──────┐
                                      │    Doctor   │
                                      └──────┬──────┘
                                            N│
                                             │1
                                      ┌──────▼──────┐
                                      │ Department  │
                                      └─────────────┘

Gallery and ContactMessage are independent records.
```