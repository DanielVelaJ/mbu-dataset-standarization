 Good, so far we are here:
 1. Scraped all of the dataset sources: zendo, papers with code, huggingface and kaggle. We also scraped links from the datasets description whenever possible.
 
 2. We used LLM that took descriptions and metadata as well as scraped links from each dataset and screened for exclusion flags: 
    - pmcoa derived
    - non-medical
    - synthetic 
    - low-quality
    - text-only
The pipeline also assessed downloads, annotations, external validation and some other factors to determine a quality score and classified the datasets according to their task type and domain.
After filtering , we got a list of 1360 datasets that survived the filters (may however still contain duplicates). The current plan is to go from highest to lowest quality score and avoid duplicates as we encounter them. 

3. We created a task taxonomy used to classify the datasets into task types and sub-task types (eg multiclass, multilabel, binary, instance segmentation, semantic segmentation, landmark detection, counting, etc.). This taxonomy is used to create templates that will be used to map dataset examples into questions in the mcvqa format.

3. We have created 43 templates that are compatible with the datasets that we have selected. Some of them are domain-agnostic and some are domain-specific. These follow the task taxonomy and were created having our 1360 datasets in mind (we asked an llm to do the domain specific templates considering the kind of datasets we have and the task taxonomy).

4. We fixed a schema for all the datasets to be represented in a standarized unified format that is compatible with our templates.

5. We are currently doing the first mvp with real datasets attempt. We want to run evaluation with 3 datasets per domain (15 total) and execute the full pipeline to catch potential improvements and blind spots in standardization before we delegate the conversion of the rest of the datasetst to other interns. 

