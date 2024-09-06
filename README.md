
# DEDSEC SITE DOWNLOADER V1.0

## Description

DEDSEC SITE DOWNLOADER V1.0 is a Python script designed to download all files from a website and upload them to a GitHub repository. The script is user-friendly, featuring a simple graphical interface and robust error handling. It is also configurable via user input, making it easy to use repeatedly.

**Disclaimer:** This script is intended for legitimate use only. Do not use it for malicious actions.

## Features

- **File Downloading:** Downloads all files (HTML, CSS, JS, PHP, JSON, PNG, JPG, ICO, etc.) from a website.
- **GitHub Upload:** Uploads the downloaded files to a GitHub repository.
- **Graphical Interface:** Uses Tkinter for a simple and user-friendly graphical interface.
- **Error Handling:** Handles potential errors for more stable usage.
- **Script Update:** Automatically updates the script from the repository.

## How It Works

1. **Download Files:** The script crawls the specified website and downloads all files to a local directory.
2. **Upload to GitHub:** The downloaded files are then committed and pushed to a GitHub repository.
3. **Graphical Interface:** A simple GUI allows users to start the download process, update the script, or exit.

## Getting Started

### Prerequisites

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure you have a GitHub account and a personal access token for interacting with the GitHub API. You can generate a token [here](https://github.com/settings/tokens).

### Usage

1. Run the script:
   ```bash
   python dedsec.py
   ```

2. Enter the required information when prompted:
   - **Site URL:** The URL of the website you want to download.
   - **GitHub Token:** Your GitHub personal access token.
   - **GitHub Username:** Your GitHub username.
   - **Repository Name:** The name of the GitHub repository where you want to upload the files.
   - **Commit Message:** The commit message for the GitHub upload.

3. Use the graphical interface to:
   - Start the download process.
   - Update the script.
   - Exit the application.

## Contributing

We welcome contributions! If you have suggestions or improvements, please fork the repository and create a pull request.

## Star the Repository

If you find this script useful, please consider starring the repository. Your support helps us continue to improve and maintain the project.

## Disclaimer

This script is provided as-is, without any warranty. Use it responsibly and in accordance with the terms of service of the websites you interact with.

---

**Note:** Always ensure you have the right to download and use the content from the websites you target. Unauthorized use of this script may violate legal terms and conditions.
```

This structure ensures that the project is organized and easy to manage, with clear instructions on how to use it.
