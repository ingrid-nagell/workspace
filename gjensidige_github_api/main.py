from datetime import datetime
import requests
import os
import re
from loguru import logger


GITHUB_TOKEN = os.getenv("GITHUB_API_TOKEN")
REPOS_ENDPOINT = f"https://api.github.com/orgs/gjensidige/repos"


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
}


def get_dbt_repos(all_repos: list) -> list:
    """ Filter out repository names staring with "dbt-". """
    dbt_repos = [n for n in all_repos if re.match("dbt-", n)]
    return dbt_repos


def get_all_repos(url, headers: dict) -> list:
    """Uses the GitHub API to extract the names of all repositories in the organization.
    Returns the names as a list.
    """
    all_repos = []
    pages = 1
    start_time = datetime.now()

    while url:
        print(f"Page {pages}")
        
        params = {
            "per_page": 100,
            "page": pages
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            result = response.json()
            if len(result) == 0:
                url = None
            else:
                names = [e["name"] for e in result]
                all_repos.extend(names)
                pages += 1

        else:
            url = None
            logger.error(f"Failed to retrieve data. Status code: {response.status_code}")
            print(response.text)
            return None

    time_used = datetime.now() - start_time
    logger.info(f"Completion time: {time_used}")
    return all_repos


if __name__ == "__main__":
    all_repos = get_all_repos(REPOS_ENDPOINT, headers)
    dbt_repos  = get_dbt_repos(all_repos)
    print(dbt_repos)