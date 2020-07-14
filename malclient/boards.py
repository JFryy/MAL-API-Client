class Boards():

    def __init__():
        return

    def get_forum_boards(self):
        uri = 'forum/boards'
        return self._api_handler.call(uri)

    def get_forum_topic_detail(self, topic_id):
        uri = f'forum/topic/{topic_id}'
        params = {limit: 100}
        return self._api_handler.call(uri)


#    TODO:
#    def get_forum_topics
