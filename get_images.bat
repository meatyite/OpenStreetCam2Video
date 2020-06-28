@echo off
set /p id="Enter track ID:"
py get_images.py %id%
pause