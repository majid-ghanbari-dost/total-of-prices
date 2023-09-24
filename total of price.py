import numpy as np
import pandas as pd
b1 = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12]])
b2 = np.array([15,25,30])
x_table = pd.DataFrame(b1,index=(["mon","tues","sat","fri"]),
                           columns=(["c1","c2","c3"]))


price_table = pd.DataFrame(b2.reshape(1,3),index=["price"],
                           columns=["c1","c2","c3"])
total = np.dot(b1,b2)
x_table["total $"] = total

print(x_table)
print("----------------")
print(price_table)
