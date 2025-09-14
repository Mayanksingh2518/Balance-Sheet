

# Balance Sheet Generator

A simple web application built with **Django, Python, and HTML** that allows users to create a balance sheet by entering values into a form. Once generated, the balance sheet can be **downloaded as a PDF** for reporting or record-keeping.

---

## 🚀 Features

* User-friendly web interface for entering balance sheet data
* Automatic generation of balance sheet (Assets = Liabilities + Equity)
* Export and download balance sheet in **PDF format**
* Built using **Django** (backend), **HTML/CSS** (frontend), and **Python libraries** for PDF generation

---

## 🛠️ Tech Stack

* **Backend**: Django, Python
* **Frontend**: HTML, CSS, Bootstrap (optional for styling)
* **PDF Generation**: ReportLab / WeasyPrint / xhtml2pdf (depending on your implementation)

---

## 📂 Project Structure

```
balance_sheet_project/
│── balance_sheet/         # Main app
│   ├── templates/         # HTML templates
│   ├── views.py           # Handles logic & PDF generation
│   ├── models.py          # (Optional) Store entries in DB
│   ├── urls.py            # Routes
│
│── static/                # CSS/JS files
│── balance_sheet_project/ # Django project settings
│── manage.py              # Django management script
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/balance-sheet-generator.git
   cd balance-sheet-generator
   ```

2. **Install dependencies directly**

   ```bash
   pip install django
   pip install reportlab   # or weasyprint/xhtml2pdf (depending on your implementation)
   ```

3. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

4. **Start the server**

   ```bash
   python manage.py runserver
   ```

5. Open browser and visit:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📝 Usage

1. Enter financial values (assets, liabilities, equity, etc.) in the form
2. Click **Generate Balance Sheet**
3. Preview balance sheet in the browser
4. Download balance sheet as **PDF**

---


## 📄 License

This project is open-source under the MIT License.
