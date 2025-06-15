#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import warnings
warnings.filterwarnings('ignore')

initiatives = pd.read_csv(r'C:\Users\Harish\OneDrive\Desktop\policy\initiatives.csv', sep = ',') #file with the actions to be taken
#print(initiatives.info())
# print(initiatives.head())

#print(initiatives.section.unique())

# policies = initiatives.groupby('section')
# food = policies.get_group('Food')
# waste = policies.get_group('Waste')
# energy = policies.get_group('Energy')
# water = policies.get_group('Water')
# climate = policies.get_group('Climate')
# trans = policies.get_group('Transportation')
# land = policies.get_group('Land Use')

#print(climate)

issues = pd.read_csv(r'C:\Users\Harish\OneDrive\Desktop\policy\user_data.csv', sep = ',') #file with the user replies
#print(issues.head())
rows = len(issues)
a = 'Number of respondents: '+ str(rows)


group_issues = issues.groupby('issues_faced_in') #groups data based on same values in issues_faced_in
issue_counts = group_issues.size() #size (no of entries) of each group
issue_counts = issue_counts.reset_index() #indexing resets from 0
issue_counts.columns = ['issues_faced_in', 'count'] #name of columns
# print(issue_counts.head())

max_num = issue_counts['count'].idxmax() #max count
priority = issue_counts.loc[max_num, 'issues_faced_in'] #most voted issue
b = "Most Prevelant Issue:" + priority #if max count by two, alphabetically first

policy = initiatives[initiatives['section']==priority].reset_index() #all those rows where section matches with priority
# print(policy)

if not policy.empty: #if atleast 1 row found with section = priority
    recommendation = random.choice(policy['priority_action'].values)
    c= 'Recommended Policy for '+ priority+ ': '+ recommendation

def plot_graph():
    plt.figure(figsize=(5,3))
    plt.bar(issue_counts['issues_faced_in'], issue_counts['count'])
    plt.xlabel('Issue Faced')
    plt.ylabel('Number of People')
    plt.title('Issues Faced By Youth')
    plt.show()    

import tkinter as tk
from tkinter import Tk, Frame, Label, Button

# Initialize Tkinter
root = Tk()
root.title('YouthConnect AI')
root.geometry('700x500')
root.configure(background='#121212')

# Function to switch to recommendation screen
def switch_to_recommendation_screen():
    home_screen_frame.grid_forget()
    recommendation_screen_frame.grid(row=0, column=0)

# Function to switch to home screen
def switch_to_home_screen():
    recommendation_screen_frame.grid_forget()
    home_screen_frame.grid(row=0, column=0)

# Home screen
home_screen_frame = Frame(root, width=700, height=500, bg='#121212')
home_screen_frame.grid(row=0, column=0)

title_label = Label(home_screen_frame, text='YouthConnect AI', bg='#121212', fg='white', font=('Arial', 30, 'bold'))
title_label.place(x=200, y=50)

generate_button = Button(home_screen_frame, text='Generate Policy', command=switch_to_recommendation_screen, bg='#00a65a', fg='white', font=('Arial', 20))
generate_button.place(x=250, y=200, width=200, height=50)

# Recommendation screen
recommendation_screen_frame = Frame(root, width=1200, height=500, bg='#121212')

back_button = Button(recommendation_screen_frame, text='Back to Home', command=switch_to_home_screen, bg='#00a65a', fg='white', font=('Arial', 20))
back_button.place(x=250, y=400, width=200, height=50)


num_respondents_label = Label(recommendation_screen_frame,text=a, bg='#121212', fg='white', font=('Arial', 20))
num_respondents_label.place(x=50, y=100)

most_prevalent_issue_label = Label(recommendation_screen_frame,text =b, bg='#121212', fg='white', font=('Arial', 20))
most_prevalent_issue_label.place(x=50, y=150)

recommended_policy_label = Label(recommendation_screen_frame,text=c, bg='#121212', fg='white', font=('Arial', 20), wraplength=500, justify = 'left')
recommended_policy_label.place(x=50, y=200)

frame1=tk.Frame(root)
frame1.grid(row=50, column=250, sticky="nsew")


button_graph=Button(recommendation_screen_frame,text="Plot Graph",bg='#00a65a', fg='white', font=('Arial', 20),command=plot_graph)
button_graph.place(x=250,y=450,width=200,height=50)


switch_to_home_screen()
root.mainloop()