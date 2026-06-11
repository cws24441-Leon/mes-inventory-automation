"""
Random Joke Generator using External API
Fetches jokes from multiple sources and displays them in various formats
"""

import requests
import json
import logging
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime

logger = logging.getLogger(__name__)


class JokeSource(Enum):
    """Available joke API sources"""
    OFFICIAL_JOKE_API = "official_joke_api"
    JOKE_API = "joke_api"
    RANDOM_USER_JOKE = "random_user_joke"


class JokeGenerator:
    """Main Joke Generator class using external APIs"""
    
    # API Endpoints
    APIS = {
        JokeSource.OFFICIAL_JOKE_API: "https://official-joke-api.appspot.com/random_joke",
        JokeSource.JOKE_API: "https://jokeapi.dev/random?format=json",
        JokeSource.RANDOM_USER_JOKE: "https://uselessfacts.jsph.pl/random.json?language=en"
    }
    
    TIMEOUT = 5  # seconds
    
    def __init__(self):
        """Initialize the joke generator"""
        self.session = requests.Session()
        self.last_joke = None
        logger.info("✓ Joke Generator initialized")
    
    def get_random_joke(self, source: JokeSource = JokeSource.OFFICIAL_JOKE_API) -> Optional[Dict]:
        """
        Fetch a random joke from the specified API source
        
        Args:
            source: The API source to use (default: OFFICIAL_JOKE_API)
            
        Returns:
            Dictionary containing joke data or None if failed
        """
        try:
            url = self.APIS[source]
            logger.info(f"Fetching joke from {source.value}...")
            
            response = self.session.get(url, timeout=self.TIMEOUT)
            response.raise_for_status()
            
            joke_data = response.json()
            self.last_joke = {
                'data': joke_data,
                'source': source.value,
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"✓ Successfully fetched joke from {source.value}")
            return joke_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch joke from {source.value}: {str(e)}")
            return None
    
    def format_official_joke(self, joke_data: Dict) -> str:
        """Format Official Joke API response"""
        return f"""
╔════════════════════════════════════════╗
║          Official Joke API             ║
╠════════════════════════════════════════╣
║ Type: {joke_data.get('type', 'N/A'): <30} ║
║                                        ║
║ Setup: {joke_data.get('setup', 'N/A')[:35]}
║ Punchline: {joke_data.get('punchline', 'N/A')[:33]}
║                                        ║
║ Joke ID: {str(joke_data.get('id', 'N/A')): <24} ║
╚════════════════════════════════════════╝
"""
    
    def format_joke_api(self, joke_data: Dict) -> str:
        """Format Joke API response"""
        categories = ", ".join(joke_data.get('category', []))
        
        if joke_data.get('type') == 'twopart':
            joke_text = f"Setup: {joke_data.get('setup', '')}\nDelivery: {joke_data.get('delivery', '')}"
        else:
            joke_text = joke_data.get('joke', 'N/A')
        
        return f"""
╔════════════════════════════════════════╗
║             Joke API                   ║
╠════════════════════════════════════════╣
║ Category: {categories: <28} ║
║ Safe: {str(joke_data.get('safe', 'N/A')): <33} ║
║                                        ║
║ {joke_text[:40]}
║                                        ║
╚════════════════════════════════════════╝
"""
    
    def format_random_fact(self, fact_data: Dict) -> str:
        """Format Random Fact API response"""
        fact = fact_data.get('text', 'N/A')[:80]
        
        return f"""
╔════════════════════════════════════════╗
║          Random Fact                   ║
╠════════════════════════════════════════╣
║                                        ║
║ {fact}
║                                        ║
║ Length: {str(len(fact_data.get('text', ''))): <26} ║
╚════════════════════════════════════════╝
"""
    
    def display_joke(self, joke_data: Dict, source: JokeSource) -> str:
        """Format and display joke based on source"""
        if not joke_data:
            return "❌ Failed to fetch joke"
        
        if source == JokeSource.OFFICIAL_JOKE_API:
            return self.format_official_joke(joke_data)
        elif source == JokeSource.JOKE_API:
            return self.format_joke_api(joke_data)
        elif source == JokeSource.RANDOM_USER_JOKE:
            return self.format_random_fact(joke_data)
        
        return json.dumps(joke_data, indent=2, ensure_ascii=False)
    
    def get_multiple_jokes(self, count: int = 3, source: JokeSource = JokeSource.OFFICIAL_JOKE_API) -> List[Dict]:
        """
        Fetch multiple jokes
        
        Args:
            count: Number of jokes to fetch
            source: The API source to use
            
        Returns:
            List of joke dictionaries
        """
        jokes = []
        for i in range(count):
            joke = self.get_random_joke(source)
            if joke:
                jokes.append(joke)
        
        logger.info(f"✓ Successfully fetched {len(jokes)} jokes")
        return jokes
    
    def search_jokes_by_type(self, joke_type: str = "general") -> Optional[Dict]:
        """
        Fetch a joke of a specific type using JokeAPI
        
        Args:
            joke_type: Type of joke (e.g., 'general', 'programming', 'knock-knock')
            
        Returns:
            Joke data or None if failed
        """
        try:
            url = f"https://jokeapi.dev/joke/{joke_type}?format=json"
            logger.info(f"Fetching {joke_type} joke...")
            
            response = self.session.get(url, timeout=self.TIMEOUT)
            response.raise_for_status()
            
            joke_data = response.json()
            logger.info(f"✓ Successfully fetched {joke_type} joke")
            return joke_data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch {joke_type} joke: {str(e)}")
            return None
    
    def get_joke_categories(self) -> Optional[List[str]]:
        """Get available joke categories from JokeAPI"""
        try:
            url = "https://jokeapi.dev/categories"
            logger.info("Fetching available categories...")
            
            response = self.session.get(url, timeout=self.TIMEOUT)
            response.raise_for_status()
            
            data = response.json()
            categories = data.get('categories', [])
            logger.info(f"✓ Found {len(categories)} categories")
            return categories
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch categories: {str(e)}")
            return None
    
    def save_joke_to_file(self, joke_data: Dict, filename: str = "jokes.json"):
        """Save joke to JSON file"""
        try:
            # Read existing jokes
            jokes = []
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    jokes = json.load(f)
            except FileNotFoundError:
                jokes = []
            
            # Add new joke
            jokes.append({
                'data': joke_data,
                'saved_at': datetime.now().isoformat()
            })
            
            # Save to file
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(jokes, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✓ Joke saved to {filename}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save joke: {str(e)}")
            return False
    
    def close(self):
        """Close the session"""
        self.session.close()
        logger.info("✓ Session closed")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    generator = JokeGenerator()
    
    try:
        # Get a random joke from Official Joke API
        print("\n" + "="*40)
        print("Random Joke #1 - Official Joke API")
        print("="*40)
        joke1 = generator.get_random_joke(JokeSource.OFFICIAL_JOKE_API)
        print(generator.display_joke(joke1, JokeSource.OFFICIAL_JOKE_API))
        
        # Get a programming joke
        print("\n" + "="*40)
        print("Random Joke #2 - Programming Joke")
        print("="*40)
        joke2 = generator.search_jokes_by_type("programming")
        print(generator.display_joke(joke2, JokeSource.JOKE_API))
        
        # Get available categories
        print("\n" + "="*40)
        print("Available Joke Categories")
        print("="*40)
        categories = generator.get_joke_categories()
        if categories:
            print(f"Categories: {', '.join(categories)}")
        
        # Save joke to file
        if joke1:
            generator.save_joke_to_file(joke1, "saved_jokes.json")
    
    finally:
        generator.close()
