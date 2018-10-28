
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'company'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/company'

mongo = PyMongo(app)

@app.route('/companies', methods=['GET'])
def index_all():
  companies = mongo.db.company_profiles
  output = []
  for company in companies.find():
    output.append({"company_url": company["uid"],"company_name":company["company_name"], "company_email":company["company_email"], "company_website": company["company_website"], "company_street_address": company["company_set_address"], "country": "vietnam", "company_description": company["company_description"], "company_phone_number": company["company_phone_number"], "industry": company["business"]})
  return jsonify({"status_code": 200,"message": "successful",'data' : output})

@app.route('/company/<name>', methods=['GET'])
def get_one(name):
  companies = mongo.db.company_profiles
  company = companies.find_one({'company_name' : name})
  if company:
    output = {"company_url": company["uid"],"company_name":company["company_name"], "company_email":company["company_email"], "company_website": company["company_website"], "company_street_address": company["company_set_address"], "country": "vietnam", "company_description": company["company_description"], "company_phone_number": company["company_phone_number"], "industry": company["business"]}
  else:
    output = "Not found"
  return jsonify({"status_code": 200,"message": "successful",'data' : output})

@app.route('/industry/<industry>', methods=['GET'])
def get_industry(industry):
  companies = mongo.db.company_profiles

  output= []
  for company in companies.find({'business' : industry}):
    	output.append({"company_url": company["uid"],"company_name":company["company_name"], "company_email":company["company_email"], "company_website": company["company_website"], "company_street_address": company["company_set_address"], "country": "vietnam", "company_description": company["company_description"], "company_phone_number": company["company_phone_number"], "industry": company["business"]})
  
  return jsonify({"status_code": 200,"message": "successful",'data' : output})

@app.route('/revenue/<revenue>', methods=['GET'])
def get_revenue(revenue):
  companies = mongo.db.company_profiles
  
  output= []
  for company in companies.find({'financial_summary.market_cap' :{ '$gte' : revenue}}):
    	output.append({"company_url": company["uid"],"company_name":company["company_name"], "company_email":company["company_email"], "company_website": company["company_website"], "company_street_address": company["company_set_address"], "country": "vietnam", "company_description": company["company_description"], "company_phone_number": company["company_phone_number"], "industry": company["business"]})
  
  return jsonify({"status_code": 200,"message": "successful",'data' : output})

if __name__ == '__main__':
    app.run(debug=True)
