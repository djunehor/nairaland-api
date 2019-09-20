from flask import Flask, jsonify, request
from flask.ext.cache import Cache
from flask import Response
from nairaland import Nairaland
from nairaland import User
import logging
from logging import StreamHandler
from nairaland.browser import Browser
import os
from dotenv import load_dotenv

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
cache.init_app(app)

file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# log to stderr
import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)

# looad env
load_dotenv('.env')
heroku = False
if os.environ.get('Heroku') == 'True':
    from selenium import webdriver
    heroku = True
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = '/app/.apt/usr/bin/google-chrome-stable'


####################################################################
# Routes
####################################################################
@app.route('/', methods=['GET'])
def index_route():
    global heroku
    return jsonify({
        'author': 'Zacchaeus Bolaji',
        'author_url': 'https://djunehor.com',
        'base_url': 'https://pynairaland.herokuapp.com',
        'heroku' : heroku,
        'project': {
            'name': 'Nairaland API',
            'url': 'https://github.com/makinde2013/nairaland-api',
            'documentation': 'https://github.com/makinde2013/nairaland-api/blob/master/README.md',
            'issues': 'https://github.com/makinde2013/nairaland-api/issues'
        },
        'endpoints': {
            'front_page_topics': '/home',  # [method=GET]
            'categories': '/categories', # [method=GET] (depth=int)
            'recent_posts': '/recent', # [method=GET] (page=int)
            'topics_new': '/topics/trending', # [method=GET] (page=int)
            'topics_trending': '/topics/new', # [method=GET] (page=int)
            'user': '/users/{user}', # [method=GET]
            'user_posts': '/users/{user}/posts', # [method=GET] (page=int)
            'user_topics': '/users/{user}/topics', # [method=GET] (page=int)
            'category_topics': '/categories/{category}/topics', # [method=GET] (page=int)
            'topic_comments': '/topics/{topic}/comments', # [method=GET] (page=int)
            'search': '/search/{term}', # [method=GET] (term=String, board=int, page=int)

            # Authenticated endpoints
            'user_followed_topics': '/user/followed_topics', # [method=GET] (page=int)
            'user_followed_boards': '/user/followed_boards', # [method=GET] (page=int)
            'user_likes_and_shares': '/user/likes_and_shares', # [method=GET] (page=int)
            'user_mentions': '/user/mentions', # [method=GET] (page=int)
            'user_posts_following': '/user/posts_following', # [method=GET] (page=int)
            'user_shares': '/user/shares', # [method=GET] (page=int)
            'topic_new': '/topics/{board}/new', # [method=GET] (title=String, content=String)
            'post_new': '/posts/{topic}/new', # [method=GET] (post_id=int, content=String, follow=Boolean)
            'post_like': '/posts/{post}/like', # [method=GET]
            'post_share': '/posts/{post}/share', # [method=GET]
        }
    })

####################################################################
# Users
####################################################################
@cache.cached(timeout=300)
@app.route('/home', methods=['GET'])
def home_route():
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.front_page_topics())
    browser.driver.quit()
    return response


####################################################################
# Categories
####################################################################
@cache.cached(timeout=300)
@app.route('/categories', methods=['GET'])
def categories():
    if request.args.get('depth'):
        try:
            depth = int(request.args.get('depth'))
        except:
            depth = 0
    else:
        depth = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)

    response = jsonify(nairaland.categories(depth))
    browser.driver.quit()
    return response


####################################################################
# Trending Topics
####################################################################
@cache.cached(timeout=300)
@app.route('/topics/trending', methods=['GET'])
def topics_trending():
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.trending_topics(page))
    browser.driver.quit()
    return response

####################################################################
# New Topics
####################################################################
@cache.cached(timeout=300)
@app.route('/topics/new', methods=['GET'])
def topics_new():
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.new_topics(page))
    browser.driver.quit()
    return response

####################################################################
# Recent Posts
####################################################################
@cache.cached(timeout=300)
@app.route('/posts/recent', methods=['GET'])
def posts_new():
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.recent_posts(page))
    browser.driver.quit()
    return response


####################################################################
# User Profile
####################################################################
@cache.cached(timeout=300)
@app.route('/users/<user>', methods=['GET'])
def user_profile(user):
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response =  jsonify(nairaland.user(user))
    browser.driver.quit()
    return response


####################################################################
# User Posts
####################################################################
@cache.cached(timeout=300)
@app.route('/users/<user>/posts', methods=['GET'])
def user_posts(user):
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.user_posts(user, page))
    browser.driver.quit()
    return response


####################################################################
# User Topics
####################################################################
@cache.cached(timeout=300)
@app.route('/users/<user>/topics', methods=['GET'])
def user_topics(user):
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.user_topics(user, page))
    browser.driver.quit()
    return response


