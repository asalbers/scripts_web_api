
import requests
import time
import json
import logging
logging.basicConfig(filename='web_api.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def query_api():
    start_time = time.time()
    r = requests.get("http://localhost:8000/api/timeDate")
    end_time = time.time()
    TTLB = end_time - start_time
    if r.status_code != 200:
        logging.error("Received response %s%s from API other than 200", r.status_code, TTLB)
    else:
        logging.info("Success, response: %s TTLB: %s", r.status_code, TTLB)

query_api()
