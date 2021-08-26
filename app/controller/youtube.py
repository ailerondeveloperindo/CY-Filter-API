import os
import googleapiclient.discovery 
import urllib.request, json
from collections import defaultdict
from model.youtube_model import Youtube_Model

class Youtube:
    #Initialize developer_key with Google API developer key
    def __init__(self):
        yt = Youtube_Model()
        self.developer_key = yt.get_devkey()
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.youtube = googleapiclient.discovery.build(
        self.api_service_name, self.api_version, developerKey = self.developer_key)


    #Get Comments and authors from a Youtube Videos through Youtube Data API, flowchart of this can be found here
    def request_comment(self, link, max_result = 100, search_term = ""):
        comment_col = defaultdict(dict)
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        #Setting up API request to get comment threads
        request = self.youtube.commentThreads().list(
            part="snippet",
            maxResults= max_result,
            searchTerms=search_term,
            textFormat="plainText",
            videoId=link
        )
        response = request.execute()
        #Populate comment_col dictionary with detail of each comments
        for x, val in enumerate(response["items"]):
            comment_col_length = len(comment_col)
            detail_array = val["snippet"]["topLevelComment"]["snippet"]
            comment_col.update({comment_col_length : val["snippet"]["topLevelComment"]["snippet"]})

        #Do another request if nextPageToken exists 
        while response.get("nextPageToken") != None:
            request = self.youtube.commentThreads().list(
                part="snippet",
                maxResults= max_result,
                searchTerms=search_term,
                textFormat="plainText",
                videoId=link,
                pageToken = response["nextPageToken"]
            )
            response = request.execute()
            for x, val in enumerate(response["items"]):
                comment_col_length = len(comment_col)
                detail_array = val["snippet"]["topLevelComment"]["snippet"]
                comment_col.update({comment_col_length : val["snippet"]["topLevelComment"]["snippet"]})
            if response.get("nextPageToken") == None:
                break
        return comment_col
    
    #Get Video details, including title, description and thumbnail from Youtube Data API
    def request_video_detail(self, link):
        video_detail = defaultdict(dict)       
        link_get = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id="+link+"&key=" + self.developer_key
        response = urllib.request.urlopen(link_get) #Sends request to Youtube Data API, response is in JSON format
        data = json.loads(response.read()) #Converts JSON response to Python Dictionary
        #Check if video exists, return message on false
        if data["pageInfo"]["totalResults"] == 0:
            return "Invalid Video ID"
        else:
            for x, val in enumerate(data["items"]):
                video_detail[x]['title'] = (str(val["snippet"]["title"]))
                video_detail[x]['description'] = (str(val["snippet"]["description"]))
                video_detail[x]['thumbnail'] = (str(val["snippet"]["thumbnails"]["medium"]["url"]))           
            return video_detail