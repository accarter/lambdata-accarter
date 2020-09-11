# lambdata-accarter
A utility class for reading raw, unformatted CSV files accessed from
USA Swimming's SWIMS database.


## Installation

```
pip install -i https://test.pypi.org/simple/ lambdata-accarter==0.0.4
```

## Usage

```
from my_lambdata.ds_utilities import SWIMSWrangler

url = 'https://raw.githubusercontent.com/accarter/lambdata-accarter/master/my_lambdata/raw_data/men_50_fr_scy.csv'

wrangler = SWIMSWrangler(url)

print(wrangler)
print(wrangler.rows[0])
```
