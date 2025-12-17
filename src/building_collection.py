class BuildingCollection:
    def __init__(self, council_bbox, pages):
        self.pages = pages
    def produce_list(self):
        if self.pages != 0:
            return [{"id":0, "type":0, "geometry": 0, "properties": 0}] * (self.pages * 100)
        return []