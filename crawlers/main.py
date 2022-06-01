import json
import requests
import logging
from telebot import TeleBot
from decouple import config
from bs4 import BeautifulSoup


def get_reddit_top_info(subreddit, minimum_votes):
    headers ={
        'User-Agent': 'IdWall desafio Scrapper',
        'From': 'felipeduarte012@gmail.com'
    }
    page = requests.get(f"https://old.reddit.com/r/{subreddit}/top/?sort=top&t=day", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    attrs = {'class': 'thing'}
    all_posts = []
    for post in soup.find_all('div', attrs=attrs):
        title = post.find('a', class_="title").text
        author = post.attrs['data-author']
        likes = post.attrs['data-score']
        link = f"https://old.reddit.com{post.attrs['data-permalink']}"
        all_posts.append({
            'subreddit': subreddit,
            'title': title,
            'likes': likes,
            'author': author,
            'link': link
        })
    filtered_posts = filter_posts_by_votes(all_posts, minimum_votes)
    return filtered_posts


def filter_posts_by_votes(posts, minimum_votes):
    return [x for x in posts if int(x.get('likes')) > int(minimum_votes)]


def gather_various_reddit_top_info(reddits: str, min_votes):
    reddits = reddits.split(';')
    result = []
    for subreddit in reddits:
        result += get_reddit_top_info(subreddit, min_votes)
    return result


bot = TeleBot(config('DUARTE_BOT_TOKEN'), parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_start_message(message):
    bot.reply_to(message, 'Oi eu sou um bot feito para o desafio IdWall')


@bot.message_handler(commands=['NadaPraFazer', 'nadaprafazer', 'ndpf'])
def send_nothing_to_do_message(message):
    try:
        input_splitted = message.text.split(' ')
        subreddits = input_splitted[1]
        min_votes = 5000
        if len(input_splitted) > 2:
            min_votes = input_splitted[2]
        results = gather_various_reddit_top_info(subreddits, min_votes)
        for result in results:
            bot.reply_to(message, json.dumps(result, indent=4, sort_keys=False))
    except IndexError as e:
        print('Entrada não contém os parametros corretos')
        raise e
    except BaseException as e:
        print('Erro desconhecido ao tentar recuperar os subreddits')
        raise e


bot.infinity_polling()
