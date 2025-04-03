import pandas as pd
import yfinance as yf
from loguru import logger


def main() -> None:
    result_dict = {}
    result = pd.DataFrame()

    df = pd.read_csv("data/ind_nifty50list.csv")
    nifty_50_list = (df["Symbol"] + ".NS").to_list()

    for indicator in nifty_50_list:
        try:
            df = yf.download(tickers=indicator, period="1d", interval="1d", multi_level_index=False)
            result_dict[indicator] = df
            logger.info(f"Downloaded data for {indicator}")
        except Exception as e:
            logger.error(f"Error downloading {indicator}: {e}")
            continue

    for k, df in result_dict.items():
        df["indicator"] = k
        result = pd.concat([result, df], axis=0)

    result.to_csv("nifty_50_data.csv", index=False)
    logger.info("Data downloaded successfully!")


if __name__ == "__main__":
    main()
