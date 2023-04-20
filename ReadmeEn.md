## Advisor Evaluation Tool

The application enables the performance of its consultants to be monitored by taking comments from users or by tagging the data it collects from csv files and extracting keywords.

### Basic Technologies of the Application

The application was developed with python 3.10.10 using bert classification, bert key extraction, flask, faker and matplotlib libraries.

### Features of the App

There is a web page in the application where the user can interact. Comments can be collected on this web page.

The application includes a training script to improve the classification performance of new upcoming comment data and a tagging script to use the trained models.

The application includes a training script to improve the classification performance of new upcoming comment data and a tagging script to use the trained models.

The application includes a script that performs key extraction to determine the areas that need to be focused by removing the keywords.

The application includes a matplotlib based script to visualize the collected data.

## Setup

The python version used is 3.10.10

```plaintext
pip install -r requirements.txt  
```

You should download the model from this link and put it in NlpPocess.

## Operating

#### To open the comment site

```plaintext
cd CommentsGather/Flask
python3 view.py
```

#### Consultant evaluation

```plaintext
python3 ConsultantEvaluation.py 
```

> Note: To get fast results, maxRow parameter is put in ConsultantEvaluation.py. You can edit or remove it if you wish.

> Note: Results are timestamp stamped under Outputs.

## Functions of Some Files and Folders

> The NlpProcess/Train.py file trains the tagging model.

> The NlpProcess/KeyExtractor.py file extracts keywords and converts them to percentiles.

> NlpProcess/SentimentLabeling.py file tags comments with pre-trained model.

> Files in the NlpProcess/Preprocces folder clean up comments and discard stopwords.

> The files in the NlpProcess/Preprocces folder hold some variables

> The files in the DataLoader folder read the data from the database and csv, clean the comments and bring them to the desired format.

> The file in the faker folder is fake mail, name, etc. provides testability.

> The file in the Graphic folder dumps the data into bar graphs.

## Features that can be improved

Here are a few topics that can be improved over time.

> While training, I trained using low batch\_size and epochs. A better model can be obtained by using more batch\_sizes and epochs.

> Text cleaning can be improved.

> Comments can be received with a better interface.

> Different evaluations can be made.

> Comments can be received with a better interface.

> A much better data visualization can be made.
