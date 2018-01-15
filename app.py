from flask import Flask, render_template, request, url_for, redirect, Markup
from datetime import datetime
import csv
import os

app = Flask(__name__)
Pricing = {'1': 6,
'2': 10,
'3': 15}
Inventory = {
	'blue': "Blue - Tri-Spinner",
	'red': "Red - Tri-Spinner",
	'green': "Green - Tri-Spinner",
	'pink': "Pink - Tri-Spinner",
	'white': "White - Tri-Spinner",
	'black': "Black - Tri-Spinner",
	'greenblue': "Green/Blue - Tri-Spinner",
	'other': "Multi-Color - Tri-Spinner"
}

def WriteToDataBase(Information):
	database = "{}/static/Database.csv".format(os.getcwd())
	with open(database, "a") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		writer.writerow(Information)

def Sold(Transaction):
	Quantity = (Transaction['Quantity'])
	Price = Pricing[Quantity]
	Info = Inventory[str(Transaction["Item"])]
	TimeStamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	PricePerUnit = float(Price) / float(Quantity)
	Information = [TimeStamp, Quantity, Info, PricePerUnit, Price]
	print('{}x {} Sold at {} for ${} each - Total Transaction Cost: ${}'.format(Quantity, Info, TimeStamp, PricePerUnit, Price))
	WriteToDataBase(Information)

@app.route('/')
def form():
	return render_template('index.html')




@app.route('/', methods=['POST'])

def Add():
	Transaction = {}
	for key, quant in request.form.items():
		Transaction["Item"] = key
		Transaction["Quantity"] = quant
	Sold(Transaction)
	'''if request.form['blue'] != None:
		print(request.form['blue'])'''
	
	return redirect(url_for('form'))



if __name__ == '__main__':
	app.run(debug=True)

