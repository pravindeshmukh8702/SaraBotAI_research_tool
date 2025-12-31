import requests
from bs4 import BeautifulSoup
from datetime import datetime

class WebScraper:
    @staticmethod
    def get_article_metadata(url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('meta', property='og:title') or soup.title
            title = title['content'] if hasattr(title, 'has_attr') and title.has_attr('content') else str(title.string) if title else "Untitled Article"
            
            description = soup.find('meta', property='og:description') or soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else "No description available"
            
            return {
                "title": title[:200] + "..." if len(title) > 200 else title,
                "description": description[:200] + "..." if len(description) > 200 else description,
                "url": url,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            return {
                "title": "Untitled Article",
                "description": f"Error fetching metadata: {str(e)}",
                "url": url,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }