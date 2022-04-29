#!/usr/bin/env python3
import sys
from sys import argv,exit

# This class is to represent particluar field (i.e minute, hour, day_of_month, month, day_of_week) in the cron string 
# Parameters:
# key - string to uniquely identify field
# name - name which will be printed in the output
# field_string - cron style field string
# start_interval - integer which represents start of the field (e.g: for hour field start_interval will be 0)
# end_interval - integer which represents end of the field (e.g: for hour field end_interval will be 23)
# values - list of integers which will be represented in the output for the field
class cron_field:
    def __init__(self, key, name, field_string, start_interval, end_interval):
        self.key = key
        self.name = name
        self.field_string = field_string
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.values = []

    # utility funtion which help fill the values in the case where the string is either a range like * or a-b
    def range_based_values(self, range_str = '*', step = 1):

        if range_str == '*':
            range_num_start = self.start_interval
            range_num_end = self.end_interval
        elif '-' in range_str:
            range_num_split = range_str.split('-')
            range_num_start =  int(range_num_split[0])
            range_num_end = int(range_num_split[1])

        if range_num_start >= self.start_interval and range_num_end <= self.end_interval:
            self.values = range(range_num_start, range_num_end + 1, step)
        else:
            print("Range {0} is out of bounds of field {1}".format(self.field_string, self.name))
            return -1
        return 0

    # setter function which will help fill the values parameter based on the input field string 
    def set_values(self):

        if '/' in self.field_string:
            field_string_split = self.field_string.split('/')
            range_num =  field_string_split[0]
            step = int(field_string_split[1])
            return self.range_based_values(range_num, step)

        if '-' in self.field_string:
            return self.range_based_values(self.field_string)

        if ',' in self.field_string:
            comma_sep_vals = self.field_string.split(',')
            for val in comma_sep_vals:
                if int(val) >= self.start_interval and int(val) <= self.end_interval:
                    self.values.append(int(val))
                else:
                    print("Value {0} provided is out of bounds of the field {1}".format(val, self.name))
                    return -1
            return 0

        if self.field_string == '*':
            self.range_based_values()
        else:
            if int(self.field_string) >= self.start_interval and int(self.field_string) <= self.end_interval:
                self.values.append(int(self.field_string))
            else:
                print("Value {0} provided is out of bounds of the field {1}".format(self.field_string, self.name))
                return -1
            return 0

    def output_string(self):

         values_list = [str(x) for x in self.values]
         values_str = ' '.join(values_list)
         return f'{self.name:14}{values_str}'


def cron_expression_parser(cron_string):
    cron_string_split = cron_string.split(' ')
    if len(cron_string_split) != 6:
        print("Not a valid cron string")
        return

    field_objects = []

    minute_str = cron_string_split[0]
    field_objects.append(cron_field("min", "minute", minute_str, 0, 59))
    hour_str = cron_string_split[1]
    field_objects.append(cron_field("hour", "hour", hour_str, 0, 23))
    day_of_month_str = cron_string_split[2]
    field_objects.append(cron_field("day_of_month", "day of month", day_of_month_str, 1, 31))
    month_str = cron_string_split[3]
    field_objects.append(cron_field("month", "month", month_str, 1, 12))
    day_of_week_str = cron_string_split[4]
    field_objects.append(cron_field("day_of_week", "day of week", day_of_week_str, 1, 7))
    command = cron_string_split[5]

    for obj in field_objects:
        if obj.set_values() == -1:
            print("Not a valid cron string")
            return


    for obj in field_objects:
        print(obj.output_string())

    print('{:14}{}'.format('command', command))


if len(sys.argv) <= 1:
    print("cron string should be provided along with the program")
    exit()

cron_string = sys.argv[1]
cron_expression_parser(cron_string)