import os

from my_lambdata.ds_utilities import SWIMSWrangler

filename = 'men_50_bk_lcm.csv'
wrangler = SWIMSWrangler(os.path.abspath(
    os.path.join(__file__, f'../raw_data/{filename}')))

print(wrangler)
print(wrangler.rows[0])
