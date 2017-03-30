# FruitCRUD
Console-based CRUD in Python3, with PyMySQL database

<h2>Dependencies:</h2>
1. PyMySQL: https://github.com/PyMySQL/
2. Python 3.6.1: https://www.python.org/downloads/release/python-361/

<h2>Setup:</h2>
<p>Create a database named 'fruitseller'</p>
<p>Use the code in fruitsellerdb.sql to create the 'fruit' table</p>
<p>Any variation in database name or table structure should be dealt with in fruitcrud.py</p>

<h2>How to use:</h2>
<p>Clone or download this repo.</p>
<p>Open your mysql server by command-line, workbench or however else</p>
<p>Paste the fruitsellerdb.sql code into a query window.</p>
<blockquote>TADAAA! Database!</blockquote>
<p>Run fruitcrud.py by right-clicking and running in Python, or by command-line.</p>

<h2>How it works:</h2>
<p>A list of fruit is displayed (in alphabetical order) from the fruit table in the fruitseller database. If empty, the app says so.</p>
<p>Pick an option under the list. A=add, E=edit, D=delete, X=exit program.</p>
<p>The "edit" and "delete" options are unavailable if the fruit table is empty.</p>
<p>Options are converted to lowercase, so "A" and "a" are valid.</p>
<h3>Adding Fruit</h3>
<p>Pick "a" as an option.</p>
<p>Enter a new name for the fruit. If it already exists, you will be warned.</p>
<p>If successful, the new name is added to the database and the "default" screen is shown.</p>
<hr />
<h3>Editing Fruit</h3>
<p>Pick "e" as an option.</p>
<p>Pick an index based on the numbers in the menu. You will be prompted until you give a number that's within range.</p>
<p>The chosen entry is shown IN UPPERCASE LETTERS. Enter a new name. If it already exists, you will be warned.</p>
<p>If successful, the fruit table is updated and the "default" screen is shown.</p>
<hr />
<h3>Deleting Fruit</h3>
<p>Pick "d" as an option.</p>
<p>Pick an index based on the numbers in the menu. You will be prompted until you give a number that's within range.</p>
<p>The chosen entry is shown IN UPPERCASE LETTERS. Enter "y" to confirm deletion, or any other character to cancel.</p>
<p>If successful, the fruit is deleted and the "default" screen is shown.</p>

