We are currently working on  a project called mbu project, please read about it in the context directory. We are currently working on the pipeline to convert datasets into mcvqa format. The general plan goes as follows: 

# Gemeral plan/
1. Define base templates to convert datasets into mcvqa format, we will be working one particular template at a time so that we can understand the approach better starting by binary classification datasets, followed by multi-class classification then multi-label classification. 

2. For each template we will generate a .md file that will explain how the template works and how it is used to generate a question in the mcvqa format. Templates are organized by **domain first**, then by task type and difficulty:

**Domain-Agnostic Templates** (work across all medical domains):
agnostic_classification_binary_1.md, agnostic_classification_binary_2.md, agnostic_classification_binary_3.md
agnostic_classification_multiclass_1.md, agnostic_classification_multiclass_2.md, agnostic_classification_multiclass_3.md
agnostic_classification_multilabel_1.md, agnostic_classification_multilabel_2.md, agnostic_classification_multilabel_3.md

**Domain-Specific Templates** (require medical domain expertise):
radiology_classification_binary_1.md, radiology_classification_binary_2.md, radiology_classification_binary_3.md
dermatology_classification_binary_1.md, dermatology_classification_binary_2.md, dermatology_classification_binary_3.md
pathology_classification_binary_1.md, ophthalmology_classification_binary_1.md, surgery_classification_binary_1.md

**Template Organization Structure**:
templates/
├── domain-agnostic/classification/binary/
├── domain-agnostic/classification/multiclass/
├── domain-agnostic/classification/multilabel/
├── domain-agnostic/classification/ordinal/
├── domain-agnostic/object-and-lesion-detection/lesion/
├── domain-agnostic/object-and-lesion-detection/anatomy/
├── domain-agnostic/object-and-lesion-detection/device/
├── domain-agnostic/segmentation/semantic/
├── domain-agnostic/segmentation/instance/
├── domain-agnostic/anatomical-landmarks-keypoints/single/
├── domain-agnostic/anatomical-landmarks-keypoints/multiple/
├── domain-agnostic/counting/direct/
├── domain-agnostic/counting/density/
├── domain-agnostic/vision-language/describe/short/
├── domain-agnostic/vision-language/describe/long/
├── domain-agnostic/vision-language/ask-and-answer/open-ended/
├── domain-agnostic/vision-language/ask-and-answer/multiple-choice/
├── domain-agnostic/vision-language/ask-and-answer/visual-reasoning/
├── domain-agnostic/vision-language/ground-and-locate/bbox/
├── domain-agnostic/vision-language/ground-and-locate/mask/
├── domain-agnostic/vision-language/ground-and-locate/multi-phrase/
├── domain-agnostic/vision-language/align-and-retrieve/image-to-text/
├── domain-agnostic/vision-language/align-and-retrieve/text-to-image/
├── domain-agnostic/vision-language/align-and-retrieve/pair-matching/
└── domain-specific/radiology/classification/binary/
└── domain-specific/dermatology/classification/binary/
└── domain-specific/pathology/classification/binary/

**Naming Convention**: `{domain}_{task}_{subtype}_{difficulty}.md`
Templates can be either easy (1), medium (2), or hard (3) difficulty levels.
Example: 
- `domain-agnostic_classification_binary_hard_1.md`
- `domain-agnostic_classification_multiclass_easy_1.md`
- `domain-agnostic_classification_multilabel_medium_1.md`
- `domain-specific_radiology_classification_binary_hard_1.md`
- `domain-specific_dermatology_classification_binary_easy_1.md`
- `domain-specific_pathology_classification_binary_medium_1.md`

3. For each template we will experiment with three different datasets of that task type and generate examples of questions made with the template. The goal for this step is to identify ways in which the template may not fit the dataset and how we can improve it further. We will be also at the same time be testing our datum schema to see if it is good enough to store all of the information needed per example. You can find our datum schema in the instructions directory.

4. When we have a good template and a good datum schema, we will generate a script to convert the datasets into the mcvqa format. 


# Workflow
You will be given specific tasks to perform usually on a .md file in the instructions directory. You will be given specific instructions on what to do. If the task is not clear you should ask for clarification until the details are clear and you have a good understanding of the task at hand. Do not continue with the task if you have questions or the task is unclear. Whenever you find a better way to do something, you should propose it and we will discuss it together but do not start implementing it until we have discussed it and agreed on the best approach. We should always aim for simplicity in our solutions and readability of the code.

Before starting any task please read all of the context files in the context directory and all of the .md files in the instructions directory to have a good understanding of the project at hand and where we are in the process.

Please update your progress on the tasks in the same .md file that describes the task and also document there the questions you had and the answers I gave you. However remember to always ask the questions in the chat to the user as well.  Also document here any other requests I may have made that are not related to the task at hand so that the task file keeps track of all the progress and decisions made.

# Coding guidelines
- We will use poetry for dependency management. 
- Allways add docstrings and comments that are clear and informative to help the reader understand the code. Follow best practices for docstrings and comments.
- Use clear and descriptive variable names.
- Use type hints and type annotations.
- Use absolute imports instead of relative imports.
- Whenever possible please avoid boilerplate code and instead use simple solutions that are easy to understand and maintain.

# About scripts
If you need to code a script to solve a task please add it in the agent_scripts directory and name it like this: task_<task_number>_<task_name>.py. This way it is easy to find and track. 