from dateutil.parser import parse
import requests
import os
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id', help='ID of the YouTube Playlist')
args = parser.parse_args()
api_key = ''#Google API Key for YouTube
playlist_vid_id = []
seconds = 0
hours = 0
minutes = 0
seconds = 0
req = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&playlistId={}&maxResults=50&key={}'.format(args.id, api_key)).content
reqjson = json.loads(req)
total_results = reqjson['pageInfo']['totalResults']
for x in range(total_results):
    playlist_vid_id.append(reqjson['items'][x]['contentDetails']['videoId'])
for each in playlist_vid_id:
    req = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id={}&key={}'.format(each, api_key)).content
    reqjson = json.loads(req)
    iso_time = reqjson['items'][0]['contentDetails']['duration']
    iso_time = str(iso_time).strip('PT')
    datetime = parse(iso_time)
    hours += datetime.hour
    minutes += datetime.minute
    seconds += datetime.second
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("Playlist: {}\nHas a length of\n{} Hours\n{} Minutes\n{} Seconds".format(args.id, hours, minutes, seconds))
