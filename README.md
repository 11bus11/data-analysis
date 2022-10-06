![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

# Data analysis
This is the third project for the Code Institute full stack software development course. The focur for this project is python. I chose to do some simple data analysis.

## User stories
I want the user to be able to:
- Import data from a google sheets document.
- Get the answer amount of each option in percent.
- Export the result to a google sheets document.

## Features
The program takes your numbers, and then it calculates how many prcent are positive, negative and avoided answers.  

### Error handling
It can also handle inputs that would cause a ValueError (if you give the program something that cant be converted to an intages). If there is a ValueError, the program will ask you to input a number instead. It will continue doing that until you comply.

If the number of answers are not the same as the supposed total answers (user input), the program will end. Before endig it the user will get be told that the nomber of answers are not the same as the inputed total answers. 

### Potential features
- Telling the user which option got the most percent.
- The user being able to name the different options.
