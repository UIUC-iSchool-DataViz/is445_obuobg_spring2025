---
name: In Class Example
tools: [Python, HTML, vega-lite, Altair]
image: assets/pngs/cars.png
description: In class example.
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---


# In Class Walkthrough

Getting some practice saving Altair/vega-lite json schemas for our Jekyll page.

## Case 1: Saving from vega-lite editor

This I created by going to the [vega-editor](https://vega.github.io/editor) and making sure I used the [vega-datasets](https://github.com/vega/vega-datasets/tree/master/data) direct link to the data and saving with the "Export" from the vega-editor.

<vegachart schema-url="{{ site.baseurl }}/assets/json/from_vega_editor.json" style="width: 100%"></vegachart>


## Case 2: Saving from Altair

### Sub-case 2a: With remotely hosted data

### Sub-case 2b: With data saved from Python






<!-- these are written in a combo of html and liquid --> 

<div class="left">
{% include elements/button.html link="https://github.com/vega/vega/blob/main/docs/data/cars.json" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/jnaiman/online_cv_public/blob/main/python_notebooks/test_generate_plots.ipynb" text="The Analysis" %}
</div>

