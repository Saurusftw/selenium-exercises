# Selenium Exercises

This project contains a pytest script that performs the 10 exercises on https://www.kimmoahola.net/selenium.html#.

Prerequisites:
- Python 3.8+
- Chrome installed (or change to another browser and adjust the driver)

Setup:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest -q
```

Notes:
- `webdriver-manager` will download the ChromeDriver automatically.
- Tests run headless by default. Remove headless option in the fixture if you want to see the browser.
- I couldn't run the tests in this environment — run locally where Chrome is available.

## Running the tests (detailed)

1. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the tests

```bash
pytest -q
```

Notes and environment considerations:
- The test fixture uses `webdriver-manager` to auto-download ChromeDriver for the installed Chrome.
- Tests run headless by default. To see the browser, edit the `driver` fixture in `tests/test_selenium_exercises.py` and remove the `--headless=new` option.
- These tests require a real browser (Chrome). I cannot run them from this environment because the runner has no graphical browser or network access to download drivers. Run locally or in a CI runner with Chrome available.
- If you prefer Firefox, replace the Chrome driver setup with `webdriver-manager` for geckodriver and use `webdriver.Firefox`.

If you'd like, I can add a GitHub Actions workflow to run these tests on push.
