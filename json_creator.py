import json


def scraped_to_json(data):
    """ Save scrape results to a JSON file. """
    try:
        with open('scrape_results.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("\nResults saved to 'scrape_results.json'")
    except Exception as e:
        print(f"Error saving results to JSON: {e}")