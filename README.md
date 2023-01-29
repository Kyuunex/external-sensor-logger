# linux_external_sensor_logger
Log sensor data from a Linux machine on an external server.

# What would you use this for?
In a situation where your computer is regularly shutting down to a suspected power or thermal issue, 
these scripts can be used to log the sensor data externally to be looked at later.  

You normally would not be able to log this data reliably on a local drive as a sudden power failure can prevent 
the data from being written and even cause filesystem corruption.

# How to use?
- Run `sensor_logger_server.py` on a local server, like a Raspberry Pi.
- Edit `sensor_logger_client.bash` and put the IP address of the local server inside.
- Run `sensor_logger_client.bash`
- Use your computer normally until your computer crashes or whatever issue you are facing happens then restart.
- Retrieve the logged data from the server's temporary memory by using one of the endpoints provided.

# Endpoints:
- GET: `/export.json.gz` - Export the data logged on the server's temporary memory as a gzip-compressed download (Recommended).
- GET: `/export.json` - Export the data logged on the server's temporary memory as an uncompressed download.
- GET: `/export_to_internal_storage` - Export the data logged on the server's temporary memory to the server's internal storage. (May not work depending on write priviliges)
- POST (JSON): `/sensor_logger` - The client logger uses this to submit sensor data, you don't need to touch it.

Note: Using any of the export endpoints or closing the server app clears the logs from the server's temporary memory.
