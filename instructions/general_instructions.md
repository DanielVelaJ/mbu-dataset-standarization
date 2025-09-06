We are currently working on  a project called mbu project, please read about it in the context directory. We are currently working on the pipeline to convert datasets into mcvqa format. The general plan goes as follows: 

# Gemeral plan/
1. Define base templates to convert datasets into mcvqa format, we will be working one particular template at a time so that we can understand the approach better starting by binary classification datasets, followed by multi-class classification then multi-label classification. 

2. For each template we will generate a .md file that will explain how the template works and how it is used to generate a question in the mcvqa format, the templates will be named like this: 
classification_binary_1.md, classification_binary_2.md, classification_binary_3.md for the binary classification template. 
classification_multi_class_1.md, classification_multi_class_2.md, classification_multi_class_3.md for the multi-class classification template. 
classification_multi_label_1.md, classification_multi_label_2.md, classification_multi_label_3.md for the multi-label classification template. 
these templates will be saved in the templates directory. Templates can be either easy, medium or hard (for the difficulty of the generated question)

3. For each template we will experiment with three different datasets of that task type and generate examples of questions made with the template. The goal for this step is to identify ways in which the template may not fit the dataset and how we can improve it further. We will be also at the same time be testing our datum schema to see if it is good enough to store all of the information needed per example. You can find our datum schema in the instructions directory.

4. When we have a good template and a good datum schema, we will generate a script to convert the datasets into the mcvqa format. 


# Workflow
You will be given specific tasks to perform usually on a .md file in the instructions directory. You will be given specific instructions on what to do. If the task is not clear you should ask for clarification until the details are clear and you have a good understanding of the task at hand. Whenever you find a better way to do something, you should propose it and we will discuss it together but do not start implementing it until we have discussed it and agreed on the best approach. We should always aim for simplicity in our solutions and readability of the code.

Before starting any task please read all of the context files in the context directory and all of the .md files in the instructions directory to have a good understanding of the project at hand and where we are in the process.

Please update your progress on the tasks in the same .md file that describes the task and also document there the questions you had and the answers I gave you. Also document here any other requests I may have made that are not related to the task at hand so that the task file keeps track of all the progress and decisions made.

# Coding guidelines
- We will use poetry for dependency management. 
- Allways add docstrings and comments that are clear and informative to help the reader understand the code. Follow best practices for docstrings and comments.
- Use clear and descriptive variable names.
- Use type hints and type annotations.
- Use absolute imports instead of relative imports.
- Whenever possible please avoid boilerplate code and instead use simple solutions that are easy to understand and maintain.

# About scripts
If you need to code a script to solve a task please add it in the agent_scripts directory and name it like this: task_<task_number>_<task_name>.py. This way it is easy to find and track. 