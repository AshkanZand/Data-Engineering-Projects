# Introduction
Extract, Transform and Load (ETL) operations are of extreme importance in the role of a Data engineer. A data engineer extracts data from multiple sources and different file formats, transforms the extracted data to predefined settings and then loads the data to a database for further processing. In this lab, you will get hands-on practice of performing these operations.

# Objectives
After completing this project, you will be able to:

Read CSV, JSON, and XML file types.
Extract the required data from the different file types.
Transform data to the required format.
Save the transformed data in a ready-to-load format, which can be loaded into an RDBMS.

##Task:
* Download the zip file containing the required data in multiple formats.
```ruby
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip" -o source.zip
```

* The data available has three headers:'name','height','weight'. Implement the extraction process for the CSV, JSON, and XML files.

* The height in the extracted data is in inches, and the weight is in pounds. However, for your application, the height is required to be in meters, and the weight is required to be in kilograms, rounded to two decimal places. Therefore, you need to write the function to perform the unit conversion for the two parameters.

* Implement the loading function for the transformed data to a target file, transformed_data.csv.

* Implement the logging function for the entire process and save it in log_file.txt.

* Test the implemented functions and log the events as done in the lab.
