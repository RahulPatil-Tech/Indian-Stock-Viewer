import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk

# Predefined list of popular Indian stocks
STOCK_LIST = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "MARUTI", "HINDUNILVR"]

def update_dropdown(*args):
    """Update the dropdown list based on user input in search_entry."""
    search_term = search_var.get().upper()
    filtered_stocks = [s for s in STOCK_LIST if search_term in s]

    # Clear old menu
    menu = dropdown['menu']
    menu.delete(0, 'end')

    # Add filtered options
    for stock in filtered_stocks:
        menu.add_command(label=stock, command=lambda value=stock: selected_stock.set(value))

    # If there are filtered options, select the first one
    if filtered_stocks:
        selected_stock.set(filtered_stocks[0])
    else:
        selected_stock.set("")

def on_closing():
    # Optional: you can add a confirmation dialog
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        import sys
        sys.exit()

def fetch_stock():
    ticker = entry.get().upper().strip()

    # If entry is empty, use selected stock from dropdown
    if not ticker and selected_stock.get():
        ticker = selected_stock.get()

    if not ticker:
        messagebox.showerror("Error", "Please enter a ticker or select from the list")
        return

    # Append NSE suffix by default if none given
    if not ticker.endswith(".NS") and not ticker.endswith(".BO"):
        ticker += ".NS"

    try:
        data = yf.download(ticker, period="1mo")
        if data.empty: # type: ignore
            messagebox.showerror("Error", f"No data found for ticker '{ticker}'")
            return

        latest = data.iloc[-1] # type: ignore

        details_text = (
            f"Ticker: {ticker}\n"
            f"Date: {latest.name.date()}\n"  # type: ignore
            f"Open: {latest['Open',ticker]:.2f}\n"
            f"High: {latest['High',ticker]:.2f}\n"
            f"Low: {latest['Low',ticker]:.2f}\n"
            f"Close: {latest['Close',ticker]:.2f}\n"
            f"Volume: {int(latest['Volume', ticker])}"  # type: ignore
        )

        details_label.config(text=details_text)

        # Plot closing prices
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(data.index, data['Close'], marker='o') # type: ignore
        ax.set_title(f"{ticker} Closing Prices (Last 1 Month)")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (INR)")
        ax.grid(True)
        fig.autofmt_xdate()

        # Clear previous plot
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Add navigation toolbar for zoom/pan
        toolbar = NavigationToolbar2Tk(canvas, plot_frame)
        toolbar.update()
        canvas.get_tk_widget().pack()

        '''# Add coordinate hover label
        coord_label = tk.Label(plot_frame, text="X: , Y: ")
        coord_label.pack()'''

        # Mouse move event to show coordinates
        def on_move(event):
            if event.inaxes:
                x, y = event.xdata, event.ydata
                #coord_label.config(text=f"X: {x:.2f}, Y: {y:.2f}")

        #canvas.mpl_connect("motion_notify_event", on_move)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to get data: {str(e)}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Indian Stock Viewer")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", on_closing)

# Manual entry field
tk.Label(root, text="Enter Stock Ticker (NSE/BSE):").pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Searchable dropdown
tk.Label(root, text="Or search/select a stock from the list:").pack(pady=5)

search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var, width=20)
search_entry.pack(pady=5)
search_var.trace_add("write", update_dropdown)

selected_stock = tk.StringVar()
selected_stock.set(STOCK_LIST[0])

dropdown = tk.OptionMenu(root, selected_stock, *STOCK_LIST)
dropdown.pack(pady=5)

tk.Button(root, text="Get Stock Data", command=fetch_stock).pack(pady=10)

details_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
details_label.pack(pady=5)

plot_frame = tk.Frame(root)
plot_frame.pack(pady=10)

root.mainloop()
