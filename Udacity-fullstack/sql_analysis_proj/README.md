# Analysis of the news PostgreSQL database
This project gives a short analysis of the news database, answering three questions.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Using this project
1. This project was made to be run in a VM provided by Udacity and the instructions will cover that usage (alternatively it should be possible to run it if you have psql, Python, and the psycopg2 package intalled).
2. Create a file `analysis.py` inside the vagrant directory with the same content as the analysis.py file in this subdirectory (since you can't clone only a part of a repo and I didn't want to create a repo for this only)
3. [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and put the `newsdata.sql` file inside the vagrant directory
4. Log in to the VM with `vagrant ssh` and run `cd \vagrant` to navigate the files
5. Load the data by using the command `psql -d news -f newsdata.sql` inside the vagrant directory
6. Quit the psql by using `Ctrl + d`
7. Run `python analysis.py`

