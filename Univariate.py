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
    def univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%",99,"Q4:100%","IQR",
                                    "1.5rule","lesser","greater","min","max"],columns=quan)
    def univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25%","Q2:50%","Q3:75%",99,"Q4:100%","IQR","1.5rule"
                                        ,"lesser","greater","min","max","Skew","Kurtosis","Variance","Standard_Deviation"],columns=quan)
        for columnName in quan:
           descriptive[columnName]["mean"]=dataset[columnName].mean()
           descriptive[columnName]["median"]=dataset[columnName].median()
           descriptive[columnName]["mode"]=dataset[columnName].mode() [0]
           descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
           descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
           descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
           descriptive[columnName][99]=np.percentile(dataset[columnName],99)
           descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
           descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]- descriptive[columnName]["Q1:25%"]
           descriptive[columnName]["1.5rule"]=1.5 * descriptive[columnName]["IQR"]
           descriptive[columnName]["lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
           descriptive[columnName]["greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"] 
           descriptive[columnName]["min"] =dataset[columnName].min()
           descriptive[columnName]["max"]=dataset[columnName].max() 
           descriptive[columnName]["Skew"]=dataset[columnName].skew() 
           descriptive[columnName]["Kurtosis"]=dataset[columnName].kurtosis() 
           descriptive[columnName]["Variance"]=dataset[columnName].var() 
           descriptive[columnName]["Standard_Deviation"]=dataset[columnName].std() 
        return descriptive

    def outliercolumnName(lesser,greater):
        lesser=[]
        greater=[]
        for columnName in quan:
            if descriptive[columnName]["min"]<descriptive[columnName]["lesser"]:
                lesser.append(columnName)
            if descriptive[columnName]["max"]>descriptive[columnName]["greater"]:
                greater.append(columnName)
        return lesser,greater
    def removeoutlier(lesser,greater):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descriptive[columnName]["lesser"]]=descriptive[columnName]["lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["greater"]]=descriptive[columnName]["greater"]
        return lesser,greater    
