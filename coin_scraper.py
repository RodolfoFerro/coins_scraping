# =========================================================
# Harvard University
# Authors: 
#     Rodolfo Ferro Pérez (ferro@cimat.mx)
#     Carlos Outeiral Rubiera (couteiral@gmail.com)
#
# Basic coin scraper for http://numismatics.org/ocre/
# =========================================================


# =========================================================
# Importing our libs:
# =========================================================
import pandas as pd
from bs4 import BeautifulSoup
import requests
import wget
import os

# =========================================================
# Defining or funtions:
# =========================================================

def coin_scraper(number_of_pages):
    """Basic coin scraper for http://numismatics.org/ocre/."""

    # Setting standard url:
    url = "http://numismatics.org/ocre/results?q=&start="

    # We create an empty dataframe:
    df = pd.DataFrame()

    # Iterate for 20 by 20 querys:
    for page in range(number_of_pages):
        print("Extracting page number {}".format(page + 1))
        # Do request:
        r    = requests.get(url + str(page * 20))
        data = r.text
        soup = BeautifulSoup(data, "lxml")

        # Extract info from soup:
        temp_df = data_extraction(soup)
        df = df.append(temp_df, ignore_index = True)

    # We return the dataframe:
    return df

def data_extraction(soup):
    """Function to extract data in the basic coin scraper."""

    # First we find all section with whole info:
    results = soup.find_all("div", class_="result-doc")

    # Tag filtering:
    tags = results[0].find_all("dt")
    tags = [ tags[i].text for i in range(len(tags)) ]

    # We create an empty dataframe:
    df = pd.DataFrame(columns=tags)

    for result in results:
        # Extract all info and images:
        data = result.find_all("dd")
        imgs = result.find_all("img")

        # Build a dictionary for dataframe appending:
        data = { tags[i] : data[i].text for i in range(len(data)) }
        # Try to add images url (if they exist):
        try:
            data["Obverse_URL"] = imgs[0]['src']
            data["Reverse_URL"] = imgs[1]['src']
        except:
            data["Obverse_URL"] = None
            data["Reverse_URL"] = None

        data = pd.Series(data)
        df = df.append(data, ignore_index = True)

    return df

def clean_df(df):
    """Function to drop any NaN values (!img urls)."""
    df.index += 1
    return df.dropna()


def save_df(df, name="dataframe.csv"):
    """Function to save the obtained dataframe."""
    df.to_csv(name)
    return

def download_images(df):
    """Function to download the images."""
    
    # Preload data:
    heads = df['Obverse_URL']
    tails = df['Reverse_URL']
    df_index = 1

    # Create directories:
    if not os.path.exists('./images/'):
        os.mkdir('./images/')
    os.chdir('./images')

    # Download images:
    for i, (url1, url2) in enumerate(zip(heads, tails)):
        file1, file2 = None, None

        print('\nTrying to download image {}. \ndf_index = {}'.format(i+1, df_index))
        try:
            # Try to download images:
            file1 = wget.download(url1)
            file2 = wget.download(url2)
            if file1 is None or file2 is None:
                # Set None urls for posterior deletion:
                df['Obverse_URL'][i] = None
                df['Reverse_URL'][i] = None
            else:
                # Rename files:
                ext1 = file1[file1.rfind('.'):]
                ext2 = file2[file2.rfind('.'):]
                os.rename(file1, 'heads{:05d}{}'.format(df_index, ext1))
                os.rename(file2, 'tails{:05d}{}'.format(df_index, ext2))
                df_index += 1
        except:
            pass
    
    # Print basic info :
    print("Total images downloaded: \n\t{} from {}".format(df_index, len(heads)))
    print("Number of indices dropped off: {}".format(len(indices)))
    
    # Clean dataframe from by setting null values from unknown images:
    df = clean_df(df)
    return df


# =========================================================
# MAIN
# =========================================================

if __name__ == '__main__':
    # Number of pages to be extracted:
    # number_pages = 590

    # Scraper:
    # df = coin_scraper(number_pages)
    # df = clean_df(df)

    # Save into csv:
    # save_df(df)

    # Download images
    df = pd.read_csv('dataframe.csv') # Load pre-downloaded dataframe
    df = download_images(df)
    save_df(df, name="coins.csv")     # Save new version
