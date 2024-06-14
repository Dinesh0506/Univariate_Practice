class Univariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
             if(dataset[columnName].dtype=='O'):
              #print("qual")
              qual.append(columnName)
             else:
              #print("quan")
              quan.append(columnName)
        return quan,qual