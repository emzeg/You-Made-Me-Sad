#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Emotional Stroop Task
# @ AU Cognitive Science 2023

# import modules
from psychopy import visual, event, core, data, gui
import random
import pandas as pd
import time

# Create popup information box
popup = gui.Dlg(title = "The Stroop Experiment")
popup.addField("Alias: ") # Empty box
popup.addField("Age: ")
popup.addField("Condition: ", choices=[1, 2]) # Dropdown menu
popup.addField("Gender: ", choices=["Male", "Female", "Non-Binary", "Other" ]) # Dropdown menu
popup.show()
if popup.OK: # To retrieve data from popup window
    ID = popup.data
elif popup.Cancel: # To cancel the experiment if popup is closed
    core.quit()

#########################################################################################
################################## Stroop Task ##########################################
#########################################################################################


NUM_REP = 6 # repetitions * 15 trials

intro = '''
Welcome to the experiment!

This is a version of the "Stroop Task". Please read the instructions very carefully.

Use the keys r, g, b, and y to indicate if the words on the screen are printed
in red, green, blue or yellow ink. Ignore the meaning of the words.

Example: if you see the word "horse" printed in green ink, you should press 'g'.
Please try to be as fast as possible. 

If you make a mistake, please do not try to correct it by pushing a second key. Just wait for the next trial.  

You will do this task twice. After the first time you will be presented with a story to read. This is not
a time task, so please take your time reading it. You will then be presented with the task for the second time.

The practice round is ready to begin, press any key when you are ready...
'''

#after practice
first_instruction = '''
Well done. You have completed the practice round. 

You will now begin the real experiment.

Press any key to begin the first task
'''

#after first task
second_instruction = '''
Well done. You have completed the first task.

You will now be presented with a diary entry of someone describing their day. 

Remember you are not being timed, so please take your time to read it.

Press any key when you are ready to begin the second task.
'''

#after second task
third_instruction = '''
Thank you for completing the story. You will do the final task.

Press any key to begin the third task
'''

#diary

diary_neutral = '''
Dear Diary,

I'm writing to you today feeling content and at peace. It's been a while since I've had a day where everything just seems to be going right, but today is one of those days. I feel like I'm in control of my life and I'm making progress towards my goals.

One of the things that's been occupying my time lately is my degree program. It's a challenging program, but I'm enjoying the challenge and the learning experience. I feel like I'm making good progress, and I'm excited about the opportunities that will be available to me when I finish.

When I think about home, I'm reminded that it's not a physical place, but rather a feeling of comfort and safety. I used to believe that I needed a physical place to call home, but over time I've come to realize that home is wherever I feel loved and accepted. Even though I don't have a physical home to go back to, I feel at home wherever I am, surrounded by the people who care about me.

I'm grateful for the people in my life who have supported and encouraged me along the way. Their love and support have given me the strength to pursue my dreams and to keep going even when things get tough. I know that I can count on them to be there for me whenever I need them.

Overall, I'm feeling really positive about my life and my future. I know that there will be challenges and obstacles to overcome, but I'm confident that I have the resilience and determination to face them head-on. I'm excited to see where my journey takes me, and I'm looking forward to all the adventures that lie ahead.

Signed,
'''

diary_sad = '''
Dear Diary,

It has come. I've been absolutely terrified of slowly falling apart, it's back and it's hitting me harder than ever before. Every day and every night it gets worse, and I feel like I'm drowning in it. Even though my day-to-day life is good, there's something very wrong going on in the background, and I just want to escape to the safety and comfort of home. But home, the place where I used to find solace, is not here right now. I placed my homes in people, not a place, and now I don't have a home here, not really, not one that makes me feel safe and comfortable.

I want to finish my degree because it'll give me some sort of opportunity, but I also feel like I'm reaching my breaking point. I need a break, but I'm terrified of what might happen if I step away. If I take a break, I might not come back, and that thought is absolutely paralyzing. It's one thing to take a degree you might never use, but it's much worse in my eyes to get so far into the degree you won't use and then not finish it. I need to finish it, even if it means breaking myself.

And the thought of going home is also tearing me apart. Because I no longer have one. I miss the familiarity of having somewhere to go back to, but now I've ruined it and I have nothing. If I go to that place, what used to be home, I'll go as a failure and be met with a door in my face. I have nowhere to go where I feel completely safe, where I can stay for an extended period of time, even just a week, where I feel I am wanted and cherished and loved the whole time, that I'm not being a burden or a nuisance. The weight of it all is crushing, and I feel like I'm suffocating. I don't know how to make it stop.

Signed,
'''

