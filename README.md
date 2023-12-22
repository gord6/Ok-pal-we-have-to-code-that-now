# Supplementary Material
## "Ok Pal, we have to code that now": Interaction Patterns of Programming Beginners with a Conversational Chatbot

In this repository we provide supplementary material (data and application) to our paper *"Ok Pal, we have to code that now": Interaction Patterns of Programming Beginners with a Conversational Chatbot.*

The repository is structured into the following subdirectories:  
* `app/` containing the application for data collection, including its own README file with instructions for development and production setup

* `data/` containing data files on which we base our analysis, see below for a detailed documentation of different variables

* `notebooks/` containing notebooks for plotting and analysis, which we briefly describe below

* `tasks/` containing the tasks that were used for our study

## Data

### data/prompts.csv
Contains all prompts we collected from the participants with respective feedback and metadata.

| Column  | Description |
| ------------- | ------------- |
| prompt | Participant prompt |
| answer  | Chatbot answer  |
| feedback  | participant feedback to prompt   (bug: *The answer of the chatbot is wrong*, not-understand: *I don't understand the answer*, missing: *The answer is incomplete*, unclear: *The answer is imprecise*, technical: *There was a technical issue*) |
| user_id  | participant identifier |
| task  | Corresponds to the task (1-7) that participants were working on when this prompt appeared |
| time  | Unix timestamp |
| prompt_position  | Prompt position within the conversation related to this specific task, where 1 = first prompt, 2 = second, etc |
| conversation_length  | total number of prompts the participant used for this task |
| prompt_tokens  | Number of tokens in prompt (tokenized with clk100_base) |
| answer_tokens  | Number of tokens in answer (tokenized with clk100_base) |
| prompt_words  | Number of words in prompt (split at space char) |
| answer_words  | Number of words in answer (split at space char) |
| language  | Language of the tutorial group |





### data/experience_questionnaire.csv
Contains participants answers to our experience questionnaire.


| Column  | Description |
| ------------- | ------------- |
| user_id  | participant identifier |
| degree  | Master/Bachelor |
| exp_logic | experience in logic programming on a Likert scale form *very experienced* to *very unexperienced* |
| exp_compared_peers  | experience compared to classmates on a Likert scale from *much worse* to *much better*|


### data/prompt_purpose_labels.csv

| Column  | Description |
| ------------- | ------------- |
| conversation_id  | conversation identifier |
| prompt_id  | prompt identifier |
| label  | prompt purpose identified in our qualitative analysis|


### data/conversational_structures.csv


| Column  | Description |
| ------------- | ------------- |
| conversation_id  | conversation identifier |
| purpose_blocks  | sequence of purpose blocks |
| structure | structure identifier|
| intention  | intention identifier|



### data/experiment_submission/control_submissions.csv

Points students achieved with their submissions either belonging to the experiment or control group. 


purpose_blocks,Code generation,Code refinement,Concept comprehension,Code comprehension,Docs querying,Bug identification,Testing


| Column  | Description |
| ------------- | ------------- |
| task | task number |  
| user_id | user identifier |  
| max_points  | absolute maximum points achievable in this task |  
| percentage_correct  | percentage of points student achieved in this task | 
| conversation_id  | identifier of conversation that belongs to this submission |  
| purpose_blocks | Sequence of purpose blocks in this conversation |  
| Code generation | Whether Code generation was part of the conversation |  
| Code refinement | Whether Code refinement was part of the conversation |  
| Concept comprehension | Whether Concept comprehension was part of the conversation |  
| Code comprehension | Whether Code comprehension was part of the conversation |  
| Docs querying | Whether Basic Programming Knowledge was part of the conversation |  
| Bug identification | Whether Bug Identidfication was part of the conversation |  
| Testing  | Whether Testing was part of the conversation |  
