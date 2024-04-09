import requests

url = (
    "https://newsapi.org/v2/everything?q=tesla&from=2024-03-09&sortBy=publishedAt&" 
    "apiKey=da82b67ed137451ab20fe574f738a71e"
)

request = requests.get(url)

content = request.text

print(content)