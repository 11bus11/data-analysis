# Data analysis
[Live site](https://data-analysis-ci.herokuapp.com/)

This is the third project for the Code Institute full stack software development course. The focus for this project is python. I chose to do some simple data analysis. The flow chart is shown below.
![Flow chart](docs/flowchart.png)

## UX - user experience
### User stories
I want the user to be able to:
- Import data from a google sheets document.
- Get the answer amount of each option in percent.
- Export the result to a google sheets document.

### Instructions and information
I have done my best to make sure all users understands what they should do. I have given clear instructions and explained what the problems are when endng the program due to input errors.

## Features
The program takes your numbers, and then it calculates how many prcent are positive, negative and avoided answers.  

### Google sheets
The program gets the data from a google sheets document. The layout of this document looks like this:
![gspread answers document](docs/sheet_answers.PNG)
![gspread output document](docs/sheet_output.PNG)

I could access the document from my program with the help of 2 API:s. Google Drive API and Google Sheets API. The instructions on how to use these were from the Code Institute "Love sandwiches" project, and the API:s can be found here: [Google API:s](https://console.cloud.google.com/apis/library). With these API:s I am able to, through the program, acces the content of a chosen google sheets document, and manipulate it.

### Error handling
It can also handle inputs that would cause a ValueError (if you give the program something that cant be converted to an intages). If there is a ValueError, the program will ask you to input a number instead. It will continue doing that until you comply. This is used when the user writes which question they want analysed.

If an input is not one of the three supported ones (yes, no, none), or if the number of answers are not the same as the supposed total answers (Extra validation due to it being very important that it is correct), the program will end. Before endig it the user will get be told that there is a problem, what the problem most likely is (based on which part of the input validation it was that failed) and to check the spreadsheet.

### Potential features
- Making it possible to analyse more than one question.
- Telling the user which option got the most percent.
- The user being able to name the different options.

## Testing
### User stories
The user is able to:
- Import data from a google sheets document.
  - The program imports the needed data from a google sheets document named "data_analysis".
- Get the answer amount of each option in percent.
  - The program calculated the percentages.
- Export the result to a google sheets document.
  - The results are exported to the google sheets document.

### Peer review
I asked a few people to try my program. They tried to break it by giving invalid inputs.

### Logic testing
I tested the logic by:
- Giving the program inputs and comparing the result to my own calculations.
- Giving the program an invalid input to make sure it reacts as expected. Did this on all inputs. 

### Linter
Due to the pep8 website being down I used the version you can download in gitpod. 

### Deployment
This project was deployed with Heroku. 
- Create an account at [Heroku](heroku.com), and do not forget you need to confirm your e-mail to do this.
- Create a list of dependencies in a text file named requirements (pip3 freeze > requirements.txt).
- Create an app by clicking the "create a new app" button found on the dashboard.
  - Choose a unique app-name.
  - Choose your region and click "create app"
- Click on settings (for the app).
  - Find the Config Vars section and add potential files that you cannot upload to github. For example API credentials. KEY is the title, and VALUE is the content.
  - Add buildpacks (below Config Vars). For this project I installed Python and Node.js. Make sure they are in the correct order.
- Go to the deploy section.
  - Choose to deploy from github.
  - Connect your account and choose a repository to deploy from.
  - Choose either Automatic or Manual deployment (recommended).
- Make sure the live site is working.

### Fixed bugs
- In the beginning of the project I created a function where I needed to return multiple values. Since I did not know how to do this in an effective way, I chose to ask a friend to explain it to me. 
- Most other buge was caused by me forgetting something small, and was fixed very easily then I finally realised what I had forgotten. One example of this is then I deployed the project to heroku, and the spreadsheet could not be reached by the program. I had forgotten to share the document...

## Credits
I got some help from Robin Koelewijn (Data Scientist) in order to propperly understand things I found confusing. He also helped me to get on the right track when I got stuck. The API part is copied from the "Love sandwiches" project, and I got some help from Robin. The instructions for how to deploy the project also came from "Love sandwiches".

Erik Vodopivec Forsman, 2022
