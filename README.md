# ACME

## Problem Statement

Company ACME is particularly interested in improving the volume and quality of traffic to its
public facing web sites from search engines. Many of these search engines are quite
sophisticated, using advanced algorithms and parallel searching techniques to provide fast,
accurate responses.This problem is however, somewhat simpler.
A group of web pages has been classified by associating a list of keywords, given in decreasing
order of relevance, with each page (i.e., the order of keywords is from the most specific keyword
to the least specific). For example, on the TopGear website a page on reviews of Ford cars may
have the keywords: Ford, Car, Review in that order; the most relevant keyword is Ford.
Queries also include a list of keywords, again from most to least relevant. For example, in a
query consisting of the keyword Ford followed by the keyword Car, Ford is more important than
Car.
In this problem you are to determine the top five (or fewer) pages that match each of an
arbitrary number of queries.

To determine the strength of the relationship between a query and a web page, assume the
keywords for each page and each query are assigned integer weights, in descending
order, starting with N, where N is the maximum number of keywords allowed for a web page and
query.
The strength of the relationship is the sum of the products of the weights associated with
each keyword that appears both in the webpage list and the query list.

## Running the CLI (Tested on Python 3.5.2)

```
python3 main.py

```


