# FastAPI Project Environment Setup Guide

## 1. Navigate to the Project Folder

Open **Git Bash** and move into your project directory:

```bash
cd fast_api
```

Make sure you're inside the correct folder by listing all files:

```bash
ls -la
```

You should be able to see files like the `app` folder and `.gitignore`.

---

## 2. Create a Python Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv .venv
```

This will generate a `.venv` folder that can be used by IDEs like PyCharm.

---

## 3. Install FastAPI and Required Packages

Install FastAPI and its default components inside the virtual environment:

```bash
pip install fastapi[all]
```

This installs FastAPI along with commonly used packages and prepares the app environment.

---

## 4. Run the FastAPI Application Using Uvicorn

Start the development server:

```bash
uvicorn app.main:app --reload
```

Explanation:

* **uvicorn** – The web server
* **app** – The `app` folder used as a module
* **main** – Refers to the `main.py` file inside the `app` folder
* **app** – The application instance created using `app = FastAPI()`

---

## 5. Test the API in Postman

Once the server is running, open **Postman** and connect to your API endpoints to test them.

---

You are now ready to begin developing your FastAPI project! 🚀
