import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import random

# Set up the Streamlit page
st.set_page_config(page_title="SigeForex Report (For SigeSquad)", layout="wide")

# CSS for blinking effect
st.markdown(
    """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    .dataframe td {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to apply cell styling
# Function to apply cell styling with type checking
def style_dataframe(df):
    styled_df = df.style.applymap(
        lambda x: (
            "background-color: lightcoral;" if isinstance(x, (int, float)) and x in [-1, -2] else
            "background-color: red;" if isinstance(x, (int, float)) and x < -2 else
            "background-color: lightgray;" if x == 0 else
            "background-color: lightgreen;" if isinstance(x, (int, float)) and x in [1, 2] else
            "background-color: green;" if isinstance(x, (int, float)) and x > 2 else
            "background-color: lightcoral;" if x == "SELL" else
            "background-color: lightgreen;" if x == "BUY" else
            ""
        ),
        subset=["Bias", "Score"]
    )
    return styled_df


def style_intraday(df):
    styled_df = df.style.applymap(
        lambda x: "background-color: lightcoral;" if x < 0 else
                  "background-color: lightgray;" if x == 0 else
                  "background-color: lightgreen;" if x > 0 else "",
        subset=["COT", "Retail", "Sentiment"]
    )
    return styled_df

# SigeForex (Report) Section
st.markdown("## SigeForex (Report)")

# Warning Box
st.markdown(
    """
    <div style="background-color: #FFDDC1; padding: 10px; border-radius: 5px; margin-top: 20px; text-align: center;">
        <strong style="color: red;">Please don't share</strong>
    </div>
    """, unsafe_allow_html=True)

# Title and Live Indicator for Pair Direction
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("## Pair Direction")
with col2:
    st.markdown(
        f"<div style='display: flex; align-items: center;'>"
        f"<span style='background-color: red; border-radius: 50%; width: 10px; height: 10px; display: inline-block; animation: blink 1s infinite;'> </span>"
        f"<span style='margin-left: 5px;'>Live</span>"
        f"<span style='margin-left: 10px;'>{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# Data for Pair Direction
pairs = [
    "NZDUSD", "NZDJPY", "NZDCHF", "EURAUD", "NZDCAD", "EURUSD", "EURGBP", "USDJPY", "EURCHF", "USDCHF",
    "CADCHF", "AUDUSD", "GBPUSD", "GBPCHF", "GBPAUD", "EURCAD", "CADJPY", "AUDJPY", "GBPJPY", "EURJPY",
    "CHFJPY", "AUDCHF", "USDCAD", "GBPCAD", "EURNZD", "AUDCAD", "XAUUSD", "AUDNZD", "GBPNZD"
]
scores = [
    -7, -5, -5, -5, -4, -4, -4, -3, -3, -2, -2, -2, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 2, 2, 2, 2, 3, 4, 6
]
bias = [
    "SELL", "SELL", "SELL", "SELL", "SELL", "SELL", "SELL", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE",
    "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "RANGE", "BUY", "BUY"
]

# Create DataFrame for Pair Direction
data_direction = pd.DataFrame({
    "Pair": pairs,
    "Score": scores,
    "Bias": bias
})

# Display styled data for Pair Direction
st.dataframe(style_dataframe(data_direction), use_container_width=True)

st.markdown("""
### Interest Rates
If interest rates are high this is good for a currency, If the change is also large strength should accelerate.

### Inflation
If inflation is high this is negative for a currency (typically if above 2%) as the currency buys less BUT it will lead to sustained or increased interest rates which are positive.

### GDP
GDP growth is positive for a currency as it attracts investment.

### Unemployment
Unemployment at high numbers is negative, as it affects the speed of interest rate growth and impacts government spending negatively.

### COT (Commitment of traders)
High percentages of non-commercial investors long on a currency is positive, as they generally have a correct bias long term.

### Retail Sentiment
High percentage of retail positioning on a currency is negative as retail sentiment is generally incorrect, but this is short term views typically.

### Interest Rates change
If 0.25% higher or lower differential, it is considered positive or negative for the currency

### Inflation change
If 0.50% higher or lower differential, it is considered positive or negative for the currency

### GDP change
If 1.00% higher or lower differential, it is considered positive or negative for the currency

### Unemployment change
If 0.10% higher or lower differential, it is considered positive or negative for the currency
""")

# Title and Live Indicator for Intraday
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("## Intraday")
with col2:
    st.markdown(
        f"<div style='display: flex; align-items: center;'>"
        f"<span style='background-color: red; border-radius: 50%; width: 10px; height: 10px; display: inline-block; animation: blink 1s infinite;'> </span>"
        f"<span style='margin-left: 5px;'>Live</span>"
        f"<span style='margin-left: 10px;'>{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# Data for Intraday
pairs_intraday = [
    "EURAUD", "EURGBP", "NZDUSD", "CADJPY", "EURUSD", "NZDCAD", "NZDJPY", "EURCAD", "EURCHF", "EURJPY",
    "EURNZD", "USDCAD", "USDCHF", "USDJPY", "CADCHF", "CHFJPY", "GBPAUD", "NZDCHF", "AUDUSD", "GBPUSD",
    "AUDCAD", "AUDJPY", "AUDNZD", "GBPCAD", "GBPCHF", "GBPJPY", "XAUUSD", "AUDCHF", "GBPNZD"
]
cot = [
    -3, -3, -1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 3, 3, 4, 4, 4, 4, 4, 4, 3, 4, 4
]
retail = [
    -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 0, 0, 0, 0, -2, -2, -2, -2, -2, -2, -2, -2, 0, 0, 0
]
sentiment = [
    -5, -5, -3, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 4
]

# Create DataFrame for Intraday
data_intraday = pd.DataFrame({
    "Pair": pairs_intraday,
    "COT": cot,
    "Retail": retail,
    "Sentiment": sentiment
})

# Display data for Intraday
st.dataframe(style_intraday(data_intraday), use_container_width=True)

st.markdown("""
### Retail Sentiment For Forex Pairs
This table shows the aggregated positions of retail traders from a number of the largest retail brokers in the industry. This data gives the overall positioning long and short on each currency pair, so you can see how the retail players are positioned. The data is taken typically from real money accounts and published by certain brokers on a regular basis each day.

### How we use this data
The large market participants (banks and institutions) move the forex markets, and they do this by placing large orders in the markets, broken down into small parts. The reason for this is they cannot often find large enough liquidity at their desired price point. To execute such orders, they look for opportunities where retail traders are overly positioned in one direction. By doing so, they can trigger stops or exploit retail sentiment to get better prices. This is why understanding retail sentiment is key for predicting short-term reversals and areas of potential liquidity.

### Summary
By combining retail sentiment data, institutional positioning, and macroeconomic indicators, this report provides a comprehensive view of the forex market. This insight helps traders make informed decisions based on a blend of short-term sentiment and long-term trends.
""")

# Add Pie Chart for COT, Retail, and Sentiment with random values
cot_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]
retail_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]
sentiment_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]

# Generate random percentages for each currency
def generate_random_percentages():
    percentages = [random.randint(1, 15) for _ in range(9)]
    total = sum(percentages)
    return [p / total * 100 for p in percentages]

cot_percentages = generate_random_percentages()
retail_percentages = generate_random_percentages()
sentiment_percentages = generate_random_percentages()

import random

# Add Pie Chart for COT, Retail, and Sentiment with random values
cot_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]
retail_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]
sentiment_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]

# Generate random percentages for each currency
def generate_random_percentages():
    percentages = [random.randint(1, 15) for _ in range(9)]
    total = sum(percentages)
    return [p / total * 100 for p in percentages]

cot_percentages = generate_random_percentages()
retail_percentages = generate_random_percentages()
sentiment_percentages = generate_random_percentages()

import random
import plotly.express as px
import streamlit as st

# Add Pie Chart for COT, Retail, and Sentiment with random values
cot_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]
retail_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]
sentiment_currencies = ["AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "NZD", "USD", "XAU"]

# Generate random percentages for each currency
def generate_random_percentages():
    percentages = [random.randint(1, 15) for _ in range(9)]
    total = sum(percentages)
    return [p / total * 100 for p in percentages]

cot_percentages = generate_random_percentages()
retail_percentages = generate_random_percentages()
sentiment_percentages = generate_random_percentages()

# Create Pie Charts for COT, Retail, and Sentiment
cot_fig = px.pie(values=cot_percentages, names=cot_currencies, title="COT Report")
retail_fig = px.pie(values=retail_percentages, names=retail_currencies, title="Retail Sentiment")
sentiment_fig = px.pie(values=sentiment_percentages, names=sentiment_currencies, title="Sentiment")

# Add blinking red dot below each pie chart
def add_blinking_dot():
    return f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <span style="background-color: red; border-radius: 50%; width: 10px; height: 10px; display: inline-block; animation: blink 1s infinite;"> </span>
        <span style="margin-left: 5px;">Updating</span>
    </div>
    """

# Streamlit layout for displaying the pie charts and blinking dots
col1, col2, col3 = st.columns([1, 1, 1])

# COT pie chart and blinking red dot labeled "Updating"
with col1:
    st.plotly_chart(cot_fig, use_container_width=True)
    st.markdown(add_blinking_dot(), unsafe_allow_html=True)  # "Updating" label below COT chart

# Retail pie chart and blinking red dot labeled "Updating"
with col2:
    st.plotly_chart(retail_fig, use_container_width=True)
    st.markdown(add_blinking_dot(), unsafe_allow_html=True)  # "Updating" label below Retail chart

# Sentiment pie chart and blinking red dot labeled "Updating"
with col3:
    st.plotly_chart(sentiment_fig, use_container_width=True)
    st.markdown(add_blinking_dot(), unsafe_allow_html=True)  # "Updating" label below Sentiment chart

# Function to apply cell styling with position-based color coding
def style_big_players(df):
    styled_df = df.style.applymap(
        lambda x: "background-color: lightgreen;" if x == "In Position" else
                  "background-color: lightcoral;" if x == "No Positions" else
                  "background-color: orange;" if x == "Getting Positions" else "",
        subset=["Position"]
    )
    return styled_df

# New Area Title SigeForex (BigPlayer) centered with regular color
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(
        """
        <div style="text-align: center; font-size: 32px; font-weight: bold; color: black; margin-bottom: 20px;">
            Big Player Position
        </div>
        """, unsafe_allow_html=True)
with col2:
    st.markdown(
        f"<div style='display: flex; align-items: center;'>"
        f"<span style='background-color: red; border-radius: 50%; width: 10px; height: 10px; display: inline-block; animation: blink 1s infinite;'> </span>"
        f"<span style='margin-left: 5px;'>Updating</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# Data for Big Players
big_players_data = {
    "Bank Name": [
        "JPMorgan Chase & Co.", "Citigroup Inc. (Citi)", "Deutsche Bank", "UBS Group AG", "Barclays", 
        "Goldman Sachs", "HSBC Holdings", "Bank of America Merrill Lynch (BofA)", "BNP Paribas", 
        "Morgan Stanley", "Standard Chartered", "Royal Bank of Canada (RBC)", "Credit Suisse", 
        "Societe Generale", "Wells Fargo"
    ],
    "Position": [
        "In Position", "In Position", "No Positions", "Getting Positions", "Getting Positions", 
        "No Positions", "In Position", "Getting Positions", "No Positions", 
        "No Positions", "In Position", "Getting Positions", "In Position", 
        "In Position", "No Positions"
    ]
}

# Create DataFrame for Big Players
big_players_df = pd.DataFrame(big_players_data)

# Display the Big Players table with applied styling
st.dataframe(style_big_players(big_players_df), use_container_width=True)

# HISTORY Section
st.markdown("## HISTORY January 3, 2025")

history = [
    ">>> SigeForex Bot Update = Morgan Stanley hit target its NZD/USD short from 0.63385 circa 1.2000 at a profit of +757 pips. Details",
    "----------------------------------------------------------------------------------------------------------------------------------",
    ">>> SigeForex Bot Update = Morgan Stanley hit target its NZD/USD short from 0.59133 circa 1.2000 at a profit of +305 pips. Details",
    "----------------------------------------------------------------------------------------------------------------------------------",
    ">>> SigeForex Bot Update = Credit Suiesse hit target its NZD/USD short from 0.60223 circa 1.4000 at a profit of +412 pips. Details",
    "----------------------------------------------------------------------------------------------------------------------------------",
    ">>> SigeForex Bot Update = JPMorgan Chase & Co. hit target its GBP/JPY long from 194.198 circa 1.1000 at a profit of +3126 pips. Details",
    ">>> SigeForex Bot Update = Bank of America Merrill Lynch (BofA) hit target its GBP/JPY long from 195.850 circa 1.1000 at a profit of +2126 pips. Details",
    ">>> SigeForex Bot Update = Bank of America Merrill Lynch (BofA) hit target its GBP/JPY long from 195.850 circa 1.1000 at a profit of +2126 pips. Details",
    ">>> SigeForex Bot Update = Credit Suisse hit target its GBP/JPY long from 196.873 circa 1.200 at a profit of +829 pips. Details"
]

# Styling the history updates
styled_history = ""
for update in history:
    # Apply color coding for specific words and numbers
    update = update.replace("Citigroup Inc. (Citi)", "<span style='background-color: orange;'>Citigroup Inc. (Citi)</span>")
    update = update.replace("JPMorgan Chase & Co.", "<span style='background-color: orange;'>JPMorgan Chase & Co.</span>")
    update = update.replace("Bank of America Merrill Lynch (BofA)", "<span style='background-color: orange;'>Bank of America Merrill Lynch (BofA)</span>")
    update = update.replace("Credit Suisse", "<span style='background-color: orange;'>Credit Suisse</span>")
    update = update.replace("+", "<span style='background-color: green;'>+</span>")  # Green background for + pips
    update = update.replace("pips.", "<span style='color: blue; text-decoration: underline;'>pips.</span>")  # Blue and underlined for "Details"

    styled_history += f"<p>{update}</p>"

# Display the styled history section
st.markdown(styled_history, unsafe_allow_html=True)