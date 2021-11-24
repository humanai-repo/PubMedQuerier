from pymed import PubMed
import csv

query = "Ott PA[Author]"

pubmed = PubMed(tool="MyTool", email="my@email.address")
results = pubmed.query(query, max_results=500)

article_fields = ["doi", "journal", "publication_date", "pubmed_id", "title"]
author_fields = ["affiliation", "firstname", "initials", "lastname"]
additional_fields = ["doc_rank", "rank"]

d = "data/"
article_writer = csv.writer(open(d + "article.tsv", 'w'), delimiter='\t')
author_writer = csv.writer(open(d + "author.tsv", 'w'), delimiter='\t')
keyword_writer = csv.writer(open(d + "keyword.tsv", 'w'), delimiter='\t')

article_writer.writerow(['rank'] + article_fields)
author_writer.writerow(additional_fields + author_fields)
keyword_writer.writerow(additional_fields + ["keyword"])

for rank, article in enumerate(results):
    article_values = [str(getattr(article, af)).replace("\n","|") for af in article_fields]
    article_writer.writerow([rank]+article_values)
    doi = article.doi
    for author_rank, author in enumerate(article.authors):
    	author_values = [author[af] for af in author_fields]
    	author_writer.writerow([rank, author_rank]+author_values)
    for kw_rank, kw in enumerate(article.keywords):
    	keyword_writer.writerow([rank, kw_rank, kw])
    print("{}: {} ({}, {})".format(rank, doi, len(article.authors), len(article.keywords)))