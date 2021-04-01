# Intro to Run-of-River Hydropower

## Preamble

In 2016 I began teaching *EENG 8222: Run-of-River Hydropower* at BCIT.  Each year I asked students for feedback on the course, and what they find most engaging about their other courses.  The response is generally that students want to work on problems that resemble the day-to-day processes and problems common in industry.  <s>So we spent 12 weeks learning how to format datetime columns in Microsoft Excel.</s>  In response, I set out to create a series of modules adapted from my fourteen years of professional experience in the hydropower industry.  

```{figure} img/sierra_leone.JPG
---
width: 800px
name: Sierra Leone Hydropower
---
Hydropower Resource Study in Sierra Leone, 2010.  
```

There's too much to cover in two sessions, so I've picked a few exercises from my EENG 8222 curriculum to try and incorporate some activities and interaction.  Your feedback is welcome, and participation is encouraged!  

## Topics Covered

### Outline for Thursday, March 25th

| Time | Duration | Topic |
|---|---|---|
| 2:30 | 10 min | Introduction, Overview |
| 2:40 | 15 min | Anatomy of a Run-of-River Facility |
| 2:55 | 35 min | Hydropower in Context of Global Energy Supply and Demand |
| 3:30 | 10 min | break |
| 3:40 | 30 min | Energy Problems: Thought Experiment in Exponential Growth |
| 4:10 | 30 min | Regional, & Local Hydropower Context: Canada & BC |
| 4:40 | 10 min | break |
| 4:50 | 40 min | Hydropower Fundamentals: Problem Set (Excel Exercise) |

### Outline for Thursday, April 1st

| Time | Duration | Topic |
|---|---|---|
| 2:30 | 10 min | Introduction, Overview |
| 2:40 | 30 min | Hydropower Resource Assessment |
| 3:10 | 20 min | Resource ID Exercise: Google Earth |
| 3:30 | 10 min | break |
| 3:40 | 35 min | Hydropower Fundamentals: Power and Energy from Streamflow (Excel Exercise) |
| 4:15 | 25 min | Modern Tools for Data Analysis (Jupyter Notebook intro.) |
| 4:40 | 10 min | break |
| 4:50 | 30 min | Hydropower In BC: Reading & Discussion |

### Water to Wire

There are many communities around BC that are not connected to the grid, instead relying on diesel fuel for electricity supply.  [Click here](https://www.bchydro.com/content/dam/BCHydro/customer-portal/documents/corporate/suppliers/transmission-system/maps/transplt-Default-0001.pdf) for a high-resolution pdf of the figure below.

```{figure} img/bc_transmission.jpg
---
width: 800px
name: BC HydroTransmission Infrastructure in BC
---
BC Hydro Electricity Transmission Infrastructure
```

Project proponents are encouraged to engage with First Nations early in the planning stage, and the Province of BC is legally oblicaed to consult and accomodate First Nations.  Guidelines on the planning and development phases are presented in the [Inter-Agency Guidebook for Project Development](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/natural-resource-use/land-water-use/crown-land/land-use-plans-and-objectives/natural-resource-major-projects/major-projects-office/guidebooks/clean-energy-projects/clean_energy_guidebook.pdf) from the Government of BC.

```{figure} img/fn_names.jpg
---
width: 800px
name: Map of First Nations Territories
---
Map of First Nations Territories [(source)](https://indigenouspeoplesresources.com/products/canada-first-nations-peoples-of-british-columbia-map)
```

### Questions

1. How many factors can you identify that affect whether a river or creek is a potential candidate for a hydropower facility?
2. Considering **regional variability in climate**, can you identify locations (black diamonds on the map above) where small hydro would be more viable?

The aim for these two sessions is to develop some intuition for how much energy can be extracted from a creek, and put this into context of how much energy we produce from other sources and how much we consume.  Hydropower is no magic bullet, but it has been vital to Canada for nearly a century.

### Additional Resources

#### Global Energy Balance

In today's presentation, we use a rough estimate of the amount of energy coming from the sun to earth, or the incident solar radiation.  For a much more detailed explanation of earth's energy balance, see the [NASA Earth Observatory](https://earthobservatory.nasa.gov/features/EnergyBalance).  For a more rigorous estimate of energy demand growth and energy generation potential, see this report from the [Sandia National Laboratory.](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiAwbbV5crvAhXIFjQIHTB1CFMQFjAEegQIGxAD&url=https%3A%2F%2Fwww.sandia.gov%2F~jytsao%2FSolar%2520FAQs.pdf&usg=AOvVaw2sjwL2LNsOKAq86W0B3cO8)

### Current Data Analysis Tools

This presentation uses the [Jupyter Book](https://jupyterbook.org/intro.html) format, which is not widely used in industry, but is being adopted widely in academia.  Jupyter Book is the combination of an interactive programming environment with a calculation file (*"calc file"* or *"work file"*) that can double as a report.  Work files or calc files are the records that engineers are required to keep as proof of their work.  An interactive work file can let a reviewer not only see the assumptions, but step into the calculation and test sensitivity, and build on ideas.  Below is an example of the type of interactivity that I believe reports can greatly benefit from.  In the discussion about the hydropower in BC, a criticism of the industry is the lack of information available to compare the condition of the aquatic ecosystem pre- and post-project.  Jupyter Book reduces the technological barriers to sharing information with a high level of transparency, but it does require some programming skills.


### Introductory Python Resources
Learning programming skills is challenging, but it's equally rewarding.  There are lots of free, high quality learning resources on the web, a few are listed below.

- [Data Insights with Python for Beginners](https://github.com/ladieslearningcode/llc-intro-to-python) (Copyright [Ladies Learning Code](https://www.canadalearningcode.ca/program/ladies-learning-code/) | [CC BY 4.0 license][CC4 license]) 
- [U of T Coders Data Carpentry Workshop](https://github.com/UofTCoders/2018-09-10-utoronto) (Copyright [U of T Coders][UT Coders] / [Software Carpentry][Software Carpentry] | [CC BY 4.0 license][CC4 license])
- [U of T Coders Cartography and Mapping Lesson](https://github.com/UofTCoders/studyGroup/tree/gh-pages/lessons/python/cartography) (Copyright  [U of T Coders][UT Coders] / [Mozilla Science Lab][mozilla] | [Apache License 2.0][Apache 2 license])
- [Python for Ecologists](http://www.datacarpentry.org/python-ecology-lesson/) (Copyright [Software Carpentry][Software Carpentry] | [CC BY 4.0 license][CC4 license])


```{figure} img/interactive_app.gif
---
width: 800px
name: interactive-app
---
Interactive application exploring water level at two locations on the same river.  
```

