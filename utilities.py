import pandas as pd
import numpy as np
import pickle
import json
import config

class Fish_Weight():
    def __init__(self,Length1,Length2,Length3,Height,Width,Species):
        self.Length1=Length1
        self.Length2=Length2
        self.Length3=Length3
        self.Height=Height
        self.Width=Width
        self.Species="Species_"+Species

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as file1:
            self.model=pickle.load(file1)

        with open(config.PROJECT_DATA_PATH, 'r') as file2:
            self.project_data=json.load(file2)

    def get_predicted_weight(self):
        self.load_model()

        test_series=pd.Series(np.zeros(len(self.project_data['columns'])),index=self.project_data['columns'])
        test_series['Length1']=self.Length1
        test_series['Length2']=self.Length2
        test_series['Length3']=self.Length3
        test_series['Height']=self.Height
        test_series['Width']=self.Width
        test_series[self.Species]=1

        weight=self.model.predict([test_series])[0]
        weight=np.around(weight,2)

        return weight


# if __name__=="__main__":
#     Length1=23.2
#     Length2=25.4
#     Length3=30
#     Height=11.52
#     Width=4.02
#     Species='Bream'
#     wt=Fish_Weight(Length1,Length2,Length3,Height,Width,Species)
#     weight=wt.get_predicted_weight()

#     print("*********************")
#     print(f"Weight of Fish :{weight}")
#     print("*********************")



        

        








# length1=23.2
# length2=25.4
# length3=30
# height=11.52
# width=4.02
# species='Bream'