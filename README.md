# Coin classification for [OCRE](http://numismatics.org/ocre/)

> ### Authors:
> New Hampshire University, Daniel Hasse <br/>
> Harvard University, Rodolfo Ferro and Carlos Outeiral

This repo contains the job done so far for the [OCRE](http://numismatics.org/ocre/) coin classificaiton project.

The project consists on ... (coin classification, should add something interesting here...)

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
