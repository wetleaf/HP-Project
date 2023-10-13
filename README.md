<<<<<<< HEAD
# HP-Project
=======
# HP-Project

## Worsksheets 
1. Days of the week Worksheets
2. Phonics Worksheets
3. Telling Time Worksheets
4. Time Worksheet
5. Clock Worksheets
6. Seasons Worksheet
7. Money Worksheets

## Problem

Our task is to produce multiple worskheets on above topics (with or without answers)

##  Idea

### Step 1: Create problems structure

For example: Consider Clock Worksheets

**Prompt BEGIN**

```
Match the following where left side contains the image of digital clock showing some time and whereas right side contains the image of analog clock showing the same time but in different order. And student will be asked to match the respective time.

Create 10 problems on above statement for kids in the above described pattern and whenever there is an image, do produce its description in square brackets

Do Give a Nice Name to these problem statement
```

**Prompt END**

**WORK TO DO:** You have to create such prompt for atleast 10 different problem structure on a worksheet. Remember, we need well descriptive prompt, not the ouput of the prompt. 

**Reference**: Use ChatGPT or LLava (here you can feed images for reference to get better result on ideas and prompt) or any other LLMs to ask for suggestions of different and creative problem structure (or prompt). For Example: " Suggest some creative problems to provide analog clock understanding to pre-schoolers with detailed explanation", etc.

**If You find other references, Do share**

 **Work Division**
 1. Arsh: 
 2. Vishal:
 3. Ratna:
 4. Parth:
 5. Harsh:

### Step 2: Create API call to a LLM model for above prompt

**WORK TO DO:** Need to test some free open-source LLMs which produces well descriptive (including Image Description) and interesting Problems given their structure.
This Step focuses more on hit and trail.

**References**
1. ChatGPT
2. LLama
3. Others will be added as per need

**Work Division**
1. Vishal:
2. Ratna:
3. Parth:
4. Arsh:
5. Harsh:

### Step 3: Extract the image desciption from the generated text and Use a Text_to_Image LLM to produce respective image

**WORK TO DO:** Given image description, we have to generate images. Make sure the description is well structured + should be a simple image (like a clock, ship etc.). Later, we will put it in the pipeline with the text generation LLM.

**References:** Recently we have, Stable diffusion, DALL-e etc. We also got an Python wrapper for text to images generation LLM. (Imagen-pytorch)

Github: https://github.com/lucidrains/imagen-pytorch

Mostly It serves our purpose but require a lot of training.

**Work Division**
1. Vishal:
2. Ratna:
3. Parth:
4. Arsh:
5. Harsh:

### Step 4: Assembling the images with the text

**WORK TO DO:** Now we have problems and their respective images. Our Task is to replace the "[]" Text with Its respective image and respresent it as a form of single img which can be concatenated to pdf

Note: It may require some hard code or manual work since we have to make the problem interactive and creative. We can use GPT4 Plugin to some extent.



Other Useful Links
1. https://github.com/Atomic-man007/Awesome_Multimodel_LLM
2. https://github.com/huggingface/transformers/tree/main/src/transformers/models
   



>>>>>>> 4370696 (TO DO)
