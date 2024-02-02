import requests
import json
import pandas as pd
import regex as re
from bs4 import BeautifulSoup

class WikipediaScraper:

    """
        Initialize the WikipediaScraper.

        Parameters:
        - base_url (str): The base URL for the Wikipedia scraper API.
        - country_endpoint (str): The endpoint for retrieving countries.
        - leaders_endpoint (str): The endpoint for retrieving leaders.
        - cookies_endpoint (str): The endpoint for managing cookies.
        - leaders_data (dict): A dictionary to store leader information.
        """
    
    def __init__(self, base_url: str,
                 country_endpoint: str,
                 leaders_endpoint: str,
                 cookies_endpoint: str,
                 leaders_data: dict):
        self.base_url = base_url
        self.country_endpoint = country_endpoint
        self.leaders_endpoint = leaders_endpoint
        self.cookies_endpoint = cookies_endpoint
        self.leaders_data = leaders_data
        self.session = requests.Session()
###########################################################################################""
        """
        Refresh the user's cookie every search.
        """
############################################################################################

    def refresh_cookie(self):
        cookie_req = self.session.get(self.base_url + self.cookies_endpoint)
        if cookie_req.status_code == 200:
            return cookie_req.cookies.get('user_cookie')
        else:
            print(f"Status Code: {cookie_req.status_code}")
###########################################################################################""
        """
        Reterive the list of countries from API
        """
############################################################################################
    def get_countries(self):
        self.refresh_cookie()
        countries_url = self.base_url + self.country_endpoint
        countries_req = self.session.get(countries_url)
        countries_req.raise_for_status()
        if countries_req.status_code == 200:
            return countries_req.json()
        else:
            print(f"Status Code: {countries_req.status_code}")

###########################################################################################""
        """
        Retrieves and processes the list of leaders for a specific country.
        """
############################################################################################

    def get_leaders(self, country):
        self.refresh_cookie()
        leaders_url = f"{self.base_url}{self.leaders_endpoint}?country={country}"
        leaders_req = self.session.get(leaders_url)
        leaders_req.raise_for_status()
        if leaders_req.status_code == 200:
            print(leaders_req.status_code)
        else:
            print(f"Status Code: {leaders_req.status_code}")

        country_leaders = []
        for leader in leaders_req.json():
            if leader:
                leader_info = leader.copy()
                leader_info["first_paragraph"] = self.get_first_paragraph(leader.get("wikipedia_url"))
                country_leaders.append(leader_info)
                print(leader_info)
                print(leader_info["first_paragraph"])
        self.leaders_data[country] = country_leaders
        self.to_json_file("leaders_data.json")
        self.to_csv_file("leaders_data.csv")

########################################################################################################""""""
        """
        Retrive the first paragraph of the Wikipedia page, 
        Removing references.
        Print cleaned first paragraph text.
        """
################################################################################################################



    def get_first_paragraph(self, wikipedia_url):
        response = self.session.get(wikipedia_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all("p"):
            if "<p><b>" in str(tag):
                extract_first_paragraph1 = tag
                extract_first_paragraph = re.sub(r'\[\d+\]', '', extract_first_paragraph1.get_text())
                return extract_first_paragraph

##################################################################################################################

        """
        Save the scrapped leaders info in json file and the CSV file with the leaders informations

        """

##################################################################################################################
    def to_json_file(self, filepath):
        with open(filepath, 'w') as json_file:
            json.dump(self.leaders_data, json_file, indent=4)

    def to_csv_file(self, filepath):
        # Collect data in a list
        data_list = []
        for country, leaders in self.leaders_data.items():
            for leader_info in leaders:
                leader_info['country'] = country  
                data_list.append(leader_info)
        result_df = pd.DataFrame(data_list)
        result_df.to_csv(filepath, index=False, encoding='utf-8')
