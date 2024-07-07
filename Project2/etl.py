import glob
import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET

def extract_form_xml(xml_file):
    '''To extract from an XML file 
    '''
    dataframe = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel']) 
    tree = ET.parse(xml_file) 
    root = tree.getroot() 
    for person in root: 
        car_model = person.find("car_model").text 
        year = int(person.find("year_of_manufacture").text) 
        price = float(person.find("price").text)
        fuel = person.find("fuel").text
        dataframe = pd.concat([dataframe if not dataframe.empty else None, pd.DataFrame([{'car_model':car_model, 'year_of_manufacture':year, 'price':price, 'fuel':fuel}])], ignore_index=True) 
    return dataframe


# Extract
def extract():
    extracted_data = pd.DataFrame(columns = ['car_model', 'year_of_manufacture', 'price', 'fuel'])
    # CSV
    for csvfile in glob.glob("datasource/*.csv"):
        extracted_data = pd.concat([extracted_data if not extracted_data.empty else None, pd.read_csv(csvfile)], ignore_index=True)

    # json
    for jsonfile in glob.glob("datasource/*.json"):
        extracted_data = pd.concat([extracted_data if not extracted_data.empty else None, pd.read_json(jsonfile,lines=True)],ignore_index=True)

    # xml
    for xmlfile in glob.glob("datasource/*.xml"):
        extracted_data = pd.concat([extracted_data if not extracted_data.empty else None, extract_form_xml(xmlfile)],ignore_index=True)

    return extracted_data

# Transform
def transform(extracted_data):
    extracted_data["price"] = round(extracted_data["price"],2)
    return extracted_data


# Load and Log
target_file = "transformed_data.csv"
log_file = "log_file.txt"

def log_progress(message):
    timeformat = "%Y-%h-%d-%H:%M:%S"
    timestamp = datetime.now().strftime(timeformat)
    with open(log_file,'a') as f:
        f.write(timestamp+','+message+"\n")        

def load_data (target_file,transformed_data):
    transformed_data.to_csv(target_file)

#%% Testing ETL operations and log progress
 

##-------- Extraction process -------- 
# Log the initialization of the ETL process  
log_progress("ETL Job Started")

# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended")

## -------- Transformation process -------- 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data)

# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 

## --------  Loading process -------- 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended")  