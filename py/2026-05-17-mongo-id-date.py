"""
Challenge: Mongo ID Date
Description: Given a MongoDB ID string, return its creation time as an ISO 8601 string.
The first 8 characters of a MongoDB ID represent a Unix timestamp (in seconds) encoded as a base-16 integer.
"""
import datetime


def mongo_id_to_date(s):
    timestamp_seconds = int(s[:8], 16)
    
    # Convert the parsed seconds into a UTC datetime object
    dt = datetime.datetime.utcfromtimestamp(timestamp_seconds)
    
    return dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")
