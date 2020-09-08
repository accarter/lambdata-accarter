import re
import pandas as pd

FULL_NAME_HEADER = 'full_name'
EVENT_HEADER = 'event_desc'

NUM_COLS = 16
FIRST_NAME_COL = 2
EVENT_COL = 5
TIME_STANDARD_COL = 9
BOY_NAMES = {"Michael", "David", "Josh"}  # Names found exclusively in men's events


class SWIMSWrangler():
    '''
    A utility class for reading raw, unformatted CSV files accessed from
    USA Swimming's SWIMS database.
    '''

    normal_field= '(".*?")'
    time_standard_field = '(""".*"""|".*?")'
    swim_regexp = re.compile(
        '.*?'.join([normal_field] * (TIME_STANDARD_COL - 1) +
                   [time_standard_field] +
                   [normal_field] * (NUM_COLS - TIME_STANDARD_COL)))

    def __init__(self, path):
        '''
        Create a SWIMSWrangler using the CSV file found at the specified path.
        '''
        self.path = path
        self.orig_headers, self.raw_rows = self._read_data()
        self.orig_name_idx, self.orig_event_idx = \
            self._find_indices(FULL_NAME_HEADER, EVENT_HEADER)
        self.distance, self.stroke, self.course = self._event_details()
        self.male_event = self._is_male_event()
        self.headers, self.rows = self._format_data()

    def _read_data(self):
        '''
        Read in the raw data from the CSV file.
        '''
        with open(self.path, 'r') as f:
            header, *rows = f.readlines()

        return (
            [col.strip('="\n') for col in header.split(',')],
            rows
        )

    def _find_indices(self, *col_names):
        return (self.orig_headers.index(name) for name in col_names)


    def _event_details(self):
        '''
        Produce a tuple containing the distance, stroke, and course for
        the swims found in the CSV file.
        '''
        # Use an arbitrary row to determine event-related information
        event = self.raw_rows[0].split(',')[EVENT_COL]
        distance, stroke, course = event.strip('="').lower().split()

        return distance, stroke.upper(), course.upper()

    def _is_male_event(self):
        '''
        Determine the gender using the available first names.
        '''
        names = set(line.split(',')[FIRST_NAME_COL].strip(' "')
            for line in self.raw_rows)

        return len(names.intersection(BOY_NAMES)) > 0

    def _format_data(self):
        '''
        Produce the headers from the original CSV file.

        Format headers to match new structure where necessary.
        '''
        headers = self.orig_headers[:]
        rows = [self._to_fields(row) for row in self.raw_rows]

        headers_map = [
            (FULL_NAME_HEADER, ['last_name', 'first_name']),
            (EVENT_HEADER, ['distance', 'stroke', 'course'])
        ]

        for header, replacements in headers_map:
            idx = headers.index(header)
            headers = self._replace_col(headers, idx, replacements)
            rows = self._replace_rows(rows, idx, header)

        for row in rows:
            row.append(self._is_male_event)

        return headers + ['male_event'], rows

    def _replace_rows(self, rows, idx, header):
        replacement_map = {
            FULL_NAME_HEADER: lambda x: self._replace_by_split(x, idx),
            EVENT_HEADER: lambda x: self._replace_by_split(x, idx)
        }
        return [replacement_map[header](row) for row in rows]

    def _to_fields(self, row):
        return list(self.swim_regexp.search(self.raw_rows[0]).groups())

    def _replace_by_split(self, row, idx):
        return self._replace_col(row, idx, row[idx].split(','))

    @staticmethod
    def _replace_col(row, idx, replacements):
        return row[:idx] + replacements + row[idx + 1:]

    def __repr__(self):
        return '<{__class__.__name__} object; ' \
            'distance={distance}, course={course}, stroke={stroke}, male_event={male_event}>'\
                .format(__class__=self.__class__, **self.__dict__)
