"""
Test goes here

"""
from main import read_file, extract_keywords, make_hashtags
from click.testing import CliRunner
from main import cli
from etl import collect_extract, query_database


def test_collect_extract():
    keywords, score, hashtags = collect_extract("text.txt")
    assert len(keywords) > 0
    assert len(score) > 0
    assert len(hashtags) > 0
    assert "#" in hashtags[0]
    kw = keywords[0].replace(" ", "")
    assert f"#{kw}" in hashtags[0]  #verify that the hashtags are in the output w/o space


def test_read_file():
    text = read_file("text.txt")
    assert "hugging" in text


def test_extract_keywords():
    text = read_file("text.txt")
    keywords = extract_keywords(text)
    assert len(keywords) > 0


def test_make_hashtags():
    text = read_file("text.txt")
    keywords = extract_keywords(text)
    hashtags = make_hashtags(keywords)
    assert len(hashtags) > 0
    assert "#" in hashtags[0]


def test_cli_extract():
    runner = CliRunner()
    result = runner.invoke(cli, ["extract", "text.txt"])
    assert result.exit_code == 0
    assert "hugging" in result.output
