from datetime import datetime


class DataManagement(object):
    def get3most(self, data):
        output = []
        i = 3
        while i > 0 and len(data) > 0:
            latestitem = max(data, key=lambda x: x['sec'])
            output.append(latestitem)
            data.remove(latestitem)
            i = i - 1
        return output

    def setformat(self, data):
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        output = []
        for x in data:
            item = {}
            item['name'] = x['name']
            item['last_time'] = datetime.strptime(x['pushed_at'], date_format).strftime("%H:%M %m-%d-%Y")
            item['sec'] = (datetime.strptime(x['pushed_at'], date_format) - datetime(1970, 1, 1)).total_seconds()
            output.append(item)
        return output
