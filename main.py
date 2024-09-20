from redvid import Downloader

dl = Downloader()
dl.max = True

dl.url = "https://www.reddit.com/r/21stCenturyHumour/comments/1dnc960/starman/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button"

# Setting the filename
dl.filename = "starman"


dl.download()






# # # Step 2: Load your 1-second video and the downloaded video
# from redvid import Downloader
# from moviepy.editor import VideoFileClip, concatenate_videoclips

# r_url=input("Enter the url : \n")
# # Step 1: Download the video from Reddit
# dl = Downloader()
# dl.max = True
# dl.overwrite = True

# dl.url = r_url
# dl.filename = "downloaded_video"
# dl.download()

# one_sec_video = VideoFileClip("/Users/satwikkumar/Desktop/redvid/Memes from Discord Farmhouse.mp4")
# downloaded_video = VideoFileClip("/Users/satwikkumar/Desktop/redvid/downloaded_video.mp4")

# # Step 3: Resize videos to match a specific resolution (e.g., 1920x1080)
# desired_resolution = (1080, 1920)  # Full HD resolution
# one_sec_video_resized = one_sec_video.resize(desired_resolution)
# downloaded_video_resized = downloaded_video.resize(desired_resolution)

# # Step 4: Concatenate the videos with audio
# final_video = concatenate_videoclips([one_sec_video_resized, downloaded_video_resized], method="compose")

# # Step 5: Save the final video with better quality and audio
# final_video.write_videofile(
#     "Memes from the Discord Farmhouse.mp4",
#     codec="libx264",
#     audio_codec="aac",
#     bitrate="3000k",  # Adjust the bitrate as needed
#     fps=30  # Ensure consistent frame rate
# )

# # Close the video clips to free up resources
# one_sec_video.close()
# downloaded_video.close()
# final_video.close()