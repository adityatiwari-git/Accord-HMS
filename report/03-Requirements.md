# 3. Software and Hardware Requirements

## 3.1 Hardware Requirements

| Component | Practical Requirement |
|---|---|
| Processor | Dual-core or better |
| RAM | 4 GB or more |
| Storage | At least 2 GB free for project/environment |
| Display | 1366 × 768 or better |
| Network | Required for package installation and external image URLs |

## 3.2 Software Requirements

| Software | Purpose |
|---|---|
| Python | Programming language |
| Django 6.1 | Backend web framework |
| SQLite | Development database |
| HTML | Page structure |
| CSS | Custom styling |
| Bootstrap 5 | Responsive frontend components |
| JavaScript | Client-side interaction where required |
| Visual Studio Code | Code editor |
| Git | Version control |
| GitHub | Remote repository |
| Modern browser | Application testing |

The current repository pins Django 6.1 and its supporting packages in `requirements.txt`.

## 3.3 Development Environment

The project uses a Python virtual environment for isolated dependencies. The `.venv` directory should not be copied between operating systems or committed to GitHub. A new environment should be created on another computer and dependencies installed from `requirements.txt`.

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Ubuntu/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 3.4 Running the Project

```bash
python manage.py migrate
python manage.py check
python manage.py runserver
```

The development site is available at `http://127.0.0.1:8000/` and Django Admin at `/admin/`.