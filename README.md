Sure! Here's the plain text version of the README without any emojis:

---

# Stock Viewer – Django App

**Stock Viewer** is a Django-based web application that helps users explore and analyze stock market data with the assistance of AI.

## Features

* Stock Chart Visualization
  View closing prices, volume, and 10-day moving averages using Matplotlib.

* AI Stock Insights (Gemini API)
  Get technical recommendations and quick analysis powered by Google's Gemini.

* Interactive Stock Chatbot
  Ask questions about trading, investing, or stocks and receive AI-driven answers.

* Currency Exchange Widget (Optional)
  Real-time USD to EUR conversion using CURRENCY\_API.

* Learning Resources
  Curated articles to help beginners understand stock trading concepts.

## Getting Started

1. Clone the repo

   ```
   git clone https://github.com/your-username/stock-viewer.git
   cd stock-viewer
   ```

2. Install dependencies

   ```
   pip install -r requirements.txt
   ```

3. Add your API keys to `views.py`

   * ALPHA\_VANTAGE\_API\_KEY
   * GEMINI\_API\_KEY
   * (Optional) CURRENCY\_API\_KEY

4. Run the development server

   ```
   python manage.py runserver
   ```

## Tech Stack

* Backend: Django, Python
* AI: Google Gemini API
* Charts: Matplotlib
* Stock Data: Alpha Vantage API
* Frontend: HTML, CSS, JavaScript

## To-Do / Improvements

* Add user authentication
* Expand chatbot functionality
* Save user queries and analysis history
* Support for more stock indicators
* add support for crypto
