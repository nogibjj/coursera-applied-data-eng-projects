#!/usr/bin/env python3

"""
Extract keywords from a text file and load them into a database.
"""
from main import extract_keywords, make_hashtags, read_file
import click
import sqlite3

DATABASE = "keywords.db"

# create a function that returns keywords, score and hashtags
# create a function that loads keywords and score into a database
def load_keywords(keywords, score, hashtags):
    """Load keywords, hashtags  and their scores into a database"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS keywords (keyword TEXT, score REAL, hashtags TEXT)"
    )
    for keyword, score, hashtags in zip(keywords, score, hashtags):
        c.execute("INSERT INTO keywords VALUES (?, ?, ?)", (keyword, score, hashtags))
    conn.commit()
    conn.close()


def collect_extract(filename):
    """Collect keywords from a file and extract them into a database"""
    keywords = []
    score = []
    text = read_file(filename)
    extracted_keyword_score = extract_keywords(text)
    for keyword_score in extracted_keyword_score:
        keywords.append(keyword_score[0])
        score.append(keyword_score[1])
    #feed keyword/score into make_hashtags to generate hashtags
    hashtags = make_hashtags(extracted_keyword_score)
    return keywords, score, hashtags


def extract_and_load(filename):
    """Extract keywords from a file and load them into a database"""
    keywords, score, hashtags = collect_extract(filename)
    load_keywords(keywords, score, hashtags)


# write a function the queries the database and returns the keywords, hashtags and scores
def query_database(order_by="score", limit=10):
    """Query the database and return keywords, hashtags and scores"""
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(f"SELECT * FROM keywords ORDER BY {order_by} DESC LIMIT {limit}")
    results = c.fetchall()
    conn.close()
    return results



@click.group
def cli():
    """An ETL cli"""


@cli.command("etl")
@click.argument("filename", default="text.txt")
def etl(filename):
    """Extract keywords from a file and load them into a database

    Example:
    python etl.py etl text.txt
    """
    extract_and_load(filename)


@cli.command("query")
@click.option("--order_by", default="score", help="Order by score or keyword")
@click.option("--limit", default=10, help="Limit the number of results")
def query(order_by, limit):
    """Query the database and return keywords, hashtags and scores

    Example:
    python etl.py query
    """
    results = query_database(order_by, limit)
    for result in results:
        print(
            click.style(result[0], fg="red"),
            click.style(str(result[1]), fg="green"),
            click.style(result[2], fg="blue"),
        )

@cli.command("delete")
def delete():
    """Delete the database

    Example:
    python etl.py delete
    """
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DROP TABLE keywords")
    conn.commit()
    conn.close()
    print("Database deleted")

if __name__ == "__main__":
    cli()
