---
layout: week
visible: true
icon: undraw_Books_l33t.svg
notitle: true
examples:
  - filename: prepMaterials
    type: iodide
    title: Prep Streamlit App Files, Week 12
    description: In class notebook
    link: https://github.com/UIUC-iSchool-DataViz/is445_obuobg_spring2025/tree/main/week12/prepMaterials
  - filename: InClass
    type: iodide
    title: In class Streamlit App, Week 12
    description: Updating storage of Streamlit files in class
    link: https://github.com/UIUC-iSchool-DataViz/is445_obuobg_spring2025/tree/master/week12/inClass
data:
  - filename: mobility.csv
    type: dataLink
    title: The Mobility dataset (online)
    description: A dataset of USA "mobility" which (I <b>think</b> comes from a <a href="https://www.census.gov/library/working-papers/2018/adrm/CES-WP-18-40R.html">a large census study from 1989-2015</a>) and is collected in several places <a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/mobility.csv">including right here</a>.  Here "mobility" is refering to how easy it is for a person to move up in economic status (<a href="http://www.stat.cmu.edu/~cshalizi/uADA/15/hw/01/hw-01.pdf">more info can be found here</a>) based on factors like parental income, location, race, etc.
    link: https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/mobility.csv
---

# Web dev with Streamlit + HuggingFace

Today we'll cover a brief intro of [Streamlit](https://streamlit.io/) on [HuggingFace Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-streamlit)and web development in general.

 
## Extra files


Full corgi dataset available [here](corg/corgiData_countries_full_2020.json).



## Optional reading list

 1. <a href="https://streamlit.io/">Streamlit docs</a>
 2. <a href="https://huggingface.co/docs/hub/en/spaces-sdks-streamlit">Streamlit on HuggingFace</a>
 3. <a href="https://altair-viz.github.io/gallery/index.html">Altair Docs</a> - in particular <a href="https://altair-viz.github.io/user_guide/data.html#including-index-data">Including Indexes</a>, <a href="https://altair-viz.github.io/altair-tutorial/notebooks/06-Selections.html">Interactivity & Selections</a>, <a href="https://altair-viz.github.io/gallery/multiline_tooltip.html#multi-line-tooltip">Multi-line tooltips</a>, <a href="https://altair-viz.github.io/user_guide/interactions.html#bindings-selections-conditions-making-charts-interactive">Interactive Binning</a>, <a href="https://altair-viz.github.io/user_guide/transform/filter.html#filter-transform">Filter Transformations</a>
 4. <a href="https://medium.com/@imanuelyosi/deploy-your-streamlit-web-app-using-hugging-face-7b9cddb11148">This blog post for a walkthrough of deploying a Streamlit space on HuggingFace</a>