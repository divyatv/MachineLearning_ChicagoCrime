-------   First week ------------------------------
Chicago Crime - Machine learning and Predictions

This branch includes 3 scripts:

data_mining.ipynb:
    input:  original Chicago Data set - the data set includes more than
            1 million raws. This can not be just used for the project.
   output:  Crime_selected.cvs - select about 2000 records for each crime type
            with total 6 crime types (total 12000 from the original dataset)

   function:  massage the data to combine the crime type in column based on 
             time, lattude and longtitue. This is essential to wite the ML code.

data_plot.ipynb:

    input:  the data set from data_mining script - Crime_selected.csv
    output:  Plot 4 types of visaulation for each crime. 

    Function:  I provide a TEST code in the __name__ == __main__ as examples.
               You can use that create a html/java script to plot the
	       data from flask as you did in project2.
	       (I have example in index.html)


ml.ipynb:
    input:  the data set from data_mining script - Crime_selected.csv
    output:  3 ML logic:  knn, decision tree, random forest

    Function: I also provide TEST code, please check __name__ == __main__ block
              You can select X_values and y_values to run all 3 ML logic. Also,               
	      I suggest you save different result in a png files and using the
	      flask to display them for demo. (Otherwise, it will take long
	      time to run).   YOu run off-line, collect the information in a 
	      directory. In the demo, you can just show the result very quick.

-----------------    On second week  -------------------------------------

start to write flask code to display plot to browser

This will be done on app.py and templates/main.html
