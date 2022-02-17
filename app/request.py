from os import link
import urllib.request,json
from .news import News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news1(category):
    '''
    Function that gets the json response to our url request
    '''
    top_headlines='top-headlines'
    get_news_url = base_url.format(top_headlines,category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        image = news_item.get('urlToImage')
        published_date = news_item.get('publishedAt')
        content = news_item.get('content')
        link = news_item.get('url')
       

        if image:
            news_object = News(id,name,author,title,description,image,published_date,content,link)
            news_results.append(news_object)
    return news_results


def get_news2(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
             id = news_details_response.get('id')
             name = news_details_response.get('name')
             author = news_details_response.get('author')
             title = news_details_response.get('original_title')
             description = news_details_response.get('description')
             image = news_details_response.get('urlToImage')
             published_date = news_details_response.get('publishedAt')
             content = news_details_response.get('content')
             link = news_details_response.get('url')

             news_object = News(id,name,author,title,description,image,published_date,content,link)
    
    return news_object


def search_news(news_name):
    search_news_url = f'https://newsapi.org/v2/top-headlines?q={news_name}&apiKey={api_key}'
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)


    return search_news_results