#from config.settings import notionToken, database_id
from notion_client import Client

# Class that handlers Notion API
class NotionHandler:
    
    # Constructor 
    def __init__(self, notionToken, database_id):
        self.notionToken = notionToken
        self.database_id = database_id
        self.client = Client(auth=notionToken)

    # Retrieves complete database
    def get_database(self):
        response = self.client.databases.retrieve(database_id= self.database_id)
        return response
    
    # Retrieves Ready to Upload Pages 
    def get_ready_pages_ids(self):
        response = self.client.databases.query(database_id= self.database_id, filter={"property": "Status", "status": {"equals": "Ready to Upload"}})
        pages = response["results"]
        page_ids = []
        for page in pages:
            page_id = page["id"]
            page_ids.append(page_id)            
        return page_ids

    # Method that retrieves needed information for each video  
    def get_ready_pages_metadata(self):
        response = self.client.databases.query(database_id= self.database_id, filter={"property": "Status", "status": {"equals": "Ready to Upload"}})
        pages = response["results"]
        for page in pages:
            title   = page["properties"]["Short Title"]["title"][0]["plain_text"] 
            description = page["properties"]["Short Description"]["rich_text"][0]["plain_text"]
            game = page["properties"]["Game"]["status"]["name"]
            filename = page["properties"]["Filename"]["rich_text"][0]["plain_text"]
            upload_date = page["properties"]["Upload Date"]["date"]["start"]
            recording_date = page["properties"]["Recording Date"]["date"]["start"]
            print(title + " - " + description + " - " + game + " - " + filename + " - " + upload_date + " - " + recording_date)     
    
    # Updates pages with its url once uploaded
    def update_page_with_url(self, page_id, youtube_url):
        response = self.client.pages.update(page_id= page_id, properties= {"Youtube URL": {"url": youtube_url}})
        return response 
    
    # Sets Status from "Ready to Upload" to "Uploaded" 
    def set_as_uploaded(self, page_id):
        response = self.client.pages.update(page_id= page_id, properties={"Status": {"status": {"name": "Uploaded"}}})
        return response


