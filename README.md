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

## Testing
### Logic testing
I tested the logic by:
- Giving the program inputs and comparing the result to my own calculations.
- Giving the program an invalid input to make sure it reacts as expected. Did this on all inputs. 

### Linter
Due to the pep8 website being down I used the version you can download in gitpod. 

## Credits
I got some help from Robin Koelewijn (Data Scientist) in order to propperly understand things I found confusing. He also helped me to get on the right track when I got stuck. The API part is copied from the "Love sandwiches" project, and I got some help from Robin.

Erik Vodopivec Forsman, 2022
