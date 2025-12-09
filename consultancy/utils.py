import requests

def get_consultancy_services():
    """Fetches a list of available services from the Consultancy API."""
    api_url = "http://127.0.0.1:8000/consultancy/"  # Make sure this URL is correct
    
    try:
        response = requests.get(api_url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status() 
        
        # Parse the JSON response
        services_data = response.json()
        return services_data
        
    except requests.exceptions.RequestException as e:
        # Handle connection errors, timeouts, etc.
        print(f"Error connecting to the Consultancy API: {e}")
        return None