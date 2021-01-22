# Jordan Machita
# jm8ux
# Homework 3: Python and Web Scraper 

# import the required modules for the program
import requests
import bs4
import csv

# store the url and use th requests module to get the content
url = 'https://eclipse.gsfc.nasa.gov/SEdecade/SEdecade2021.html' 
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) 
html = response.content
# print(html)

# use BeautifulSoup to help clean up the content
soup = bs4.BeautifulSoup(html, features="lxml")
# print(soup.prettify())

# extract just the table in question after inspecting the html code to figure out how
table = soup.find('table', attrs={'class': 'datatab'})
# print(table.prettify())


list_of_rows = [] # initialize an empty list where we will store the rows
for row in table.findAll('tr'): # iterate through all rows of our table
    list_of_cells = [] # initialize an empty list where we store the cells for the row
    # print(row.prettify()) 
    for cell in row.findAll('td'): # iterate through each cell
        text = cell.text.replace('&nbsp;', '') # extract the text of the cell
        list_of_cells.append(text) # append the text to our list of cells for the row
        # print(cell.prettify())
    list_of_rows.append(list_of_cells) # append the list of cells to the list of rows as a row

print(list_of_rows) # we use print statements throughout to check our progress

outfile = open('./eclipse.csv', 'w') # open/create a csv file to store the data
writer = csv.writer(outfile) # initialize a csv writer
writer.writerows(list_of_rows) # store the list of rows as the rows in the csv

# we now have a csv file 'eclipse.csv' with the data from the table on the NASA website!


# Sources: 
# I used the following source (provided by the professor in Module 4) to help me build the web scraper
# https://first-web-scraper.readthedocs.io/en/latest/#