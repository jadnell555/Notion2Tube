import os
from config.settings import notionToken, database_id, base_path
from src.notion_handler import NotionHandler
from pprint import pprint

#main function
def main(): 
    ssdConnected = os.path.exists(base_path) # checks if the path exists 

    # Check if SSD is connected
    if ssdConnected:
        print("SSD Connected")

    #Instantiates NotionHandler Class
    notion = NotionHandler(notionToken, database_id) 
    
    #For loop that receives the array of page_ids 
        # Method that gets needed information for each video
        # Uploader.py 
        # update_page_with_url
        #set_as_uploaded
    pageIds = notion.get_ready_pages_ids()
    index = 0

    for i in pageIds:
        notion.set_as_uploaded(pageIds[index])
        notion.update_page_with_url(pageIds[index], "test" + str(index) + ".url")
        index = index + 1 


if __name__ == "__main__":
    main()

"""
def youtubeAPI():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        
    )
    response = request.execute()

    print(response)
"""

# Error Handling   
# Notifications (Upload Succesful or not)