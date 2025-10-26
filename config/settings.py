import os
from dotenv import load_dotenv

load_dotenv() # loads env

base_path = os.getenv('VIDEO_BASE_PATH') # gets base path contents
notionToken = os.getenv('NOTION_API_KEY') # gets notion Token
database_id = os.getenv('NOTION_DATABASE_ID') #gets notion database id

# Youtube API handler 
scopes = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtube.readonly",
          "https://www.googleapis.com/auth/youtubepartner"]


