import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import json

# scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# api_key = 

def main():

    # youtube = googleapiclient.discovery.build(
    #     'youtube', 'v3', developerKey=api_key )

    # request = youtube.search().list(
    #     part="snippet",
    #     maxResults=50, # how to search the top ?
    #     q="Candy,BAEKHYUN,cover,by", # comma-sperated values, track name + artist name 
    #     fields = 'items/snippet'
    # )
    # response = request.execute()


    ''' No need to print it out so 
    1- make the interface 
    2- place the vidos there 
    3- the template will render the info in synchronization '''

    for item in range(len(response['items'])):
        print(response['items'][item]["snippet"]['title'])


    # with open('youtube_results.txt', 'w') as f:
    #     json.dump(response['items']["snippet"]['title'], f, indent= 4)


if __name__ == "__main__":
    main()

    # what parameter to pass to get the videos 
    ''' 
     'kind': 'youtube#video'
     'regionCode' :

     '''


    # what to information to fetch from every video
    ''' 
     'channelTitle': 'Adinda Negara'
     'title' :
     'thumbnails''default' OR 'medium'
     'publishTime' 

     '''

class youtube:
    def __init__(self):
        # api_key =
        youtube = googleapiclient.discovery.build(
        'youtube', 'v3', developerKey= api_key )

    def search(self, q):
        request = self.youtube.search().list(
            part="snippet",
            maxResults=50, # how to search the top ?
            q=f"{q},cover,by", # comma-sperated values, track name + artist name 
            fields = 'items/snippet'
        )

        response = request.execute()

        return response

    def write(self, response):
        with open('youtube_results.txt', 'w'):
            json.dump(response['items']["snippet"]['title'], f, indent= 4)



