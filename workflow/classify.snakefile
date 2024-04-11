
#rule train_model:


#rule transcribus_model:
	#input:
		#model = "Output/model/CNN_{optimizer}_{epochs}_{batchsize}",
		#classes = "Output/Train_Test_Set/y_train.csv",
		#image = "static/predict/{img}.jpg"
	#output:
		#result = "Output/Prediction/{img}/result_CNN_{optimizer}_{epochs}_{batchsize}_{img}.txt",
		#plot = "Output/Prediction/{img}/result_CNN_{optimizer}_{epochs}_{batchsize}_{img}.pdf"
	#conda: 
		#"env/classify.yml"
	#script:
		#"scripts/predict_image.py"

rule process_transcribus_output:
	input:
		raw_labels = "output/transcribus/transkribus_txt_{label_num}"
	output:
		tags = "output/transcribus/processed_labels/transkribus_txt_{label_num}.csv"
	conda:
		"env/process_transcribus_output.yml"
	script:
		"scripts/process_transcribus_output.py"


