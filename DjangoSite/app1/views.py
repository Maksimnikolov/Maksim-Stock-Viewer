from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from .forms import StockForm
from alpha_vantage.timeseries import TimeSeries
import google.generativeai as genai
import re
import requests
import datetime
import json

# API Keys
ALPHA_VANTAGE_API_KEY = 'NI8CF4AA1T164B1X'
GEMINI_API_KEY = 'AIzaSyBPvZbi_l23Fx9DhFRdbNy_RILYskdeMN0'

genai.configure(api_key=GEMINI_API_KEY)


def get_stock_data(symbol):
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='compact')
    data = data.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    })
    return data


def clean_gemini_output(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    return text


def analyze_with_gemini(df, symbol):
    summary = df.describe().round(2).to_string()
    prompt = f"""
    You are a stock market analyst. Analyze the following summary of {symbol} stock:

    {summary}

    Give a very brief technical recommendation (Buy/Sell/Hold) with reasoning. Make it 3 sentences long. Also include the full name of the stock.
    """
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(prompt)
    return clean_gemini_output(response.text)


def get_simple_recommendation(df, symbol):
    summary = df.describe().round(2).to_string()
    prompt = f"""
    Based on this stock data summary for {symbol}, answer only with one word: Buy, Sell, or Hold. No explanation.

    {summary}
    """
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    response = model.generate_content(prompt)
    word = response.text.strip().capitalize()
    return word if word in ["Buy", "Sell", "Hold"] else "Hold"


def create_chart(df, columns, title):
    plt.figure(figsize=(10, 4))
    df[columns].plot(title=title)
    plt.grid()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = base64.b64encode(buf.read()).decode()
    plt.close()
    return f"data:image/png;base64,{image}"


def stock_view(request):
    chart = None
    volume_chart = None
    ma_chart = None
    insight = None
    recommendation = None
    error = None

    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol'].upper()
            try:
                df = get_stock_data(symbol)

                # Calculate Moving Average
                df['MA10'] = df['Close'].rolling(window=10).mean()

                # Generate Charts
                chart = create_chart(df, 'Close', f"{symbol} Closing Price (Last 30 Days)")
                volume_chart = create_chart(df, 'Volume', f"{symbol} Volume (Last 30 Days)")
                ma_chart = create_chart(df, ['Close', 'MA10'], f"{symbol} 10-Day Moving Average")

                # AI Analysis
                insight = analyze_with_gemini(df, symbol)
                recommendation = get_simple_recommendation(df, symbol)

            except Exception as e:
                error = f"Error fetching data: {e}"
    else:
        form = StockForm()

    return render(request, 'app1/website.html', {
        'form': form,
        'chart': chart,
        'volume_chart': volume_chart,
        'ma_chart': ma_chart,
        'insight': insight,
        'recommendation': recommendation,
        'error': error,
    })


def terminology_view(request):
    return render(request, 'app1/terminology.html')
