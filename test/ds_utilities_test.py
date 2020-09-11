import os
import unittest
from my_lambdata.ds_utilities import SWIMSWrangler


url = 'https://raw.githubusercontent.com/accarter/lambdata-accarter/master/my_lambdata/raw_data/men_50_fr_scy.csv'


class TestSWIMSWrangler(unittest.TestCase):
  def setUp(self):
    self.wrangler = SWIMSWrangler(url)
  
  def test_headers(self):
    headers = [
      'result_rank', 'first_name', 'last_name', 'distance', 'time_id',
      'distance', 'stroke', 'course', 'swimmer_age', 'swim_time_formatted', 
      'alt_adj_swim_time_formatted', 'standard_name', 'meet_name', 
      'swim_date', 'club_name', 'lsc_id', 'foreign_yesno', 
      'hytek_power_points', 'event_id', 'male_event'
    ]

    for h in headers:
      self.assertIn(h, self.wrangler.headers)

    self.assertEqual(len(headers), len(self.wrangler.headers))

    


if __name__ == '__main__':
  unittest.main()
