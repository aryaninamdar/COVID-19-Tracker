import Tkinter as tk
import requests
import matplotlib
matplotlib.use('TkAgg')
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

# ------ Creating the GUI Skeleton ------
window = tk.Tk()
window.title("COVID-19 Tracker")
window.geometry('1500x900')
window.resizable(width=False, height=False)

# Create different sections on screen
canvas = tk.Canvas(window, width=1500, height=900)
canvas.create_line(0, 70, 1500, 70, fill='black')
canvas.create_line(1100, 70, 1100, 900)
canvas.pack()

# Create widgets/elements
# Country Label
country_label = tk.Label(canvas, text='Enter a Country Name', font=('Calibri', 20))
country_label.place(x=10, y=20)

# Country Input Box
country_input = tk.Entry(canvas, font=('Calibri', 20), width=15)
country_input.place(x=220, y=15)

# Start and End Date Label and Input
start_date_label = tk.Label(canvas, text='Start Date (MM/DD/YY)\n Earliest: 1/22/20', font=('Calibri', 20))
start_date_label.place(x=430, y=5)
start_date_input = tk.Entry(canvas, font=('Calibri', 20), width=7)
start_date_input.place(x=653, y=15)

end_date_label = tk.Label(canvas, text='End Date (MM/DD/YY)\n Latest: Yesterday', font=('Calibri', 20))
end_date_label.place(x=770, y=5)
end_date_input = tk.Entry(canvas, font=('Calibri', 20), width=7)
end_date_input.place(x=985, y=15)

# Button to display statistics on click
search_button = tk.Button(canvas, text='Search COVID-19 Data', font=('Calibri', 20), width=20, command=lambda: retrieveData())
search_button.place(x=1175, y=20)

# Declaring labels for modification in upcoming function
total_cases_label = tk.Label(canvas)
total_deaths_label = tk.Label(canvas)
total_recoveries_label = tk.Label(canvas)
stats_title = tk.Label(canvas)
graph_gui = tk.Label(canvas, font=('Calibri', 30))
graph_gui.place(x=15, y=75)

# ------ GET DATA FROM API ------
covid_api = 'https://corona.lmao.ninja/v2/historical?lastdays=all' # THIS IS THE GOOD API WITH ALL DATES. DO NOT CHANGE. DOOOO NOOOOOTTTTTTT CHANNNNGGGGEEEEEEE
data = requests.get(covid_api)
data = data.json()

