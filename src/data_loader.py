def get_sp_data():
    import pandas as pd
    url = f"https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables=pd.read_html(url)
    return tables[0]


def download_and_save_prices(
    tickers: list,
    start_date: str,
    end_date: str,
    file_format: str = 'parquet',
    filename: str = 'multi_ticker_prices'
):
    import os
    import yfinance as yf
    import pandas as pd

    # Navigate up from src/ to project root, then into Data/Raw/
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    save_path = os.path.join(root_path, 'Data')
    os.makedirs(save_path, exist_ok=True)

    raw_data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False)
    data=raw_data['Adj Close']
    file_path = os.path.join(save_path, f"{filename}.{file_format}")

    if file_format == 'parquet':
        data.to_parquet(file_path)
    elif file_format == 'csv':
        data.to_csv(file_path)
    else:
        raise ValueError("Unsupported file format.")

    print(f"Data saved to {file_path}")