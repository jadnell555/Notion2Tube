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
    def get_database(self, database_id):
        response = self.client.databases.retrieve(database_id= database_id)
        return response
    
    # Retrieves Ready to Upload Rows
    # EDIT to only get page ids and store them as an array
    def get_ready_to_upload(self, database_id):
        response = self.client.databases.query(database_id= database_id, filter={"property": "Status", "status": {"equals": "Ready to Upload"}})
        return response
    
    # Method that retrieves needed information for each video
    

    # Updates pages with its url once uploaded
    def update_page_with_url(self, page_id, youtube_url):
        response = self.client.pages.update(page_id= page_id, properties= {"Youtube URL": {"url": youtube_url}})
        return response 
    
    # Sets Status from "Ready to Upload" to "Uploaded" 
    def set_as_uploaded(self, page_id):
        response = self.client.pages.update(page_id= page_id, properties={"Status": {"status": {"name": "Uploaded"}}})
        return response


