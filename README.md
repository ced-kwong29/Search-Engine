# cs121-search-engine

## Contributors

Alexander Le - alexanvl - 22558269
Rayan Tighiouart - rtighiou - 88255446
William Mejia - wmejiahi - 18183195
Cedric Kwong - cwkwong - 11234388

## General specifications

You will develop two separate programs: an indexer and a search component.
Indexer

### Indexer

Create an inverted index for the corpus with data structures designed by you.

- Tokens: all alphanumeric sequences in the dataset.
- Stop words: do not use stopping while indexing, i.e. use all words, even
  the frequently occurring ones.
- Stemming: use stemming for better textual matches. Suggestion: Porter
  stemming, but it is up to you to choose.
  -Important text: text in bold (b, strong), in headings (h1, h2, h3), and
  in titles should be treated as more important than the in other places.
  Verify which are the relevant HTML tags to select the important words.

### Search

Your program should prompt the user for a query. This doesn’t need to be
a Web interface, it can be a console prompt. At the time of the query,
your program will stem the query terms, look up your index, perform some
calculations (see ranking below) and give out the ranked list of pages that are
relevant for the query, with the most relevant on top. Pages should be identified
at least by their URLs (but you can use more informative representations).

- Ranking: at the very least, your ranking formula should include tf-idf,
  and consider the important words, but you are free to add additional
  components to this formula if you think they improve the retrieval.

## Main challenges

Design efficient data structures, devise efficient file access, balance memory usage and response time.

## Operational constraints

Typically, the cloud servers/VMs/containers that run search engines don’t have
a lot of memory. As such, you must design and implement your programs as
if you are dealing with very large amounts of data, so large that you cannot
hold the inverted index all in memory. Your indexer must off load the inverted
index hash map from main memory to a partial index on disk at least 3 times
during index construction; those partial indexes should be merged in the end.
Optionally, after or during merging, they can also be split into separate index
files with term ranges. Similarly, your search component must not load the
entire inverted index in main memory. Instead, it must read the postings from
the index(es) files on disk

# Milestone 1

## Building the inverted index

Now that you have been provided the HTML files to index, you may build your
inverted index off of them. The inverted index is simply a map with the token
as a key and a list of its corresponding postings. A posting is the representation
of the token’s occurrence in a document. The posting typically (not limited to)
contains the following info (you are encouraged to think of other attributes that
you could add to the index):

- The document name/id the token was found in.
- Its tf-idf score for that document (for MS1, add only the term frequency).
  Some tips:
- When designing your inverted index, you will think about the structure
  of your posting first
- You would normally begin by implementing the code to calculate/fetch
  the elements which will constitute your posting.
- Modularize. Use scripts/classes that will perform a function or a set of
  closely related functions. This helps in keeping track of your progress,
  debugging, and also dividing work amongst teammates if you’re in a group.
- We recommend you use GitHub as a mechanism to work with your team
  members on this project, but you are not required to do so.

# Milestone 2

**Goal**: Develop a search and retrieval component
At least the following queries should be used to test your retrieval:

1. cristina lopes
2. machine learning
3. ACM
4. master of software engineering

### Developing the Search component

Once you have built the inverted index, you are ready to test document retrieval
with queries. At the very least, the search should be able to deal with boolean
queries: AND only.
If you wish, you can sort the retrieved documents based on tf-idf scoring
(you are not required to do so now, but doing it now may save you time in
the future). This can be done using the cosine similarity method. Feel free to
use a library to compute cosine similarity once you have the term frequencies
and inverse document frequencies (although it should be very easy for you to
write your own implementation). You may also add other weighting/scoring
mechanisms to help refine the search results.

## Milestone 3

**Goal**: Develop a complete search engine

During this last stretch, you will improve and finalize your search engine.
Come up with a set of at least 20 queries that guide you in evaluating
how well your search engine performs, both in terms of ranking performance
(effectiveness) and in terms of runtime performance (efficiency). At least half of
those queries should be chosen because they do poorly on one or both criteria;
the other half should do well. Then change your code to make it work better
for the queries that perform poorly, while preserving the good performance of
the other ones, and while being as general as possible
