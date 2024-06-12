from datetime import datetime

_sectionID=0
_highway=0
_section=0
_sectionLength=0
_sectionDescription=''
_date=datetime.now()
_description=''
_group=''
"""
Types of counts and analysis - see t able below
TC - Traffic Count
VC - Vehicle Classification
TM - Turning Movement. These represent the various approach movements (left, thru, right) that pass through an intersection over a given period of time
SA - Signal Analysis. Driven by PP (Priority Points at or near 100)
LT - Left Turn Lane warrant nomographs within the Geometric Design Standards for Ontario Highways
RT - Right Turn Lane warrant nomographs prescribed by the Ohio Department of Transportation
"""
_type=''
_county=''
#Percentage of Trucks on the highway
_ptrucks=0
#Average Daily Traffic
_adt=0
#Annual Average Daily Traffic
_aadt='ignore'
#The direction vehicles are traveling
_direction=''
#This is the speed at which 85% of the vehicles are traveling at, or below
_85pct='ignore'
_priorityPoints='ignore'

def get_sectionID():
    """Get the section ID."""
    return _sectionID

def set_sectionID(value):
    """Set the section ID."""
    global _sectionID
    _sectionID = value
    
def get_highway():
    """Get the highway."""
    return _highway

def set_highway(value):
    """Set the highway."""
    global _highway
    _highway = value

def get_section():
    """Get the section."""
    return _section

def set_section(value):
    """Set the section."""
    global _section
    _section = value

def get_sectionLength():
    """Get the section length."""
    return _sectionLength

def set_sectionLength(value):
    """Set the section length."""
    global _sectionLength
    _sectionLength = value

def get_sectionDescription():
    """Get the section description."""
    return _sectionDescription

def set_sectionDescription(value):
    """Set the section description."""
    global _sectionDescription
    _sectionDescription = value

def get_date():
    """Get the date."""
    return _date

def set_date(value):
    """Set the date."""
    global _date
    _date = value

def get_description():
    """Get the description."""
    return _description

def set_description(value):
    """Set the description."""
    global _description
    _description = value

def get_group():
    """Get the group."""
    return _group

def set_group(value):
    """Set the group."""
    global _group
    _group = value

def get_type():
    """Get the type."""
    return _type

def set_type(value):
    """Set the type."""
    global _type
    _type = value

def get_county():
    """Get the county."""
    return _county

def set_county(value):
    """Set the county."""
    global _county
    _county = value

def get_ptrucks():
    """Get the percentage of trucks on the highway."""
    return _ptrucks

def set_ptrucks(value):
    """Set the percentage of trucks on the highway."""
    global _ptrucks
    _ptrucks = value

def get_adt():
    """Get the average daily traffic."""
    return _adt

def set_adt(value):
    """Set the average daily traffic."""
    global _adt
    _adt = value

def get_aadt():
    """Get the annual average daily traffic."""
    return _aadt

def set_aadt(value):
    """Set the annual average daily traffic."""
    global _aadt
    _aadt = value

def get_direction():
    """Get the direction."""
    return _direction

def set_direction(value):
    """Set the direction."""
    global _direction
    _direction = value

def get_85pct():
    """Get the 85th percentile speed."""
    return _85pct

def set_85pct(value):
    """Set the 85th percentile speed."""
    global _85pct
    _85pct = value

def get_priorityPoints():
    """Get the priority points."""
    return _priorityPoints

def set_priorityPoints(value):
    """Set the priority points."""
    global _priorityPoints
    _priorityPoints = value

def printDTO():
    """Print the DTO object."""
    print("Section ID: " + str(_sectionID))
    print("Highway: " + str(_highway))
    print("Section: " + str(_section))
    print("Section Length: " + str(_sectionLength))
    print("Section Description: " + str(_sectionDescription))
    print("Date: " + str(_date))
    print("Description: " + str(_description))
    print("Group: " + str(_group))
    print("Type: " + str(_type))
    print("County: " + str(_county))
    print("Percentage of Trucks: " + str(_ptrucks))
    print("ADT: " + str(_adt))
    print("AADT: " + str(_aadt))
    print("Direction: " + str(_direction))
    print("85th Percentile: " + str(_85pct))
    print("Priority Points: " + str(_priorityPoints))
    print("\n")