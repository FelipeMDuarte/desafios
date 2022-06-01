import requests
from pprint import pprint
from bs4 import BeautifulSoup


def get_reddit_top_info(subreddit, minimum_votes=5000):
    headers ={
        'User-Agent': 'IdWall desafio Scrapper',
        'From': 'felipeduarte012@gmail.com'
    }
    page = requests.get(f"https://old.reddit.com/r/{subreddit}/top/?sort=top&t=day", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    attrs = {'class': 'thing'}
    all_posts = []
    for post in soup.find_all('div', attrs=attrs):
        title = post.find('p', class_="title").text
        author = post.find('a', class_="author").text
        likes = post.find("div", attrs={"class": "score likes"}).attrs['title']
        link = post.find('a', class_="bylink").attrs['href']
        all_posts.append({
            'subreddit': subreddit,
            'title': title,
            'author': author,
            'likes': likes,
            'link': link
        })
    filtered_posts = [x for x in all_posts if int(x.get('likes')) > minimum_votes]
    return filtered_posts


def gather_various_reddit_top_info(reddits: str):
    reddits = reddits.split(';')
    for subreddit in reddits:
        pprint(get_reddit_top_info(subreddit))


gather_various_reddit_top_info("worldnews;cats")
