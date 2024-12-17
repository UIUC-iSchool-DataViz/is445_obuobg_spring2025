---
layout: week
visible: true
icon: undraw_playing_fetch_cm19.svg
notitle: true
examples:
  - filename: In Class Streamlit Files
    type: iodide
    title: In class Streamlit materials, Week 13
    description: Updating storage of Streamlit files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2024/tree/master/week13/inClassStreamlit
  - filename: Prep Streamlit Files
    type: iodide
    title: Prep Streamlit materials, Week 13
    description: Updating storage of Streamlit files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2024/tree/master/week13/prepStreamlit
  - filename: In Class Jekyll Files
    type: iodide
    title: In class Jekyll materials, Week 13
    description: Updating storage of Jekyll files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2024/tree/master/week13/inClassJekyll
  - filename: prepJekyll
    type: iodide
    title: Prep Jekyll Files, Week 12
    description: In class notebook
    link: https://github.com/UIUC-iSchool-DataViz/is445_bcubcg_fall2024/tree/main/week13/prepJekyll
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset (online)
    description: A dataset of USA "mobility" which (I <b>think</b> comes from a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">a large census study from 1989-2015</a>) and is collected in several places <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">including right here</a>.  Here "mobility" is refering to how easy it is for a person to move up in economic status (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info can be found here</a>) based on factors like parental income, location, race, etc.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
  - filename: building_inventory.csv
    type: dataLink
    title: Buildings dataset
    description: Illinois buildings dataset
    link: https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/building_inventory.csv
  - filename: corgs_per_country_over_time_columns_2020.csv
    type: dataLink
    title: Corgis per country over time 
    description: This dataset is from the <a href="http://cardiped.net/">Cardigan Archives</a> and <a href="https://github.com/UIUC-iSchool-DataViz/spring2020/blob/master/week12/corg/grabCorgData_subpages.py">scraped using Beautiful Soup in Python</a> and <a href="https://github.com/UIUC-iSchool-DataViz/spring2020/blob/master/week12/corg/calc_corgData.ipynb">further processed in Python</a> into this form.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/corgs_per_country_over_time_columns_2020.csv

---

# Intro to SciViz & More with Streamlit/Jekyll

We do a few more things with Streamlit and Jekyll.


We talk a little bit about 3D graphics and how it relates to Scientific Visualization, and carry on with Streamlit/Jekyll and add in some Altair in Python.

Also, here is a slightly more in-depth explanation of path/ray tracing:

<iframe width="560" height="315" src="https://www.youtube.com/embed/frLwRLS_ZR0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Extra files

Full corgi dataset available [here](corg/corgiData_countries_full_2020.json).



## Optional reading list

1. <a href="https://streamlit.io/">Streamlit docs</a>
2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a> with a focus on <a href="https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app">Multi-page apps</a>
3. <a href="https://medium.com/@imanuelyosi/deploy-your-streamlit-web-app-using-hugging-face-7b9cddb11148">This blog post for a walkthrough of deploying a Streamlit space on HuggingFace</a>
4. <a href="https://books.google.com/books?hl=en&lr=&id=jUw7DwAAQBAJ&oi=fnd&pg=PA91&dq=scientific+visualization+misinformation&ots=Cv0QmoCdM2&sig=7xycURu8Um_C9VtHqf-aWg4qaEo#v=onepage&q=scientific%20visualization%20misinformation&f=false">Chapter 5: Dimensions of Visual Misinformation in the Emerging Media Landscape in the book "Misinformation and Mass Audiences"</a> 
