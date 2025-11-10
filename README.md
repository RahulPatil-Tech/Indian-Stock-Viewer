# 📈 **Indian Stock Viewer** 🇮🇳  
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

A **beautiful Python desktop app** built using **Tkinter**, **Matplotlib**, and **yFinance** that lets you **search, view, and visualize Indian stock data** in real-time.  

View **Open, High, Low, Close, and Volume**, and explore **1-month price trends** of top Indian companies — all in one sleek GUI! 🚀  

---

## ⚡ **Features**

✨ **Search & Select Stocks** — Choose from a predefined list or type manually.  
🔍 **Dynamic Dropdown Search** — Instantly filters stocks as you type.  
🏦 **NSE/BSE Support** — Automatically appends “.NS” if not specified.  
📊 **Interactive Chart** — Zoom, pan, and explore closing prices easily.  
⚙️ **Smooth Error Handling** — Friendly alerts for missing or invalid tickers.  
🪟 **Clean Tkinter Interface** — Compact, responsive, and easy to use.  

---

## 🧩 **Tech Stack**

| 🧠 Component | 🛠️ Library/Tool |
|--------------|----------------|
| 🐍 Language | Python 3.x |
| 🖥 GUI | Tkinter |
| 💹 Stock Data | yFinance |
| 📈 Plotting | Matplotlib |
| ⚙️ Integration | FigureCanvasTkAgg, NavigationToolbar2Tk |

---

## 💼 **Predefined Stock List**

These popular Indian stocks are included by default:  

```python
["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "MARUTI", "HINDUNILVR"]
```


---

## 🚀 How to Run  

### 🧾 1️⃣ Clone the Repository  
```bash
git clone https://github.com/RahulPatil-Tech/Indian-Stock-Viewer.git
cd indian-stock-viewer
```
### ⚙️ 2️⃣ Install Dependencies
## Make sure you have Python 3.x installed, then run:
```bash
pip install yfinance matplotlib
```

### ▶️ 3️⃣ Run the App
```bash
python stock_viewer.py
```

------

## 🖼️ App Preview  

### 🪟 Main Window  
- Enter a stock ticker manually or search from the dropdown.  
- Click **“Get Stock Data”** to fetch the latest 1-month performance.  

---

### 📊 Plot Area  
- Visualizes the **closing price for the last 30 days**.  
- Includes an **interactive zoom/pan toolbar** for deeper analysis.  

---

## 📸 Screenshots  

### 🪟 Example — TCS Stock Data  
<img width="650" height="292" alt="Stock Info" src="https://github.com/user-attachments/assets/984b5990-e14a-4215-80e7-aee741f59a98" />

### 📉 Price Trend Chart  
<img width="650" height="498" alt="Price Chart" src="https://github.com/user-attachments/assets/fe338036-da43-46fc-944b-f1d90c15b076" />

---

## 🧠 Code Overview  

### 🧩 Key Components  

| Function | Description |
|-----------|--------------|
| `update_dropdown()` | Filters stock list dynamically based on user input. |
| `fetch_stock()` | Fetches stock data using **yFinance** and updates the UI. |
| `on_closing()` | Safely exits the app with confirmation dialog. |
| `FigureCanvasTkAgg` | Embeds **Matplotlib** charts inside the Tkinter window. |

---

## 💡 Example Output  

**Example:** Fetching **TCS** stock data 👇  
```bash 
Ticker: TCS.NS
Date: 2025-11-10
Open: 3842.50
High: 3901.00
Low: 3820.00
Close: 3887.45
Volume: 2534782
```

**Plot:**  
📉 Line chart showing the **closing price trend for the last 30 days**.  

---

## 🧰 Troubleshooting  

🟠 **“No data found” error** → Verify the stock symbol or check your internet connection.  
🟣 **Blank chart** → Wait a few seconds; Yahoo Finance may throttle requests.  
🔵 **Dependencies missing** → Install required libraries via:  

```bash
pip install yfinance matplotlib
```

## 🚧 Future Enhancements  

✨ Planned features for upcoming versions:  

- 🚀 **Add multi-stock comparison**  
- 📆 **Include intraday charts**  
- 💾 **Export stock data as CSV**  
- 🌙 **Add dark mode support**  

---

## 👨‍💻 Author  

**Rahul Patil**  
💡 *Developed with ❤️ in Python & Tkinter*  
🌐 [GitHub Profile](https://github.com/RahulPatil-Tech)  

---

## 🪪 License  

This project is licensed under the **MIT License** — feel free to use, modify, and share.  

---

## 🌟 Support the Project  

If you found this project useful, please consider:  
⭐ **Giving it a star** on GitHub  
📢 **Sharing it** with fellow developers and learners! 🙌  




