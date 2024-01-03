from flask import Flask, render_template ,request
import mysql.connector

app = Flask(__name__)
##   name 	is the application name

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
	if request.method == 'POST':
		start_year  = request.form['start_year']
		end_year    = request.form['end_year']
		select_city = request.form['select_city']
	else:
		start_year  = request.args.get('start_year', '')
		end_year    = request.args.get('end_year', '')
		select_city = request.args.get('select_city', '')
	artworks= select_artworks_db(start_year, end_year,select_city )
	return render_template('process.html', start_year=start_year, end_year=end_year, 
		select_city=select_city, artworks=artworks)


def select_artworks_db(start_year, end_year,select_city ):
	URL = "ec2-18-221-156-42.us-east-2.compute.amazonaws.com"; 
	conn = mysql.connector.connect(host= URL, user='root', 
		 password='ceit2018', database='Artwork_db')
	cursor =  conn.cursor()

	sql = """SELECT author.surname AS author, 
					artwork.name AS artwork,
					category FROM Author as author, Artwork  as artwork
					WHERE 
					  author.authorCode = artwork.author 
					 AND birthYear >= %s 
					 AND birthYear <= %s
					 AND artwork.city = %s
					 ORDER BY surname, artwork"""

	
	data =(start_year, end_year,select_city)
	# Insert new 
	cursor.execute(sql , data)
	artworks = cursor.fetchall()
	for artwork in artworks:
		print (artwork)
	cursor.close()
	conn.close()

	return artworks


if __name__ == '__main__':
	app.run()
