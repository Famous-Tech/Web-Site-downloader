import os
import requests
from bs4 import BeautifulSoup
from git import Repo
from colorama import Fore, Style, init
import tkinter as tk
from tkinter import messagebox
import threading
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
            file_name = os.path.join(folder, file_url.split('/')[-1])
            with open(file_name, 'wb') as f:
                f.write(file_response.content)
            print(Fore.YELLOW + f"Downloaded: {file_name}")
            logging.info(f"Downloaded: {file_name}")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Failed to download: {file_url} - {e}")
            logging.error(f"Failed to download: {file_url} - {e}")

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

def start_download():
    try:
        download_site_files(SITE_URL, DOWNLOAD_DIR)
        upload_to_github(DOWNLOAD_DIR, REPO_NAME, GITHUB_TOKEN, GITHUB_USERNAME, COMMIT_MESSAGE)
        messagebox.showinfo("Success", "Download and upload completed successfully!")
    except Exception as e:
        logging.error(f"Error: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

def main_menu():
    root = tk.Tk()
    root.title("DEDSEC SITE DOWNLOADER V1.0")

    tk.Label(root, text="DEDSEC SITE DOWNLOADER V1.0", font=("Arial", 16)).pack(pady=10)
    tk.Label(root, text="DEV : FAMOUS-TECH", font=("Arial", 12)).pack(pady=5)
    tk.Label(root, text="DON’T USE FOR MALICIOUS ACTIONS", font=("Arial", 12)).pack(pady=5)

    global SITE_URL, GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME, COMMIT_MESSAGE
    SITE_URL = input(Fore.CYAN + "Enter the site URL to download: ")
    GITHUB_TOKEN = input(Fore.CYAN + "Enter your GitHub token: ")
    GITHUB_USERNAME = input(Fore.CYAN + "Enter your GitHub username: ")
    REPO_NAME = input(Fore.CYAN + "Enter the repository name: ")
    COMMIT_MESSAGE = input(Fore.CYAN + "Enter the commit message: ")

    tk.Button(root, text="Start Downloading", command=lambda: threading.Thread(target=start_download).start()).pack(pady=10)
    tk.Button(root, text="Update the Script", command=update_script).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
