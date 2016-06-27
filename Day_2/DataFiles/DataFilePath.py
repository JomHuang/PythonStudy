"""
相关数据文件存储路径
"""

FILE_PATH = "../DataFiles/";
PEOPLE_FILE_PATH = "../DataFiles/people-file";
PEOPLE_PICKLE_PATH = "../DataFiles/people-pickle";
PEOPLE_SHELVE_PATH = "../DataFiles/people-shelve";
CLASS_SHELVE_PATH="../../DataFiles/class-shelve";

class DataFilePath:
    def __init__(self):
        self.FILE_PATH = FILE_PATH;
        self.PEOPLE_FILE_PATH = PEOPLE_FILE_PATH;
        self.PEOPLE_PICKLE_PATH = PEOPLE_PICKLE_PATH;
        self.PEOPLE_SHELVE_PATH = PEOPLE_SHELVE_PATH;
        self.CLASS_SHELVE_PATH=CLASS_SHELVE_PATH;

    def READ_FILE_PATH(self):
        return self.FILE_PATH;

    def READ_PEOPLE_FILE_PATH(self):
        return self.PEOPLE_FILE_PATH;

    def READ_PEOPLE_PICKLE_PATH(self):
        return self.PEOPLE_PICKLE_PATH;

    def READ_PEOPLE_PICKLE_RECS_PATH(self, dataName):
        return self.FILE_PATH + dataName;

    def READ_PEOPLE_SHELVE_PATH(self):
        return self.PEOPLE_SHELVE_PATH;

