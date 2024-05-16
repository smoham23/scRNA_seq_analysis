import requests
import os
import tarfile  


def download(url, directory):
    print(f"Downloading {url}")
        # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Get the file name from the URL
    file_name = url.split('/')[-1]

    # Set the path to save the file
    file_path = os.path.join(directory, file_name)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the file to the specified directory
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully to: {file_path}")
        with tarfile.open(file_path, 'r') as tar:
            tar.extractall(directory)
        print(f"File extracted successfully to: {directory}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def download_from_file(file_path, directory):
    # Read URLs from the input file
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    # Download each URL
    for url in urls:
        # Remove newline characters
        url = url.strip()
        if url:  # Check if URL is not empty
            download(url, directory)

if __name__ == "__main__":
    file_path = "database_links"  
    directory = "database"  
    
    download_from_file(file_path, directory)