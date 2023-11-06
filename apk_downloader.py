#!/usr/bin/python3
import requests
from google_play_scraper import app

banner = '''
       d8888               888                 d8b      888             d8888                                 
      d88888               888                 Y8P      888            d88888                                 
     d88P888               888                          888           d88P888                                 
    d88P 888 88888b.   .d88888 888d888 .d88b.  888  .d88888          d88P 888 88888b.  88888b.  .d8888b       
   d88P  888 888 "88b d88" 888 888P"  d88""88b 888 d88" 888         d88P  888 888 "88b 888 "88b 88K           
  d88P   888 888  888 888  888 888    888  888 888 888  888        d88P   888 888  888 888  888 "Y8888b.      
 d8888888888 888  888 Y88b 888 888    Y88..88P 888 Y88b 888       d8888888888 888 d88P 888 d88P      X88      
d88P     888 888  888  "Y88888 888     "Y88P"  888  "Y88888      d88P     888 88888P"  88888P"   88888P'      
8888888b.                                  888                        888     888      888                    
888  "Y88b                                 888                        888     888      888                    
888    888                                 888                        888     888      888                    
888    888  .d88b.  888  888  888 88888b.  888  .d88b.   8888b.   .d88888  .d88b.  888d888                    
888    888 d88""88b 888  888  888 888 "88b 888 d88""88b     "88b d88" 888 d8P  Y8b 888P"                      
888    888 888  888 888  888  888 888  888 888 888  888 .d888888 888  888 88888888 888                        
888  .d88P Y88..88P Y88b 888 d88P 888  888 888 Y88..88P 888  888 Y88b 888 Y8b.     888                        
8888888P"   "Y88P"   "Y8888888P"  888  888 888  "Y88P"  "Y888888  "Y88888  "Y8888  888 

               Written by Learn Tech With Deepak
               youtube: https://www.youtube.com/channel/UCq6THg2VnvaKWnOPF7FGmLw
'''
print(banner)
print(" ")

# Define the package name of the app you want to download
package_name = input("Please type or paste Package name Here: ")

# package_name = 'com.manageengine.patchmanagerplus'  # Replace with the actual package name

# Search for the app and get its information
app_info = app(
   package_name,
   lang='en',    # Language (optional)
   country='us'  # Country (optional)
)

if 'url' in app_info:
   app_url = app_info['url']  # Correct key is 'url'
   app_name = app_info['title']  # Extract the app name

   # Download the APK file with the app's original name
   response = requests.get(app_url)
   if response.status_code == 200:
       with open(f'{app_name}.apk', 'wb') as apk_file:
           apk_file.write(response.content)
           print(f"APK for '{app_name}' downloaded successfully.")
   else:
       print("Failed to download APK.")
else:
   print(f"App with package name '{package_name}' not found on Google Play Store.")
