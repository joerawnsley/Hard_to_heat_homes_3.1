import os
from dotenv import load_dotenv

load_dotenv()
EPC_TOKEN = os.getenv("EPC_ENCODED_API_TOKEN")
OS_KEY = os.getenv("OS_API_KEY")

OS_BASE_URL = "https://api.os.uk/features/ngd/ofa/v1/collections/bld-fts-building-4/items?"
EPC_BASE_URL = 'https://epc.opendatacommunities.org/api/v1/domestic/search?'