def retrieveData():
    # ------ GET TOTAL CASES DEATHS AND RECOVERIES FOR A SPECIFIC COUNTRY OVER A SPECIFIC TIME SPAN. ALSO GIVE COVID-19 HEADLINES (SIDEBAR) ------
    # get values of country/date input
    inputted_country = country_input.get()
    inputted_start_date = start_date_input.get()
    inputted_end_date = end_date_input.get()

    # declare x and y values list for graph
    dates = []
    cases = []

    # get data from inputted country and display then on sidebar
    for country_index in range(273):
        if (data[country_index]['country'] == inputted_country):
            # create gui elemets to display statistics of the country
            stats_title.config(text=(str(inputted_country) + "'s Stats as of " + str(inputted_end_date)), font=('Calibri', 25))
            stats_title.place(x=1110, y=80)
            canvas.create_line(1100, 130, 1500, 130)

            try:
                # display stats
                total_cases_label.config(text=("Total Cases: " + str(data[country_index]['timeline']['cases'][inputted_end_date])), font=('Calibri', 25))
                total_cases_label.place(x=1110, y=140)
                total_deaths_label.config(text=("Total Deaths: " + str(data[country_index]['timeline']['deaths'][inputted_end_date])), font=('Calibri', 25))
                total_deaths_label.place(x=1110, y=190)
                total_recoveries_label.config(text=("Total Recoveries: " + str(data[country_index]['timeline']['recovered'][inputted_end_date])), font=('Calibri', 25))
                total_recoveries_label.place(x=1110, y=240)

                # generate x and y values for graph
                for i in data[country_index]['timeline']['cases']:
                    dates.append(str(i))
                    cases.append(data[country_index]['timeline']['cases'][i])

            except KeyError:
                stats_title.config(text="Invalid Date(s) Entered")
                total_cases_label.config(text="Total Cases: ---")
                total_deaths_label.config(text="Total Deaths: ---")
                total_recoveries_label.config(text="Total Recoveries: ---")

    # get headlines fron news api and display it on sidebar
    url = ('http://newsapi.org/v2/top-headlines?'
            'q=COVID-19&'
            'country=us&'
            'apiKey=4f52ee91c734419f8ab8ffeea5010742')

    related_media = requests.get(url)
    related_media = related_media.json()

    related_media_title = tk.Label(canvas, text="Top COVID-19 Headlines", font=('Calibri', 25))
    related_media_title.place(x=1110, y=340)

    canvas.create_line(1100, 390, 1500, 390)

    try:
        # dispay headlines in the GUI
        headline_1 = tk.Label(canvas, text=related_media['articles'][0]['title'], font=('Calibri', 15), wraplength=380)
        headline_1.place(x=1110, y=400)

        headline_2 = tk.Label(canvas, text=related_media['articles'][1]['title'], font=('Calibri', 15), wraplength=380)
        headline_2.place(x=1110, y=480)

        headline_3 = tk.Label(canvas, text=related_media['articles'][2]['title'], font=('Calibri', 15), wraplength=380)
        headline_3.place(x=1110, y=560)

        headline_4 = tk.Label(canvas, text=related_media['articles'][3]['title'], font=('Calibri', 15), wraplength=380)
        headline_4.place(x=1110, y=640)

        headline_5 = tk.Label(canvas, text=related_media['articles'][4]['title'], font=('Calibri', 15), wraplength=380)
        headline_5.place(x=1110, y=640)
    except IndexError:
        print(" ")

    # ------ MANIPULATE, PLOT, AND DISPLAY DATA ------
    # filter covid data from API to only include inputted range of dates
    sorted_dates = [x for _, x in sorted(zip(cases, dates))]
    cases.sort()

    try:
        # filter covid data from API to only include inputted range of dates
        i = 0
        while sorted_dates[i] != inputted_start_date:
            sorted_dates.remove(sorted_dates[i])
            cases.remove(cases[i])

        sorted_dates.reverse()
        cases.reverse()

        j = 0
        while sorted_dates[j] != inputted_end_date:
            sorted_dates.remove(sorted_dates[j])
            cases.remove(cases[j])

        sorted_dates.reverse()
        cases.reverse()

        # plot data on graph
        x = [x for x in sorted_dates]
        y = [y for y in cases]
        fig = plt.figure(figsize=(10, 8), dpi=100)
        axs = fig.add_subplot(111)
        axs.plot(x, y)
        axs.set_title(str(inputted_country) + ": " + str(inputted_start_date) + " to " + str(
            inputted_end_date) + " COVID-19 Cases", fontsize=20)
        plt.xlabel("Date", fontsize=15)
        plt.ylabel("Cases", fontsize=15)
        axs.set_xticks(sorted_dates[::15])
        axs.set_xticklabels(sorted_dates[::15], rotation=45)
        plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
        plt.savefig('covid.png')

        # display graph on the GUI
        plotted_data = Image.open('covid.png')
        graph = ImageTk.PhotoImage(plotted_data, master=window)
        graph_gui.config(image=graph)
        graph_gui.photo_ref = graph

    except IndexError:
        # handle human error
        stats_title.config(text="Invalid Country/Date(s) Entered")
        total_cases_label.config(text="Total Cases: ---")
        total_deaths_label.config(text="Total Deaths: ---")
        total_recoveries_label.config(text="Total Recoveries: ---")

window.mainloop()
