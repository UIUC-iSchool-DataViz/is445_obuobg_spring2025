---
title: Lecture 9.1 - Viz audience
layout: lecture
description: >-
 Considerations of audience
date: 2023-10-17

---

## Last Week

<img src="../week09/images/week09.png">

notes:
reminder of where we are!  

---

## This Week

<img src="images/week10.png">

notes:
this week we will discuss how one has to consider the audience of their visualization - is your audience you? your peers? others?

we'll start linking stuff together more in altair (which we started last week) and streamlit on huggingface


---

## Today

 1. Viz for Self/Peers/Others
 1. Review about final projects
 1. Streamlit and HuggingFace

note:
we'll get to making some apps with streamlit and huggingface!

---

<br />
<br />
<br />

# TOPIC 1: Viz Audience

---

## Three Classes of Visualizations

1. Viz for Self
1. Viz for Experts
1. Viz for the Public

---

## Viz for Self

There are no rules!

<img src="https://media1.giphy.com/media/EJIqwKKY30Dlu/giphy.gif">

notes:
Labels don't matter. Colors don't have to look nice. Interactivity doesn't have to be fast. Here we are just trying to get something on screen that represents the data. Often this is challenge enough.

As the designer, you know what choices you have made, so "elegant design" isn't a huge deal - although don't go too crazy or you could make things more confusing for yourself.  

---

## Viz for Self

<img src="images/walsh.gif" width="700"/>

notes:
This is an example from AJ (the in-person instructor). He uses 3D software like Houdini in his "everyday" life and so this is his software of choice.  Here, he used 3D software to make a 2D plot, and arranged points to look like a bar chart even though they were rendered as individual points - aka a scatter plot.

It just had to work, and we used the most convenient software.

---

## Viz for Self

<img src="images/L25n128TNG_tmp_gas_metallicity_history.png" width="700"/>

notes:
Here are some examples from my work

There are plots of data from a large scale simulation of the universe.  Here, I'm curious about how the average number of elements heavier than helium in our simulation changes over time.

---

## Viz for Self

name of: L25n512TNG_shenplot_STARS_ylimn0p5_bins_largeEu_1e2_nx050_ny050_sn099.png

<img src="images/L25n512TNG_shenplot_STARS_ylimn0p5_bins_largeEu_1e2_nx050_ny050_sn099.png" width="500"/>

notes:
You can even tell from the name of the file (which runs off the page here) that I'm playing with a bunch of things.  For example I'm plotting here stars, but there is no way you'd really get that from the actual plot itself.

These are plots that show an example of how one might "explore" the data - look for relationships.

---

## Viz for Self

Later this became (viz for peers)

<img src="images/L75n1820TNG_eufef07065_allMstar_eucut_massweighted_bigrange_rfracAll_histo.png" width="600"/>

