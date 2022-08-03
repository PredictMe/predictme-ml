import requests
import json
import os
import sys
import eth_abi
import pandas as pd
import numpy as np
import time
from ml import ML
from scaler import Scaler

iexec_out = os.environ['IEXEC_OUT']
iexec_in = os.environ['IEXEC_IN']

class Utils:
   
    def ensureDeterministicOutput(response_json,unix_timestamp):
        for x in range(len(response_json)):
            if(int(response_json[x][6]) > unix_timestamp):
                del response_json[x]
        return response_json

    def parser(klines):
        seq_x = list()
        for row in klines:
            row[0] = int(row[0])    #open time
            row[1] = float(row[1])  #open
            row[2] = float(row[2])  #high
            row[3] = float(row[3])  #low
            row[4] = float(row[4])  #close
            row[5] = float(row[5])  #volume
            row[6] = int(row[6])    #close time
            row[7] = float(row[7])  #quote asset volume
            row[8] = int(row[8])    #number of trades
            row[9] = float(row[9])  #taker buy base asset volume
            row[10] = float(row[10])#taker buy quote asset volume
            row[11] = float(row[11])#ignore
            seq_x.append(row)
        return np.array(seq_x)
        
class Binance:

    def fetchCandlesticks():
        url = 'https://api.binance.com/api/v3/klines'
        params = {
            'symbol': "BTCUSDT",
            'interval': "1h",
            'limit': '500',
            'endTime' : unix_timestamp
        }
        json_data = requests.get(url, params=params).json()
        json_data = Utils.ensureDeterministicOutput(json_data,unix_timestamp)
        seq_x = Utils.parser(json_data)
        return seq_x


if __name__ == '__main__':
    print("oracle started")
    prediction = 0  # default returned value to avoid attack on scheduler
    
    try:
        milliseconds = int(round(time.time() * 1000))
        #unix_timestamp = int(sys.argv[1])
        unix_timestamp = milliseconds
        print(unix_timestamp)
        #fetch data
        seq_x = Binance.fetchCandlesticks()

        #edit data
        seq_x = seq_x[-240:,[2,3,7]]
        scaler = Scaler()
        seq_x_scaled = scaler.fit_transform(seq_x)
        seq_x_scaled_reshaped = np.reshape(seq_x_scaled,(1,240,2))

        #load model
        ml = ML("test.h5")

        #predict
        prediction_scaled = ml.predict(seq_x_scaled_reshaped)

        #prepare result
        prediction = scaler.inverse(prediction_scaled)
        prediction = int(prediction)

    except Exception as e:
        print('Execution Failure: {}'.format(e))

    callback_data = eth_abi.encode_abi(['uint256'],  [prediction]).hex()
    callback_data = '0x{}'.format(callback_data)
    print('callback_data: {}'.format(callback_data))
    print('prediction: {}'.format(prediction))
    with open(iexec_out + '/result.txt', 'w+') as fout:
        fout.write("done")
    with open(iexec_out + '/computed.json', 'w+') as f:
        json.dump({"callback-data": callback_data, "prediction_debug" : prediction, "deterministic-output-path" : iexec_out + '/result.txt'}, f)
