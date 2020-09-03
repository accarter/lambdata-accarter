# lambdata-accarter
A collection of data science utility functions


## Installation

```
pip install -i https://test.pypi.org/simple/ lambdata-accarter==0.0.3
```

## Usage

```
from my_lambdata.ds_utilities import ConfusionMatrix

cm = ConfusionMatrix(85, 58, 8, 36)

print('Accuracy: ', cm.accuracy())
print('Precision: ', cm.precision())
print('Recall: ', cm.recall())
```
