import requests

# https://www.npoint.io/docs/2d57921a512f10430fb0
ENDPOINT = "https://api.npoint.io/2d57921a512f10430fb0"

class GetBlogPosts:
    def __init__(self) -> None:
        self.content = requests.get(url=ENDPOINT).json()
        self.n_posts = len(self.content)
    
    def get_single_post(self, id: int) -> dict:
        for post in self.content:
            if post['id'] == id:
                return post
    
    def get_post_info(self, id: int) -> tuple:
        post = self.get_single_post(id)
        return post["title"], post["subtitle"], post["body"]
