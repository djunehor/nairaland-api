Nairaland API
=========

####Please open issues and make pull requests regarding this at [makinde2013/nairaland-api](http://github.com/makinde2013/nairaland-api).

An unofficial API for Nairaland.

### Table of Contents
* [API Usage](#api-usage)
* [Features](#features)
* [Installation](#installation)
* [Contributing](#contributing)

# API Usage
### API Base URL: `https://pynairaland.herokuapp.com` (Inactive for now)

## Endpoints Summary
* GET: [`/home`](#api-home)
* GET: [`/categories`](#api-categories) {depth=Int}
* GET: [`/categories/<category>/topics`](#api-categories-topics) {page=Int}

* GET: [`/topics/<topic>/posts`](#api-topics-posts) {page=Int}
* GET: [`/topics/trending`](#api-topics-trending) {page=Int}
* GET: [`topics/new`](#api-topics-new) {page=Int}
* GET: [`/posts/recent`]('#api-posts-recent) {page=Int}
* POST: [`/search`](#api-search) {term: String, page=Int, board=Int}
    
* GET: [`/users/<user>`](#api-user)
* GET: [`/users/<user>/posts`](#api-user-posts) {page=Int}
* GET: [`/users/<user>/topics`](#api-user-topics) {page=Int}

###### AUTHENTICATED ROUTES
* GET: [`/user/followed_boards`](#api-user-followed-boards) {page=Int}
* GET: [`/user/followed_topics`]('#api-user-followed-topics) {page=Int}
* GET: [`/user/likes_and_shares`](#api-user-like-share) {page=Int}
* GET: [`/user/mentions`](#api-user-mentions) {page=Int}
* GET: [`/user/following_posts`](#api-user-following-posts) {page=Int}
* GET: [`user/shared_with`](#api-user-shared-with) {page=Int}
* POST: [`user/topics/<board>/new`](#api-user-topic-new) {*title=String, *content=String}
* POST: [`user/posts/<topic>/new`](#api-user-post-new) {*content=String, follow=Boolean}
* POST: [`user/posts/like`](#api-user-post-like) {*post_id=Int, unlike=Boolean}
* POST: [`user/posts/share`](#api-user-post-share) {*post_id=Int, unshare=Boolean}

### GET: `home`
#### api-home
Example usage: `GET http://<BASE_URL>/home`

Example result:
```json
{
  "data": [
    {
      "id": "5425224",
      "title": "Europa League:  Manchester United Vs Astana  Today (0 - 0) Live",
      "url": "https://www.nairaland.com/5425224/manchester-united-vs-astana-europa#82384860"
    },
    {
      "id": "5426155",
      "title": "AMAA 2019: 'King Of Boys’, ‘The Delivery Boy’ Lead Nominations (See Full List)",
      "url": "https://www.nairaland.com/5426155/amaa-2019-nominees-nomination-list"
    }
    ]  
}
```

### GET: `/categories`
Get all categories
#### api-categories
#####`GET http://BASE_URL/categories`
##### `GET http://BASE_URL/categories?depth=2`

Output (excerpt):
```json
{
  "data": [
    {
      "id": "9",
      "name": "Nairaland / General",
      "sub_categories": [],
      "title": " class=g",
      "url": "https://nairaland.com/nairaland"
    },
    {
      "id": "12",
      "name": "Entertainment",
      "sub_categories": [],
      "title": "Entertainment threads that won't fit into any child board. class=g",
      "url": "https://nairaland.com/entertainment"
    },
    {
      "id": "8",
      "name": "Science/Technology",
      "sub_categories": [],
      "title": " class=g",
      "url": "https://nairaland.com/science"
    }
  ]
}
```

### GET: `/categories/<category>/topics`
Get all topics in a category
#### api-category-topics
#####`GET http://BASE_URL/categories/<category>/topics`
##### `GET http://BASE_URL/categories/<category>/topics?page=2`

Output (excerpt):
```json
{
  "data": [
    {
      "creator": {
        "name": "Seun",
        "url": "https://nairaland.com/seun"
      },
      "id": "2792995",
      "last_post_creator": {
        "name": "Youthleader22",
        "url": "https://nairaland.com/youthleader22"
      },
      "last_post_time": "2019-09-17 18:44:00",
      "posts": "3783",
      "title": "Nairaland Says No To Secessionists",
      "url": "https://nairaland.com/2792995/nairaland-says-no-secessionists",
      "views": "410702"
    },
    {
      "creator": {
        "name": "PaChukwudi44",
        "url": "https://nairaland.com/pachukwudi44"
      },
      "id": "5425996",
      "last_post_creator": {
        "name": "Raddie",
        "url": "https://nairaland.com/raddie"
      },
      "last_post_time": "2019-09-19 20:46:00",
      "posts": "85",
      "title": "P&ID: We Will Continue Efforts To Identify, Seize Nigerian Assets",
      "url": "https://nairaland.com/5425996/p-id-continue-efforts-identify",
      "views": "9238"
    }
    ],
  "meta": {
    "next_page": 1,
    "page": 0,
    "per_page": 64,
    "previous_page": 0,
    "total_entries": 640,
    "total_pages": 10
  }
}
```

### GET: `/topics/<topic>/posts`
Get all posts in a topic (thread)
#### api-topic-posts
#####`GET http://BASE_URL/topics/<topic>/posts`
##### `GET http://BASE_URL/topics/<topic>/posts?page=2`

Output (excerpt):
```json
{
  "data": [
    {
      "content": "Coolest like Thermocool or what... Onikan will soon be Moved to Abuja to Generate some revenue....  ",
      "date_posted": "2019-09-19 20:23:00",
      "likes": 0,
      "shares": 0,
      "user": {
        "name": "inoki247",
        "url": "https://nairaland.com/inoki247"
      }
    },
    {
      "content": "Hmmm",
      "date_posted": "2019-09-19 00:00:00",
      "likes": 0,
      "shares": 0,
      "user": {
        "name": "benkz001",
        "url": "https://nairaland.com/benkz001"
      }
    }
    ],
  "meta": {
    "next_page": 1,
    "page": 0,
    "per_page": 64,
    "previous_page": 0,
    "total_entries": 640,
    "total_pages": 10
  }
}

```

### GET: `/users/<user>`
Get user profile
#### api-user
#####`GET http://BASE_URL/users/<user>`

Output (excerpt):
```json
{
  "data": {
    "follower_count": 1,
    "followers": [
      {
        "name": "Seun",
        "url": "https://www.nairaland.com/seun"
      }
    ],
    "gender": "m",
    "last_seen": "2019-09-19 20:50:00",
    "location": null,
    "name": "bolaji21",
    "personal_text": "God is good",
    "post_count": "688",
    "sections_most_active_in": [],
    "signature": null,
    "time_registered": "2011-08-11 00:00:00",
    "time_spent_online": "28 days & 1 hour",
    "topic_count": "19",
    "twitter": null,
    "url": "https://nairaland.com/bolaji21"
  }
}

```

# Features
### Currently implemented
* Front page topics
* Recent topics
* Trending topics
* Latest posts (comments)
* Categories
* Category topics
* User Profile
* User posts
* User Topics
* User followed boards
* User followed topics
* Posts by who user is following
* Posts shared to user
* Search
* Create topic
* Create post (comment) with quote
* Like/Unlike post (comment)
* Share/Unshare post (comment)

### Todo
* Unit tests
* Cache data with memcached

# Installation
You will need [Python 3](https://www.python.org/download/). [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies. It is recommended that you run in a virtual environment. You can create a virtual environment by running `py -m venv [folder-name]`
- Clone the repo `https://github.com/makinde2013/nairaland-api`
- Install requirements `pip install -r requirements.txt`
- Download chrome driver for your OS [here](https://chromedriver.chromium.org/) and place in the project directory i.e same place server.py is. For windows, the name should be `chromedriver.exe`, while for LINUX, the name should be `chromedriver`
- Rename `.env.example` to `.env` and update with your nairaland login. If you're on LINUX, set LINUX=True

To run the API locally:
```bash
$ pip install -r requirements.txt
$ python server.py
```

# Contributing
Feel free to submit a pull request or an issue!  
Nairaland API uses the [pynairaland package](https://github.com/makinde2013/pynairaland).
