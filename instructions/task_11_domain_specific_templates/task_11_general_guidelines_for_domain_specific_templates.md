Our question generation pipeline has both domain-agnostic and domain-specific templates. The domain-agnostic templates are organized in the templates/domain-agnostic directory.

# Task 11: General Guidelines for Domain-Specific Templates
So far we have a set of general domain templates, these are organized according to the docs/mbu_medical_vision_taxonomy_table.md file as well as the docs/task_taxonomy_template_repository_mapping.md file. 

Now we need to create templates that are specific to particular domains. These templates will follow the same taxonomy and be located in the templates/domain-specific/{domain} directory. Isnide each domain the directory must follow the same organization as the general domain-agnostic templates. 

To create the domain-specific templates we should first understand the datasets that are available for each domain. 
1. You can find the metadata for each of the datasets that we have selected in the data/dataset_metadata/dataset_metadata.csv file. Look at about_dataset_metadata folder and read all of its contents to learn how to read the metadata. 
2. One of the fields of the metadata is the medical domain. So you must filter the metadata to only include the datasets that are from the domain that you are interested in so that then you can read the description of each of the datasets and all the information there is about them. 
3. Once you have familiarized yourself with the datasets that are available in the domain you are working on, you can start to create the templates. Remember that the templates must follow the same structure as the general domain-agnostic templates but now we can include information that is more specific to the domain such as the terminology of the domain, the types of images that are used in the domain, the types of questions that are asked in the domain, etc. 

Remember that you can create scripts in the agent_scripts directory to help you with the task. (please name them according to the task and the domain they are for, also see the general_instructions.md file for naming conventions). 