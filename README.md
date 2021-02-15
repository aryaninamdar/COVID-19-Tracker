# COVID-19-Tracker
A user friendly app that uses real-time data to track COVID-19 rates from around the world.

## How it Works
Python is used along with the NovelCovidAPI, NewsAPI, Tkinter, and Matplotlib to create this tracker.

NovelCvidAPI: https://documenter.getpostman.com/view/8854915/SzS7R6uu?version=latest

NewsAPI: https://newsapi.org/

## App Demonstration
Upon the startup of the app, the GUI will look like this: https://drive.google.com/file/d/18GPihRsGB7T9_XtZl4imaY-wsfJATRrH/view?usp=sharing

From here, enter the name of any country followed by a start data and an end date. As stated in the GUI, there are certain bounds for the dates that the app can process. The earliest date that cane be enter is 1/22/20 and the latest date you can enter is the day prior to the day you are running the app.

If all input is correct, you will be shown a graph of the COVID-19 cases of that country over the inputted time range, and you will also be provided with the countries total cases, deaths, and recoveries up until the end date. Additionally, you will also be given some of the top COVID-19 hedlines currently in the news.
An example of such an output is here: https://drive.google.com/file/d/19Lomzg9t04Int4nPcnlRGAJIXUaBSBG-/view?usp=sharing

However, if you enter invalid input (mispelled country name, nonexistent date, out of range date), you will be shown a message on the right sidebar that notifies you of the error you have made. An example of this message is shown here:  https://drive.google.com/file/d/1VI1ukz7eu7oSmATLjtU_4ojYp-nhheua/view?usp=sharing
