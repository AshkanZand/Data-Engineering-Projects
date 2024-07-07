# Introduction
Extract, Transform and Load (ETL) operations are of extreme importance in the role of a Data engineer. A data engineer extracts data from multiple sources and different file formats, transforms the extracted data to predefined settings and then loads the data to a database for further processing. In this lab, you will get hands-on practice of performing these operations.

# Objectives
After completing this project, you will be able to:

Read CSV, JSON, and XML file types.
Extract the required data from the different file types.
Transform data to the required format.
Save the transformed data in a ready-to-load format, which can be loaded into an RDBMS.

## Goal perform ETL operations on the data available in the link below:
```ruby
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/datasource.zip" -o datasource.zip
```
 
* Create a folder data_source and use the terminal shell to change the current directory to \home\project\data_source. Create a file etl_practice.py in this folder.

* Download and unzip the data available in the link shared above.

* The data available has four headers: 'car_model', 'year_of_manufacture', 'price', 'fuel'. Implement the extraction process for the CSV, JSON, and XML files.

* Transform the values under the 'price' header such that they are rounded to 2 decimal places.

* Implement the loading function for the transformed data to a target file, transformed_data.csv.

* Implement the logging function for the entire process and save it in log_file.txt.

* Test the implemented functions and log the events as done in the lab.

