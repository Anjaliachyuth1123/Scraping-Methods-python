from googleapiclient.discovery import build
import xlsxwriter

api_key = 'YOUR_API_KEY'
channel_id = 'UC0RhatS1pyxInC00YKjjBqQ'  # Example: GeeksforGeeksVideos

youtube = build('youtube', 'v3', developerKey=api_key)

# Get uploads playlist ID
channel_res = youtube.channels().list(
    part='contentDetails',
    id=channel_id
).execute()

playlist_id = channel_res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Get videos from uploads playlist
video_titles = []
video_views = []
video_durations = []

next_page_token = None
while True:
    pl_request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    )
    pl_response = pl_request.execute()

    video_ids = []
    for item in pl_response['items']:
        video_titles.append(item['snippet']['title'])
        video_ids.append(item['snippet']['resourceId']['videoId'])

    # Get video stats + duration
    vid_request = youtube.videos().list(
        part='statistics,contentDetails',
        id=','.join(video_ids)
    )
    vid_response = vid_request.execute()

    for item in vid_response['items']:
        video_views.append(item['statistics'].get('viewCount', '0'))
        duration = item['contentDetails']['duration'].replace('PT', '')
        video_durations.append(duration)

    next_page_token = pl_response.get('nextPageToken')
    if not next_page_token:
        break

# Write to Excel
workbook = xlsxwriter.Workbook('youtube_data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, "Title")
worksheet.write(0, 1, "Views")
worksheet.write(0, 2, "Duration")

for i, (title, view, dura) in enumerate(zip(video_titles, video_views, video_durations), start=1):
    worksheet.write(i, 0, title)
    worksheet.write(i, 1, view)
    worksheet.write(i, 2, dura)

workbook.close()
print("✅ Scraping completed using API. Data saved to youtube_data.xlsx")
