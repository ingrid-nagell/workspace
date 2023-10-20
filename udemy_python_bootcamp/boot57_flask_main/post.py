import requests


class Post:
    API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

    def __init__(self) -> None:
        self.response = requests.get(Post.API_URL).json()
        self.no_of_posts = len(self.response)

    def get_post(self, id):
        for post in self.response:
            if post["id"] == id:
                return post
