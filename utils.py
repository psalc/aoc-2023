import os
from urllib.request import Request, urlopen

class InputReader:
    def __init__(self, day_number):
        self.base_url = 'https://adventofcode.com/2023/day'
        self.day_number = str(day_number)
        self.session_id = os.environ.get('SESSION_ID')

    def _make_url(self):
        url = os.path.join(self.base_url, self.day_number, 'input')
        return url
    
    def _read_input(self):
        url = self._make_url()
        req = Request(url)
        req.add_header('Cookie', f"session={self.session_id}")
        resp = urlopen(req)
        return resp
    
    def split_lines(self):
        data = self._read_input()
        return [line.decode().strip() for line in data]
    
