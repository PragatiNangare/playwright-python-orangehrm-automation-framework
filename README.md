# 🚀 Playwright Python Automation Framework

An advanced UI automation framework built using **Playwright (Python)** and **Pytest**, designed with scalability, maintainability, and real-world testing practices.

---

## 📌 Features

* ✅ Page Object Model (POM) design pattern
* ✅ Pytest fixtures for setup & teardown
* ✅ Data-driven testing using JSON
* ✅ Logging system for debugging
* ✅ Screenshot capture on test failure
* ✅ Allure reporting (steps + screenshots)
* ✅ Retry mechanism for flaky tests
* ✅ Parallel execution using pytest-xdist
* ✅ Negative testing & edge case coverage

---

## 🧰 Tech Stack

* **Language:** Python
* **Automation Tool:** Playwright
* **Test Runner:** Pytest
* **Reporting:** Allure

---

## 📁 Project Structure

```
project-root/
│
├── pages/              # Page Object classes
├── tests/              # Test cases
├── utils/              # Utilities (logger, data loader)
├── config/             # Config files (YAML)
├── test_data.json      # Test data
├── conftest.py         # Fixtures
└── requirements.txt    # Dependencies
```

---

## ▶️ How to Run Tests

### 🔹 Install dependencies

```
pip install -r requirements.txt
```

---

### 🔹 Run tests

```
pytest
```

---

### 🔹 Run tests in parallel

```
pytest -n auto
```

---

### 🔹 Generate Allure report

```
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🧪 Sample Test Scenarios

* ✔ Add Employee (positive flow)
* ✔ Missing required fields (negative testing)
* ✔ Duplicate Employee ID (edge case)
* ✔ Data-driven employee creation

---

## 📊 Reporting

Allure report includes:

* Step-by-step execution
* Screenshots on failure
* Logs
* Test status (pass/fail)

---

## 🧠 Key Highlights

* Built scalable automation framework from scratch
* Implemented real-world testing strategies
* Handled flaky tests using retries and smart waits
* Designed reusable and maintainable architecture

---

## 👩‍💻 Author

Pragati Nangare

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
