# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import webbrowser
import numpy 
import os
import matplotlib.pyplot as plt
from tkinter import ttk
from PIL import ImageTk, Image

# this allows for the image (brain.png) to be accessed from current directory
# makes it easier to load images

os.chdir(os.path.dirname(sys.argv[0]))

 
 # THE WINDOW PSEUDOCODE REFERS TO LINE 23 to LINE 362 (they are essentially the same displays, but with different information for the different parts of the brain)      
 # these windows are what appears when the user clicks the corresponding buttons
 # these windows contain pertinent information for each section
 # these windows include labels, on which the text can be displayed
                   
def second_window():
    window=Tk()
    window.title("Temporal Lobe")
    window.geometry('500x500')
    window.configure(bg='grey')
    label00=Label(window, text="TEMPORAL LOBE"
    ,wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 36)).place(x=47,y=10)
    label0=Label(window, text="LOCATION: Bottom middle part of cortex"
    ", right behind the temples", relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Responsible for processing"
     " auditory information from the ears", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: Focused on hearing, selective"
    " listening. Receives sensory information from ears. Discerns various"
    " sounds and pitches.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=280)
    label3=Label(window, text="DISORDERS: Pick's Disease (caused by atrophy),"
    " temporal lobe epilepsy, schizophrenia", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=400)
    label4=Label(window, text="Source:https://brainmadesimple.com/temporal-lobe/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=470)
    label5=Label(window, text="Source:https://en.wikipedia.org/wiki/Temporal_lobe#Disorders", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=485)
    
    
#Cerebellum
def third_window():
    window=Tk()
    window.title("Cerebellum")
    window.geometry('500x500')
    window.configure(bg='grey')
    label00=Label(window, text="CEREBELLUM",
    relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 36)).place(x=90,y=10)
    label0=Label(window, text="LOCATION: Directly on top of the spinal cord"
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Responsible for control of balance and posture"
     ", voluntary movements, motor learning and cognitive functions."
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: One of the oldest parts of the vertebrate brain"
    ", made up of 3 lobes (flocculonodular, posterior, anterior), contains over 50 percent"
    " of all brain neurons.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=280)
    label3=Label(window, text="DISORDERS: Pick's Disease (caused by atrophy),"
    " temporal lobe epilepsy, schizophrenia", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=400)
    label4=Label(window, text="Source:https://brainmadesimple.com/temporal-lobe/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=485)
    
#Lateral Sulcus 
def fourth_window():
    window=Tk()
    window.title("Lateral sulcus")
    window.geometry('500x500')
    window.configure(bg='grey')
    label00=Label(window, text="LATERAL SULCUS",
    relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 36)).place(x=45,y=10)
    label0=Label(window, text="LOCATION: Inferior surface of the brain; close to"
    " anterior perforated substance; most visible on lateral surface. Found in both"
    " hemispheres of the brain."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=4,y=90)
    label1=Label(window, text="FUNCTION: Separates the frontal and parietal lobes from the"
    " temporal lobe. Houses the insular cortex." 
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=6,y=180)
    label2=Label(window, text="OVERVIEW: One of the earliest developing sulci (brain groove);"
    " contains many side branches." , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=260)
    label3=Label(window, text="DISORDER: Perisylvian syndrome (rare neurological disease;"
    " symptoms include difficulty chewing, swallowing, low muscle tone, epilepsy, learning"
    " disorders.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=330)
    label4=Label(window, text="Source:https://www.sciencedirect.com/topics/neuroscience/lateral-sulcus"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=483)
    label5=Label(window, text="Source:https://psychology.wikia.org/wiki/Sylvian_fissure"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=470)
    label6=Label(window, text="Source:https://en.wikipedia.org/wiki/Lateral_sulcus"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=457)
    label7=Label(window, text="Source:https://en.wikipedia.org/wiki/Perisylvian_syndrome"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=444)

    
#Frontal Lobe
def fifth_window():
    global window
    window=Tk()
    window.title("Frontal Lobe")
    window.geometry('500x680')
    window.configure(bg='grey')
    label00=Label(window, text="FRONTAL LOBE",
    relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 36)).place(x=70,y=10)
    label0=Label(window, text="LOCATION: Part of the cerebral cortex; near the front of the head,"
    " under the frontal skull bones and near the forehead. Divided into two: left and right side."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Controls important cognitive skills in humans, such as"
    " emotional expression, problem solving, memory, language, judgement,etc. 'Control panel' of"
    " our personality and our ability to communicate. Also responsible for primary motor function."
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: Largest of the four major lobes. Located at the front of"
    " each hemisphere. Contains most dopamine neurons in the cerebral cortex. Found in"
    " all mammal; last region of the brain to evolve.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=320)
    label3=Label(window, text="DISORDERS: Most common place for brain injury to occur. Damage can"
    " cause personality changes, limited facial expressions, and difficulty in the interpretation of"
    " information. Causes of damage include strokes, traumatic brain injuries, Alzheimers,"
    " Parkinsons, and frontal lobe epilepsy.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=440)
    label4=Label(window, text="Source: https://www.medicalnewstoday.com/articles/318139#What-is-the-frontal-lobe"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=634)
    label5=Label(window, text="Source: https://www.healthline.com/human-body-maps/frontal-lobe#1"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=648)
    label6=Label(window, text="Source: https://en.wikipedia.org/wiki/Frontal_lobe#Damage"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=662)

#Precentral Gyrus
def sixth_window():
    #global window
    #window.destroy()
    window=Tk()
    window.title("Precentral gyrus")
    window.geometry('500x500')
    window.configure(bg='grey')
    label00=Label(window, text="PRECENTRAL GYRUS",
    relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 36)).place(x=8,y=10)
    label0=Label(window, text="LOCATION: diagonally oriented;situated in the posterior portion"
    " of the frontal lobe. Immediately anterior to the central sulcus."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: involved in executing voluntary motor movements. "
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: Prominent gyrus (ridge on the cerebral cortex; internal"
    " layer contains large pyramidal neurons called Betz cells, which send axons to motor neurons/cranial nerves."
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=260)
    label3=Label(window, text="DISORDERS: Paralysis/palsy; caused by lesions of the precentral gyrus; primarily affects"
    " the contralateral (opposite to the structure) side of the body.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=370)
    label4=Label(window, text="Source: https://radiopaedia.org/articles/precentral-gyrus?lang=us", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=10,y=472)
    label4=Label(window, text="Source: https://en.wikipedia.org/wiki/Precentral_gyrus", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=10,y=485)


#Central sulcus
def seventh_window():
    window=Tk()
    window.title("Central sulcus")
    window.geometry('500x525')
    window.configure(bg='grey')
    label00=Label(window, text="CENTRAL SULCUS",
    relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 36)).place(x=43,y=10)
    label0=Label(window, text="LOCATION: Runs down the middle of the lateral surface of the brain,"
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Separates the frontal lobe from the parietal lobe. "
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: Prominent landmark of the brain; fold in the cerebral cortex"
    " in the brains of vertebrates", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=280)
    label3=Label(window, text="DISORDERS: Abnormal surface morphology has been found in the central"
    " sulci of children with attention defecit/hyperactivity disorder (ADHD).", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=385)
    label4=Label(window, text="Source: https://www.neuroscientificallychallenged.com/glossary/central-sulcus"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=504)
    label5=Label(window, text="Source: https://en.wikipedia.org/wiki/Central_sulcus", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=490)
    label6=Label(window, text="Source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4551868/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=475)

#Postcentral gyrus
def eighth_window():
    window=Tk()
    window.title("Postcentral gyrus")
    window.geometry('500x590')
    window.configure(bg='grey')
    label00=Label(window, text="POSTCENTRAL GYRUS",
    relief="solid",wraplength=0,borderwidth=0,
    bg="grey", font=("Times New Roman", 34)).place(x=8,y=10)
    label0=Label(window, text="LOCATION: Lies in the parietal lobe, posterior to"
    " the central sulcus."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Location of the primary somatosensory cortex,"
    " the main sensory receptive area for the sense of touch."
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: Prominent structure in parietal lobe. Initially"
    " defined from surface stimulation studies of Wilder Penfield. Location contains map of"
    " sensory space called homunculus.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=280)
    label3=Label(window, text="DISORDERS: Damage may lead to  loss of proprioception (perception"
    " or awareness of bodily position, movement), astereognosis (inability to identify objects"
    " via active touch), and loss of vibratory sense. Extent and location of damage depends on"
    " specific location of injury.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=400)
    label4=Label(window, text="Source: https://radiopaedia.org/articles/postcentral-gyrus?lang=us"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=530)
    label5=Label(window, text="Source: https://www.sciencedirect.com/topics/neuroscience/postcentral-gyrus"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=545)
    label6=Label(window, text="Source: https://psychology.wikia.org/wiki/Postcentral_gyrus"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=560)
    label7=Label(window, text="Source: https://www.imaios.com/en/e-Anatomy/Anatomical-Parts/Postcentral-gyrus"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=575)

#Parietal lobe
def ninth_window():
    window=Tk()
    window.title("Parietal lobe")
    window.geometry('500x700')
    window.configure(bg='grey')
    label00=Label(window, text="PARIETAL LOBE",
    relief="solid",wraplength=0,borderwidth=0,
    bg="grey", font=("Times New Roman", 34)).place(x=72,y=10)
    label0=Label(window, text="LOCATION: Part of cerebral cortex; lies between the occipital"
    " and frontal lobes (above temporal lobe). Upper, back part of cortex."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Five major functions: analysis of somatic sensation (touch,"
    " limb position, temperature), space analysis, motor system targeting, generation of attention,"
    " and analysis of visual motion."
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=180)
    label2=Label(window, text="OVERVIEW: Part of cortex; carries out extremely specific"
    " functions. Required to process information in seconds.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=280)
    label3=Label(window, text="DISORDERS: Impairment causes a failure to interpret stimulus; reception"
    " still possible. Damage results in abnormalities in body image and spatial relations. Damage to left"
    " parietal lobe can affect verbal memory and ability to recall digits. Can result in 'Gertsmann's Syndrome'."
    "Includes right-left confusion, agraphia (difficulty writing), acalculia (difficulty with mathematics),"
    " aphasia (difficulty with language), and more. Difficulty to the right parietal lobe affects non-verbal memory."
    " Can impair self-care skills; makes it harder to construct and draw. Damage to both sides can cause"
    " 'Balint's Syndrome', a visual attention and motor syndrome. Inability to control gaze, reach, etc."
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=360)
    label4=Label(window, text="Source: https://www.sciencedirect.com/topics/neuroscience/parietal-lobe"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=650)
    label5=Label(window, text="Source: https://brainmadesimple.com/parietal-lobe/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=665)
    label6=Label(window, text="Source: https://www.neuroskills.com/brain-injury/parietal-lobes/"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=680)
    
#Occipital lobe
def tenth_window():
    window=Tk()
    window.title("Occipital lobe")
    window.geometry('500x515')
    window.configure(bg='grey')
    label00=Label(window, text="OCCIPITAL LOBE",
    relief="solid",wraplength=0,borderwidth=0,
    bg="grey", font=("Times New Roman", 34)).place(x=72,y=10)
    label0=Label(window, text="LOCATION: Encompasses the posterior portion of the human cerebral"
    " cortex. Surface area is approximately twelve percent of total surface area of the neocortex"
    " (part of brain involved in higher-order brain functions such as sensory perception and cognition)."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Primarily responsible for vision."
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=230)
    label2=Label(window, text="OVERVIEW: Integral in visual information process; need to be very fast"
    " to process the rapid information from the eyes.", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=280)
    label3=Label(window, text="DISORDERS: Impairment results in visual confusion; complete or partial blindness,"
    " or visual agnosia (impairment in recognition of visually presented objects)", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=370)
    label4=Label(window, text="Source: https://brainmadesimple.com/occipital-lobe/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=450)
    label5=Label(window, text="Source: https://www.sciencedirect.com/topics/neuroscience/occipital-lobe"
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=465)
    label6=Label(window, text="Source: https://en.wikipedia.org/wiki/Neocortex", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=480)
    label7=Label(window, text="Source: https://en.wikipedia.org/wiki/Visual_agnosia", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=495)
    
#Pons
def eleventh_window():
    window=Tk()
    window.title("Pons")
    window.geometry('500x780')
    window.configure(bg='grey')
    label00=Label(window, text="PONS",
    relief="solid",wraplength=0,borderwidth=0,
    bg="grey", font=("Times New Roman", 34)).place(x=200,y=10)
    label0=Label(window, text="LOCATION: Found in the hindbrain, the lowest region of"
    " the brain. Located above the medulla, and below the midbrain. Anterior part of the"
    " posterior cranial fossa."
    , relief="solid",wraplength=500,borderwidth=0,
    bg="grey", font=("Times New Roman", 16)).place(x=10,y=90)
    label1=Label(window, text="FUNCTION: Latin for 'bridge', connects the two hemispheres"
    " of the cerebrum and connects cerebral cortex to medulla oblongata. Vital to central"
    " and peripheral nervous system. Also involved in autonomic/sensory functions such as"
    " arousal, respiration, fine motor control, Circadian Cycle (sleep cycle)."
     , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=10,y=200)
    label2=Label(window, text="OVERVIEW: Largest part of brainstem. Group of nerves that"
    " serves as a connection between cerebrum and cerebellum. All nervous system information"
    " passes through the pons at some point."
    , relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=380)
    label3=Label(window, text="DISORDER: Central Pontine Myelinolysis (neurological disorder"
    " in which the myelin, a covering that protects pontine nerve cells, is being destroyed."
    " Generally occurs as result of other illness. No cure; may lead to permanent nerve damage."
    " Symptoms include muscle weakness, tremors, slowed speech, mental confusion/hallucinations"
    " , intellectual impairment. Most common cause is a rapid increase in blood sodium levels."
    " Reason for damage unclear at this time. Alcoholism and malnutrition increase CPM risk." ,
    relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 16)).place(x=4,y=500)
    label4=Label(window, text="Source:https://brainmadesimple.com/pons/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=765)
    label5=Label(window, text="Source:https://teachmeanatomy.info/neuroanatomy/brainstem/pons/", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=750)
    label6=Label(window, text="Source:https://www.healthline.com/health/central-pontine-myelinolysis#causes", relief="solid",wraplength=500,
    borderwidth=0, bg="grey", font=("Times New Roman", 8)).place(x=4,y=735)

# This information is the structural background for the frame   
root = Tk()
root.geometry('2400x2400')
root.title ('Brain Map')
frame=Frame(root)
frame.pack()

# Code for dropdown menu for links to external information. 
menu = Menu(root)
root.config(menu=menu)

# These are the urls that, when clicked, will open up a browser revealing information about the brain
def openUrl1():
    webbrowser.open_new(url1)
url1 = ('https://academic.oup.com/brain')

Menu1 = Menu(menu)
menu.add_cascade(label="Oxford ~ BRAIN: Journal of Neurology", menu=Menu1)
Menu1.add_command(label="Read", command=openUrl1)
Menu1.config(fg='black')

def openUrl2():
    webbrowser.open_new(url2)
url2 = ('https://www.ninds.nih.gov/Disorders/Patient-Caregiver-Education/Hope-Through-Research/Traumatic-Brain-Injury-Hope-Through')

Menu2 = Menu(menu)
menu.add_cascade(label="National Institute of Neurological Disorders and Stroke: Traumatic Brain Injury", menu=Menu2)
Menu2.add_command(label="Read", command=openUrl2)



# These values are the coordinates for the curved lines that distinguish between parts of the brain (I acquired these values through trial and error).
x1=1104
y1=476
x2=1014
y2=565
x3=995
y3=660
x4=1162
y4=670
x5=1033
y5=566
x6=819
y6=400
x7=635
y7=601
x8=720
y8=265
x9=683
y9=445
x10=712
y10=536
x11=957
y11=295
x12=892
y12=408
x13=901
y13=500
x14=849
y14=255
x15=813
y15=388
x16=817
y16=495

#These are the configurations for the canvas including aspects such as color, placement, and text.
canvas = Canvas(root, width = 2400, height = 2400, background='dark slate gray')
canvas.place(x=0, y=0)
#This allows for the canvas to be opened up to a zoomed state.
root.state('zoomed')
canvas.create_text(800, 100, text = 'The Human Brain Map', font = ('Times New Roman', 70), justify = 'right', fill='Gainsboro')
canvas.create_text(800, 950, text = 'Vishnu Vijayakumar 2020', fill='Gainsboro', font = ('Times New Roman', 12, 'bold'))
canvas.create_line(782,781,847,683,fill ='black',width=1.5)

#These buttons are bound to the windows that contain the information. When clicked, the corresponding window will appear.
button3=Button(root, text="KILL", fg="Red",bg='Khaki', command=root.quit) # closes entire program
button3.place(x=1760, y=800)
button3.config(height=10, width=15)
button4 = Button(root,text="Temporal Lobe", wraplength=60, bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=second_window)
button4.place(x=810, y=570)
button5 = Button(root, wraplength= 60, text="Cerebellum", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=third_window)
button5.place(x=920, y=680)
button7 = Button(root, wraplength= 60, text="Pons", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=eleventh_window)
button7.place(x=780, y=760)
button8 = Button(root, wraplength= 60, text="Occipital lobe", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=tenth_window)
button8.place(x=1035, y=580)
button9 = Button(root, wraplength= 60, text="Parietal lobe", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=ninth_window)
button9.place(x=979, y=435)
button9 = Button(root, wraplength= 60, text="Postcentral gyrus", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=eighth_window)
button9.place(x=839, y=330)
button9 = Button(root, wraplength= 60, text="Central sulcus", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=seventh_window)
button9.place(x=795, y=410)
button10 = Button(root, wraplength= 60, text="Frontal lobe", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=fifth_window)
button10.place(x=583, y=410)
button11 = Button(root, wraplength= 60, text="Lateral sulcus", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=fourth_window)
button11.place(x=363, y=517)
button10 = Button(root, wraplength= 60, text="Precentral gyrus", bg='LightPink4', fg='ghost white',font=('Times New Roman', 10), borderwidth=1, command=sixth_window)
button10.place(x=732, y=340)

#This section is where the aforementioned coordinates are used to create the lines that distinguish the parts of the brain.

#image = ImageTk.PhotoImage(file="C:\\Users\Vishnu Vijayakumar\\Documents\\pythonproject\\brainimage.png")
image = ImageTk.PhotoImage(file="The Brain Image.png")
canvas.create_image(800,500, image=image)  # Image was resized after import to increase size; to make it easier for user to see/interact
canvas.create_line(x1,y1,x2,y2,x3,y3, smooth="true", fill="black", width=2)
canvas.create_line(x1,y1,x4,y4,x3,y3, smooth="true", fill="black", width=2)
canvas.create_line(x5,y5,x6,y6,x7,y7, smooth="true", fill="black", width=2)
canvas.create_line(x8,y8,x9,y9,x10,y10, smooth="true", fill="black", width=2)
canvas.create_line(x11,y11,x12,y12,x13,y13, smooth="true", fill="black", width=2)
canvas.create_line(x14,y14,x15,y15,x16,y16, smooth="true", fill="black", width=2)
canvas.create_line(408,542,712,533,fill ='black',width=1.5)


# This block of code was implemented to track the coordinates of the mouse. Originally inteneded to be incorporated as a feature of the project,
# this is now obsolete but has been maintained in this state for the purposes of documentation
#cursormotioncoordinatetracker
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x,y))
root.bind('<Motion>', motion)

# For display
canvas.pack()
root.mainloop()
root.destroy()
