# This class is responsible for creating a datasource object

class DataSource(object):

    def __init__(self,orderStreams):

        self.orderStreams = orderStreams.copy()


    def returnData(self):
        return self.orderStreams