# Coin classification for [OCRE](http://numismatics.org/ocre/)

![Obverse of DE-MUS-814819/18200444: Münzkabinett Berlin](http://ww2.smb.museum/mk_edit/images/n0/457/vs_opt.jpg)

> ### Authors:
> New Hampshire University, Daniel Hasse <br/>
> Harvard University, Rodolfo Ferro and Carlos Outeiral

## Description 📝

This repo contains the job done so far for the [OCRE](http://numismatics.org/ocre/) coin classificaiton project.

The project consists on ... (coin classification, should add something interesting here...)

## Requirements 💻

* [Python 3.x](https://www.python.org/)
* [Pandas](http://pandas.pydata.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [OpenCV](http://opencv.org/)
* [Jupyter notebook](http://jupyter.org/) (recommended)

## Development phases ⚙️

The phases of the development consist on:

1. Scraping [OCRE](http://numismatics.org/ocre/) to create a training dataset:
	* Scraping and dropping off data without images (since we want to train a NN using image features)

2. Preprocessing:
	* Downloading images from DB (obtained dataset)
	* Feature extraction (which includes the image processing for each coin)

3. Pre-classifier:
	* Heads or tails
	* Period
	* Specs

4. Build NN
5. Train classifier and predict

## How to use it 📕
