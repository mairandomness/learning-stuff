# Code that runs an analysis of the news database
# and returns the answer to the following questions:
# 1. What are the 3 most popular articles of all time?
# 2. Who are the most popular article authors of all time?
# 3. On which days did more than 1% of requests lead to errors?

import psycopg2

DBNAME = "news"


def run_query(query):
    """Takes query and gets the resulting table from the database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def pretty_print(table, descrip):
    """Takes table and a description and prints it nicely"""
    for line in table:
        print("%s - %s%s" % (line[0], line[1], descrip))


def main():
    """calls run_query and prints the analysis"""

    three_most_popular = """\
    SELECT articles.title, count(*) AS num
    FROM articles, log
    WHERE '/article/' || articles.slug = log.path
    AND log.status = '200 OK'
    GROUP BY articles.title
    ORDER BY num DESC
    LIMIT 3;"""

    authors_most_popular = """\
    SELECT authors.name, count(*) AS num
    FROM articles, log, authors
    WHERE '/article/' || articles.slug = log.path
    AND log.status = '200 OK'
    AND authors.id = articles.author
    GROUP BY authors.name
    ORDER BY num DESC;"""

    error_percentage = """\
    SELECT * from
    (SELECT log.time::date as date,
    ROUND((100.0 * SUM(CASE WHEN status = '404 NOT FOUND' THEN 1 ELSE 0 END)
    / count(*)), 2) AS percent
    FROM log
    GROUP by date) t
    WHERE percent > 1;"""

    print("The three most popular articles of all time are:")
    pretty_print(run_query(three_most_popular), " views")
    print("")

    print("The most popular authors of all time are:")
    pretty_print(run_query(authors_most_popular), " views")
    print("")

    print("The days in which the error percentage\
 in requests was bigger than 1% were:")
    pretty_print(run_query(error_percentage), "% of errors")


if __name__ == "__main__":
    main()
