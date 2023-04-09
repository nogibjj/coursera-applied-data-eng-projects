[![CI](https://github.com/nogibjj/coursera-applied-data-eng-projects/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/coursera-applied-data-eng-projects/actions/workflows/cicd.yml)

## Projects for Specialization

### ETL (Extract, Transform, Load)
#### A. Keyword Extractor Tool to HashTag Tool (Lab 1)

Tasks:

1.  Look at the `text.txt` file and notice it is a video transcription.
2.  Run `main.py` by typing `python main.py --help`.  Notice there are two tools:  `extract` and `hashtags`
3.  Next convert the text into keywords using the `python main.py extract`.  What do you see?
4.  Now run `python main.py hashtags`.  What do you see?
5.  Next convert the command-line tool to have another flag that limits the keywords to a maximum of the top keywords (lowest score is better).
6.  Grab some text on the internet, say wikipedia or a blog post and create hashtags with it.

#### B. SQLite Origin B. Python C. SQLite Destination (Lab 2)

Tasks:

1. Run `python etl.py`, notice there are three commands that work for ETL:  `delete`, `etl` and `query`
2. The ETL command extracts the keywords from the file and puts them in a sqlite database.  Run it `python etl.py etl`.
3. Now that the database has been created and data loaded into it. Query the database for the top results with `python etl.py query`
4. Change the command-line flag to return only five results
5. Create your own version of this tool in GitHub and extend the database with different metadata using another NLP tool.
