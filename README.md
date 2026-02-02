
# Health Tracker Dashboard

A simple Flask-based web application to track daily health activities such as exercise, meditation, and sleep.  
Built with a clean backend structure, server-side form validation, and a responsive UI using Bootstrap.

---

## 🚀 Features

- Add daily health data (date, exercise, meditation, sleep)
- Form handling and validation using **Flask-WTF**
- Responsive UI with **Bootstrap**
- Clean and lightweight Flask backend
- HTML, CSS, and Bootstrap based frontend
- Easy to understand and extend

---

## 🛠 Tech Stack

- Python
- Flask
- Flask-WTF
- WTForms
- **Bootstrap 5**
- HTML
- CSS

---

## 📂 Project Structure

```

Healthcre_tracker/
│
├── app.py
├── forms.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── form.html
│
├── static/
│   └── css/
│       └── style.css
│
└── instance/        (ignored, local data only)

````

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/dhanusm-13/Healthcre_tracker.git
cd Healthcre_tracker
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 Notes

* Bootstrap is used via CDN for responsive styling
* Virtual environment and runtime files are excluded from version control
* Local data (if any) should be stored inside the `instance/` folder
* This project is intended for learning and local development

---

## 📌 Author

**Dhananjaya S M**
GitHub: [https://github.com/dhanusm-13](https://github.com/dhanusm-13)

