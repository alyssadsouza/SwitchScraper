import pandas as pd
from playwright.sync_api import sync_playwright
from constants import GAMES_DF_COLUMNS
from scraper import SwitchScraper

if __name__ == "__main__":

    with sync_playwright() as playwright:
        switch_scraper = SwitchScraper(playwright)
        data = switch_scraper.get_game_deals()

    df = pd.json_normalize(data)[GAMES_DF_COLUMNS]
    df.to_csv("data.csv")
