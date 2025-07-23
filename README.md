# Flight Price Monitor & Data Extractor

This Python script uses the BOOKING.COM API (via RapidAPI) to search for flights based on user-defined parameters. It parses the returned data, exports flight details to Google Sheets, and sends email alerts if any flights are below a configurable price threshold.

Its core use case is helping users track and analyze flight prices in real time, and to build a historical dataset for future data analysis or decision making.

---

## ✈️ Features

- 🔎 Searches flights using the BOOKING.COM API
- 📊 Exports flight data to Google Sheets
- 📬 Sends email alerts for flights below a price threshold
- 🗃️ Saves JSON and TXT logs of flight data in a runtime directory
- ⚙️ Highly configurable via `config.py` and `.env`
- 🐳 Optional Docker support for clean deployment

---

## 🧰 Tech Stack

- **Language:** Python 3.12
- **Dependencies:**
  - `requests`
  - `python-dotenv`
  - `google-api-python-client`
  - `google-auth-httplib2`
  - `google-auth-oauthlib`
  - `smtplib`, `EmailMessage`, `json`, `datetime`
- **Environment:**
  - Uses [`uv`](https://pypi.org/project/uv/) for environment and dependency management
  - Optional Docker setup included
- **External Services:**
  - [BOOKING.COM Flights API](https://rapidapi.com/DataCrawler/api/booking-com15) via RapidAPI
  - Google Sheets API

---

## 📁 Project Structure

.
├── main.py # Main script: API calls, parsing, email logic
├── config.py # Customizable parameters (API config, thresholds, etc.)
├── gsheets.py # Handles Google Sheets export
├── .env # Holds sensitive env variables (user-provided)
├── pyproject.toml # Dependency definitions (used with uv)
├── token.json # Google OAuth token (auto-generated)
├── credentials.json # Google API credentials (user-provided)
├── runtime-outputs/ # Output folder for runtime-generated .json/.txt
├── uv.lock # uv dependencies
├── README.md
├── README.Docker.md # Separate README for Docker-based deployment

---

## ⚙️ Configuration

### `.env` Variables

Create a `.env` file in the root directory with the following keys:

RAPIDAPI_KEY=your_rapidapi_key_here
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=recipient_email@gmail.com
SPREADSHEET_ID=your_google_sheet_id
PASSWORD=your_app_generated_email_password

> 🔒 The `PASSWORD` should be an **App Password**, not your email login password.

### `config.py` Parameters

Customize the API request and alert settings:

- Flight search parameters (e.g., origin, destination, dates, passengers)
- Price threshold for triggering email alerts
- Email subject line and formatting
- Whether to enable/disable Google Sheets or email functionality

---

## 🚀 Usage

### 1. Clone the Repository

git clone https://github.com/Isaackap/FlightDataScript.git
cd FlightDataScript

### 2. Install Dependencies

#### Option A: Using `uv` (recommended if not using Docker)

uv venv
uv pip install -r requirements.txt # or use `uv add` manually
uv run main.py

#### Option B: Using Docker

docker compose up --build

Follow the steps in `README.Docker.md` for full Docker instructions.

---

## ✉️ Output

- ✅ **Email Alert** if any flights are below your price threshold
- 📤 **Google Sheets** receives structured flight data (requires setup)
- 📝 **Local files**: `.json` response and `.txt` summaries saved to `/runtime-outputs/`

Example confirmation:
Email has been sent to (Email Address)
Data exported to Google Sheets Successfully

---

## 📝 Prerequisites

- Python 3.12 (or use Docker)
- Google Sheets API enabled with proper OAuth setup:
  - Place your `credentials.json` in the root directory
  - First-time auth will create `token.json` automatically
- A valid [RapidAPI](https://rapidapi.com) key for the BOOKING.COM API
- Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833)

---

## 📌 Notes

- If you only want part of the functionality, you can comment out the `sendEmail()` and/or `gsheets.main()` calls in `main.py`.
- All personal credentials are excluded from source control by default — ensure `.env`, `token.json`, and `credentials.json` are not committed.

---

## 📄 License

MIT License — free for personal or commercial use.

---

## 👤 Author

**Isaac Kapeel**
