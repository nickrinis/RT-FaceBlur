"""Data Base Generator"""

import pandas as pd


def generate_data():
    
    # Create a dataFrame and return it.
    header = ['id', 'username', 'password', 'clearance']
    data = [[10, 'K.Thomas', 'felina@19', 'clearance 0'], 
            [11, 'M.Nicholaos', '2118159!', 'clearance 2'],
            [12, 'M.Oscar', '1617#2198', 'clearance 1'],
            [13, 'S.Michael', '!vidi1234', 'clearance 1'],
            [14, 'J.Felix', 'Koump7#4321', 'clearance 0']]
        
    pd_user_data = pd.DataFrame(data, columns=header)

    return pd_user_data
