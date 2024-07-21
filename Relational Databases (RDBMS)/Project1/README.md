# Project Overview
In the project you will design a database using an ERD tool and implement the database schema using PostgreSQL, MySQL and (optionally) Db2. (This project is based on the IBM Data Engineering Professional Certificate)

## Scenario
In this scenario, you have recently been hired as a Data Engineer by a New York based coffee shop chain that is looking to expand nationally by opening a number of franchise locations. As part of their expansion process, they want to streamline operations and revamp their data infrastructure.

Your job is to design their relational database systems for improved operational efficiencies and to make it easier for their executives to make data driven decisions.

Currently their data resides in several different systems: Accounting software, suppliers' databases, point of sales (POS) systems, and even spreadsheets. You will review the data in all of these systems and design a central database to house all data. You will then create the database objects and load them with source data. Finally, you will create subsets of data that your business partners require, export them, and then load them into staging databases that use different RDBMS.

## Data used in this project
In your scenario, you will be working with data from the following sources:

* Staff information held in a spreadsheet at headquarters (HQ)
* Sales outlet information held in a spreadsheet at HQ
* Sales data output as a CSV file from the POS system in the sales outlets
* Customer data output as a CSV file from a custom customer relationship management system
* Product information maintained in a spreadsheet exported from your supplier's database

## Objectives
* Identify entities
* Identity attributes
* Create an entity relationship diagram (ERD) using the pgAdmin ERD tool
* Normalize tables
* Define keys and relationships
* Create database objects by generating and running the SQL script from the ERD tool
* Create a view and export the data
* Create a materialized view and export the data
* Import data into a MySQL database using phpMyAdmin GUI tool
