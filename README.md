# 🔑 Python Password Manager (Local)

A desktop application designed to help you organize and store your digital credentials locally and securely. Built using Python's `tkinter` for the UI and `json` for data persistence.

## ✨ Key Features
* **Local Storage:** Your passwords stay on your machine in a `parole.json` file. No cloud required.
* **Search Functionality:** Quickly find the email and password for any saved site by typing its name.
* **Modern UI:** Dark-themed interface with high-contrast elements for better readability.
* **Data Validation:** Prevents saving empty fields to ensure your database stays clean.

## 🛠️ How it Works
This app uses Python's built-in `json` and `os` libraries:
1. When you save a password, the app checks if `parole.json` exists.
2. It reads the existing data, updates it with your new entry, and saves it back.
3. The `Search` button looks through the JSON dictionary and triggers a popup with your information.

## 🚀 Installation & Usage
Since this project uses only Python's standard libraries, **no extra installations** (like pip) are required!

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/password-manager.git](https://github.com/your-username/password-manager.git)
