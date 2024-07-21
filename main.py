from googleapiclient.discovery import build

api_key = 'AIzaSyBHcKYf0GyzFD0KVPllI1kqGq4-rHu2emw'
youtube = build(
	'youtube',
	'v3',
	developerKey=api_key
)

# Make a request to YouTube API
request = youtube.channels().list(
	part='statistics',
	id='UCCgLoMYIyP0U56dEhEL1wXQ'
)

# Get a response from API
response = request.execute()

print(response)