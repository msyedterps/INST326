class City:
    '''This class holds data representing a city
    
    Attributes:
    -name: the input string that contains the name of the city
    -neighbors: Starts off as an empty dictionary that will be populated with cities
    '''
    def __init__(self, Name):
        '''This init method sets the name argument to an attribute then sets the neighbor's attribute
        to an empty dictionary
        
        Arguments:
        -self: The instance itself
        -Name: The name of a city
        '''
        self.Name = Name
        self.neighbors = dict()
    
    def __repr__(self):
        '''Return the name attribute of the instance
        
        Arguments:
        -self:  The instance itself
        '''
        return self.Name
        
    def add_neighbor(self, neighbor, distance, interstate):
        '''Create key/value pairs with the neighbors attribute
        
        Arguments:
        -self: the instance itself
        -neighbor: The neighboring city, the city object that will be connected to this instance and vice versa
        -distance: The distance between two cities
        -interstate: The interstate number that connects the two cities
        '''
        
        self.neighbor = neighbor
        self.distance = distance
        self.interstate = interstate
        
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = distance, interstate
        elif self not in self.neighbors:
            self.neighbors[neighbor] = distance, interstate
        
        
        
        #For each neighbor that is passed in from the current city, if it is not present then a key/value pair will be created
    
    def get_dict(self):
        print(self.neighbors)
        return self.neighbors
        
class Map:
    '''This class stores that map data as a form of Graph
    
    Attributes:
    -cities: a list of all of the unique city objects that make up the Graph structure
    '''
    cities = list()
    new_relationship = dict()
    def __init__(self, relationships):
        '''init methods takes the cities attribute to an empty list and string together a list of connecting cities if possible
        
        Arguments:
        -self: The instance itself
        -relationships: A dictionary where the keys are individual cites and the values are a list of tuples
        '''
        
        self.relationships = relationships
        
        for city in self.relationships:
            if city not in self.cities:
                city_name = City(city)
                self.cities.append(city_name)
                
                
                
                    
                    
            
    
            
            
        

        
    def get_cities(self):
            print(self.cities)
        
        #Relationships is an empty dictionary containing all city relationships
        
       

graph = {
            "Baltimore": [("Washington", 45, "95"), ("Philadelphia", 106, "95")],
            "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")],
            "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
            "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
            "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
            "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
            "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
            "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
            "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
            "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
            "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
            "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")], 
            "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
            "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27")],
            "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
            "Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"),("Nashville", 180, "40"), ("Ashville", 116, "40")],
            "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingham", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
            "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
            "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
            "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
            "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
            "Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
            "Youngstown":[("Pittsburgh", 67, "76")],
            "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")],
            "Pittsburgh": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
            "Bedford": [("Pittsburgh", 107, "76")], #COMEBACK
            "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
            "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence", 95, "181"), ("Pittsburgh", 389, "76")],
            "Scranton": [("Syracuse", 130, "81")],
            "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 106, "95"), ("New York", 95, "95")]
}

mapA = Map(graph)

mapA.get_cities()