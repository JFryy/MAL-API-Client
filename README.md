# MAL-API-Client
A third party object oriented python3 client library for MyAnimeList's newly released official REST API.

## Installation

`pip install malclient --user`


## Authentication
This client library requires an OAuth2 access token to interface with. While OAuth2 is fantastic for delegating user authorization to third party web applications, it isn't the easiest authentication option for simple automation or scraping (what this client's ideal scope is generally guided towards). Luckily [there is a great guide for authenticating an application and retreiving credentials for this api](https://myanimelist.net/blog.php?eid=835707) which you can use with this library. Please refer to that guide 

Once an access token is retrieved, you can simply authenticate with this api with the following:
```python
import malclient

client = malclient.Client()
client.init(access_token="<your-access-token>")

```

If this client library is being used in a long running context, you may want to be periodically refresh your access token. This can be done via the following, and will update future request headers with the newly returned `access_token` and set your new `refresh_token` as an attribute ou can refference.
```python
 client.refresh_bearer_token(
            client_id="<your-client-id>",
            client_secret="<your-client-secret>",
            refresh_token="<your-refresh-token>"))
```

For any other issues regarding authentication, [please refer to the following guide](https://myanimelist.net/blog.php?eid=835707). There are some potential plans in the future for more simple authentication methods, however for now this seems to be the method sanctioned by MyAnimeList.

## Quick Start Examples
Below are some examples to demonstrate some usage of this client for MAL's REST API. Please note that responses are serialized to python objects for reffering to attributes directly, however printing the object at top level will return a dictionary for finding attributes.

```python
    import malclient

    client = malclient.Client()
    client.init(access_token="<your-access-token>")
    
    # search anime, returns list
    anime = client.search_anime("cowboy", limit=20)
    for ani in anime:
        # print all attributes as dictionary for refference
        print(ani)
        # print attribute
        print(ani.title)

    # Get individual anime by ID
    anime = client.get_anime_details(1)
    print(anime.title)
    print(anime)

    # Update Myanime List based off of search results
    anime = client.search_anime("dorohedoro", limit=1)
    my_status = {
        'status': 'watching',
        'score': 7
    }
    status = client.update_anime_my_list_status(anime[0].id, my_status)

    # get my user info
    print(client.get_user_info())
    # get my anime list (you can get other users by name)
    for anime in client.get_user_anime_list():
        print(anime.title, anime.score)

    # Update manga list based off search results
    manga = client.search_manga('doro')
    my_status = {
        'status': 'reading',
        'score': 9
    }
    client.update_manga_my_list_status(manga[0].id, my_status)
```

#### To Dos
- [] Pagination support
- [] Alternative authentication methods when they become available upstream
- [] Unit and Integration tests
- [] Fix Token Refresh Method
