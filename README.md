# Order Food Project
This readme is created for "Order_Food" Project. The objective of the project is to create a function which helps the owner of a dog shelter to calculate the total food quantity which needs to be ordered for next month. The project also contains pytests to validate edge, error, boundary and happypath test cases

## Environment
To run the python function and the pytests associated with it, make sure python and pytests are installed on your laptop
For example: This project is created using **Spyder**(Python 3.8)

## Sample Installation Instructions
Anaconda distribution comes with over 250 packages automatically installed, and over 7,500 additional open-source packages can be installed from PyPI as well as the conda package and virtual environment manager
- Go to https://www.anaconda.com/products/individual
- Install Anaconda ( This project is executed on Anaconda3) for windows or linux or Mac
- After the successful installation go to Start --> Folder Anaconda3--> Launch Spyder

## Features
This project contains the following folder structure:

![image](https://user-images.githubusercontent.com/51870349/129499345-f3262889-725b-419c-a81e-57d6cec67d29.png)

- **orderqty.py**: This is a Python runnable function. It has four input parameters: each size of dog i.e s_dog(small), m_dog(medium), l_dog(large) currently in your shelter and the remaining food from last month (r_food). The functions returns the total order quantity to be ordered for next month

- **Pytest**: Following are the pytests to unit test orderqty function
    - test_edge_cases.py
    - test_error_cases.py
    - test_boundary_cases.py
    - test_happypath_cases.py
    
- **Test Data**: The test data for the various pytests are in a comma separated text file:
    - test_edge_cases.txt: The data is built using the beginning or the end of a range for number of dogs. Small Dogs = 0 or 30, Medium Dogs = 0 or 30, Large Dogs = 0 or 30 and their combination. Remaining food =0 
    - test_error_cases.txt: These cases help to test the "else" path of the code
      1. The scenarios are "Small and/or medium and/or large dog = negative number 
      2. Fractional number of dogs: For example - If the number of small dogs is 1.5. The function returns a value of -999 for order_qty for all the error scenarios. The expected output of this scenario is -999 which is present in the .txt file. But the function has a bug in it which is detected by the pytest as seen in the sample output           highlighted by red color. The developer has not initialized the variables as int values and hence as default they are used as "Float". 
      
         |Input to orderqty.py|Expected output                |   Actual output             | Reason for failure |
         |----------------    |-------------------------------|-----------------------------|--------------------| 
         |1.5,4,6,20          |         -999                  |           306.0               |There should be a check present in the code if the number of dogs has a decimal point|  
    
    - test_boundary_cases.txt: Here the data contains "Just Inside-Just Outside" values. If the number of dogs is 1 and/or 31, 32 etc
    - test_happypath_cases.txt: The data contains known input, which executes without exception and produces an expected output. Example: If at the end of the month I have 5 small dogs, 3 medium dogs, 7 large dogs, and a leftover food supply of 17lbs. Then the order_qty is 363.6 lbs

- Cases not covered in Acceptance Criteria
    - Change in number and/or size of dogs during of the course of the month. This will impact the order quantity. We are working with the assumption that the number/size of dogs will remain constant for 30 days, which might not be true in real life scenarios. An alternative would be to develop a predictive model to estimate average number of dogs for next 30 days based on prior history
    - Minimum order quantity is not defined. This might be a requirement when actually sourcing food supply.
      1. For example: (S*10 + M*20+ L*30) – remaining food = 0.1. Hence the order quantity would be 0.1 *1.2 = 0.12lbs
    - Upper limit of remaining food is not defined. For example: What if the user enters remaining food = 1000000 by mistake

## Sample Output
![image](https://user-images.githubusercontent.com/51870349/129500494-0d3d487e-d928-4f2a-bb56-83971dc43e23.png)

## How to run the pytests
Go to "Run" on the toolbar of Spyder and click on "Run unit tests"
