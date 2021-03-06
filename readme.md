# Data Expo 2009 - Airline on-time performance
## by (Mahmoud Lotfi)

## Dataset

- The data consists of flight arrival and departure details for all commercial flights within the USA, from October 1987 to April 2008. 
- This is a large dataset: there are nearly 120 million records in total, and takes up 1.6 gigabytes of space compressed and 12 gigabytes when uncompressed. 
- The data comes originally from RITA where it is described in detail. 
- the data in bzipped csv file. 
- These files have derivable variables removed, are packaged in yearly chunks and have been more heavily compressed than the originals.
- in this project we will discuss flight delay for 2008 data set
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

### 01. Flights without cancellation nor divertion dataset:
#### What is the structure of your dataset?
> There are 6,851,832 flight observations with 26 features in 2008 without diverted/cancelled flights and missing or incorrect??? data.
#### What is/are the main feature(s) of interest in your dataset?
> Delayed flights in terms of carriers, origin & time.
#### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
> ArrDelay, Month, DayOfWeek, DepTime, ArrTime, UniqueCarrier.
### 02. Flights that have been Cancellation:
#### What is the structure of your dataset?
> There are 137,434 flight observations with 12 features in 2008.
#### What is/are the main feature(s) of interest in your dataset?
 - what are the worstest airlines in terms of cancelled flighes?
 - what are the most cases of flights cancelled?
#### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
> UniqueCarrier, CancellationCode

### 03. Flights that have been diverted:
#### What is the structure of your dataset?
> There are 17,265 flight observations with 12 features in 2008.
#### What is/are the main feature(s) of interest in your dataset?
> what are the Origin & Dest that have the most diverted flighes?
#### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
> Origin & Dest.

## Key Insights for Presentation
### key findings:
01. Flights status distribution in 2008
02. Flight delay reasons and how much they contribute to the number of delayed flights
03. The worest day to travel.
04. Which Airlines have the longest delays?
05. What is the worst time of day to travel?

### insights :
01. It turn out most of flight arrive early , nearly 70%.
02. We also see that the weather is not the main reason for delays. Weather only contributes to 2% of the delays.
03. The wostest arrival time delay ocurr Tuesday for most of carriers
04. B6 had the worst for arrivals delay and the lowest departure delay, while AQ, HA and YV has the lowest arravial delay
05. unstable arrival delay between 12:00 AM to 05:00 AM, a huge crowd gathered between 05:00 AM to 06:00 AM


## How to Run the project:
- Insrt raw data download in __"./data/raw"__
- Run the script __"Communicate-Dtata-Finding\src\data\make_dataset.py"__
- Now you can find output data from script  __"Communicate-Dtata-Finding/data/interim/*.csv"__
- Run the notebook in __"Communicate-Dtata-Finding\notebooks\exploration.ipynb"__ to find __Exploratory data__
- Run the notebook in __"Communicate-Dtata-Finding\notebooks\explanatory.ipynb"__ to find __Explanatory data__

## Resources :
- [DataExpo2009](https://community.amstat.org/jointscsg-section/dataexpo/dataexpo2009)
- [Kaggle](https://www.kaggle.com/adveros/flight-delay-eda-exploratory-data-analysis)
