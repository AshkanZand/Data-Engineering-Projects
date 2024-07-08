# Introduction
Using databases is an important and useful method of sharing information. To preserve repeated storage of the same files containing the required data, it is a good practice to save the said data on a database on a server and access the required subset of information using database management systems.

In this project, you'll learn how to create a database, load data from a CSV file as a table, and then run queries on the data using Python.

# Objectives
* Create a database using Python
* Load the data from a CSV file as a table to the database
* Run basic "queries" on the database to access the information

# Scenario
Consider a dataset of employee records that is available with an HR team in a CSV file. As a Data Engineer, you are required to create the database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS. The headers of the available data are :
<table>
  <thead>
    <tr>
    <th>Header</th>
    <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ID</td>
      <td>Employee ID</td>
    </tr>
    <tr>
      <td>FNAME</td>
      <td>First Name</td>
    </tr>
    <tr>
      <td>LNAME</td>
      <td>Last Name</td>
    </tr>
    <tr>
      <td>CITY</td>
      <td>City of residence</td>
    </tr>
    <tr>
      <td>CCODE</td>
      <td>Country code (2 letters)</td>
    </tr>
  </tbody>
</table>

* Download the csv file available in the link shared above.
```python
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv" -o INSTRUCTOR.csv
```
