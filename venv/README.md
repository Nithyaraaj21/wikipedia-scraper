# Wikipedia Scraper

Wikipedia Scraper is a Python script designed to retrieve information about historical leaders for various countries from a web service. The script utilizes web scraping techniques to extract details and the first paragraph of their Wikipedia page.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Outputs](#file-outputs)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Requirements

To run the Wikipedia Scraper, ensure you have the following installed:

- Python 3.x
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:Nithyaraaj21/wikipedia-scraper_Project2.git
    cd wikipedia-scraper
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script to scrape data from the web service and save the results:

```bash
python main.
```
## File Outputs

The script generates two output files:

1. leaders_data.json: A JSON file containing structured data of historical leaders for each country along with the first paragraph of their Wikipedia page.

2. leaders_data.csv: A CSV file containing the same data as the JSON file but in tabular format.

## Project Structure
The project follows this structure:

**src/:** Contains the source code.
     **scraper.py: Defines the WikipediaScraper class.
**main.py:** The main script to execute the Wikipedia Scraper.
**requirements.txt:** Lists the required Python packages.
**README.md:** The project's readme file.


## Contributing
Feel free to contribute