from bs4 import BeautifulSoup
import requests as req


class ScrapeClass:

    """
        Class that makes request to thehackernews.com
        and scrapes and parses the popular headlines.
        the scraper fetches the title, url and image url
        and returns this in a dictionary
    """

    def __init__(self):
        self.url = "https://thehackernews.com/"
        self.articles = dict()
        self.soup = None


    def validate_request(self):
        # Method that handles the request to hackernews

        request = req.get(self.url)
        if request.status_code == 200:
            self.soup =  BeautifulSoup(request.text, 'html.parser')
            return True
        else:
            return False


    def parse_articles(self):

        # Fetch the top articles
        top_articles = self.soup.find_all("div", {"class": "cf pop-article clear"})

        for article in top_articles:

            # fetch article title from soup
            article_title = article.find("div", {"class": "pop-title"} ).text

            # Store the title as key and a dict as value to store the image & article url
            self.articles[article_title] = dict()

            # fetch article url and image from soup
            self.articles[article_title]['article_url'] = article.find("a", {"class": "pop-link"})['href']
            self.articles[article_title]['image_url'] = article.find("img", {"class": "lazyload"})['data-src']

        return self.articles