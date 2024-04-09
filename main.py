import requests

url = (
    "https://newsapi.org/v2/everything?q=tesla&from=2024-03-09&sortBy=publishedAt&" 
    "apiKey=da82b67ed137451ab20fe574f738a71e"
)

# make request
request = requests.get(url)
# get json from response data
content = request.json()

# access articles titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
