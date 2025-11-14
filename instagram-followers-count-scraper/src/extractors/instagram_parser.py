thonimport requests
from bs4 import BeautifulSoup

class InstagramParser:
    def __init__(self):
        self.base_url = "https://www.instagram.com"

    def get_profile_data(self, username):
        url = f"{self.base_url}/{username}/"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve data for {username}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        profile_data = self.extract_data(soup)
        return profile_data

    def extract_data(self, soup):
        script_tag = soup.find('script', {'type': 'text/javascript'}, text=lambda t: t and 'window._sharedData' in t)
        json_data = script_tag.string.split('= ', 1)[1].rstrip(';')
        data = json.loads(json_data)
        user_data = data['entry_data']['ProfilePage'][0]['graphql']['user']
        return {
            'profilePic': user_data['profile_pic_url_hd'],
            'userName': user_data['username'],
            'followersCount': user_data['edge_followed_by']['count'],
            'followsCount': user_data['edge_follow']['count'],
            'timestamp': '2025-04-15 - 13:10',
            'userUrl': f"{self.base_url}/{user_data['username']}",
            'userFullName': user_data['full_name'],
            'userId': user_data['id'],
            'biography': user_data['biography'],
            'externalUrl': user_data.get('external_url', '')
        }