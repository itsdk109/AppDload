#!/usr/bin/python3
import requests
from google_play_scraper import app
import os

# Define the main function
def main():
    # Get the system's username
    system_username = os.getlogin()
    # Print the banner
     # Get the package name from user input
    print(f"==> Mr. {system_username}! Please type or paste the package name of the app")
    package_name = input("you want to download (i.e: com.example.myaaps): ")
    print(" ")
    # Get app info using the provided package name
    app_info = get_app_info(package_name)
    
    # Check if app info is found
    if app_info:
        # Download and save the APK
        download_and_save_apk(app_info, system_username)
    else:
        print(f"App with package name '{package_name}' not found on Google Play Store.")

# Define a function to print the banner
def print_banner():
    banner = '''
========================================================================                                 
=        #    #   ##       ### ### ###  #                              =
=       # #  # #  # #       #  # # # #  #                              =
=       ###  ###  # #       #  # # # #  #                              =
=       # #  # #  # #       #  # # # #  #                              =
=       # #  # #  ##        #  ### ###  #####                          =
=     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                 =
=     x        Android APPs Downloader       x                         =
=     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                 =
=                                                                      =
=   Written by Learn Tech With Deepak                                  =
=   Youtube Channel: @learntechwithdeepak                              =
=   Link: https://www.youtube.com/channel/UCq6THg2VnvaKWnOPF7FGmLw     =
========================================================================   
    '''
    print(banner)
    print(" ")



# Define a function to get app info based on package name
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

# Define a function to download and save the APK
def download_and_save_apk(app_info, system_username):
    app_url = app_info.get('url')
    app_name = app_info.get('title', 'UnknownApp')

    if not app_url:
        print("App URL not found.")
        return

    response = requests.get(app_url)
    if response.status_code == 200:
        with open(f'{app_name}.apk', 'wb') as apk_file:
            apk_file.write(response.content)
            print(" ")
            print(f"Congratulations! \nMr. {system_username}, Your '{app_name}' is Downloaded Successfully.")
            print(" ")
            print(f"Thanks for using it, Mr. {system_username}")
    else:
        print("Failed to download APK....")

# Check if the script is being run as the main program
if __name__ == "__main__":
    print(" ")
    main()
 