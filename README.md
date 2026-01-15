# 🚀 SauceDemo Automation Framework (Python + Selenium)

## 📌 Project Overview
This project is a **Modular Test Automation Framework** designed to validate the critical E2E flows of the [SauceDemo](https://www.saucedemo.com/) e-commerce platform. 

Unlike simple linear scripts, this project utilizes the **Page Object Model (POM)** design pattern to ensure scalability, maintainability, and separation of concerns—mimicking real-world enterprise QA standards.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Library:** Selenium Webdriver
* **Design Pattern:** Page Object Model (POM)
* **Browser:** Chrome (Incognito Mode & Anti-Bot Detection enabled)

## 📂 Project Structure
The project is architected to separate data, logic, and execution:

* `jalankan_test.py` ➡️ **Test Runner**: The entry point that executes the test scenarios.
* `halaman_login.py` ➡️ **Page Object**: Contains all locators and methods (encapsulation).
* `data_rahasia.py` ➡️ **Data Layer**: Stores test data (credentials, URLs) securely.

## 🧪 Key Features Implemented
1.  **Robust Error Handling:** Uses `try-except` blocks to catch failures gracefully without crashing.
2.  **Stealth Mode:** Configured Chrome Options to bypass basic bot detection and remove "Chrome is being controlled" banners.
3.  **Modular Assertions:** Custom validation logic to verify login success and dashboard rendering.

## 🚀 How to Run
1.  Clone this repository.
2.  Ensure Python and Selenium are installed (`pip install selenium`).
3.  Run the test runner:
    ```bash
    python jalankan_test.py
    ```

---
*Created by [Antonius Rildo] - Master in Computer Science & QA Enthusiast*