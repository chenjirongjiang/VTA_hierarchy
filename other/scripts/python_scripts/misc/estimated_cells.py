import pandas
path = 'C:/Users/Chenj/hpc/websums/Wang/'
files=['SAMN21889406.csv','SAMN21889407.csv','SAMN21889409.csv','SAMN21889411.csv','SAMN21889416.csv','SAMN21889422.csv','SAMN21889423.csv','SAMN21889424.csv','SAMN21889433.csv','SAMN21889436.csv']
for file in files:
    content=pandas.read_csv(f'{path}{file}')
    print(content['Estimated Number of Cells'][0])

