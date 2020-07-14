from .request_handler import APICaller
from .anime import Anime
from .my_list import MyList
from .boards import Boards
from .manga import Manga
import requests
import logging


class Client(Anime, Manga, MyList, Boards):
    """
    MAL Base Client Object for interfacing with the MAL REST API.
    """

    def __init__(self):
        self.anime_fields = [
            "id",
            "title",
            "main_picture",
            "alternative_titles",
            "start_date",
            "end_date",
            "synopsis",
            "mean",
            "rank",
            "popularity",
            "num_list_users",
            "num_scoring_users",
            "nsfw",
            "created_at",
            "updated_at",
            "media_type",
            "status",
            "genres",
            "my_list_status",
            "num_episodes",
            "start_season",
            "broadcast",
            "source",
            "average_episode_duration"
            "rating",
            "pictures",
            "background",
            "related_anime",
            "related_manga",
            "recommendations",
            "studios",
            "statistic",
        ]

        self.manga_fields = [
            "id",
            "title",
            "main_picture",
            "alternative_titles",
            "start_date",
            "end_date",
            "synopsis",
            "mean",
            "rank",
            "popularity",
            "num_list_users",
            "num_scoring_users",
            "nsfw,created_at",
            "updated_at",
            "media_type,status",
            "genres",
            "my_list_status",
            "num_volumes",
            "num_chapters",
            "authors{first_name,last_name}",
            "pictures",
            "background",
            "related_anime",
            "related_manga",
            "recommendation",
        ]
        return

    def init(self, access_token=None, refresh_token=None):
        base_url = "https://api.myanimelist.net/"
        version = 'v2'
        self.base_url = base_url + f'{version}/'
        self.bearer_token = access_token
        self.refresh_token = refresh_token
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {self.bearer_token}'
        }
        self._api_handler = APICaller(base_url=self.base_url,
                                      headers=self.headers)

    # retrieve oauth bearer token via username and password... leave this out of the initialization process and leave a seperate method for setting bearer token stuff, this is gross!!!
    @staticmethod
    def get_bearer_token(client_id, client_secret, code, code_verifier):
        base_url = "https://myanimelist.net/v1/"
        uri = "oauth2/token"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        api_handler = APICaller(base_url=base_url, headers=headers)
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "code_verifier": code_verifier,
            "grant_type": "authorization_code"
        }

        return api_handler.call(uri=uri, method="post", data=data)

    def refresh_bearer_token(self, client_id, client_secret, refresh_token):
        base_url = "https://myanimelist.net/v1/"
        uri = "oauth2/token"
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'basic {}'
        }
        api_handler = APICaller(base_url=base_url, headers=headers)
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret
        }

        # print response json of authentication, reinstantiate caller method.
        response = api_handler.call(uri=uri, method="post", data=data)
        print("Refreshing token with client id and secret:")
        print(response)
        self.bearer_token = response.access_token
        self.refresh_token = response.refresh_token
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Bearer {response.access_token}',
            'X-MAL-Client-ID': '{}'
        }
        self._api_handler = APICaller(base_url=self.base_url,
                                      headers=self.headers)
        return