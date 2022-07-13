#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calculations of time converting from seconds to desiginated form.
Seconds_in_a_year = 60*60*24*365
Seconds_in_a_day = 60*60*24
Seconds_in_an_hour = 60*60
Seconds_in_a_minute = 60


# In[2]:


import time


# In[3]:


#Variables for the input of event details.
Name_of_event= input('Enter the name of the event \n')
Year_of_event = int(input('Enter the year of your event e.g. 2022-2100 \n'))
Month_of_event = int(input ('Enter the month of your event e.g. 1-12 \n'))
Day_of_event = int(input ('Enter the day of your event e.g. 1-31 \n'))


# In[4]:


#Assignment of current time to the variable current_time_seconds .
current_time_seconds = time.time()


# In[5]:


import datetime, time


# In[6]:


#Assignment of event time to the variable Event_time .
Event_time = datetime.datetime(Year_of_event, Month_of_event, Day_of_event)


# In[7]:


time.mktime(Event_time.timetuple())


# In[8]:


Time_difference = time.mktime(Event_time.timetuple()) - current_time_seconds


# In[9]:


#Assignment of calculated time differences between the current time to the chosen date.
years = int(Time_difference// Seconds_in_a_year)

days = int(Time_difference % Seconds_in_a_year) // Seconds_in_a_day

hours = int(Time_difference % Seconds_in_a_year % Seconds_in_a_day) // Seconds_in_an_hour

minutes = int(Time_difference % Seconds_in_a_year % Seconds_in_a_day % Seconds_in_an_hour) // Seconds_in_a_minute

seconds = int(Time_difference % Seconds_in_a_year % Seconds_in_a_day % Seconds_in_an_hour % Seconds_in_a_minute)


# In[10]:


#Assignment of event day, month and year to dd/mm/yyyy format (individual variales changed to str to avoid array formatting)
Date_dd_mm_yyyy = (str(Day_of_event) + "/" + str(Month_of_event) + "/" + str(Year_of_event))


# In[11]:


print(Name_of_event, "is on the", Date_dd_mm_yyyy, "(",years, "year/s,", days, "day/s,", hours,"hour/s,", minutes, "minute/s and", seconds, "second/s later."")")


# In[ ]:




