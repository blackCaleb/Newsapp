from flask import render_template
from . import main
from flask import render_template,redirect,url_for
from ..request import get_news1,get_news2,search_news

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    current_news = get_news1('current')
    world_wide_news = get_news1('World')
    title = 'Home - Welcome to The best News Website Online'
    head = 'todays headlines'

    return render_template('index.html',title = title,head = head,current = current_news,world = world_wide_news)
    

@main.route('/news/<news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news2(id)
    title = f'{news.title}'
    return render_template('news.html',id = news_id,news = news,title = title)

@main.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)
