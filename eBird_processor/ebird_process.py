'''
Get to final version
- make command line flags; formalize
- good documentation (after above)
- test on bad/naive computer
- investigate pulling observer from HTML/ASK ERIC
- output # counties in summary
- update county arrays


'''



# main method, drives all the other methods  
def main():
    # processes data to get latest 10, first 10, and high 10 for all species.
    '''
    N_counties = ["Jo Daviess", "Stephenson", "Winnebago", "Boone", "McHenry", "Lake", "Carroll", "Ogle", "DeKalb", "Kane", "DuPage", "Cook", "Whiteside", "Lee", "Kendall", "Will", "Grundy", "La Salle", "Bureau", "Putnam", "Marshall", "Stark", "Henry", "Rock Island"]
    C_counties = ["Mercer", "Warren", "Henderson", "Know", "Peoria", "Woodford", "Livingston", "Kankakee", "Iroquois", "Ford", "McLean", "Tazewell", "Fulton", "McDonough", "Hancock", "Mason", "Schuyler", "Logan", "De Witt", "Piatt", "Champaign", "Vermilion", "Menard", "Macon", "Cass", "Brown", "Adams", "Pike", "Scott", "Morgan", "Sangamon", "Christian", "Shelby", "Moultrie", "Douglas", "Edgar", "Coles", "Montgomery", "Macoupin", "Greene"]
    S_counties = ["Calhoun", "Jersey", "Madison", "Bond", "Fayette", "Effingham", "Cumberland", "Clark", "Crawford", "Jasper", "Clay", "Marion", "Clinton", "St. Clair", "Washington", "Jefferson", "Richland", "Lawrence", "Wabash", "Edwards", "Wayne", "Monroe", "Randolph", "Perry", "Franklin", "Hamilton", "White", "Gallatin", "Saline", "Williamson", "Jackson", "Union", "Johnson", "Pope", "Hardin", "Massac", "Pulaski", "Alexander"]
    '''
    obsList = processData('test_data.txt')
    # writes a full description of the observations, including all 10 of each category
    # the categories are sorted such that the first entry is the "best"
    writeFull(obsList, "output.txt")
    # writes a summary of the data (high, first, last, and county list for all species)
    writeSumm(obsList, "summary.txt")
    
    #now for tiers
    '''
    Nobs = processSelect('IL_data.txt', N_counties)
    writeFull(Nobs, "N_full.txt")
    writeSumm(Nobs, "N_summ.txt")
    
    Cobs = processSelect('IL_data.txt', C_counties)
    writeFull(Cobs, "C_full.txt")
    writeSumm(Cobs, "C_summ.txt")
    
    Sobs = processSelect('IL_data.txt', S_counties)
    writeFull(Sobs, "S_full.txt")
    writeSumm(Sobs, "S_summ.txt")
    '''
    
        
# obs class to store data of individual observations
# stores name, count, county, date, location, and observation ID (all pulled from ebird)
class obs:
    def __init__(self, name, count, county, date, loc, obsID, breed, bba, comments, userID):
        self.name = name
        self.count = count
        self.county = county
        self.date = date
        self.loc = loc
        self.obsID = obsID
        self.breed = breed
        self.bba = bba
        self.comments = comments
        self.userID = userID
        
# species class to store the top 10s for a given species, plus a list of all counties
class species:
    def __init__(self, name):
        self.name = name
        self.counties = []
        self.bbaCodes = []
        self.bbaCats = []
        self.high = []
        self.first = []
        self.last = []
        self.num = 0
    # method to add a sighting to the list
    # this is where the sighting is checked to see if it should be added to a top 10
    # all top 10s are also sorted here, too
    def addSighting(self, obs):
        if obs.breed not in self.bbaCodes and obs.breed != "":
            self.bbaCodes.append(obs.breed)
        if obs.bba not in self.bbaCats and obs.bba !="":
            self.bbaCats.append(obs.bba)
        if self.num < 10:
            self.num+=1
            self.high.append(obs)
            self.high.sort(key = lambda x: x.count, reverse=True)
            self.first.append(obs)
            self.first.sort(key = lambda y: y.date)
            self.last.append(obs)
            self.last.sort(key = lambda z: z.date, reverse=True)
        else:
            self.num +=1
            if(obs.count > self.high[9].count):
                del self.high[9]
                self.high.append(obs)
                self.high.sort(key = lambda x: x.count, reverse=True)
            if(obs.date < self.first[9].date):
                del self.first[9]
                self.first.append(obs)
                self.first.sort(key = lambda y: y.date)
            if(obs.date > self.last[9].date):
                del self.last[9]
                self.last.append(obs)
                self.last.sort(key = lambda z: z.date, reverse=True)

    # method for updating county list
    def addCounty(self, county):
        if county not in self.counties:
            self.counties.append(county)
    
    # placeholder method
    def read_brCodes(self):
        pass
        

