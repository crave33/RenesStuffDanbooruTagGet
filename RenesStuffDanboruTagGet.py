import requests
import json
from typing import Any, Dict

class DanbooruTagFetcher:
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {"required": {"image_id": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("tags", "prompt")
    FUNCTION = "fetch_tags"  # This tells ComfyUI which method to run
    CATEGORY = "Renes_Stuff"

    def fetch_tags(self, image_id: str):
        if not image_id:
            return ("", "[ERROR]: Image ID cannot be empty!")

        base_url = 'https://danbooru.donmai.us/posts'
        response = requests.get(f'{base_url}/{image_id}.json')
        
        if response.status_code != 200:
            return ("", f"[ERROR]: {response.status_code}")
        
        data = json.loads(response.text)
        
        character = data.get('tag_string_character', "")
        origin = data.get('tag_string_copyright', "")
        tags = data.get('tag_string_general', "")
        prompt = f'{character} {origin} {tags}'
        
        return (tags.replace(" ", ", "), prompt.replace(" ", ", "))

NODE_CLASS_MAPPINGS = {"DanbooruTagFetcher": DanbooruTagFetcher}
NODE_DISPLAY_NAME_MAPPINGS = {"DanbooruTagFetcher": "Danbooru Tag Fetcher"}