thonimport requests
import json
from .extractors.instagram_parser import InstagramParser
from .outputs.data_exporter import DataExporter

class InstagramScraper:
    def __init__(self, config):
        self.config = config
        self.instagram_parser = InstagramParser()
        self.data_exporter = DataExporter()

    def scrape_profiles(self, usernames):
        profile_data = []
        for username in usernames:
            data = self.instagram_parser.get_profile_data(username)
            profile_data.append(data)
        return profile_data

    def export_data(self, data):
        self.data_exporter.export_to_json(data, 'output_sample.json')

if __name__ == "__main__":
    with open('data/inputs.sample.json', 'r') as file:
        config = json.load(file)
    scraper = InstagramScraper(config)
    usernames = ['cristiano', 'leonmessi']
    data = scraper.scrape_profiles(usernames)
    scraper.export_data(data)