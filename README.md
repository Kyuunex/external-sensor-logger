# linux_external_sensor_logger
Log sensor data from a Linux machine on an external server.

# What would you use this for?
In a situation where your computer is regularly shutting down to a suspected power or thermal issue, 
these scripts can be used to log the sensor data externally to be looked at later.  

You normally would not be able to log this data reliably on a local drive as a sudden power failure can prevent 
the data from being written and even cause filesystem corruption.