####################################################################
# Category Topics
####################################################################
@cache.cached(timeout=300)
@app.route('/categories/<category>/topics', methods=['GET'])
def category_topics(category):
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)
    response = jsonify(nairaland.category_topics(category, page))
    browser.driver.quit()
    return response


####################################################################
# Category Topics
####################################################################
@cache.cached(timeout=300)
@app.route('/topics/<topic>/posts', methods=['GET'])
def topic_posts(topic):
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)

    response = jsonify(nairaland.topic_posts(topic, page))
    browser.driver.quit()
    return response


####################################################################
# Search Term
####################################################################
@cache.cached(timeout=300)
@app.route('/search', methods=['POST'])
def search():
    if not request.form.get('term'):
        return jsonify({'error': 'term is required!'}), 422
    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0

    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    nairaland = Nairaland(browser)

    board = request.form.get('board') if request.form.get('board') else 0
    response = jsonify(nairaland.search(request.form.get('term'), board, page))
    browser.driver.quit()
    return response


# AUTHENTICATED ROUTES
####################################################################
# User Followed Topics
####################################################################
@cache.cached(timeout=300)
@app.route('/user/followed_topics', methods=['GET'])
def user_followed_topics():
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0
    response = jsonify(user.followed_topics(page))
    browser.driver.quit()
    return response


####################################################################
# User Followed Boards
####################################################################
@cache.cached(timeout=300)
@app.route('/user/followed_boards', methods=['GET'])
def user_followed_boards():
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0
    response = jsonify(user.followed_boards(page))
    browser.driver.quit()
    return response


####################################################################
# Posts containing user name (mention)
####################################################################
@cache.cached(timeout=300)
@app.route('/user/mentions', methods=['GET'])
def user_mentions():
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0
    response = jsonify(user.mentions(page))
    browser.driver.quit()
    return response


####################################################################
# Posts by people user is following
####################################################################
@cache.cached(timeout=300)
@app.route('/user/following_posts', methods=['GET'])
def user_following_posts():
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0
    response = jsonify(user.following_posts(page))
    browser.driver.quit()
    return response


####################################################################
# Posts Shared by people user is following
####################################################################
@cache.cached(timeout=300)
@app.route('/user/shared_with', methods=['GET'])
def user_shared_with():
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    if request.args.get('page'):
        try:
            page = int(request.args.get('page'))
        except:
            page = 0
    else:
        page = 0
    response = jsonify(user.shared_with(page))
    browser.driver.quit()
    return response


####################################################################
# Create new Topic
####################################################################
@cache.cached(timeout=300)
@app.route('/user/topics/<board>/new', methods=['POST'])
def user_topic_new(board):
    if not request.form.get('title') or not request.form.get('content'):
        return jsonify({'error': 'Title and Content are required!'}), 422
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    response = jsonify(user.new_topic(board, request.form.get('title'), request.form.get('content')))
    browser.driver.quit()
    return response


####################################################################
# Create new Post
####################################################################
@cache.cached(timeout=300)
@app.route('/user/posts/<topic>/new', methods=['POST'])
def user_post_new(topic):
    if not request.form.get('content'):
        return jsonify({'error': 'Content is required!'}), 422
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    response = jsonify(user.new_post(topic, request.form.get('content'), request.form.get('post_id'), request.form.get('follow')))
    browser.driver.quit()
    return response


####################################################################
# Like a Post
####################################################################
@cache.cached(timeout=300)
@app.route('/user/posts/like', methods=['POST'])
def user_post_like():
    if not request.form.get('post_slug'):
        return jsonify({'error': 'Post Slug is required!'}), 422
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    response = jsonify(user.like_post(request.form.get('post_slug'), request.form.get('unlike')))
    browser.driver.quit()
    return response


####################################################################
# Share a post
####################################################################
@cache.cached(timeout=300)
@app.route('/user/posts/share', methods=['POST'])
def user_post_share():
    if not request.form.get('post_slug'):
        return jsonify({'error': 'Post Slug is required!'}), 422
    # load browser for current request
    global heroku, chrome_options, CHROMEDRIVER_PATH
    if heroku:
        browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    else:
        browser = Browser(os.environ.get('LINUX'))
    user = User(browser)

    # login first
    if not browser.login(username=os.environ.get('NL_USERNAME'), user_pass=os.environ.get('NL_PASSWORD')):
        browser.driver.quit()
        return jsonify({'error': 'Login failed'})

    response = jsonify(user.like_post(request.form.get('post_slug'), request.form.get('unshare')))
    browser.driver.quit()
    return response


####################################################################
# Start Flask
####################################################################
if __name__ == '__main__':
    app.run(debug=True)
