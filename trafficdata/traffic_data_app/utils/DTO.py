from datetime import datetime

class DTO:
    def __init__(self):
        self.sectionID = 0
        self.highway = 0
        self.section = 0
        self.sectionLength = 0
        self.sectionDescription = ''
        self.date = datetime.now()
        self.description = ''
        self.group = ''
        self.type = ''
        self.county = ''
        self.ptrucks = 0
        self.adt = 0
        self.aadt = 'ignore'
        self.direction = ''
        self.pct85 = 'ignore'
        self.priorityPoints = 'ignore'

    def get_sectionID(self):
        """Get the section ID."""
        return self._sectionID

    def set_sectionID(self, value):
        """Set the section ID."""
        self.sectionID = value
        
    def get_highway(self):
        """Get the highway."""
        return self.highway

    def set_highway(self, value):
        """Set the highway."""
        self.highway = value

    def get_section(self):
        """Get the section."""
        return self.section

    def set_section(self, value):
        """Set the section."""
        self.section = value

    def get_sectionLength(self):
        """Get the section length."""
        return self.sectionLength

    def set_sectionLength(self, value):
        """Set the section length."""
        self.sectionLength = value

    def get_sectionDescription(self):
        """Get the section description."""
        return self.sectionDescription

    def set_sectionDescription(self, value):
        """Set the section description."""
        self.sectionDescription = value

    def get_date(self):
        """Get the date."""
        return self.date

    def set_date(self, value):
        """Set the date."""
        self.date = value

    def get_description(self):
        """Get the description."""
        return self.description

    def set_description(self, value):
        """Set the description."""
        self.description = value

    def get_group(self):
        """Get the group."""
        return self.group

    def set_group(self, value):
        """Set the group."""
        self.group = value

    def get_type(self):
        """Get the type."""
        return self.type

    def set_type(self, value):
        """Set the type."""
        self.type = value

    def get_county(self):
        """Get the county."""
        return self.county

    def set_county(self, value):
        """Set the county."""
        self.county = value

    def get_ptrucks(self):
        """Get the percentage of trucks on the highway."""
        return self.ptrucks

    def set_ptrucks(self, value):
        """Set the percentage of trucks on the highway."""
        self.ptrucks = value

    def get_adt(self):
        """Get the average daily traffic."""
        return self.adt

    def set_adt(self, value):
        """Set the average daily traffic."""
        self.adt = value

    def get_aadt(self):
        """Get the annual average daily traffic."""
        return self.aadt

    def set_aadt(self, value):
        """Set the annual average daily traffic."""
        self.aadt = value

    def get_direction(self):
        """Get the direction."""
        return self.direction

    def set_direction(self, value):
        """Set the direction."""
        self.direction = value

    def get_85pct(self):
        """Get the 85th percentile speed."""
        return self.pct85

    def set_85pct(self, value):
        """Set the 85th percentile speed."""
        self.pct85 = value

    def get_priorityPoints(self):
        """Get the priority points."""
        return self.priorityPoints

    def set_priorityPoints(self, value):
        """Set the priority points."""
        self.priorityPoints = value

    # def printDTO():
    #     """Print the DTO object."""
    #     print("Section ID: " + str(self.sectionID))
    #     print("Highway: " + str(_highway))
    #     print("Section: " + str(_section))
    #     print("Section Length: " + str(_sectionLength))
    #     print("Section Description: " + str(_sectionDescription))
    #     print("Date: " + str(_date))
    #     print("Description: " + str(_description))
    #     print("Group: " + str(_group))
    #     print("Type: " + str(_type))
    #     print("County: " + str(_county))
    #     print("Percentage of Trucks: " + str(_ptrucks))
    #     print("ADT: " + str(_adt))
    #     print("AADT: " + str(_aadt))
    #     print("Direction: " + str(_direction))
    #     print("85th Percentile: " + str(_85pct))
    #     print("Priority Points: " + str(_priorityPoints))
    #     print("\n")