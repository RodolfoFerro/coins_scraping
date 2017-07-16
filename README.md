# Coin classification for [OCRE](http://numismatics.org/ocre/)

![Obverse of DE-MUS-814819/18200444: Münzkabinett Berlin](http://ww2.smb.museum/mk_edit/images/n0/457/vs_opt.jpg)

<!--
> ### Authors:
> Harvard University, Rodolfo Ferro and Carlos Outeiral
> New Hampshire University, Daniel Hasse <br/>
-->

## Description 📝

This project consists on a classifier of coins from the Roman Empire. This was developed in collaboration by **Rodolfo Ferro**, **Carlos Outeiral** (*Harvard University*) and **Daniel Haas** (*New Hampshire University*).

The idea of classification consists on applying *Machine Learning* techniques in order to identify classes in objects of interest. This enables the automatic classification of any new coin of Roman Empire that might be discovered, since we already have a trained classifier.

The classifier consists on a *Neural Network* which has been trained with a dataset of previously classified coins, obtained from the [Online Coins of the Roman Empire (OCRE)](http://numismatics.org/ocre/). For this, several phases of development were worked, which are explained in the following section.


## Development phases ⚙️


#### 1. Web scraping [OCRE](http://numismatics.org/ocre/) to create a training dataset

Web scraping (web harvesting or web data extraction) consists on scraping data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. It is a form of copying, in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.

For our particular case, we scraped and dropped off data without images (since we wanted to train a *Neural Network* using image features).


#### 2. Preprocessing the dataset

We downloaded the images from the database (the previously obtained dataset) and did some feature extraction of each coin's image (obverse and reverse).

The feature extraction consists on identifying features in coin images that let us do the processing in order to predict a class of a new coin. These features were used to train our model that classifies coins, and were obtained by applying *Computer Vision* techniques to every image in our previously obtained dataset.


#### 3. Building a pre-classifier

The pre-classifier consists on mapping all the constructed and obtained features from our training dataset in the correct data structure that will be used in the construction of our *Neural Network*.

For our particular case, we identified if the image is head or tails, we identified the age/period, and any other specs.


#### 4. Build the *Neural Network*

A *Neural Network* is a *Machine Learning* model based on humans' neural networks which interact in a similar way, so they simulate the learning model of a human neural net.


#### 5. Train classifier and predict

Training the classifier consists on feeding the *Neural Network* previously constructed with our training dataset, so it cal learn classes of coins in order to know how to classify a new coin.


## Requirements 💻

### Execution
* [Python 3.x](https://www.python.org/)
* [Pandas](http://pandas.pydata.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [OpenCV](http://opencv.org/)
* [Jupyter notebook](http://jupyter.org/) (recommended)

### Scraping
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [wget](https://pypi.python.org/pypi/wget)


## How to use it 📕
