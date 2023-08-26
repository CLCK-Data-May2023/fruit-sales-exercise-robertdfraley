# In this exercise we will create a Pandas Dataframe with fruit sales information and write the data to a CSV file. This exercise is based on the Lesson 1 exercise in the Kaggle Learn Pandas course.




#Instructions
#Accept the exercise from GitHub. GitHub will automatically create a new repo for you with an open Pull Request for your changes.
#Clone the new repo to your machine.
#Create a virtual environment, activate it, and install the required packages. (see instructions below)
#Add your code to the specified file.
#Add/Commit/Push your code back to GitHub.GitHub will run the automated tests when you push.
#Review the Pull Request on your repo to see the status of the tests.
#“Turn in” the assignment in Google Classroom.

#Write a Python program that creates a Pandas Dataframe that matches the table below:
#
#Apples	Bananas
#2017 Sales	35	21
#2018 Sales	41	34
import pandas as pd
fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])
#print(fruit_sales)

#Write the data to a file called fruit.csv in the project directory.
#Make sure to add the fruit.csv file to the repo before committing and pushing back to GitHub.
pd.DataFrame.to_csv(fruit_sales, path_or_buf='fruit.csv')
