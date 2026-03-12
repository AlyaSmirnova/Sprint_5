# 📚 Stellar Burgers: UI Automation Framework

![CI/CD Status](https://github.com/AlyaSmirnova/Sprint_5/actions/workflows/ui-tests.yml/badge.svg)
[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![Selenium](https://img.shields.io/badge/Tested%20with-Selenium-green?logo=selenium\&logoColor=white)](https://www.selenium.dev)
[![Reports](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)](https://github.com/USERNAME/REPOSITORY)

## ✅ Table of Contents
1. [Description](#-description)
2. [Tech Stack & Tools](#-tech-stack-&-tools)
3. [Project Architecture](#-project-architecture)
4. [Allure Reporting Features](#-allure-reporting-features)
5. [Test Coverage](#-test-coverage)
6. [Execution Guide](#-execution-guide)
7. [CI/CD Workflow](#-cicd-workflow)

## 💫 Description

This project features an automated UI testing suite for the **Stellar Burgers** service — a space-themed fast-food application where users can assemble and order unique burgers.
The framework validates critical user journeys, including registration, authentication, navigation, and personal account management, ensuring a seamless user experience across the platform.

## 🧑‍💻 Tech Stack & Tools
- **Language:** Python 3.10+
- **Framework:** [Pytest](https://docs.pytest.org/)
- **Browser Automation:** [Selenium WebDriver](https://www.selenium.dev)
- **Reporting:** Allure Framework (with automated screenshots on failure)
- **CI/CD:** GitHub Actions

## 📁 Project Architecture
```text

    ├── .github/workflows/     # CI/CD pipeline configuration 
    ├── allure-results/        # Raw test execution data (generated after run) 
    ├── src                    # Support modules & utilities
    │   ├── config.py          # Global settings (URL, Timeouts)
    │   ├── data.py            # Test data (Credentials)
    │   ├── helpers.py         # Generators (User registration data)
    │   ├── locators.py        # Web element selectors
    │ 
    ├── tests/                 # UI Test scenarios
    │   ├── test_login.py
    │   ├── test_logout_from_personal_account.py
    │   ├── test_redirection_from_personal_account.py
    │   ├── test_redirection_to_personal_account.py
    │   ├── test_registration_form.py    
    │   ├── test_transition_to_sections.py
    │   
    ├── conftest.py             # Fixtures
    ├── requirements.txt        # List of project dependencies
    └── README.md               # Comprehensive project documentation
```

## 📊 Allure Reporting Features
The project is integrated with the **Allure Framework** to provide deep visibility into the UI automation process. Key features include:

*   **Visual Evidence:** Automated **browser screenshots** are captured and attached to the report for every failed test, enabling rapid debugging.
*   **Dynamic Test Documentation:** Uses `@allure.title` and `@allure.description` to transform technical code into readable test scenarios.
*   **Hierarchical Grouping:** Tests are organized by **Suites** (e.g., Authentication) and **Features** (e.g., Login Logic) for structured analysis.
*   **Step-by-Step Execution:** Detailed `@allure.step` logging tracks every user action, such as clicking buttons or filling forms, in real-time.

## 🧪 Test Coverage
The automation suite provides comprehensive coverage for the following functional modules of the **Stellar Burgers** service:

### 1. User Authentication & Registration
* **New User Signup:** Successful registration with valid data.
* **Input Validation:** Error handling for invalid registration (e.g., password length < 6 characters).
* **Login Entry Points:** Verification of authorization via the Main Page, "Personal Account" button, Registration form, and Password Recovery page.

### 2. Navigation & User Interface
* **Personal Account Access:** Seamless transition to the user profile section for authorized users.
* **Constructor Navigation:** Quick redirection back to the burger builder from the Account section via the "Constructor" button or the company Logo.
* **Ingredient Categories:** Switching between "Buns", "Sauces", and "Fillings" tabs in the main constructor.

### 3. Session Management
* **Secure Logout:** Verification of the "Exit" button functionality and correct redirection to the login page after session termination.

### 4. Technical Implementation
* **Dynamic Waits:** Usage of `WebDriverWait` and `expected_conditions` to handle asynchronous element loading.
* **Stable Interactions:** Implementation of **JavaScript Click** and **Scroll-into-view** methods to bypass UI overlays and animations.

## 🚀 Execution Guide

### 1. Environment Setup
Clone the repository and set up a local virtual environment to ensure dependency isolation:

1. **Clone repository**
> ```bash 
> git clone https://github.com/AlyaSmirnova/Sprint_5
> cd Sprint_5
📦 Repository: [Sprint_5](https://github.com/AlyaSmirnova/Sprint_5)

2. **Create a virtual environment**
> ```bash 
> python -m venv venv

3. **Activate the virtual environment**
> ```bash 
> source venv/bin/activate

4. **Install required dependencies**
> `$ pip install -r requirements.txt`

### 2. Running Tests
Execute the full test suite and collect raw data for the Allure report:
> ```bash 
> pytest -v --alluredir=allure-results

### 3. Generatig Allure Report
Transform the raw data into a visual, interactive HTML report:
> ```bash 
> allure serve allure-results

## ⚙️ CI/CD Workflow
The project is fully automated using **GitHub Actions**. Upon every `push` to the **main** branch or any `Pull Request` creation:

1.  **Environment Provisioning:** A clean **Ubuntu** runner is initialized in the cloud.
2.  **Browser Setup:** The latest **Google Chrome** browser and **ChromeDriver** are automatically installed and configured.
3.  **Dependency Management:** Python environment is set up and all required libraries (Selenium, Pytest, Allure) are installed from `requirements.txt`.
4.  **Headless Execution:** The full UI test suite is executed in **headless mode** to ensure stability in the server environment.
5.  **Artifact Generation:** Test results, including **automated screenshots on failure**, are collected and stored as build artifacts for further analysis.
