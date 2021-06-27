import pandas as pd
def problem3_7(csv,row):
	df=pd.read_csv(csv)
	# df=pd.DataFrame(csv,columns=['flower','price'])
	df.columns=['flower','price']
	df.index=df['flower']
	df.drop('flower',axis=1,inplace=True)
	print(df['price'][row])
problem3_7('humpty.csv',"alyssum")
