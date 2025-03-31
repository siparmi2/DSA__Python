"""
coderbyte challenge for printing the count of how many keys with 'age' are greater than or equal to 50.
"""
import requests
import re

def count_age_above_50():
    # Make GET request to the API endpoint
    response = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
    data = response.json()
    
    # Extract the data string
    data_str = data['data']
    
    # Find all age values using regular expression
    ages = re.findall(r' age=(\d+)', data_str)
    
    # Convert ages to integers and count those >= 50
    count = sum(1 for age in map(int, ages) if age >= 50)
    
    # Print the final count
    print(count)

# Call the function
count_age_above_50()