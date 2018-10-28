from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.company
data =db.company_profiles.find({'financial_summary.market_cap' :{ '$gte' : "81,000,000,000"}})
for company in data:
	print(company)
