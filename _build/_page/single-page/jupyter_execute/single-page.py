# Homework 2: Compass operator results
*** 
**Subject:** Digital Image processing, FCSE 2021 <br> 
**Student:** Kiril Zelenkovski <br> 
**Deadline:** Tuesday, 22 April 2021 <br> 

## 📗 Assigment 

Implement **Compass operator** for edge detection. 
- Calculate and display result of each filter (*Figure 1*) 
- Calculate and display result from combination of all filters (*Figure 2*) 
- Tested on different values for threshold (*Figure 3*)

<br>

<details><summary> <b>📈 Browse figures</b> </font> </summary><br>
Coresponding figures with solutions and their path: <br> 
<t><t>  &#8594; <u><b>Figure 1:</b></u> <code>../.figures/fig1_filter_images_direction.html</code> <br>
<t><t>  &#8594; <u><b>Figure 2:</b></u> <code>../.figures/fig2_original_adaptive.html</code> <br> 
<t><t>  &#8594; <u><b>Figure 3:</b></u> <code>../.figures/fig3_threshold_slider.html</code> <br>
    
---
**Note:** 

You can load figures (which are html) located in <code>.figures</code> folder with browser without running the code. Plotly has its own *JavaScript* and the functionallity is not lost if you don't run the code. 
    
---
</details>
    
<details><summary> <b>💻 Execute locally</b> </font> </summary><br>

The required packages can be installed using pip:

```Bash
pip install -r requirements.txt
```

---
**Note:**

You can either tun the Python script or the Jupyter notebook to get the results. 

Python dependencies are: 
- <code>numpy</code>==1.18.5  
- <code>opencv-python</code>==4.5.1.48  
- <code>plotly</code>==4.11.0

---
</details>



## Solutions 

### Figure 1

```{admonition} 📊 Fig1. 
Calculating the result of each filter in all possible directions "North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West". After we implement each filter we apply it to the <code>"Barbara.tif</code> image and the result is displayed using the **Plotly** Updatemenus plot. You can navigate which output you desire by selecting an option from the dropdown menu.

The result is all filtered images based on different filter direction.
```

from IPython.core.display import display, HTML
display(HTML('.figures/fig1_filter_images_direction.html'))

### Figure 2

```{admonition} 📊 Fig2. 
In this figure we have the original image vs the image with the the Edge total (no applied threshold) and we have the Image with applied Adaptive Threshold. The idea is to comapre all the 3 outputs before we play around with the threshold value.The result is displayed using the **Plotly** Updatemenus plot. You can navigate which output you desire by selecting an option from the dropdown menu.
```

from IPython.core.display import display, HTML
display(HTML('.figures/fig2_original_adaptive.html'))

### Figure 3

```{admonition} 📊 Fig3.  
This figure uses a slider from the **Plotly** library for better comparison of result that different threshold values give. 

The resulting image can be modified by sliding through the range of the slider and the displayed image is the one with applied threshold value.  
```

from IPython.core.display import display, HTML
display(HTML('.figures/fig3_threshold_slider.html'))