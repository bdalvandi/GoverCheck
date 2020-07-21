# class to import a PMR file and extract the content, then make the output
import re
import pandas as pd
import numpy as np
import datetime as dt
import locale

class Pmr:

    # pmr_file: the full path and filename of the pmr file generated in VAX
    # frq_obj: the object ID of frequency used in the PMR file. normally it is '3058FRHZ'
    def __init__(self, pmr_file, frq_obj='3058FRHZ'):
        locale.setlocale(locale.LC_ALL, 'English')

        self.__fileName = pmr_file
        self.frqObj = frq_obj

        # regex patterns to extract data from pmr file
        self.__rx_unit = r'^\s+(\d+)\s+(\d\d\d\w+)\s+(\w+)\s+\w{3,4}\s+(\d+)'  # each presentation section of object ID, unit name, unit number
        self.__rx_header = r'^Time\s+(\|\s+(\w{8})\s+)+'  # header of each section starting with Time, object Ids, ...
        self.__rx_object = r'(\d{4}\w{4})'  # object ID
        self.__rx_date_time = r'^TRIGGER EVENT:\s+(\d\d-\d\d-\d\d)\s+(\d\d:\d\d:\d\d)'  # the line presenting event date and time
        self.__rx_row = r'^(\d\d:\d\d:\d\d)\s+("|(-?\d+\.\d\d\s[ABIFMN?]?))\s+'  # rows of each data section
        self.__rx_value = r'"|(-?\d+\.\d\d)'  # values in each row
        self.__rx_duration = r'^POST MORTEM\D+(\d\d:\d\d:\d\d)\D+(\d\d:\d\d:\d\d)'  # first line presenting start and stop time
        self.__table_columns = ['Object', 'Time', 'Value']  # column names to make a table of extracted data
        self.__unit_dict = {}  # dictionary to assign unit name and unit code to object ID: {'OBJECTID':{[UNIT_NAME, UNIT_CODE]}, ...}
        self.__table = []  # table to hold all extracted data as [OBJECTID, TIME, VALUE]
        self.__pmr_dict = {}  # dictionary to to export data as {'OBJECTID':{[TIME,VALUE], ...}, ...}

        with open(pmr_file) as f:
            __lines = f.readlines()
        for line in __lines:

            # extractin date and times
            match = re.search(self.__rx_duration, line)
            if match:
                self.__startTime = match.group(1)
                self.__stopTime = match.group(2)

            match = re.search(self.__rx_date_time, line)
            if match:
                self.__eventDate = match.group(1)
                self.__eventTime = match.group(2)
                continue

            # creating units dictionary
            match = re.search(self.__rx_unit, line)
            if match:
                unit_object = match.group(2)
                if unit_object == self.frqObj:
                    self.__unit_dict[unit_object] = ['FREQUENCY', '000-FRQ']
                    continue
                plant_code = unit_object[0:3]
                unit_code = unit_object[4:6]
                unit_plant = match.group(3)
                unit_number = 'G' + match.group(4)
                self.__unit_dict[unit_object] = [unit_plant + '_GEN_' + unit_number, plant_code + '-' + unit_number]
                continue

            # extracting headers of data each section
            match = re.search(self.__rx_header, line)
            if match:
                objects = re.findall(self.__rx_object, line)
                continue

            # getting values from each data row
            match = re.search(self.__rx_row, line)
            if match:
                time_point = match.group(1)
                values = re.findall(self.__rx_value, line)
                for i in range(len(objects)):
                    try:
                        val = float(values[i])
                    except:
                        val = None
                    self.__table.append([objects[i], pd.to_datetime(time_point, format='%H:%M:%S'), val])

        self.__df = pd.DataFrame.from_records(self.__table,
                                              columns=self.__table_columns)  # temp dataframe befor making pivot
        self.__pv_raw = self.__df.pivot_table(index='Object', values='Value',
                                              columns='Time')  # making the pivot based on OBJECTID, TIME
        self.__cols = list(self.__pv_raw.columns)
        self.__r = self.__pv_raw.shape[0]
        self.__t_start = dt.datetime.strptime(self.__startTime, '%H:%M:%S')
        self.__t_stop = dt.datetime.strptime(self.__stopTime, '%H:%M:%S')
        self.__t_delta = dt.timedelta(seconds=1)
        self.__t_cols = []
        while self.__t_start <= self.__t_stop:
            self.__t_cols.append(self.__t_start)
            self.__t_start += self.__t_delta
        for col in self.__t_cols:
            if col not in self.__cols:
                self.__pv_raw[col] = [np.NaN for i in range(self.__r)]
        self.__pv_raw = (((self.__pv_raw).transpose()).sort_index()).transpose()
        self.__pv = self.__pv_raw.interpolate(axis=1)  # interpolate to fill the blanks and make output as DataFrame

    @property  # when pmr data started to be recorded
    def startTime(self):
        return self.__startTime

    @property  # when data recording stopped
    def stopTime(self):
        return self.__stopTime

    @property  # date of event
    def eventDate(self):
        return self.__eventDate

    @property  # time of event
    def eventTime(self):
        return self.__eventTime

    @property  # returns the result as a DataFrame
    def dataAsFrame(self, u_name=True, nils=False):
        if not nils:
            self.__tmp = self.__pv.aggregate(['max'], axis=1)
            self.__pv = self.__pv[self.__tmp['max'] > 0]
        if u_name:
            self.__pv.index = self.__pv.index.map(lambda x: self.__unit_dict[x][0])
            self.__pv = self.__pv.sort_index()
            return self.__pv
        else:
            return self.__pv

    @property  # returns the result as a Dictionary
    def dataAsDict(self):
        return (self.__pv.transpose()).to_dict()  # make output as Dictionary

    @property  # returns the pmr file name and path
    def fileName(self):
        return self.__fileName

    @property  # returns the units dictionary of the pmr file
    def unitsAsDict(self):
        return self.__unit_dict

    @property  # returns the units dictionary as a Dataframe
    def unitsAsFrame(self):
        return pd.DataFrame.from_dict(self.__unit_dict, orient='index', columns=['Unit', 'Code'])
