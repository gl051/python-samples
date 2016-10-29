import requests
from bs4 import BeautifulSoup

URL_ROOT = "https://www.themoviedb.org/"

# Most popoular movie
endpoint = URL_ROOT + "discover/movie"

# payload
payload = {'sort_by': 'popularity.desc', 'primary_release_year': '2011'}
YEAR = 1945
payload['primary_release_year'] = YEAR

# use request to get the response from the API
try:
    response = requests.get(endpoint, payload)

    if response.status_code is not requests.codes.ok:
        print ('Error with this url {}'.format(r.url))
    else:
        # use BeautifulSoup to parse the HTML file returned
        soup = BeautifulSoup(response.text, "html.parser")
        # get all the tag title results
        # i.e <a alt="Desire" class="title result" href="/movie/86331" id="movie_86331" title="Desire">Desire</a>
        tags = soup.find_all('a', class_='title result')
        # get the title (form the tag value)
        titles = [tag.string for tag in tags]
        # print order by popularity
        print ("YEAR: {}".format(YEAR))
        for i, t in enumerate(titles, start=1):
            print ("#{} {}".format(i, t))
except Exception as ex:
    print ('Ops!')
    print (ex)
