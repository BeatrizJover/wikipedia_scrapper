# Wikipedia_Scrapper Project

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)


## Description
This project fetches data about country leaders, including their names and Wikipedia URLs, from a public API. It retrieves the first paragraph from each leader's Wikipedia page and stores the information in a JSON file. 

## Features

- Fetches country and leader information from a public API (`https://country-leaders.onrender.com`).
- Retrieves the first paragraph of each leader's Wikipedia page.
- Saves the data to a JSON file (`leaders.json`).
- Handles expired cookies and retries using a session-based approach.

## Requirements

- Python 3.6+
- Required libraries: `requests`, `BeautifulSoup`, `json`, `re`

You can install the necessary libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the Jupyter Notebook: Open `wikipedia_scraper.ipynb` in Jupyter Notebook and run the cells to fetch the leaders' data and save it to a JSON file.

    ```bash
    jupyter notebook wikipedia_scraper.ipynb
    ```

2. Check the results: After running the notebook, the `leaders.json` file will contain a dictionary with the names of leaders and their first Wikipedia paragraph.

## Contributors
* [BeatrizJover](https://github.com/BeatrizJover)


