import imgprocessing as ip
import pandas as pd
import os
import cv2
import random

def loadData(datafile, imgfolder):

	df = pd.read_csv(datafile)
	os.chdir(imgfolder)
	props = []
	imgs = []

	for _, entry in df.iterrows():

		mint = entry['Mint']
		den = entry['Denomination']
		date = entry['Date']
		props.append([date, mint, den])

		heads = loadImage(entry['heads'])
		tails = loadImage(entry['tails'])
		mheads = messupImage(heads)
		mtails = messupImage(tails)
		imgs.append([mheads, mtails])

	return props, imgs

def loadImage(file):

	img = cv2.imread(file)
	if not img.shape[0] == 128 or not img.shape[1] == 128:
		return ip.scaleImg(img)

	return img

def messupImage(img, n):

	messedImages = []

	for _ in range(n):

		i = ip.blurImage(ip.addNoise(ip.rotateImage(img)), random.randint(1,4))
		messedImages.append(i)

	return messedImages
 