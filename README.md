# City_handbook

City_handbook is a Django-powered web application that serves as a repository for places and information about the city. The app provides an API that allows users to browse different categories of places based on location, name or address. For example, users can search for cafes, restaurants or museums based on the desired location.


## Requirements

* Python 3.6+
* Django 3.0+
* Django-REST-Framework 3.12+

## Installation

To install City_handbook, first clone the GitHub repository:

```
$ git clone https://github.com/Azimjonm2333/city_handbook.git
```

Then navigate into the project directory:

```
$ cd city_handbook
```

Next, install the project dependencies:

```
$ pip install -r requirements.txt
```

Finally, run the migrations to set up the database:

```
$ python manage.py migrate
```

## Getting started

To get started with the project, start the Django development server:

```
$ python manage.py runserver
```

Next, open a browser and navigate to http://localhost:8000/api.

## API Endpoints

Below are the available API endpoints:

* `/api/places` – Get a list of all places
* `/api/places/{id}` – Get a specific place by ID
* `/api/places/category/{id}` – Get all places based on a specific category ID
* `/api/places/city/{id}` – Get all places based on a specific city ID
* `/api/places/name/{name_place}` – Search for places by name
* `/api/places/address/{name_place}` – Search for places by address

## Usage

City_handbook provides an easy-to-use API for browsing and searching places in the city. The API can be accessed via HTTP requests using any tool that supports HTTP, like web browsers, cURL or JavaScript libraries like axios.


Here's an example of how to use the API to retrieve a list of all places:

```
import requests

response = requests.get('http://localhost:8000/api/places')
print(response.json())
```

This would output a JSON-encoded list of all the places in the repository.



## Info

**Default Login: `admin`**

**Password: `admin`**
