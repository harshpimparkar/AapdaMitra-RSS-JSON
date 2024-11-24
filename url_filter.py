import feedparser
from typing import List

class DisasterNewsFilter:
    def __init__(self):
        # Keywords related to natural disasters
        self.natural_disaster_keywords = [
            'earthquake', 'flood', 'tsunami', 'hurricane', 'cyclone',
            'landslide', 'drought', 'wildfire', 'forest fire', 'volcanic',
            'tornado', 'storm', 'avalanche', 'heatwave', 'cold wave'
        ]
        
        # Keywords related to man-made disasters
        self.manmade_disaster_keywords = [
            'explosion', 'fire', 'collapse', 'crash', 'accident',
            'chemical leak', 'oil spill', 'nuclear', 'contamination',
            'derailment', 'building collapse', 'industrial accident'
        ]

    def fetch_feed(self, feed_url: str) -> List[dict]:
        """
        Fetch and parse an RSS feed.
        :param feed_url: The URL of the RSS feed.
        :return: A list of entries from the RSS feed.
        """
        try:
            feed = feedparser.parse(feed_url)
            return feed.entries
        except Exception as e:
            print(f"Error fetching feed {feed_url}: {str(e)}")
            return []

    def is_disaster_related(self, text: str) -> tuple:
        """
        Check if text contains disaster-related keywords.
        :param text: Text to analyze.
        :return: A tuple (is_disaster, disaster_type).
        """
        text = text.lower()
        
        # Check for natural disasters
        for keyword in self.natural_disaster_keywords:
            if keyword in text:
                return True, 'natural'
                
        # Check for man-made disasters
        for keyword in self.manmade_disaster_keywords:
            if keyword in text:
                return True, 'man-made'
                
        return False, None

    def filter_disaster_news(self, feeds: List[str]) -> List[str]:
        """
        Filter disaster-related news from multiple RSS feeds.
        :param feeds: A list of RSS feed URLs.
        :return: A list of links to disaster-related news articles.
        """
        disaster_news = []
        
        for feed_url in feeds:
            entries = self.fetch_feed(feed_url)
            
            for entry in entries:
                # Combine title and description for keyword search
                text_to_check = f"{entry.get('title', '')} {entry.get('description', '')}"
                
                is_disaster, disaster_type = self.is_disaster_related(text_to_check)
                
                if is_disaster:
                    disaster_news.append(entry.get('link', ''))
        
        return disaster_news
