import os
from urllib.request import Request, urlopen, HTTPError

class InputReader:
    def __init__(self, day_number):
        self.base_url = 'https://adventofcode.com/2023/day'
        self.day_number = str(day_number)
        try:
            self.session_id = os.environ['SESSION_ID']
        except KeyError:
            print('You must store a session cookie as an environment variable SESSION_ID. Otherwise, get your input manually.')
            raise

    def _make_url(self):
        url = os.path.join(self.base_url, self.day_number, 'input')
        return url
    
    def _read_input(self):
        url = self._make_url()
        req = Request(url)
        req.add_header('Cookie', f"session={self.session_id}")
        try:
            resp = urlopen(req)
            return resp
        except HTTPError as e:
            print(f"Unable to download input: {e}")
            raise
    
    def split_lines(self):
        data = self._read_input()
        return [line.decode().strip() for line in data]
    
