from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
  
# Create an instance of Flask
marsflask = Flask(__name__)
# Use PyMongo to establish Mongo connection
marsgo = PyMongo(marsflask, uri="mongodb://localhost:27017/weather_app")

# Route to render index.html template using data from Mongo
@marsflask.route("/")
def home():

# Find one record of data from the mongo database
    render_mars = marsgo.db.collection.find_one()
    # urlcollections['news_title'] = titletext
    # urlcollections['news_p'] = news_p
    # urlcollections['featured_img'] = image
    # urlcollections['mars_weather']= weather
    # urlcollections['html_table']=html_table
    # urlcollections['hemisphere_image_url'] = hemisphere_image_urls

# Return template and data
    return render_template("index.html", marstabloid=render_mars)

# Route that will trigger the scrape function
@marsflask.route("/scrape")
def scrape():

# Run the scrape function
    render_mars = scrape_mars.scrape_info()
    print(render_mars)
# Update the Mongo database using update and upsert=True
    marsgo.db.collection.update({}, render_mars, upsert=True)

# Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    marsflask.run(debug=True)
