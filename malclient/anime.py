class Anime():

    def __init__():
        return

    def get_anime_details(self, id):
        id = str(id)
        params = {
            'fields': ','.join(self.anime_fields),
        }
        uri = f'anime/{id}'
        return self._api_handler.call(uri, params=params)

    # need pagination here
    def search_anime(self, keyword, limit=20):
        uri = 'anime'
        params = {
            "q": keyword,
            'fields': ','.join(self.anime_fields),
            'limit': limit
        }
        return self._api_handler.call(uri=uri, params=params)

    def get_anime_ranking(self, ranking_type="all", limit=20):
        uri = 'anime/ranking'
        ranking_types = [
            "all", "airing", "upcoming", "tv", "ova", "movie", "special",
            "bypopularity", "favorite"
        ]
        if ranking_type not in ranking_types:
            return
        params = {
            "ranking_type": ranking_types,
            "fields": ','.join(self.anime_fields),
            "limit": limit
        }
        return self._api_handler.call(uri=uri, params=params)

    def get_seasonal_anime(self, year, season, sort="anime_score", limit=20):
        seasons = ["winter", "spring", "summer", "fall"]
        if season not in season:
            return

        sort_options = ["anime_score", "anime_num_list_users"]
        if sort not in sort_options:
            return
        uri = f'anime/season/{year}/{season}'

        params = {
            "sort": sort,
            "limit": limit,
            "fields": ','.join(self.anime_fields)
        }
        return self._api_handler.call(uri=uri, params=params)

    def get_suggested_anime(self, limit=20):
        uri = 'anime/suggestions'
        params = {"limit": limit}
        return self._api_handler.call(uri=uri, params=params)
