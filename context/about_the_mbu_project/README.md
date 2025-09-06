This file contains information about the context files related to the mbu project. Here we explain what is the status of the project, what is the goal of the project, who are the participants, what is the timeline, etc. 

- paper_context.txt: 
this file talks about the paper we are aiming to generate with this project. 

The overall idea is that we want to generate useful questions to convert each of the examples of any given dataset into mcvqa format. This will allow us to evaluate the performance of vision-language models on the datasets. 

So far we have performer the following tasks: 
1. We have scraped datasets from zenodo, huggingface, kaggle, paperswithcode and we used a smart classification and scoring system to gather relevant metadata and scores from each dataset.  
2. We have standarized the metadata of all the datasets to a unified schema. You can find these in the data/dataset_metadata directory. 
3. This repository (where we are now): The goal is to generate a pipeline and overall templates to convert datasets into mcvqa format.
