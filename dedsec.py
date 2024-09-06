import os
import requests
from bs4 import BeautifulSoup
from git import Repo
from colorama import Fore, Style, init
import logging
import subprocess

init(autoreset=True)

# Configuration GitHub
GITHUB_TOKEN = ''
GITHUB_USERNAME = ''
REPO_NAME = ''
COMMIT_MESSAGE = ''
SITE_URL = ''
DOWNLOAD_DIR = 'site_files'

# Logger
logging.basicConfig(filename='logs/script.log', level=logging.INFO)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ==================================================
    DEDSEC SITE DOWNLOADER V1.0
    DEV : FAMOUS-TECH
    LEGION : DEDSEC
    LOCATION : IN THE WORLD 🌐
    DON’T USE FOR MALICIOUS ACTIONS
    ==================================================
    """
    print(Fore.GREEN + banner)

def download_site_files(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for link in soup.find_all(['a', 'link', 'script'], href=True):
        file_url = link['href']
        if file_url.startswith('/'):
            file_url = url + file_url
        elif not file_url.startswith('http'):
            file_url = url + '/' + file_url

        try:
            file_response = requests.get(file_url)
            file_response.raise_for_status()  # Raise an HTTPError for bad responses
            
            # Extract the file name from the URL
            file_name = os.path.join(folder, file_url.split('/')[-1])
            
            # Check if the file name is too long and truncate it if necessary
            if len(file_name) > 255:  # 255 is a common limit for file names
                file_name = os.path.join(folder, file_url.split('/')[-1][:255 - len(folder) - 1])

            with open(file_name, 'wb') as f:
                f.write(file_response.content)
            print(Fore.YELLOW + f"Downloaded: {file_name}")
            logging.info(f"Downloaded: {file_name}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Failed to download: {file_url} - {e}")
            logging.error(f"Failed to download: {file_url} - {e}")
        except OSError as e:
            print(Fore.RED + f"Failed to save file: {file_name} - {e}")
            logging.error(f"Failed to save file: {file_name} - {e}")

def upload_to_github(folder, repo_name, github_token, github_username, commit_message):
    repo_url = f'https://{github_token}@github.com/{github_username}/{repo_name}.git'
    repo = Repo.init(folder)
    repo.git.add(A=True)
    repo.index.commit(commit_message)
    origin = repo.create_remote('origin', repo_url)
    origin.push(refspec='master:master')
    print(Fore.BLUE + f"Uploaded to GitHub: {repo_url}")
    logging.info(f"Uploaded to GitHub: {repo_url}")

def update_script():
    try:
        print(Fore.YELLOW + "Updating the script...")
        subprocess.run(['git', 'pull'], check=True)
        print(Fore.GREEN + "Script updated successfully!")
        logging.info("Script updated successfully")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Failed to update the script: {e}")
        logging.error(f"Failed to update the script: {e}")

def main_menu():
    clear_screen()
    print_banner()

    global SITE_URL, GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME, COMMIT_MESSAGE
    SITE_URL = input(Fore.CYAN + "Enter the site URL to download: ")
    GITHUB_TOKEN = input(Fore.CYAN + "Enter your GitHub token: ")
    GITHUB_USERNAME = input(Fore.CYAN + "Enter your GitHub username: ")
    REPO_NAME = input(Fore.CYAN + "Enter the repository name: ")
    COMMIT_MESSAGE = input(Fore.CYAN + "Enter the commit message: ")

    while True:
        print("\nOptions:")
        print("1. Start Downloading")
        print("2. Update the Script")
        print("3. Exit")
        choice = input(Fore.CYAN + "Choose an option: ")

        if choice == '1':
            download_site_files(SITE_URL, DOWNLOAD_DIR)
            upload_to_github(DOWNLOAD_DIR, REPO_NAME, GITHUB_TOKEN, GITHUB_USERNAME, COMMIT_MESSAGE)
            print(Fore.GREEN + "Download and upload completed successfully!")
        elif choice == '2':
            update_script()
        elif choice == '3':
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
