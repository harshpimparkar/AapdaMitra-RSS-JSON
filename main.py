from url_filter import DisasterNewsFilter
from page_scraper import scrape_articles
from json_creator import scraped_to_json

scrape_results = []

def main():
    #RSS feeds
    feeds = [
        'https://www.thehindu.com/news/national/feeder/default.rss',
        'https://ddnews.gov.in/en/tag/rss/',
        'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
        'https://feeds.feedburner.com/ndtvnews-latest',
        'https://zeenews.india.com/rss/india-national-news.xml',
        'https://www.cnbctv18.com/commonfeeds/v1/cne/rss/india.xml',
        'https://services.india.gov.in/feed/rss?cat_id=12&ln=en',
        'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml',
    ]
    
    #Disaster news filter
    disaster_filter = DisasterNewsFilter()
    
    # Filter disaster-related news URLs
    disaster_news_urls = disaster_filter.filter_disaster_news(feeds)
    print(f"\nFound {len(disaster_news_urls)} disaster-related news items:")
    for url in disaster_news_urls:
        print(url)
    
    # Scrape content from the filtered URLs
    print("\nScraping filtered articles...")
    global scrape_results
    scrape_results = scrape_articles(disaster_news_urls)
    
    # Print processing summary
    successful = sum(1 for result in scrape_results if result["status"] == "success")
    print("\nProcessing Summary:")
    print("-" * 50)
    print(f"Total articles processed: {len(scrape_results)}")
    print(f"Successfully parsed: {successful}")
    print(f"Failed: {len(scrape_results) - successful}")

if __name__ == "__main__":
    main()
    print("\nExample: Accessing scrape results in another module:")
    scraped_to_json(scrape_results)
    #print(scrape_results)
    