#outro
outro = '''
You have completed the experiment. 
Thank you for your participation! <3 
'''

# define window
win = visual.Window(fullscr=True, color = 'Black')

# get date for unique logfile id
date = data.getDateStr() 

# define a stop watch
stopwatch = core.Clock()                                  

# colors
Colors = ['red', 'blue', 'green', 'yellow']
# prepare words

Practice_Stimuli = [{'word':'chair', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.06}, {'word':'window', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.72}, 
    {'word':'stone', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': -0.33},{'word': 'speak', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.52}, 
    {'word':'truck','emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.10}] 

Practice_Stimuli = Practice_Stimuli*NUM_REP
random.shuffle(Practice_Stimuli)

Stimuli = [{'word': 'happy', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.92}, {'word': 'party', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.20}, 
    {'word':'good', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 1.82},{'word': 'gift', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.34},
    {'word':'friend', 'emotional': 'emotional', 'valence': 'positive', 'sentiment': 2.28}, {'word': 'sad', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -2.99},
    {'word':'angry', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -3.05}, {'word': 'crime', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -3.17}, 
    {'word':'pain', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -3.27},{'word': 'distress', 'emotional': 'emotional', 'valence': 'negative', 'sentiment': -2.67},
    {'word':'chair', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.06}, {'word':'window', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.72}, 
    {'word':'stone', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': -0.33},{'word': 'speak', 'emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.52}, 
    {'word':'truck','emotional': 'neutral', 'valence': 'neutral', 'sentiment': 0.10}] 

Stimuli = Stimuli*NUM_REP
random.shuffle(Stimuli)

# prepare pandas data frame for recorded data
columns = ['ID', 'Age', 'Gender', 'Word', 'Color', 'Condition', 'Trial', 'Emotional', 'Valence','Sentiment', 'Correct', 'Reaction_time']
STROOP_DATA = pd.DataFrame(columns=columns)

# define function that shows text
def msg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 0.05) # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
    win.flip() # flip the screen to reveal the stimulus
    event.waitKeys() # wait for any key press



# show instructions
msg(intro)


# practice loop through trials
for i in range(len(Practice_Stimuli)):
    # choose random color from list
    col = random.choice(Colors)
    # Word
    txt = Practice_Stimuli[i]['word']
    # prepare stimulus
    stimulus = visual.TextStim(win, text=txt, color = col)
    # draw stimulus
    stimulus.draw()
    win.flip()
    # reset stop watch
    stopwatch.reset()                              #reset the clock to 0:0:0 
    # record key press
    key = event.waitKeys(keyList = ['escape', 'r', 'g', 'b', 'y'])                  # wait for any key press
    # get reaction time at key press
    reaction_time = stopwatch.getTime()            # asks the stopwatch for the time since reset and save to the variable reation_time
    
    # check if response is correct
    if key[0] == col[0]:
        correct = 1
    elif key[0] != col[0]:
        correct = 0
    elif key[0] == 'escape':
        core.quit()
        win.close()
        
    # append all recorded data to the pandas DATA 
    STROOP_DATA = STROOP_DATA.append({
        'ID': ID[0],
        'Age': ID[1],
        'Condition': ID[2],
        'Gender': ID[3],
        'Word': txt,
        'Color': col,
        'Trial': 'Practice',
        'Emotional': Stimuli[i]['emotional'],
        'Valence': Stimuli[i]['valence'],
        'Sentiment': Stimuli[i]['sentiment'],
        'Correct': correct, 
        'Reaction_time': reaction_time
        }, ignore_index=True)
    
    # show blank screen
    stimulus = visual.TextStim(win, '')
    stimulus.draw()
    win.flip()
    core.wait(0.5)

core.wait (1)

msg(first_instruction)

# loop through trials
for i in range(len(Stimuli)):
    # choose random color from list
    col = random.choice(Colors)
    # Word
    txt = Stimuli[i]['word']
    # prepare stimulus
    stimulus = visual.TextStim(win, text=txt, color = col)
    # draw stimulus
    stimulus.draw()
    win.flip()
    # reset stop watch
    stopwatch.reset()                              #reset the clock to 0:0:0 
    # record key press
    key = event.waitKeys(keyList = ['escape', 'r', 'g', 'b', 'y'])                  # wait for any key press
    # get reaction time at key press
    reaction_time = stopwatch.getTime()            # asks the stopwatch for the time since reset and save to the variable reation_time
    
    # check if response is correct
    if key[0] == col[0]:
        correct = 1
    elif key[0] != col[0]:
        correct = 0
    elif key[0] == 'escape':
        core.quit()
        win.close()
        
    # append all recorded data to the pandas DATA 
    STROOP_DATA = STROOP_DATA.append({
        'ID': ID[0],
        'Age': ID[1],
        'Condition': ID[2],
        'Gender': ID[3],
        'Word': txt,
        'Color': col,
        'Trial': 'First',
        'Emotional': Stimuli[i]['emotional'],
        'Valence': Stimuli[i]['valence'],
        'Sentiment': Stimuli[i]['sentiment'],
        'Correct': correct, 
        'Reaction_time': reaction_time
        }, ignore_index=True)
    
    # show blank screen
    stimulus = visual.TextStim(win, '')
    stimulus.draw()
    win.flip()
    core.wait(0.5)

core.wait (1)

msg(second_instruction)

if ID[2] == 1:
    msg(diary_neutral)
elif ID[2] == 2:
    msg(diary_sad)

core.wait (1)

msg(third_instruction)

# loop through trials
for i in range(len(Stimuli)):
    # choose random color from list
    col = random.choice(Colors)
    # Word
    txt = Stimuli[i]['word']
    # prepare stimulus
    stimulus = visual.TextStim(win, text=txt, color = col)
    # draw stimulus
    stimulus.draw()
    win.flip()
    # reset stop watch
    stopwatch.reset()                              #reset the clock to 0:0:0 
    # record key press
    key = event.waitKeys(keyList = ['escape', 'r', 'g', 'b', 'y'])                  # wait for any key press
    # get reaction time at key press
    reaction_time = stopwatch.getTime()            # asks the stopwatch for the time since reset and save to the variable reation_time
    
    # check if response is correct
    if key[0] == col[0]:
        correct = 1
    elif key[0] != col[0]:
        correct = 0
    elif key[0] == 'escape':
        core.quit()
        win.close()
        
    # append all recorded data to the pandas DATA 
    STROOP_DATA = STROOP_DATA.append({
        'ID': ID[0],
        'Age': ID[1],
        'Condition': ID[2],
        'Gender': ID[3],
        'Word': txt,
        'Color': col,
        'Trial': 'Second',
        'Emotional': Stimuli[i]['emotional'],
        'Valence': Stimuli[i]['valence'],
        'Sentiment': Stimuli[i]['sentiment'],
        'Correct': correct, 
        'Reaction_time': reaction_time
        }, ignore_index=True)
    
    # show blank screen
    stimulus = visual.TextStim(win, '')
    stimulus.draw()
    win.flip()
    core.wait(0.5)


print(STROOP_DATA)

logfile_name = 'logfile_{}_{}.csv'.format(ID[0],date)
STROOP_DATA.to_csv(logfile_name)

core.wait (1)
msg(outro)
core.quit()
