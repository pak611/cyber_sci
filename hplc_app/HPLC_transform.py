

import os
from skimage import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def plot_to_df(pathname, x_max,  y_max):


    #pathname = '/Users/patrickkampmeyer/Dropbox/Ph.D/OrganoNet/Websites/ChemDataPro/chemdataprowebsite/media/images/'


    filename = os.listdir(pathname)[0]


    image = io.imread(pathname+filename, as_gray=True)


    indices = np.where(image == 1, 0, image)
    indices = np.where(indices != 0, 1, indices)


    pixcor = np.where(indices == 1)



    df = pd.DataFrame(pixcor)

    df.iloc[0,:] = -df.iloc[0,:] + max(abs(df.iloc[0,:]))


    # now to transform this

    #x_max = 5
    #y_max = 5

    x_actmax = x_max
    y_actmax = y_max

    x_trans = (x_actmax/max(df.iloc[1,:]))*df.iloc[1,:]
    y_trans = (y_actmax/max(df.iloc[0,:]))*df.iloc[0,:]




    x_arr = np.array(x_trans).reshape(x_trans.shape[0], 1)

    y_arr = np.array(y_trans).reshape(y_trans.shape[0], 1)

    trans_arr = np.append(x_arr, y_arr, axis = 1)

    trans_df = pd.DataFrame(trans_arr)



    return(trans_df)

