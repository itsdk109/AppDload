#!/usr/bin/python3
import requests
from google_play_scraper import app

def main():
    print_banner()

    package_name = input("Please type or paste the package name of the app you want to download: ")

    app_info = get_app_info(package_name)
    
    if app_info:
        download_and_save_apk(app_info)
    else:
        print(f"App with package name '{package_name}' not found on Google Play Store.")

def print_banner():
    banner = '''
========================================================================                                 
=        #    #   ##       ### ### ###  #                              =
=       # #  # #  # #       #  # # ###  #                              =
=       ###  ###  # #       #  # # # #  #                              =
=       # #  # #  # #       #  # # # #  #                              =
=       # #  # #  ##        #  ### ###  #####                          =
=     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                         =
=     x        Android AAPs Downlaoder       x                         =
=     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                         =
=                                                                      =
=   Written by Learn Tech With Deepak                                  =
=   YouTube: https://www.youtube.com/channel/UCq6THg2VnvaKWnOPF7FGmLw  =
========================================================================   
    '''
    print(banner)
    print(" ")

def get_app_info(package_name):
    try:
        app_info = app(
            package_name,
            lang='en',    # Language (optional)
            country='us'  # Country (optional)
        )
        return app_info
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def download_and_save_apk(app_info):
    app_url = app_info.get('url')
    app_name = app_info.get('title', 'UnknownApp')

    if not app_url:
        print("App URL not found.")
        return

    response = requests.get(app_url)
    if response.status_code == 200:
        with open(f'{app_name}.apk', 'wb') as apk_file:
            apk_file.write(response.content)
            print(f"APK for '{app_name}' downloaded successfully.")
    else:
        print("Failed to download APK....")

if __name__ == "__main__":
    main()
    
