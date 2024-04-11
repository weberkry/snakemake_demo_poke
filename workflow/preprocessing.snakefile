rule list_train_data:
	input:
		train = config["train_folder"]
	output:
		train_matrix="Output/Preprocessing/train_matrix.npy",
		classes="Output/Preprocessing/class.csv"
	conda: 
		"env/preprocessing_images.yml"
	script:
		"scripts/preprocessing_images.py"
	
rule train_test_split:
	input:
		X = "Output/Preprocessing/train_matrix.npy",
		y = "Output/Preprocessing/class.csv"
	output:
		X_train = "Output/Train_Test_Set/X_train.npy",
		X_val = "Output/Train_Test_Set/X_val.npy",
		y_train = "Output/Train_Test_Set/y_train.csv",
		y_val = "Output/Train_Test_Set/y_val.csv"
	conda:
		"env/classify.yml"
	script:
		"scripts/train_test_split.py"

rule distribution_train_set:
	input:
		y_train = "Output/Train_Test_Set/y_train.csv"
	output:
		plot = "Output/Train_Test_Set/distribution_train_set.pdf"
	conda:
		"env/classify.yml"
	script:
		"scripts/distribution_train_set.py"