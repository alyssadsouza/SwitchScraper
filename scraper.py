import time
from playwright.sync_api import TimeoutError
import json

class Scraper:
    def __init__(self, playwright, slow_mo, headless):
        self.browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        # List to store request and response details
        self.requests = []
        self.responses = []

        # Set up event handlers to capture requests and responses
        self.page.on("request", self.handle_request)
        self.page.on("response", self.handle_response)

    def handle_request(self, request):
        """Invoked each time a request is made."""
        pass

    def handle_response(self, response):
        """Invoked each time a response is received."""
        pass

    def close(self):
        """Closes the browser."""
        self.browser.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


class SwitchScraper(Scraper):
    """
    Scrapes the Nintendo Switch store for game deals.
    """

    def __init__(self, playwright, slow_mo=1000, headless=False):
        super().__init__(playwright=playwright, slow_mo=slow_mo, headless=headless)
        self.deals_url = "https://www.nintendo.com/en-ca/store/games/#p=1&sort=df&f=topLevelFilters&topLevelFilters=Deals"
        self.query_response_endpoint = "store_game_en_ca/query"
        self.data = []

    def load_more_results(self) -> bool:
        try:
            self.page.get_by_text("Load more results").click(timeout=10000)
            return True
        except TimeoutError:
            print("No more results to load.")
            return False
        except Exception as e:
            raise Exception(f"Error occurred while loading more results: {e}")

    def get_game_deals(self) -> list[dict]:
        self.page.goto(self.deals_url)
        try:
            # Get the API response data
            # handle_response called each time new results are loaded
            while self.load_more_results():
                time.sleep(4)  # Pause for 4 seconds after each scroll
                break
            
            # self.data contains all data received at query_response_endpoint
            return self.data
        except Exception as e:
            print(f"Error occurred while scrolling: {e}")
            return []

        # Return the data

    def handle_response(self, response):
        if self.query_response_endpoint in response.url:
            self.responses.append(
                {
                    "url": response.url,
                    "status": response.status,
                    "headers": response.headers,
                    "body": response.body(),
                }
            )
            data = json.loads(response.body())
            print(data["hits"])
            self.data += data["hits"]
