class Manga():

    def __init__():
        return

    def search_manga(self, query, limit=20):
        uri = 'manga'
        params = {
            "q": query,
            "limit": limit,
            "fields": ','.join(self.manga_fields)
        }
        return self._api_handler.call(uri, params=params)

    def get_manga_details(self, manga_id):
        uri = f'manga/{manga_id}'
        params = {"fields": ','.join(self.manga_fields)}
        return self._api_handler.call(uri, params=params)

    def get_manga_ranking(self, ranking_type="manga", limit=20):
        ranking_types = [
            "novels", "oneshots", "doujin", "manhwa", "manhua", "bypopularity",
            "favorite"
        ]

        if ranking_type not in ranking_types:
            return
        params = {
            "ranking_type": ranking_type,
            "limit": limit,
            "fields": ','.join(self.manga_fields)
        }
        return self._api_handler.call(uri, params)
