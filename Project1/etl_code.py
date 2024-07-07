import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

#%% Extraction

def extract_from_csv(file_to_process):
    '''extract from a CSV file
    ''' 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

def extract_from_json(file_to_process):
    '''To extract from a JSON file
    ''' 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe

def extract_from_xml(file_to_process):
    '''To extract from an XML file 
    '''
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) 
    tree = ET.parse(file_to_process) 
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe if not dataframe.empty else None, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe

def extract():
    '''to identify which function to call on basis of the filetype of the data file.
    ''' 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
     
    # process all csv files 
    for csvfile in glob.glob("source/*.csv"):
        extracted_data = pd.concat([extracted_data if not extracted_data.empty else None, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("source/*.json"): 
        extracted_data = pd.concat([extracted_data if not extracted_data.empty else None, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("source/*.xml"): 
        extracted_data = pd.concat([extracted_data if not extracted_data.empty else None, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data

#%% Transformation  

def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data

#%% Loading and Logging

def load_data(target_file, transformed_data):
    '''load the transformed data to a CSV
    ''' 
    transformed_data.to_csv(target_file)

def log_progress(message): 
    '''to implement the logging operation
    '''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n')

#%% Testing ETL operations and log progress

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended")  