import requests
import time

def check_website_status(url):
    """Check if a website is up and return the status code."""
    # Add https:// if not included
    if not url.startswith('http'):
        url = 'https://' + url
        
    try:
        # Try to connect to the website
        response = requests.get(url, timeout=5)
        return {
            'url': url,
            'status_code': response.status_code,
            'online': True,
            'response_time': response.elapsed.total_seconds()
        }
    except requests.exceptions.RequestException:
        # Handle any exceptions that occur
        return {
            'url': url,
            'status_code': None,
            'online': False,
            'response_time': None
        }

# Demo usage
if __name__ == "__main__":
    # List of websites to check
    websites = []
    
    # Get user input
    print("Enter websites to check (one per line, blank line to finish):")
    while True:
        site = input("> ")
        if not site:
            break
        websites.append(site)
    
    # If no sites were entered, use some examples
    if not websites:
        websites = ["google.com", "example.com", "thissiteprobablydoesntexist123456789.com"]
        print("Using example websites:", ", ".join(websites))
    
    # Check each website
    print("\nChecking website status...")
    for site in websites:
        result = check_website_status(site)
        
        if result['online']:
            print(f"✅ {result['url']} - Status code: {result['status_code']}, " 
                  f"Response time: {result['response_time']:.2f}s")
        else:
            print(f"❌ {result['url']} - Offline or unreachable")
