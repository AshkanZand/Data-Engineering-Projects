# Introduction
n this project, you will work on real-world data and perform the operations of Extraction, Transformation, and Loading (ETL) as required.

### Objectives
* Use Webscraping techniques to extract information from any website as per requirement.
* Use Pandas data frames and dictionaries to transform data as per requirement.
* Load the processed information to CSV files and as Database tables
* Query the database tables using SQLite3 and pandas libraries
* Log the progress of the code properly

# Scenario
You have been hired as a data engineer by research organization. Your boss has asked you to create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR and INR as well, in accordance with the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

Your job is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

Particulars of the code to be made have been shared below.

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Value</th>
</tr>
</thead>
<tbody><tr>
<td>Code name</td>
<td><code>banks_project.py</code></td>
</tr>
<tr>
<td>Data URL</td>
<td><code>https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks</code></td>
</tr>
<tr>
<td>Exchange rate CSV path</td>
<td><a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv" target="_blank" rel="noopener noreferrer">https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv</a></td>
</tr>
<tr>
<td>Table Attributes (upon Extraction only)</td>
<td><code>Name</code>, <code>MC_USD_Billion</code></td>
</tr>
<tr>
<td>Table Attributes (final)</td>
<td><code>Name</code>, <code>MC_USD_Billion</code>, <code>MC_GBP_Billion</code>, <code>MC_EUR_Billion</code>, <code>MC_INR_Billion</code></td>
</tr>
<tr>
<td>Output CSV Path</td>
<td><code>Largest_banks_data.csv</code></td>
</tr>
<tr>
<td>Database name</td>
<td><code>Banks.db</code></td>
</tr>
<tr>
<td>Table name</td>
<td><code>Largest_banks</code></td>
</tr>
<tr>
<td>Log file</td>
<td><code>code_log.txt</code></td>
</tr>
</tbody></table>
