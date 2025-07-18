Sure! Here's a clean, all-text version of your `README.md` without any emojis or images:

---

````markdown
# Django Stock Viewer

A Django web application that allows users to explore stock data, view visual charts, receive AI-generated insights using Google's Gemini API, and interact with an educational chatbot to learn about stock trading.

## Features

- Search and analyze any stock ticker (e.g., AAPL, MSFT, TSLA)
- Automatically generated charts:
  - Closing prices
  - Volume
  - Moving averages
- AI analysis using Gemini:
  - Technical recommendations (Buy/Sell/Hold)
  - Summary insights based on historical data
- Chatbot for learning about stock trading
- Curated educational articles for beginners

## Demo

Watch a short demo here:  
https://youtu.be/plwx20ybDuY

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-viewer.git
   cd stock-viewer
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your environment variables in a `.env` file:

   ```
   ALPHA_VANTAGE_API_KEY=your_key_here
   GEMINI_API_KEY=your_key_here
   ```

4. Run the Django server:

   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to:

   ```
   http://127.0.0.1:8000/
   ```

## Tech Stack

* Python
* Django
* Alpha Vantage API
* Google Gemini API
* Matplotlib
* HTML, CSS, JavaScript
