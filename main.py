import schedule
import time
from scraper import ScrapeClass
from mailer import create_email, send_email


def main():
    scraper = ScrapeClass()

    # Validate if scraper works, parse articles
    # construct the email and send it
    if scraper.validate_request():
        articles = scraper.parse_articles()
        email_text = create_email(articles)
        send_email(email_text)


if __name__ == "__main__":
    schedule.every().monday.do(main)
    while True:
        schedule.run_pending()
        time.sleep(600)
