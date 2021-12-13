import gzip
import json
import pandas as pd


class Data:
    def getDataFrame(nRows):
        contents = gzip.open('get.gz', 'rt', encoding='utf-8')
        data = contents.read()
        data_json = json.loads(data)
        df = pd.DataFrame(data_json)
        df = Data.rename(df)
        df = df.iloc[-nRows:]
        print(df)
        return df

    def rename(df):
        df = df.rename(columns={df.columns[0]: 'openTime', df.columns[1]: 'open',
        df.columns[2]: 'high', df.columns[3]: 'low',df.columns[4]: 'close', df.columns[5]: 'volume',
        df.columns[6]: 'closeTime',df.columns[7]: 'quoteAssetVolume',df.columns[8]: 'numberOfTrades',
        df.columns[9]: 'takerBuyBaseAssetVolume',df.columns[10]: 'takerBuyQuoteAssetVolume',df.columns[11]: 'ignore', })
        return df


if __name__ == '__main__':
    Data.getData(5)
    