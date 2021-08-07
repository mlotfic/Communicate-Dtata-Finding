# Data Expo 2009 - Airline on-time performance
## by (Mahmoud Lotfi)

## Dataset

- The data consists of flight arrival and departure details for all commercial flights within the USA, from October 1987 to April 2008. 
- This is a large dataset: there are nearly 120 million records in total, and takes up 1.6 gigabytes of space compressed and 12 gigabytes when uncompressed. 
- The data comes originally from RITA where it is described in detail. 
- the data in bzipped csv file. 
- These files have derivable variables removed, are packaged in yearly chunks and have been more heavily compressed than the originals.
- in this project we will discuss​ flight delay for 2008 data set
- Script locat 

#### individual years:

1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008

#### This dataset is composed by the following variables:
01.	Year	           1987-2008                                                                      
02.	Month	           1-12                                                                         
03.	DayofMonth	       1-31                                                                         
04.	DayOfWeek	       1 (Monday) - 7 (Sunday)                                                      

05.	DepTime	           actual departure time (local, hhmm)                                          
06.	CRSDepTime	       scheduled departure time (local, hhmm)                                       
07.	ArrTime	           actual arrival time (local, hhmm)                                            
08.	CRSArrTime	       scheduled arrival time (local, hhmm)                                         

09.	UniqueCarrier	   unique carrier code 
10.	FlightNum	       flight number 
11.	TailNum	           plane tail number: aircraft registration, unique aircraft identifier

12.	ActualElapsedTime  in minutes 
13.	CRSElapsedTime	   in minutes 
14.	AirTime	           in minutes      

15.	ArrDelay	       arrival delay, in minutes: A flight is counted as "on time" if it operated less than 15 minutes later the scheduled time shown in the carriers' Computerized Reservations Systems (CRS).
16.	DepDelay	       departure delay, in minutes                                                  

17.	Origin	           origin IATA airport code                                                     
18.	Dest	           destination IATA airport code                                                
19.	Distance	       in miles                                                                     

20.	TaxiIn	           taxi in time, in minutes                                                     
21.	TaxiOut	           taxi out time in minutes                                                     

22.	Cancelled	       was the flight cancelled?                                                    
23.	CancellationCode   reason for cancellation (A = carrier, B = weather, C = NAS, D = security)    
24.	Diverted	       1 = yes, 0 = no                                                              

25.	CarrierDelay	   in minutes: 
    - Carrier delay is within the control of the air carrier. 
    - Examples of occurrences that may determine carrier delay are: 
        - aircraft cleaning, aircraft damage, awaiting the arrival of connecting passengers or crew, 
        - baggage, bird strike, cargo loading, catering, computer, outage-carrier equipment, 
        - crew legality (pilot or attendant rest), damage by hazardous goods, engineering inspection, fueling, 
        - handling disabled passengers, late crew, lavatory servicing, maintenance, oversales, 
        - potable water servicing, removal of unruly passenger, slow boarding or seating, 
        - stowing carry-on baggage, weight and balance delays.                                                                  
26.	WeatherDelay	   in minutes: Weather delay is caused by extreme or hazardous weather conditions that are forecasted or manifest themselves on point of departure, enroute, or on point of arrival. 

27.	NASDelay	       in minutes: Delay that is within the control of the National Airspace System (NAS) may include: non-extreme weather conditions, airport operations, heavy traffic volume, air traffic control, etc.                                                                 
28.	SecurityDelay	   in minutes:Security delay is caused by evacuation of a terminal or concourse, re-boarding of aircraft because of security breach, inoperative screening equipment and/or long lines in excess of 29 minutes at screening areas.                                                                   
29.	LateAircraftDelay  in minutes: Arrival delay at an airport due to the late arrival of the same aircraft at a previous airport. The ripple effect of an earlier delay at downstream airports is referred to as delay propagation. 


## Summary of Findings

> Summarize all of your findings from your exploration here, whether you plan on bringing them into your explanatory presentation or not.


## Key Insights for Presentation

> Select one or two main threads from your exploration to polish up for your presentation. Note any changes in design from your exploration step here.


## How to Run the project:
- Insrt raw data download in __"./data/raw"__
- Run the script __"Communicate-Dtata-Finding\src\data\make_dataset.py"__
- Now you can find output data from script  __"Communicate-Dtata-Finding/data/interim/*.csv"__
- Run the notebook in __"Communicate-Dtata-Finding\notebooks\exploration.ipynb"__ to find __Exploratory data__
- Run the notebook in __"Communicate-Dtata-Finding\notebooks\explanatory.ipynb"__ to find __Explanatory data__

## Resources :
- [DataExpo2009](https://community.amstat.org/jointscsg-section/dataexpo/dataexpo2009)
- [Kaggle](https://www.kaggle.com/adveros/flight-delay-eda-exploratory-data-analysis)