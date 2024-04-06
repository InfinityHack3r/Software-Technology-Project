<p align = "center">

<h1 align = "center">Software Technology Project</h1>
<h2 align = "center">| 🐍python |</h2>
</p>

## **Introduction**
Welcome to the culmination of the "Software Technology". This project showcases the skills, knowledge and expertise acquired throughout the course, all channeled into a Python-driven application. The project is divided into 10 parts each designed to test a specific skill or concept.

# Contents

- [Challenge Activity 1: Population projection](#challenge-activity-1-population-projection)
- [Challenge Activity 2: Student Information Display Tool](#challenge-activity-2-student-information-display-tool)
- [Challenge Activity 3: Sales Prediction Tool](#challenge-activity-3-sales-prediction-tool)
- [Challenge Activity 4: Pound to Kilogram Converter](#challenge-activity-4-pound-to-kilogram-converter)
- [Challenge Activity 5: Turtle Graphics Pattern Generator](#challenge-activity-5-turtle-graphics-pattern-generator)
- [Challenge Activity 6: Quiz Mark Calculator GUI](#challenge-activity-6-quiz-mark-calculator-gui)
- [Challenge Activity 7: Lap Timer Tool](#challenge-activity-7-lap-timer-tool)
- [Challenge Activity 8: Fat and Carbs Tracker](#challenge-activity-8-fat-and-carbs-tracker)
- [Challenge Activity 9: Stadium Seating Revenue Calculation Tool](#challenge-activity-9-stadium-seating-revenue-calculation-tool)
- [Challenge Activity 10: City Skyline Creation with Turtle Graphics Package](#challenge-activity-10-city-skyline-creation-with-turtle-graphics-package)




## Challenge Activity 1: Population projection

### Analysis:

The Population Projection tool is designed to predict Australia's population for the next five years using four main factors: birth rate, death rate, immigration rate and the current population. Users have the flexibility to input custom values for these elements, allowing the tool to offer a range of population predictions tailored to specific scenarios. This adaptability enhances its utility, whether it's researchers are examining demographic trends or policymakers planning for the future. This Python tool provides valuable insights making it an essential resource for diverse users.

### Algorithm design:

The central algorithm revolves around computing the annual growth based on user inputs: birth rate, death rate and immigration rate. To encapsulate the logic:

Annual Growth = (birth rate / SECONDS_IN_YEAR) - (death rate / SECONDS_IN_YEAR) + (immigration rate / SECONDS_IN_YEAR)

The formula takes the yearly averages of births, deaths and immigrants and gives us a net annual growth rate.

![pic](/Challenge%20Activity%201%20Population%20projection/Excalidraw.png)

### Evidence of testing

- **Valid inputs test**
  - Input: Valid values for birth rate, death rate, immigration rate and current population.
  - Expected result: Successful calculation and display of projected population.
- **Non-numeric inputs test**
  - Input: Non-numeric inputs for any field.
  - Expected Result: Display an error message indicating invalid input.
- **High values test**
  - Input: Extremely high values for birth rate, death rate and immigration rate.
  - Expected Result: The tool should handle it without crashing.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%201%20Population%20projection/1.png)|![pic](/Challenge%20Activity%201%20Population%20projection/2.png)|![pic](/Challenge%20Activity%201%20Population%20projection/3.png)|


### Reflection

The algorithm, while seemingly straightforward, had to be carefully designed to cater to varied input scenarios ensuring validity across the board. Testing was paramount revealing crucial insights into potential pitfalls and areas of improvement. Looking ahead the application could benefit from added features like trend analysis and predictive modelling, diving deeper into demographic intricacies. Collaboration with experts in the field might elevate its utility making it indispensable for demographic research.

### Code

See files attached

## Challenge Activity 2: Student Information Display Tool

### Analysis

The problem is collecting various pieces of information about a student, including their name, address, suburb, state, postcode, telephone number and course. Once the user inputs all the necessary details and clicks the "Submit" button, the tool displays the information in a message box and also saves it to a text file. The tool aims to streamline the process of collecting and storing student information in a structured manner.

### Algorithm Design

In the initial stage I set up a Tkinter root window, defining its title and size constraints. Following this, I created labels and entry fields for each data point I intended to collect, arranging them neatly using a grid layout.

![pic](/Challenge%20Activity%202%20Student%20Information%20Display%20Tool//excalidraw.png)

### Evidence of Testing

- **Valid Inputs Test**
  - Input: Valid strings for each field.
  - Expected Result: The information is displayed in a message box and saved to the "student_information.txt" file correctly.
- **Empty Fields Test**
  - Input: Leaving one or more fields empty and clicking "Submit".
  - Expected Result: The information is displayed and saved with empty values for the missing fields.
- **Special Characters Test**
  - Input: Including special characters (e.g., &, %, $) in the fields.
  - Expected Result: The special characters are displayed and saved correctly without causing any errors.


### Reflection

I set up a user interface with various input fields and implementing functionality to collect, display and save user inputs. The project highlighted the importance of user-friendly design, ensuring that the tool is intuitive and straightforward to use in future iterations. It may be beneficial to add validation checks to ensure the integrity of the data entered like checking that the telephone field contains only numbers.

### Code

See files attached

## Challenge Activity 3: Sales Prediction Tool

### Analysis

In this project, I created a Python GUI application that assists users in predicting the annual profit of a company based on its total sales and a specified profit margin. The tool is designed to be straightforward, allowing users to input the projected total sales and the profit margin with a default value of 23% to calculate and display the projected profit.

### Algorithm Design

To construct the sales prediction tool, I initiated a Tkinter root window and established a frame to input projected sales and a profit margin, which defaults to 23%. I implemented a "Calculate Profit" button that when clicked activates the calculate_profit function. This function retrieves the user inputs, calculates the profit using the formula `profit = projected_sales * (profit_margin / 100)` and displays the result rounded to two decimal places.

![pic](/Challenge%20Activity%203%20Sales%20Prediction%20Tool/excalidraw.png)

### Evidence of Testing

- **Valid Inputs Test**
  - Input: I entered valid numbers for the projected sales and profit margin.
  - Expected Result: The tool correctly calculated and displayed the projected profit.
- **Invalid Inputs Test**
  - Input: I entered non-numeric values in the fields to test the error handling.
  - Expected Result: The tool displayed an error message prompting for valid numeric inputs.
- **Default Profit Margin Test**
  - Input: I used the default profit margin value to calculate the profit.
  - Expected Result: The tool used the default profit margin of 23% to calculate and display the projected profit.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%203%20Sales%20Prediction%20Tool/1.png)|![pic](/Challenge%20Activity%203%20Sales%20Prediction%20Tool/2.png)|![pic](/Challenge%20Activity%203%20Sales%20Prediction%20Tool/3.png)|

### Reflection

I am satisfied with the sales projection tool’s current simplicity and efficiency. Looking ahead, I am eager to enhance it with more features, including graphical representations of profit predictions, options to save and analyse multiple projections and perhaps tools for comparing different profit scenarios side by side.

### Code

See files attached

## Challenge Activity 4: Pound to Kilogram Converter

### Analysis

I developed a Python GUI application that assists users in converting mass from pounds to kilograms. The user is prompted to input the mass in pounds and upon clicking the "Convert" button, the equivalent mass in kilograms is displayed. The conversion uses the formula `kilograms = pounds × 0.454`.

### Algorithm Design

To create the pound to kilogram converter, I initiated a Tkinter root window and set up a frame to hold the necessary widgets: a label instructing the user to enter the mass in pounds, an entry field for the input, a button to initiate the conversion and a label to display the result. The core of the application is the convert_to_kg function, which is triggered when the "Convert" button is clicked the conversion uses the formula `kilograms = pounds × 0.454`.

![pic](/Challenge%20Activity%204%20Pound%20to%20Kilogram%20Converter/excalidraw.png)

### Evidence of Testing

- **Valid Input Test**
  - Input: A valid numerical input for the mass in pounds.
  - Expected Result: The application calculates and displays the correct mass in kilograms.
- **Invalid Input Test**
  - Input: A non-numerical input.
  - Expected Result: The application displays an error message prompting for a valid number.
- **Boundary Test**
  - Input: Extremely high or low values for the mass in pounds.
  - Expected Result: The application handles it accurately, providing the correct conversion.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%204%20Pound%20to%20Kilogram%20Converter/1.png)|![pic](/Challenge%20Activity%204%20Pound%20to%20Kilogram%20Converter/2.png)|![pic](/Challenge%20Activity%204%20Pound%20to%20Kilogram%20Converter/3.png)|

### Reflection

Developing this pound to kilogram converter was a straightforward. It allowed me to apply my knowledge of Python and Tkinter to create a simple, user-friendly tool. I am pleased with the functionality it offers, efficiently converting pounds to kilograms with just a click. Looking forward, I am considering adding more features such as the ability to convert kilograms to pounds and perhaps even extending it to a multi-unit converter that can handle various types of conversions, offering users a more versatile tool.

### Code

See files attached

## Challenge Activity 5: Turtle Graphics Pattern Generator

### Analysis

In this project, I was tasked with creating a Python program using the turtle graphics library to draw a specific pattern: two diamonds touching each other at one corner. The objective was to accurately replicate the design shown in the figure provided, ensuring the diamonds are symmetrical and touch each other precisely at one point.

### Algorithm Design

To draw two touching diamonds, I first set up the turtle with a thicker pen size and the fastest speed. I then used the goto command to move the turtle to the correct positions to draw the first diamond. Repeating this process, I drew the second diamond touching the first one at a corner. Finally, I hid the turtle and displayed the completed drawing using the turtle graphics main loop.

![pic](/Challenge%20Activity%205%20Turtle%20Graphics%20Pattern%20Generator/excalidraw.png)

### Evidence of Testing

- **Visual Inspection**
  - Input: Running the script with the defined coordinates for the diamond vertices.
  - Expected Result: A visual representation of two touching diamonds displayed without any distortions or errors.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%205%20Turtle%20Graphics%20Pattern%20Generator/1.png)|

### Reflection

It allowed me to explore the functionalities of the library while focusing on the precision required to replicate the design accurately. I am satisfied with the outcome, as the program successfully draws two symmetrical diamonds touching at a point. Looking forward, I am considering experimenting with adding colours and filling the diamonds to enhance the visual appeal of the pattern. Additionally, I see potential in developing a feature that allows users to create different patterns by inputting their preferred coordinates, making the tool more interactive and versatile.

### Code

See files attached

## Challenge Activity 6: Quiz Mark Calculator GUI

### Analysis

In this project, I created a Python GUI application to calculate the total mark based on the scores of four quizzes. The user is required to input the marks of each quiz, which should be integers between 0 and 10. The program then calculates and displays the total mark.

### Algorithm Design

I utilized Tkinter to establish a root window and a frame to house the necessary widgets, including labels and entry fields for inputting the marks of four quizzes. These entry fields were stored in a list for easy retrieval. I integrated a "Calculate Sum" button to invoke the calculate_total_mark function, which gathers the user-inputted marks, verifies their validity (ensuring they are integers between 0 and 10) and computes the total mark to be displayed. If an input is found to be invalid, a corresponding error message is showcased.

![pic](/Challenge%20Activity%206%20Quiz%20Mark%20Calculator%20GUI/excalidraw.png)

### Evidence of Testing

- **Valid Input Test**
  - Input: Valid integer inputs between 0 and 10 for each quiz mark.
  - Expected Result: The application calculates and displays the correct total mark.
- **Out-of-Range Input Test**
  - Input: An input outside the range of 0 to 10 for any quiz mark.
  - Expected Result: The application displays an error message indicating the valid range for quiz marks.
- **Invalid Input Test**
  - Input: Non-integer inputs for any quiz mark.
  - Expected Result: The application displays an error message prompting for valid numbers.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%206%20Quiz%20Mark%20Calculator%20GUI/1.png)|![pic](/Challenge%20Activity%206%20Quiz%20Mark%20Calculator%20GUI/2.png)|![pic](/Challenge%20Activity%206%20Quiz%20Mark%20Calculator%20GUI/3.png)|

### Reflection

I creating a user-friendly interface that efficiently calculates the total mark based on individual quiz scores the functionality it offers, providing immediate feedback on the total score while validating the input to ensure accuracy. Looking forward I am considering adding features such as the ability to calculate the average score and perhaps a grade based on the total mark, enhancing the application's utility for students tracking their performance.

### Code

See files attached

## Challenge Activity 7: Lap Timer Tool

### Analysis

I was tasked with creating a GUI program that assists users in recording and analysing their lap times. The user inputs the number of laps they ran and then inputs the individual lap times. The program calculates and displays the fastest lap time, the slowest lap time, and the average lap time.

### Algorithm Design

To construct the Lap Timer Tool, I initiated a Tkinter root window and set up a primary frame to host various widgets including labels, entry fields and buttons. I implemented functionalities to start and stop a timer and dynamically generate entry fields based on the number of laps inputted. The calculate_lap_times function is central to this tool, gathering the lap times inputted and determining the fastest, slowest and average lap times to display them to the user. Error handling is integrated to manage invalid inputs effectively.

![pic](/Challenge%20Activity%207%20Lap%20Timer%20Tool/excalidraw.png)

### Evidence of Testing

- **Valid Input Test**
  - Input: Valid number of laps and respective lap times.
  - Expected Result: The application calculates and displays the fastest, slowest and average lap times correctly.
- **Invalid Number of Laps Test**
  - Input: A number of laps less than 1.
  - Expected Result: The application displays an error message prompting a valid number of laps.
- **Invalid Lap Times Test**
  - Input: Non-numeric or negative lap times.
  - Expected Result: The application displays an error message prompting valid lap times.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%207%20Lap%20Timer%20Tool/1.png)|![pic](/Challenge%20Activity%207%20Lap%20Timer%20Tool/2.png)|![pic](/Challenge%20Activity%207%20Lap%20Timer%20Tool/3.png)|

### Reflection

The tool efficiently facilitates the recording of lap times and instantly provides valuable insights into the user's performance, showcasing the fastest, slowest and average lap times. In the future, I envision enhancing the tool by adding features such as a reset button to clear all fields quickly and possibly a graphical representation of the lap times for a more visual analysis.

### Code

See files attached

## Challenge Activity 8: Fat and Carbs Tracker

### Analysis

Tasked with creating a GUI program to assist a nutritionist in calculating the calories derived from the fat and carbohydrates consumed by individuals in a day. The nutritionist uses two formulas to calculate the calories: calories from fat are calculated as `fat grams × 3.9` and calories from carbs are calculated as `carb grams × 4`. The program should facilitate quick and accurate calculations by allowing the nutritionist to input the grams of fat and carbs and then displaying the calculated calories.

### Algorithm Design

To build the Fat and Carbs Tracker, I initiated a Tkinter root window and established a frame to house the necessary widgets, including labels and entry fields for the input of fat and carb grams. A "Calculate" button was integrated to invoke the calculate_calories function, which retrieves the input values, validates them to be positive and performs the calculations using the given formulas to determine the calories from fat and carbs. The results are then displayed to the user and error handling is incorporated to manage invalid inputs effectively.

![pic](/Challenge%20Activity%208%20Fat%20and%20Carbs%20Tracker/excalidraw.png)

### Evidence of Testing

- **Valid Input Test**
  - Input: Valid positive numbers for fat and carb grams.
  - Expected Result: The application calculates and displays the correct calories from fat and carbs.
- **Negative Input Test**
  - Input: Negative numbers for fat and/or carb grams.
  - Expected Result: The application displays an error message prompting valid positive numbers.
- **Non-numeric Input Test**
  - Input: Non-numeric inputs for fat and/or carb grams.
  - Expected Result: The application displays an error message prompting valid positive numbers.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%208%20Fat%20and%20Carbs%20Tracker/1.png)|![pic](/Challenge%20Activity%208%20Fat%20and%20Carbs%20Tracker/2.png)|![pic](/Challenge%20Activity%208%20Fat%20and%20Carbs%20Tracker/3.png)|

### Reflection

The tool serves as a reliable assistant for the nutritionist ensuring precise and rapid calculations of calories from fat and carbs based on daily consumption data. Looking ahead, I see potential for further enhancements, such as incorporating a feature to save daily entries and generate reports over time, providing a more comprehensive view of an individual's diet.

### Code

See files attached

## Challenge Activity 9: Stadium Seating Revenue Calculation Tool

### Analysis

The objective of this project is to create a GUI tool that helps in calculating the total revenue generated from the sale of tickets in a stadium. The stadium has three classes of seats - A, B, and C, each having different costs. The user should be able to input the number of tickets sold and the cost of tickets for each class and the program should calculate and display the total revenue generated.

### Algorithm Design

To build the Stadium Seating Revenue Calculation Tool, I initiated a Tkinter root window and set up a frame to hold the necessary widgets. I created labels and entry fields for users to input the number of tickets sold and the cost for each class of seats, with default values for the costs already inputted. I also implemented a "Calculate Revenue" button that triggers the calculate_revenue function when clicked.

![pic](/Challenge%20Activity%209%20Stadium%20Seating%20Revenue%20Calculation%20Tool/excalidraw.png)

### Evidence of Testing

- **Valid Input Test**
  - Input: Valid positive numbers for the number of tickets sold and the cost for each class of seats.
  - Expected Result: The application calculates and displays the correct total revenue.
- **Negative Input Test**
  - Input: Negative numbers for the number of tickets sold and/or the cost for any class of seats.
  - Expected Result: The application displays an error message prompting valid positive numbers.
- **Non-numeric Input Test**
  - Input: Non-numeric inputs for the number of tickets sold and/or the cost for any class of seats.
  - Expected Result: The application displays an error message prompting valid positive numbers.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%209%20Stadium%20Seating%20Revenue%20Calculation%20Tool/1.png)|![pic](/Challenge%20Activity%209%20Stadium%20Seating%20Revenue%20Calculation%20Tool/2.png)|![pic](/Challenge%20Activity%209%20Stadium%20Seating%20Revenue%20Calculation%20Tool/3.png)|

### Reflection

The tool serves as a reliable assistant for stadium management, ensuring precise and rapid calculations of total revenue based on ticket sales data. Looking ahead, I see potential for further enhancements, such as incorporating a feature to save daily entries and generate reports over time, providing a more comprehensive view of the stadium's revenue trends.

### Code

See files attached

## Challenge Activity 10: City Skyline Creation with Turtle Graphics Package

### Analysis

The goal of this project is to create a graphical representation of a city skyline at night using Python's turtle graphics package. The skyline should feature a series of buildings with varying heights and widths, each having a number of windows, some of which are illuminated. The sky should be populated with stars, represented by randomly placed white dots. The program should be modular, with separate functions handling the drawing of the buildings the windows and the stars.

### Algorithm Design

To create a city skyline with a night sky backdrop using the turtle graphics package, I initiated a drawing screen with a black background and set up a turtle with a white pen colour for drawing. I designed three main functions: one to draw the building outlines with a grey fill colour, another to add windows to the buildings with a random chance of being illuminated and a third to add stars in the sky, ensuring they only appear above the horizon line to maintain realism.

![pic](/Challenge%20Activity%2010%20City%20Skyline%20Creation%20with%20Turtle%20Graphics%20Package/excalidraw.png)

### Evidence of Testing

- **Building Appearance Test**
  - Verify that buildings appear correctly with varied heights and widths as specified in the building specifications.
- **Window Appearance Test**
  - Confirm that windows appear correctly on the buildings, with a random selection of windows being drawn to create a natural look.
- **Star Appearance Test**
  - Ensure that stars appear only in the sky and not on the buildings, with a random distribution of sizes and positions to mimic a real starry sky.

|  |  |  |  
|:---:|:---:|:---:|
|![pic](/Challenge%20Activity%2010%20City%20Skyline%20Creation%20with%20Turtle%20Graphics%20Package/1.png)|

### Reflection

The project challenged me to think about how to represent objects like buildings and stars graphically and how to use randomization to create a more natural and realistic scene. Looking forward, I can envision expanding this project to include more detailed elements such as moon phases, moving clouds, or even animated elements like flying birds or airplanes to bring the skyline to life further.

### Code

See files attached
