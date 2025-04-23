from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class FewShotPosts:
    def __init__(self, db_name="genai", collection_name="posts"):
        self.df = None
        self.unique_tags = None
        self.load_posts(db_name, collection_name)

    def load_posts(self, db_name, collection_name):
        mongo_uri = os.getenv("MONGO_URI")  # Add MONGO_URI in your .env
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]
        
        posts = list(collection.find({}, {"_id": 0}))  # Exclude _id from documents
        self.df = pd.json_normalize(posts)
        self.df['length'] = self.df['line_count'].apply(self.categorize_length)
        all_tags = self.df['tags'].apply(lambda x: x).sum()
        self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &
            (self.df['language'] == language) &
            (self.df['length'] == length)
        ]
        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Medium", "Hinglish", "Job Search")
    print(posts)
