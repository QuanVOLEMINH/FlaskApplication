from datetime import datetime


class datamanagement(object):
    def get3most(self, data):
        list = []
        i = 3
        while ((i > 0) and (len(data) > 0)):
            maxPricedItem = max(data, key=lambda x: x['sec'])
            list.append(maxPricedItem)
            data.remove(maxPricedItem)
            i = i - 1
        return list

    def setFormat(self, data):
        i = len(data)
        date_format = "%Y-%m-%dT%H:%M:%SZ"
        list = []
        for x in data:
            item = {}
            item['name'] = x['name']
            item['last_time'] = datetime.strptime(x['pushed_at'], date_format).strftime("%H:%M %m-%d-%Y")
            item['sec'] = (datetime.strptime(x['pushed_at'], date_format) - datetime(1970, 1, 1)).total_seconds()
            list.append(item)
        return list
