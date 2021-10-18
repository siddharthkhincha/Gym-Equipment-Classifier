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
To speed up training, the model weights were initialise to the imagenet weights.
![Resnet Architecture](https://www.researchgate.net/publication/331364877/figure/fig3/AS:741856270901252@1553883726825/Left-ResNet50-architecture-Blocks-with-dotted-line-represents-modules-that-might-be.png)




Installation
------------

Pattern supports Python 2.7 and Python 3.6. To install Pattern so that it is available in all your scripts, unzip the download and from the command line do:
```bash
cd pattern-3.6
python setup.py install
```

If you have pip, you can automatically download and install from the [PyPI repository](https://pypi.python.org/pypi/pattern):
```bash
pip install pattern
```

If none of the above works, you can make Python aware of the module in three ways:
- Put the pattern folder in the same folder as your script.
- Put the pattern folder in the standard location for modules so it is available to all scripts:
  * `c:\python36\Lib\site-packages\` (Windows),
  * `/Library/Python/3.6/site-packages/` (Mac OS X),
  * `/usr/lib/python3.6/site-packages/` (Unix).
- Add the location of the module to `sys.path` in your script, before importing it:

```python
MODULE = '/users/tom/desktop/pattern'
import sys; if MODULE not in sys.path: sys.path.append(MODULE)
from pattern.en import parsetree
```



License
-------

**BSD**, see `LICENSE.txt` for further details.



Contribute
----------

The source code is hosted on GitHub and contributions or donations are welcomed.
