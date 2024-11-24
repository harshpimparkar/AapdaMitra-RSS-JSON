from newspaper import Article
import json

# Global variable to store the results
scraped_articles = []

def parse_article(url):
    """
    Parse a single article and extract its details.
    :param url: The URL of the article to scrape.
    :return: A dictionary containing article details or an error message.
    """
    try:
        # Initialize and download the article
        article = Article(url)
        article.download()
        article.parse()

        # Get the publish date if available
        date = None
        if article.publish_date:
            date = article.publish_date.strftime("%Y-%m-%d")

        # Return the article details
        return {
            "title": article.title,
            "content": article.text,
            "text_length": len(article.text),
            "publish_date": date,
            "url": url,
            "status": "success"
        }

    except Exception as e:
        return {
            "url": url,
            "status": "failed",
            "error": str(e)
        }

def scrape_articles(urls):
    """
    Scrape multiple articles from the list of URLs.
    :param urls: List of URLs to scrape.
    :return: A list of results from scraping.
    """
    global scraped_articles  # Ensure we're modifying the global variable
    scraped_articles.clear()  # Clear the previous results before scraping new ones
    results = []
    for url in urls:
        result = parse_article(url)
        results.append(result)
        store_results_in_variable(result)  # Store the results in the global variable
    return results

def store_results_in_variable(result):
    """
    Store results in a global variable.
    :param result: A dictionary containing article details.
    """
    global scraped_articles
    scraped_articles.append(result)

def get_scraped_results():
    """
    Get the stored scraped results.
    :return: A list of scraped articles.
    """
    return scraped_articles
