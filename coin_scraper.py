# =========================================================
# Author: Rodolfo Ferro Pérez
# University of Guanajuato feat. Harvard Internship
# Email:  ferro@cimat.mx
#
# Basic coin scraper for http://numismatics.org/ocre/
# =========================================================


# =========================================================
# Importing our libs:
# =========================================================
import pandas as pd
from bs4 import BeautifulSoup
import requests


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
    return df.dropna()


def save_df(df, path):
    """Function to save the obtained dataframe."""
    df.to_csv("dataframe.csv")
    return


# =========================================================
# MAIN
# =========================================================

if __name__ == '__main__':
    # Number of pages to be extracted:
    number_pages = 1

    # Scraper:
    df = coin_scraper(number_pages)
    df = clean_df(df)

    # Save into csv:
    save_df(df, "coins.csv")
