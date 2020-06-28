@echo off
set /p folder="Enter folder (tab):"
set /p fps="Enter framerate (default: 15)"
IF NOT DEFINED fps SET "fps=15"
cd %folder%

ffmpeg -start_number 0 -framerate %fps% -i %%d.jpg -vcodec mpeg4 video.mp4
start video.mp4
pause