def processSelect(name, counties):
    from datetime import datetime
    import csv
    selectObs = []
    # species list is a quick workaround here, but could be output if needed
    speciesList = []
    with open(name, encoding="utf8") as text:
        data = csv.reader(text, delimiter='\t')
        next(data, None)
        for i in data:
            if i[16] in counties:
                try:
                    o = obs(i[4], int(i[8]), i[16], datetime.strptime(i[27], "%Y-%m-%d"), i[22], i[30], i[9], i[10], i[45], i[29])
                except:
                    o = obs(i[4], 0, i[16], datetime.strptime(i[27], "%Y-%m-%d"), i[22], i[30], i[9], i[45], i[10], i[29])
                if o.name not in speciesList:
                    speciesList.append(o.name)
                    selectObs.append(species(o.name))
                for j in selectObs:
                    if j.name == o.name:
                        j.addCounty(o.county)
                        j.addSighting(o)
    return selectObs

            
# processed input and forms observation list
def processData(name):
    from datetime import datetime
    import csv
    fullObs = []
    # species list is a quick workaround here, but could be output if needed
    speciesList = []
    with open(name, encoding="utf8") as text:
        data = csv.reader(text, delimiter='\t')
        next(data, None)
        for i in data:
            try:
                o = obs(i[4], int(i[8]), i[16], datetime.strptime(i[27], "%Y-%m-%d"), i[22], i[30], i[9], i[10], i[45], i[29])
            except:
                o = obs(i[4], 0, i[16], datetime.strptime(i[27], "%Y-%m-%d"), i[22], i[30], i[9], i[10], i[45], i[29])
            if o.name not in speciesList:
                speciesList.append(o.name)
                fullObs.append(species(o.name))
            for j in fullObs:
                if j.name == o.name:
                    j.addCounty(o.county)
                    j.addSighting(o)
    return fullObs

# method to write out full data, including all top 10s (labeled in last column)
# each observation has all of its associated info output, too
def writeFull(input, fname):
    import csv
    with open(fname, 'w', newline='', encoding="utf8") as csvfile:
        output = csv.writer(csvfile, delimiter = '\t')
        output.writerow(["Species", "Count", "County","Date","Location","Observation ID", "BBA Code", "BBA Cat", "Comments", "Obs ID", "Obs Type"])
        for entry in input:
            for a in entry.high:
                output.writerow([a.name,a.count,a.county,a.date.strftime('%m/%d/%Y'),a.loc,a.obsID,a.breed,a.bba,a.comments,a.userID,"High Count"])
            for b in entry.first:
                output.writerow([b.name,b.count,b.county,b.date.strftime('%m/%d/%Y'),b.loc,b.obsID,b.breed,a.bba,b.comments,b.userID, "First"])
            for c in entry.last:
                output.writerow([c.name,c.count,c.county,c.date.strftime('%m/%d/%Y'),c.loc,c.obsID,c.breed,a.bba,c.comments,c.userID, "Last"])

# method to write a quick summary of each species (high, first, last, and counties)
def writeSumm(input, fname):
    import csv
    with open(fname, 'w', newline='', encoding="utf8") as csvfile:
        output = csv.writer(csvfile, delimiter = '\t')
        output.writerow(["Species", "High Count", "First Date", "Last Date", "Number of Counties", "Counties", "Breeding Codes", "BBA Category"])
        for entry in input:
            output.writerow([entry.name,entry.high[0].count,entry.first[0].date.strftime('%m/%d/%Y'),entry.last[0].date.strftime('%m/%d/%Y'), len(entry.counties),', '.join([str(x) for x in entry.counties]), ', '.join([str(x) for x in entry.bbaCodes]), ', '.join([str(x) for x in entry.bbaCats])])
    
if __name__ == '__main__':
    main()