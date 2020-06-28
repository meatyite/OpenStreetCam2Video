# OpenStreetCam2Video
Python script to take tracks from OpenStreetCam and turn them into stopmotion videos<br/>
## Instructions
*YOU NEED FFMPEG AND PYTHON 3 FOR THIS.*<br/>
*CURRENTLY THE BATCH SCRIPTS REMOVE THE NEED TO TYPE LONG COMMANDS, BUT THEY ONLY WORK ON WINDOWS. I NEED PEOPLE TO PULL REQUEST ME A TRANSLATION TO SHELL SCRIPT.* <br/>

1) Download and extract the repository
2) Go on [OpenStreetCam.org] and find a track you would like to turn into a video. Copy its' ID.
3) (On windows) open get_images.py, enter the track id. (Linux/Other) Open terminal, type `python3 get_images.py (track id)`.
4) Once done, (On windows) open compile_video.bat, enter folder and framerate. (Linux/Other) Open terminal, cd into track folder, type `ffmpeg -start_number 0 -framerate 15 -i %d.jpg -vcodec mpeg4 video.mp4`
5) Done! video will be created in the track folder.
