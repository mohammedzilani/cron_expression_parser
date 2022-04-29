# Cron Expression Parser

This is a command line application which will help parse strings formatted as cron expressions.
E.g: ~$ cron_expression_parser ＂*/15 0 1,15 * 1-5 /usr/bin/find＂

## Steps to run the program (on a linux os)
1. git clone https://github.com/mohammedzilani/cron_expression_parser.git
2. Under dist folder, we can find cron_expression_parser application
3. Run the program with the full path in the same way as mentioned in the example above

If suppose for any reason above workflow didn't work, one can still run the `cron_expression_parser.py` script in the following way:

`cron_expression_parser.py ＂*/15 0 1,15 * 1-5 /usr/bin/find＂`

## Tests that were performed
All the tests that were performed are mentioned here

```
1. Valid 5 field cron string with command

root@DESKTOP-U4Q4CB8:~# cron_expression_parser "*/15 0 1,15 * 1-5 /usr/bin/find"
minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find

2. Program run without passing the cron string

root@DESKTOP-U4Q4CB8:~# cron_expression_parser                                                                                          
cron string should be provided along with the program

3. Not a valid string (only 4 fields were mentioned)

root@DESKTOP-U4Q4CB8:~# cron_expression_parser "*/15 0 1,15 * /usr/bin/find"                                                            
Not a valid cron string

4. Cron string with one of the time field mentioned with both range as well as step (e.g: 3-50/15 for the minute field)

root@DESKTOP-U4Q4CB8:~# cron_expression_parser "3-50/15 0 1,15 * 1-5 /usr/bin/find"                                                   
minute        3 18 33 48                                                                                                             
hour          0                                                                                                                       
day of month  1 15                                                                                                                    
month         1 2 3 4 5 6 7 8 9 10 11 12                                                                                             
day of week   1 2 3 4 5                                                                                                               
command       /usr/bin/find

5. Cron string with fields out of range

root@DESKTOP-U4Q4CB8:~# cron_expression_parser "3-50/15 0 1,15 * 1-8 /usr/bin/find"                                                   
Range 1-8 is out of bounds of field day of week                                                                                       
Not a valid cron string 

All these tests were performed for changing all the time fields

```
