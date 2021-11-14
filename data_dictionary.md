### Data Dictionary ###

**Sourced from Sobhan Moosavi**
https://smoosavi.org/datasets/us_accidents

| #   	|Attribute	|Description	|Nullable   	|
|---	|---	|---	|---	|
|1	|ID	|This is a unique identifier of the accident record.	|No|
|2	|Severity	|Shows the severity of the accident, a number between 1 and 4, where 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay).	|No|
|3	|Start_Time	|Shows start time of the accident in local time zone.	|No|
|4	|End_Time	|Shows end time of the accident in local time zone. End time here refers to when the impact of accident on traffic flow was dismissed.	|No|
|5	|Start_Lat	|Shows latitude in GPS coordinate of the start point.	|No|
|6	|Start_Lng	|Shows longitude in GPS coordinate of the start point.	|No|
|7	|End_Lat	|Shows latitude in GPS coordinate of the end point.	|Yes|
|8	|End_Lng	|Shows longitude in GPS coordinate of the end point.	|Yes|
|9	|Distance(mi)	|The length of the road extent affected by the accident.	|No|
|10	|Description	|Shows natural language description of the accident.	|No|
|11	|Number	|Shows the street number in address field.	|Yes|
|12	|Street	|Shows the street name in address field.	|Yes|
|13	|Side	|Shows the relative side of the street (Right/Left) in address field.	|Yes|
|14	|City	|Shows the city in address field.	|Yes|
|15	|County	|Shows the county in address field.	|Yes|
|16	|State	|Shows the state in address field.	|Yes|
|17	|Zipcode	|Shows the zipcode in address field.	|Yes|
|18	|Country	|Shows the country in address field.	|Yes|
|19	|Timezone	|Shows timezone based on the location of the accident (eastern, central, etc.).	|Yes|
|20	|Airport_Code	|Denotes an airport-based weather station which is the closest one to location of the accident.	|Yes|
|21	|Weather_Timestamp	|Shows the time-stamp of weather observation record (in local time).	|Yes|
|22	|Temperature(F)	|Shows the temperature (in Fahrenheit).	|Yes|
|23	|Wind_Chill(F)	|Shows the wind chill (in Fahrenheit).	|Yes|
|24	|Humidity(%)	|Shows the humidity (in percentage).	|Yes|
|25	|Pressure(in)	|Shows the air pressure (in inches).	|Yes|
|26	|Visibility(mi)	|Shows visibility (in miles).	|Yes|
|27	|Wind_Direction	|Shows wind direction.	|Yes|
|28	|Wind_Speed(mph)	|Shows wind speed (in miles per hour).	|Yes|
|29	|Precipitation(in)	|Shows precipitation amount in inches, if there is any.	|Yes|
|30	|Weather_Condition	|Shows the weather condition (rain, snow, thunderstorm, fog, etc.)	|Yes|
|31	|Amenity	|A POI annotation which indicates presence of amenity in a nearby location.	|No|
|32	|Bump	|A POI annotation which indicates presence of speed bump or hump in a nearby location.	|No|
|33	|Crossing	|A POI annotation which indicates presence of crossing in a nearby location.	|No|
|34	|Give_Way	|A POI annotation which indicates presence of give_way in a nearby location.	|No|
|35	|Junction	|A POI annotation which indicates presence of junction in a nearby location.	|No|
|36	|No_Exit	|A POI annotation which indicates presence of no_exit in a nearby location.	|No|
|37	|Railway	|A POI annotation which indicates presence of railway in a nearby location.	|No|
|38	|Roundabout	|A POI annotation which indicates presence of roundabout in a nearby location.	|No|
|39	|Station	|A POI annotation which indicates presence of station in a nearby location.	|No|
|40	|Stop	|A POI annotation which indicates presence of stop in a nearby location.	|No|
|41	|Traffic_Calming	|A POI annotation which indicates presence of traffic_calming in a nearby location.	|No|
|42	|Traffic_Signal	|A POI annotation which indicates presence of traffic_signal in a nearby loction.	|No|
|43	|Turning_Loop	|A POI annotation which indicates presence of turning_loop in a nearby location.	|No|
|44	|Sunrise_Sunset	|Shows the period of day (i.e. day or night) based on sunrise/sunset.	|Yes|
|45	|Civil_Twilight	|Shows the period of day (i.e. day or night) based on civil twilight.	|Yes|
|46	|Nautical_Twilight	|Shows the period of day (i.e. day or night) based on nautical twilight.	|Yes|
|47	|Astronomical_Twilight	|Shows the period of day (i.e. day or night) based on astronomical twilight.	|Yes|