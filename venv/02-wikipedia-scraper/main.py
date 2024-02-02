# main.py
from time import perf_counter
start_time = perf_counter()
from src.scraper import WikipediaScraper

if __name__ == "__main__":
    
    
    wikipedia_scraper = WikipediaScraper(
    base_url="https://country-leaders.onrender.com",
    country_endpoint="/countries",
    leaders_endpoint="/leaders",
    cookies_endpoint="/cookie",
    leaders_data={}
)

    countries = wikipedia_scraper.get_countries()

    if countries:
           for country in countries:
              wikipedia_scraper.get_leaders(country)

        # Save the leaders data into a JSON file
    wikipedia_scraper.to_json_file(filepath="leaders_data.json")
print(f"\nTime spent to finish the task: {perf_counter() - start_time} seconds.")    