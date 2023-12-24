# GenerationCovers
I created a dataset and converted the PROGAN architecture to conditional so that it could create images of album covers by genre. I couldn't train her because of the lack of capacity. Anyone who is just interested in this topic or can even train this neural network, use it, but just contact me. There is also a torrent for this marked-up dataset

I was based and studied on the commercials of the channel 
Aladdin Person so for a deeper dive into this topic, check out his channel.  I was inspired to create this project by the article Album Cover Generation from Genre Tags by Alexander Hepburn, Ryan McConville, and Raul Santos-Rodriguez

Based on the few results that I still managed to get, I can say that this neural network gives a result, although it takes, of course, several days, if not weeks, to train it. I would also like to note that I tried to transfer calculations from GPU to TPU on the same Google Collab, but either TPU is untenable for this neural network, or I just didn't figure it out.

There may certainly be errors in the neural network itself, since I did not conduct a full course of its training, keep this in mind!!!!

Progan_Labels.ipynb is the file of the neural network itself, just run it
coversHQ.rar.torrent is a dataset distribution file, if the distribution is not going on or the torrent is not working, contact me
splitter.py - a folder division script for the dataset to make it easier to upload to the cloud
yandexapi.py - a script for downloading and processing images from the Yandex music service