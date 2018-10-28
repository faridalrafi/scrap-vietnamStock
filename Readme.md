Task1 -> python task1.py # Scrap listed companies
	 Python task1-2.py # Scrap company_profiles

Import to mongodb :  mongoimport --db company --collection company_profiles --file company_profiles.json --jsonArray

Task2 -> python app.py #start flask apps
Task 2 Endpoint :
Get ALL Companies: ROOT_URL/companies
Filter By Name : ROOT_URL/company/BEN%20TRE%20AQUAPRODUCT%20IMPORT%20AND%20EXPORT%20JSC
Filter By Industry: ROOT_URL/industry/%20Food%20processing
Filter By GTE_Revenue: ROOT_URL/revenue/10000


	
