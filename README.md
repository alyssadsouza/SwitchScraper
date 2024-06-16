# SwitchScraper

SwitchScraper is a Python project designed to scrape the Nintendo Switch store for game deals. This project uses [Playwright](https://playwright.dev/python/docs/intro) for browser automation.

## Setup

To set up the project, follow these steps:

### 1. Clone the repository

```sh
git clone https://github.com/alyssadsouza/SwitchScraper.git
cd SwitchScraper
```

### 2. Set up a virtual environment

It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment using the following commands:

```bash
python3 -m venv venv
source venv/bin/activate # on macOS and Linux
venv\Scripts\activate # or Windows
```
### 3. Install the requirements

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Ensure you have Playwright installed and set up by running:

```bash
playwright install
```

After setting up the environment and installing the dependencies, you can run the scraper by with the `main.py` script.

```bash
python main.py
```

This will open a Chromium browser, navigate to the Nintendo Switch store game deals page, and scrape the available deals.

## Project Structure

```
SwitchScraper/
│
├── scraper.py            # Contains the Scraper and SwitchScraper classes
├── main.py               # Main script to run the scraper
├── constants.py          # Contains constants used in the project
├── requirements.txt      # Lists the dependencies
└── README.md             # Project documentation
```