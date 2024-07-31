import os
from googleapiclient.discovery import build

def get_channel_data(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.channels().list(
        part='snippet,statistics',
        id=channel_id
    )
    
    response = request.execute()

    if 'items' in response:
        channel_data = response['items'][0]
        return channel_data
    else:
        print("Channel not found or API key invalid.")
        return None

def main():
    api_key = os.getenv('YOUTUBE_API_KEY')
    
    if not api_key:
        raise ValueError("API key not found. Please set the YOUTUBE_API_KEY environment variable.")
    
    channel_id = 'UCCgLoMYIyP0U56dEhEL1wXQ'

    channel_data = get_channel_data(api_key, channel_id)

    if channel_data:
        snippet = channel_data['snippet']
        statistics = channel_data['statistics']

        print("Channel Title:", snippet['title'])
        print("Channel Description:", snippet['description'])
        print("View Count:", statistics['viewCount'])
        print("Subscriber Count:", statistics['subscriberCount'])
        print("Video Count:", statistics['videoCount'])
    else:
        print("Failed to retrieve channel data.")

if __name__ == "__main__":
    main()