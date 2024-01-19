from file import SearchAndCreateData

DB = {}
keywords = [
    "flutter",
    "python",
    "kotlin",
]

for i in range(len(keywords)):
    data = SearchAndCreateData(keywords[i])
    DB[keywords[i]] = data.Search()
    data.CreateCSV(DB[keywords[i]])
