pip install discord

Rem this part of the install is only if you are running the collector scripts, otherwise this can be ignored


set /p ans= Do you want to intall the collector modules (y/n) 
if /i "%ans:~0,1%" EQU "Y" (

  Echo you selected Yes.


  rem image collection
  pip install bing_image_downloader
  pip install pillow

) else (
    Echo you selected no
    )
pause
