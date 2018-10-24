import pandas as pd
import numpy as np
from collections import Counter

#Syntax: outliers = detect_outliers(<df>,<integer>,['Feature1', 'Feature2'])
#Returns indecies to drop, evaluate with df.iloc[outliers]

#Outlier detection
def detect_outliers(df,n,features):
	outlier_indicies = []

	#Iterate thorugh columns
	for col in features:
		Q1 = np.percentile(df[col].dropna(), 25)
		Q3 = np.percentile(df[col].dropna(), 75)
		#IQR
		IQR = Q3 - Q1
		outlier_step = 1.5 * IQR

		#Outlier list of indicies
		outlier_list_col = df[(df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step)].index
		outlier_indicies.extend(outlier_list_col)

	#Count outlier indicies, returns (item,number_of_counts)
	outlier_indicies = Counter(outlier_indicies)
	#Counter -> counts number of times a number exists in outlier_indices
	multiple_outliers = list(k for k, v in outlier_indicies.items() if v > n)

	return multiple_outliers
