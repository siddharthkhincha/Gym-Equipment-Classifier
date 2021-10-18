Gym Equipment Classifier
=======



We’re all the same when we get started (and for a while after too!) – gym equipment names are confusing and you can sometimes feel more than a little helpless in regards to what does what.
This project is an attempt to solve this problem with the help of immensely powerful Convolutional Neural Networks which do all the heavy lifting for us.

Currently the Neural Network can accurately classify the following equipment:
 * Bench Press 
 * Bicycle
 * Leg Press
 * Pec Deck
 * Rowing
 * Treadmill


Data
-------
To my surprise, there was no existing dataset classifying gym equpiment. The entire dataset used for this project was compiled through web scraping.
Every single image was cross verified to avoid issues such as wrongly classified,incorrect and ambigous images.
The dataset contains 1472 images across the 6 classes:
 * Train Set : 1189
 * Test Set  : 283

Model
-------
The CNN model used is based on the Resnet50 architecture. 
To speed up training, the model weights were initialised to the imagenet weights.
![Resnet Architecture](https://www.researchgate.net/publication/331364877/figure/fig3/AS:741856270901252@1553883726825/Left-ResNet50-architecture-Blocks-with-dotted-line-represents-modules-that-might-be.png)


Results
------
On applying several image augmentation techniques and hyperparameter tuning, the model was able to achieve a 89% accuracy on the test set, which given the limited dataset size and the existing ambiguity in classifying equipment, is a great score.
![Training Plot](https://github.com/siddharthkhincha/Gym-Equipment-Classifier/blob/master/plot.png)

License
-------

**MIT**, see `LICENSE.txt` for further details.



Contribute
----------

The source code is hosted on GitHub and contributions or donations are welcomed.
