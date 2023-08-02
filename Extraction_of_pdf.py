from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlencode
from selenium.common.exceptions import NoSuchElementException
from PyPDF2 import PdfMerger
import os
import shutil
from datetime import datetime, timedelta

def retrieve_case_sheets(keywords):
    base_url = "https://indiankanoon.org/search/"
    query_string = urlencode({"formInput": " ".join(keywords)})
    search_url = base_url + "?" + query_string

    driver = webdriver.Chrome()
    driver.get(search_url)

    case_sheet_links = driver.find_elements(By.CSS_SELECTOR, ".result_title a")
    case_sheet_urls = []

    for link in case_sheet_links:
        case_sheet_url = link.get_attribute("href")
        case_sheet_urls.append(case_sheet_url)

    merger = PdfMerger()

    for url in case_sheet_urls:
        driver.get(url)
        try:
            download_button = driver.find_element(By.XPATH, "//input[@value='Get this document in PDF']")
            download_button.click()
        except NoSuchElementException:
            continue
    driver.quit()

def move_downloaded_files(source_directory, destination_directory):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    current_time = datetime.now()
    threshold_time = current_time - timedelta(minutes=10)

    for file_name in os.listdir(source_directory):
        file_path = os.path.join(source_directory, file_name)
        if os.path.isfile(file_path):
            modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if modified_time >= threshold_time:
                destination_path = os.path.join(destination_directory, file_name)
                shutil.move(file_path, destination_path)
                print(f"Moved file '{file_name}' successfully!")

# Usage example
source_directory = "C:/Users/Harshenee_CB/Downloads"
destination_directory = "C:/Users/Harshenee_CB/Documents/HackerX"

move_downloaded_files(source_directory, destination_directory)

# Usage example
keywords = ["Third party claim", "Bajaj"]
retrieve_case_sheets(keywords)
#This code works as downloads and shifts the file place as well

