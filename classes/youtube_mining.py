class Youtube:
    
    #Initialize developer_key with Google API developer key
    def __init__(self, dev_key):
        self.developer_key = dev_key

    #Get Comments and authors from a Youtube Videos through Youtube Data API
    def request_comment(self, link, max_result, search_term):
        comment_collection = defaultdict(dict)
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = self.developer_key)

        #Setting up API request to get comment threads
        request = youtube.commentThreads().list(
            part="snippet",
            maxResults= max_result,
            searchTerms=search_term,
            textFormat="plainText",
            videoId=link
        )
        response = request.execute()
        for x, val in enumerate(response["items"]):
            comment_collection[x]['content'] = (str(val["snippet"]["topLevelComment"]["snippet"]["textDisplay"]))
            comment_collection[x]['author'] = (str(val["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]))
        return comment_collection
    
    #Get Video details, including title, description and thumbnail from Youtube Data API
    def request_video_detail(self, link):
        video_detail = defaultdict(dict)       
        link_get = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id="+link+"&key=" + self.developer_key
        response = urllib.request.urlopen(link_get)
        data = json.loads(response.read())
        for x, val in enumerate(data["items"]):
            video_detail[x]['title'] = (str(val["snippet"]["title"]))
            video_detail[x]['description'] = (str(val["snippet"]["description"]))
            video_detail[x]['thumbnail'] = (str(val["snippet"]["thumbnails"]["medium"]["url"]))           
        return video_detail
