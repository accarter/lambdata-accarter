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

filename = 'men_50_bk_lcm.csv'
wrangler = SWIMSWrangler(os.path.abspath(
    os.path.join(__file__, f'../raw_data/{filename}')))

print(wrangler)
print(wrangler.rows[0])
```
