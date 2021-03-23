# Intro to Run-of-River Hydropower

## Preamble

In 2016 I began teaching *EENG 8222: Run-of-River Hydropower* at BCIT.  Each year I asked students for feedback on the course, and what they find most engaging about their other courses.  The response is generally that students want to work on problems that resemble the day-to-day processes and problems common in industry.  <s>So we spent 12 weeks learning how to format datetime columns in Microsoft Excel.</s>  In response, I set out to create a series of tasks adapted from my work experience in identifying hydropower resources in various places around the world.  

```{figure} img/sierra_leone.JPG
---
width: 800px
name: Sierra Leone Hydropower
---
Hydropower Resource Study in Sierra Leone, 2010.  
```

Since this topic will be presented online in just two sessions, I've adapted a few exercises from my EENG 8222 curriculum to incorporate more interactivity.  I know some students are working full time, so spending your limited free time watching video lectures is really tough.  I know this because I'm also currently a student. 

## Topics Covered

There are many communities around BC that are not grid connected, typically relying on diesel fuel for electricity supply.  In EENG 8222, small teams of students develop a proposal for a run-of-river hydropower project.  The proposal is built progressively throughout the term as we cover the material.  The aim for the two sessions we have together is to develop some intuition for how much energy can be extracted from a creek, and put this into context of how much energy we actually consume.  

### Thursday, March 25th

| Time | Duration | Topic |
|---|---|---|
| 2:30 | 10 min | Introductions |
| 2:40 | 50 min | Hydropower in Context of Global, Regional, Local Supply and Demand |
| 3:30 | 10 min | break |
| 3:40 | 30 min | Current State of Hydropower In BC: Reading & Discussion |
| 4:10 | 15 min | Anatomy of a run-of-river project |
| 4:25 | 10 min | break |
| 4:35 | 30 min | Hydropower Fundamentals: The Power Equation (Excel exercise) |
| 5:05 | 25 min | Modern Data Analysis Tools (Jupyter Notebook) |


This presentation uses the [Jupyter Book](https://jupyterbook.org/intro.html) format, which is not widely used in industry, but is being adopted widely in academia.  Jupyter Book is the combination of an interactive programming environment with a calculation file (*"calc file"* or *"work file"*) that can double as a report.  Work files or calc files are the records that engineers are required to keep as proof of their work.  An interactive work file can let a reviewer not only see the assumptions, but step into the calculation and test sensitivity, and build on ideas.  Below is an example of the type of interactivity that I believe reports can greatly benefit from.  In the discussion about the hydropower in BC, a criticism of the industry is the lack of information available to compare the condition of the aquatic ecosystem pre- and post-project.  Jupyter Book reduces the technological barriers to sharing information with a high level of transparency, but it does require some programming skills.

```{figure} img/interactive_app.gif
---
width: 800px
name: interactive-app
---
Interactive application exploring water level at two locations on the same river.  
```

