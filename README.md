Market Basket Analysis

A System to find all the frequent purchased products by using Apriori Algorithm. Also association rules for frequent items. 

SPECIFICATIONS: 
	Specifications will be provided in a “​ config.csv​ ” file, located in the ​ same folder​  as the source 
	code. The config file will contain the absolute path of the input data file, the absolute path of the 
	file where you have to write the algorithm outputs, support and confidence values, and a “flag” 
	variable indicating whether you have to find the frequent itemsets and/or association rules 
	corresponding to the given support and confidence values.
	
	config.csv: 
	Text before the commas will remain the same in the actual config files, however, order of the 
	lines may change. The values of the support and confidence parameters will lie in the range 
	[0,1].
	The “flag” parameter in the config file can take 2 values: 0/1, as follows: 
	if flag==0: 
	You have to mine only the frequent itemsets for the given support. 
	if flag==1: 
	You have to mine both the frequent itemsets as well as the association rules for the 
	given  support and confidence values
	
	input.csv: 
	Input data file will be a comma separated (.csv) file, containing one transaction per line. 
	The location of the input file will be against the key “input” in the config file. 	
	
	output.csv: 
	You have to run the apriori algorithm on the given input data for the support and confidence 
	values provided in the config file, and write the output to the file provided in the config.csv file 
	against the key “output”. The output file will always be a comma separated (.csv) file. 
