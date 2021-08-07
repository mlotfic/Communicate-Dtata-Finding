# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime 
import time
from pathlib import Path
import os

relative_path = Path(__file__).parents[2]

if not os.path.exists('{}/data/interim'.format(relative_path)):
    os.makedirs('{}/data/interim'.format(relative_path))
'''
schema = { 
    'Year' : str, 
    'Month' : str,
    'DayofMonth' : str,
    'DayOfWeek' : str,
    'DepTime' : str,
    'CRSDepTime' : str,
    'ArrTime' : str,
    'CRSArrTime' : str,
    'UniqueCarrier' : str,
    'FlightNum' : str,
    'TailNum' : str,    
    'ActualElapsedTime' : int,
    'CRSElapsedTime' : int, 
    'AirTime' : int, 
    'ArrDelay' : int,      
    'DepDelay' : int,
    'Origin' : str, 
    'Dest' : str, 
    'Distance' : int,
    'TaxiIn' : int,
    'TaxiOut' : int,    
    'Cancelled' : bool,
    'CancellationCode' : str,
    'Diverted' : bool,
    'CarrierDelay' : int,      
    'WeatherDelay' : int,
    'NASDelay' : int,
    'SecurityDelay' : int,
    'LateAircraftDelay' : int

}
'''
# user define function
def load_dataset(year='2008'):
    '''
    Description: load dataset acoordding to year
    parameter year string
    return dataframe
    '''
    t1 = time.time()
    df = pd.read_csv('{}/data/raw/{}.csv.bz2'.format(relative_path, year), compression='bz2', dtype=str, na_values=['na', '-', '.', ''])
    t2 = time.time()
    print('Elapsed loading time :', t2-t1)
    return df

def validate_int2str(col, l=1, _min=False):
    '''
    validate data to int and then to str
    parameter : float , int string number
    col : string text
    l : min length of the number
    _min: bool
    return : string type 
    '''
    try:
        if col: 
            col = int(float(col))
            if (_min and (l > len(str(col)))):
                return np.NaN
            elif (_min and (l <= len(str(col)))):
                col = str(col).zfill(4) 
                col = datetime.strptime(col, '%H%M').time().strftime("%I:%M %p")        
            return col   
        else: 
            return np.NaN          
    except Exception as e:      
        return np.NaN

'''
# test function
print(validate_int2str("1.0", 1, 1))
print(validate_int2str("1.0", 0, 1))
print(validate_int2str("12.0x"))
print(validate_int2str("12.0"))
'''
def validate_str(col):
    '''
    validate data to str
    parameter : float , int string number
    col : string text
    return : string type 
    '''
    try:
        if str(col).strip():     
            return str(col)    
        else: 
            return np.NaN          
    except Exception as e:      
        return np.NaN
'''
# test function
print(validate_str(""))
print(validate_str("    "))
print(validate_str("     \n"))
print(validate_str("12.0x"))
print(validate_str("12.0"))
print(validate_str(12))
'''

# load dataset 2008
df = load_dataset()


# correcting dates formate
df['DepTime'] = df['DepTime'].apply(lambda x: str(int(x)).zfill(4) if pd.notnull(x) else x)
df['CRSDepTime'] = df['CRSDepTime'].apply(lambda x: str(int(x)).zfill(4) if pd.notnull(x) else x)
df['ArrTime'] = df.ArrTime.apply(lambda x: str(int(x)).zfill(4) if pd.notnull(x) else x)
df['CRSArrTime'] = df.CRSArrTime.apply(lambda x: str(int(x)).zfill(4) if pd.notnull(x) else x)

# validate data
df['Year']              = df['Year'].apply(lambda x: validate_str(x))
df['Month']             = df['Month'].apply(lambda x: validate_str(x))
df['DayofMonth']        = df['DayofMonth'].apply(lambda x: validate_str(x))
df['DayOfWeek']         = df['DayOfWeek'].apply(lambda x: validate_str(x))

'''
#Col 1 = where you want the values replaced
#Col 2 = where you want to take the values from
df.["Col 1"].fillna(df.["Col 2"], inplace=True)
# datetime(year, month, day, hour, minute, second, microsecond)
'''
# remove one number value and reformat hh:mm AM
t1 = time.time()
df['DepTime']           = df['DepTime'].apply(lambda x: validate_int2str(x, l=1, _min=True))       
df['CRSDepTime']        = df['CRSDepTime'].astype('str').apply(lambda x: validate_int2str(x, l=1, _min=True))          
df['ArrTime']           = df['ArrTime'].astype('str').apply(lambda x: validate_int2str(x, l=1, _min=True))            
df['CRSArrTime']        = df['CRSArrTime'].astype('str').apply(lambda x: validate_int2str(x, l=1, _min=True))          
t2 = time.time()
print('Elapsed loading time :', t2-t1)


# filling nan to zero to modify schema
df['CarrierDelay'].fillna(0, inplace=True)  
df['WeatherDelay'].fillna(0, inplace=True)  
df['NASDelay'].fillna(0, inplace=True)  
df['SecurityDelay'].fillna(0, inplace=True)  
df['LateAircraftDelay'].fillna(0, inplace=True)  

df['CarrierDelay']      = df['CarrierDelay'].astype('int')  
df['WeatherDelay']      = df['WeatherDelay'].astype('int') 
df['NASDelay']          = df['NASDelay'].astype('int') 
df['SecurityDelay']     = df['SecurityDelay'].astype('int') 
df['LateAircraftDelay'] = df['LateAircraftDelay'].astype('int') 



# divide dataset into
# divide dataset in two
# - flights
# - cancelled
# - diverted

# df[~df.CancellationCode.notna()]
flights = df[~(df.Diverted == 1)]
flights = flights[~(flights.Cancelled == 1)].drop(columns=['Cancelled', 'CancellationCode', 'Diverted'])

t1 = time.time()
flights.to_csv('{}/data/interim/{}.csv'.format(relative_path, 'flights'), index=False)
t2 = time.time()
print('Elapsed saving time :', t2-t1)
del flights

df_cancelled = df[df.Cancelled == '1'].drop(columns=['DepTime', 'ArrTime', 'ActualElapsedTime', 'AirTime', 'ArrDelay',
                                                  'DepDelay', 'TaxiIn', 'TaxiOut', 'Cancelled', 'Diverted', 'CarrierDelay',
                                                  'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'])

t1 = time.time()
df_cancelled.to_csv('{}/data/interim/{}.csv'.format(relative_path, 'canceled'), index=False)
t2 = time.time()
print('Elapsed saving time :', t2-t1)
del df_cancelled

df_diverted = df[df.Diverted == '1'].drop(columns=['ArrTime', 'CRSArrTime', 'UniqueCarrier', 'ActualElapsedTime', 
                                                 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay', 'Origin', 
                                                 'Dest', 'Distance', 'Cancelled', 'CancellationCode', 'Diverted', 
                                                 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 
                                                 'LateAircraftDelay'])
t1 = time.time()
df_diverted.to_csv('{}/data/interim/{}.csv'.format(relative_path, 'diverted'), index=False)
t2 = time.time()
print('Elapsed saving time :', t2-t1)
del df_diverted
