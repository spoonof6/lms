import csv
from youtubesearchpython import VideosSearch

# Example: Try different limits to find the maximum feasible limit
limits_to_try = [10, 20, 30, 40, 50]

for limit in limits_to_try:
    videosSearch = VideosSearch('new criminal laws', limit=limit)
    print(f"Trying limit={limit}")
    try:
        results = videosSearch.result()
        print(f"Number of results: {len(results['result'])}")
    except Exception as e:
        print(f"Error occurred with limit={limit}: {e}")

# Choose the highest limit that works without errors
chosen_limit = 50  # Adjust based on successful testing

# Fetch data with the chosen limit
videosSearch = VideosSearch('new criminal laws', limit=chosen_limit)

# Extract relevant data from search results
data_to_write = []
for video in videosSearch.result()['result']:
    title = video['title']
    published_time = video['publishedTime']
    duration = video['duration']
    view_count = video['viewCount']['text']
    channel_name = video['channel']['name']
    video_link = f'https://www.youtube.com/watch?v={video["id"]}'

    data_to_write.append([title, published_time, duration, view_count, channel_name, video_link])

# Writing to CSV
csv_filename = 'videos_data.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header
    csv_writer.writerow(['Title', 'Published Time', 'Duration', 'View Count', 'Channel Name', 'Video Link'])
    # Write data
    csv_writer.writerows(data_to_write)

print(f'CSV file "{csv_filename}" has been created successfully.')
