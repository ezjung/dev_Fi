# Umami scripts usage


## 1. Setting file

##### 1-1. mkfolder.py
###### Begining of the month

makes folders begining of the month

need to give args 'year' and 'month' in digits

generate dummie file to be replaced

meta/shift/7shift report file = 2020_05A.csv
meta/shift/7shift report file = 2020_05B.csv

meta/uber/Uber_2020_05_Dimond.csv
meta/uber/Uber_2020_05_Uptown.csv

meta/square/square report file = 2020_05A_Dimond.csv
meta/square/square report file = 2020_05A_Uptown.csv
meta/square/square report file = 2020_05B_Dimond.csv
meta/square/square report file = 2020_05B_Uptown.csv

meta/square/square report file = pmethod_A_Dimond_Day.csv
meta/square/square report file = pmethod_A_Dimond_Night.csv
meta/square/square report file = pmethod_A_Uptown_Day.csv
meta/square/square report file = pmethod_A_Uptown_Night.csv
meta/square/square report file = pmethod_B_Dimond_Day.csv
meta/square/square report file = pmethod_B_Dimond_Night.csv
meta/square/square report file = pmethod_B_Uptown_Day.csv
meta/square/square report file = pmethod_B_Uptown_Night.csv

```
$ mkfolder.py 2020 07 A
```
##### 1-2. config.py

###### biMonthly

has static variables for calculation

## 2. Emp_compensation_Calculation

##### 2-1. emp_hr.py

Calculate employee hours by dates in tabular format by the locations.

emp_hr.py requires,

Data/emp.csv

meta/shift/7shift report file = 2020_05A.csv format

square data general
meta/square/square report file = 2020_05A_Dimond.csv

4 x square data payment method report
meta/square/square report file = pmethod_A_Dimond_Day.csv
meta/square/square report file = pmethod_A_Dimond_Night.csv
meta/square/square report file = pmethod_A_Uptown_Day.csv
meta/square/square report file = pmethod_A_Uptown_Night.csv

##### 2-2. emp_com.py

To calculate the commission of workers. execute bi Monthly

implement after process emp_hr.py


## 3. Delivery parse for Night work commission

##### 3-1. caviar_scrap.py

Scraping caviar website and makes a table for 'Delivery' and 'Pickup' based on the location

Need to give an argv 'D' or 'U' 

```
$ caviar_scrap.py D # or U
```



##### 3-2. caviar_parse.py

caviar_parse.py requires caviar_scrap.py data parsed into 

all caviar sales by the month

night time caviar sales for night time calculation



##### 3-3. uber_parse.py

uber_parse.py requires uber data downloaded from their website.

When saving file, file name format is 

```
Uber_2020_05_Dimond.csv
```

csv data is parsed into 

all uber sales by the month

night time uber sales for night time calculation


## 4. Night compensation Calculation

##### 4-1. emp_night.py

Once a month use it.

Requires 

caviar_parse, uber_parse

square night time report 

Input on 2020_06_manual_input.xslx

generate report/2020_05_Dimond_Night.csv


##### 4-2. emp_night2.py


generate xlsx file to print checks