[Paper if you're really curious](https://arxiv.org/pdf/1707.03401.pdf)

notes:
later, that plot became this plot right here which can be thought of as viz-for peers

While its probably not something that you all understand (unless there are some astronomers in our midst) - you can see I'm more careful here about fonts, presentatin, color schemes and actually labeling things


---

## Viz for Self

Let's talk about exploration.

 * What are characteristics of data that would influence how you visualize it?
 * What information do you have that would be visually interesting?
 * What information do you not have that you need to understand the importance of the data?

Example: A banking database where each record is a bank transaction and the fields include date, deposit or withdrawal amount, customer id, and the interest rate of the account.

notes:
some questions you want to be asking while you are exploring your data with the intent to visualize it

in these examples -- what do you think are some interesting things to visualize? what information would a consumer of your viz need to know?

---

## Viz for Self

Let's talk about exploration.

 * What are characteristics of data that would influence how you visualize it?
 * What information do you have that would be visually interesting?
 * What information do you not have that you need to understand the importance of the data?

Example: A spreadsheet of experimental crop growth measurements where each record is a measurement, and the fields include date, plant species, plant id number, number of leaves, plant height, number of internodes, and average leaf length.

notes:
internodes = the number of "generations" of a plant, aka how many branches come off the main stem.

in these examples -- what do you think are some interesting things to visualize? what information would a consumer of your viz need to know?


---

## Viz for Self

Let's talk about exploration.

 * What are characteristics of data that would influence how you visualize it?
 * What information do you have that would be visually interesting?
 * What information do you not have that you need to understand the importance of the data?

Example: A computational simulation of a galaxy where each record is a timestep in the evolution of the 3D grid, and the fields include time, X position, Y position, Z position, gas density, gas temperature, gas metallicity, and number of stars.

notes:
in these examples -- what do you think are some interesting things to visualize? what information would a consumer of your viz need to know?


---

## Viz for Self

What do you want to get out of visualization for yourself?

 * Do you want to find meaning?
 * Do you want to understand how to guide further visualizations?
 * Is the story you want to tell already known to you?
 * What __shortcuts__ can you take?

notes:
shortcut ideas ... subsampling, delete unused fields, use a simpler tool, manually select outliers by hand instead of doing it procedurally

forget labels that others have to figure out

don't worry about color schemee

---

## Viz for Experts

To design a visualization for experts, you need to analyze how they process information.

 * What do they know?
 * What conventions will they assume?
 * Are they able to fill in the blanks of information?

---

## Viz for Experts

<img src="images/sci_tornado.png" width="700"/>

notes:
Here's a series of visualizations made by or for domain experts that AJ just had lying around on his laptop.

What are some things you notice they have in common?

---

## Viz for Experts

<img src="images/sci_canup.png" width="350"/>

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

<img src="images/sci_convection.png" width="700"/>

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

<img src="images/sci_flu.png" width="700"/>

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

<img src="images/sci_genes.png" width="700"/>

notes:
Here's a series of visualizations made by or for domain experts that I just had lying around on my laptop.

What are some things you notice they have in common?

---

## Viz for Experts

Experts often want to interrogate the data themselves.

How can they do that?
 * Linked Dashboards
 * Side-by-side comparison plots
 * Text annotation with specific values listed
 * Color bar annotation

notes:
ask students - other ideas? what about interactivity? (Interactivity needs to be decent)

---

## Viz for Experts

Experts are looking to isolate variables to make scientific conclusions.

How can we make visualizations more analytical?
 * Reduce the dimensionality of the image (slices)
 * Viewpoint from "outside the box"
 * Extremely high contrast color choices (or highlight different features)

notes:
ask students - other ideas? What about animated data?

---

## Viz for the Public

This is what you're most accustomed to, because usually YOU are the public.

<img src="images/basedonatruestory.jpg" width="700"/>

notes:
Who here is an expert on the historical accuracy of movies? Do you think this visualization was created for those experts? Or was it created for you? How can you tell?

---

## Jargon

Definition: Special words or expressions that are used by a particular profession or group and are difficult for others to understand.

<img src="images/hurricane.jpg" width="400"/>

notes:
When working with experts on their data, they will often try to use words that are specific to their field. As a data communicator, it's your job to decipher that jargon and make it more approachable to the public.

---

## Jargon

<img src="images/upgoerfive.png" width="600"/>

[xkcd.com/1133](https://xkcd.com/1133/)

notes:
This XKCD webcomic makes fun of how much jargon scientists use. He tries to explain NASA's Saturn V rocket using only the 1000 most common words in the English language. 

He actually wrote a whole book about science this way called "Thing Explainer."

---

## Jargon

[Simple Writer](https://xkcd.com/simplewriter/)

notes:
And here's a neat tool he created to help you write your own!

Before:
"The Advanced Visualization Lab creates cinematic treatments of supercomputer data for immersive displays."

After:
"The very good picture making team creates movies of huge computer information for screens you can be inside of."

---

## Storytelling

Let's just get it out there: humans don't respond to data. They respond to stories.

Which of these do you care about more?
 * Global average atmospheric carbon dioxide is 405 ppm.
 * Polar bears are dying because the ice they use to hunt is melting.

notes:
In visualization, we really want to tell a story, not just a list of facts.

**plug for data storytelling class!**

---

## Storytelling

Why is that?

<img src="images/storytelling.jpg"> <!-- width="1000"/>-->

notes:
Emotional response to storytelling is an evolutionary trait humans developed to form stronger social bonds and learn from each other's experience.

---

## Storytelling

<iframe width="1024" height="576" src="https://www.youtube-nocookie.com/embed/r4k6Gm4tlXw?si=yX3Z66_h1aYZF04d?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

notes:
play to ~2:43

---

## Storytelling

Freytag's Pyramid

<img src="images/freytag.png" width="700"/>

notes:
A story needs setup, conflict, and resolution. One thing many novice storytellers forget is to have a resolution or ending. You need to wrap it up in a neat package!

aside - "denouement" is one of my favorite words

---

## Storytelling

Characters and Conflict
 * People as subjects: Two political candidates are battling for office
 * People as researchers: Dr. Smith is trying to cure cancer
 * Objects as characters: The photons are trying to push their way to the sun's surface

notes:
each story is going to have different sorts of characters and different kinds of conflicts

here are a few examples - you can even make scientific data into a story!  Don't you really want to root for the photons to make it out of the sun?

---

## Know your Audience

<iframe width="853" height="480" src="https://www.youtube.com/embed/opqIa5Jiwuw?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

notes:
so, we won't watch this whole thing, but it is worth checking out how the jargon/language changes when he's talking to different groups of folks

---

## Know your Audience

What do you know about them?
 * Age
 * Nationality
 * Occupation
 * Affiliation with a Special Interest / Organization
 * Or is it literally EVERYBODY (web publishing)

notes:
You can hone your narrative for certain audiences. If it's the broadest audience, like for journalism shared online, you need to keep in mind that there will be children, grandparents, experts, politicians, people with money, etc all in the audience.

---

## Visualization for the Public

Images can be more powerful than words, text, and numbers. Images can tell stories.

<img src="images/mlkjr.jpg" width="700"/>

notes:
What can you say about this event given the picture? How is this different from an average day on the National Mall in DC?

What is the story of this photograph?

notice that you need the CONTEXT of US history to "get" this story however

---

## Visualization for the Public

Context is vital for the public.
 * Embed multiple datasets
 * Place something familiar to relate to the unfamiliar
 * Smooth transitions so you can see where you've come from and where you're going to

notes:
This is different from a visualization for Experts where you usually want to isolate the dataset.

With experts, you can asssume some background of understanding.  You might start a presentation or paper with a background summary, but based on the field you don't have to explain as much.  For example, if I'm giving a astronomy talk, I can assume folks know the difference between newtonian gravity and general relativistc treatments and roughly when each apply (GR for going fast, or near big things).

---

## Visualization for the Public

Context is vital for the public.

<img src="images/canup.gif" width="600"/>

notes:
The AVL created this sequence for a movie, which originally moved much slower on a large screen, and had a narrator explaining the sequence. Someone recaptured it and made it into a gif, sharing it on reddit with the caption "A simulation of the Earth's moon being formed."

What context might have been lost?

How well does the imagery speak for itself?

---

## Visualization for the Public

Identifying the narrative
 * Do you first find data, or first find a story?
 * What is the difference between the data narrative and a narrative for the public?

notes:
In visualization for the public, typically we will start with a dataset, and then build a narrative around it, and seek out more data to build context.

Data narrative = what the data collector is researching

Public narrative = what makes an interesting story and provides context

This is different than viz for experts where you are typically talking about the dataset you have been working with specifically.

---

## Visualization for the Public

 1. Aesthetics Matter
 1. Interactivity should not have any lag or latency
 1. Relative values are often more important than specific values
 1. Limit the amount of text/reading
 1. Limit the amount of information being packed in

---

## Visualization for the Public

 * [Election Forecast - fivethirtyeight](https://projects.fivethirtyeight.com/2018-midterm-election-forecast/senate/)
 * [Online Dating - okCupid](https://theblog.okcupid.com/exactly-what-to-say-in-a-first-message-2bf680806c72)
 * [DiCaprio Love Life - reddit](https://www.reddit.com/r/dataisbeautiful/comments/azjti7/leonardo_dicaprio_refuses_to_date_a_woman_over_25/)

notes:
What are the narratives of these visualizations? How are they different than just a list of facts?

