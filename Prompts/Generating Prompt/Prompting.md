# Prompting

## Introduction

Prompting depends on the task. 

For **generation tasks**, the prompt should be a description of the task.

By [$reference^1$](#best-practices), the prompt should contain the following:

- A description of the task
- Instructions for the model
- Formatting instructions
- Examples

## Methodology

Since the project's requirement is to generate a worksheet, we have divided the prompt into two parts:-

- Question type: Using the topic title, LLMs can generate multiple question types. Located in [Prompt Topics.md](Prompt%20Topics.md).
- Question content: Once the type of question is decided, LLMs can now generate multiple questions of that type with different modes, such as fill-in-the-blank, multiple-choice, etc. Located in [Prompt Question.md](Prompt%20Question.md).

For an example, if the topic is "Clocks", then the LLMs can generate a question type such as "Tell Time" and then generate questions of that type.

## Prompt Format

### Part 1: Question Type

**Example prompt for the topic "Money" would be:**

> Arguments:
> ```
> Years: 8 to 9
> Number: 3
> Topic: Money
> Country: India
> ```
> 
> From the topic [Topic], create [Number] question types for students of [Country] aged [Years].
> 
> Instructions:
> 1. Create types of questions, not questions.
> 2. Ensure region-specific words are used, example, in cases of money.
> 3. Ensure the questions types can be answered by students of the given age.
> 4. Ensure the questions have variables that are easily substitutable.
> 
> Desired Format:
> ```
> Title: [Topic]
> Questions: [Number]
> 
> Questions:
> [List of Questions]
> ```
> 
> Example:
> ```
> Title: Clocks
> Number: 5
> 
> Questions:
> 1. Convert from Digital to Analog time.
> 2. Convert from Analog to Digital time.
> 3. Convert from 12-hour to 24-hour time.
> 4. Convert from 24-hour to 12-hour time.
> 5. Calculate the time difference between two times.
> ```

**This prompt would generate question types such as:**

> Title: Money
> Number: 3
> 
> Questions:
> 1. Calculate the total amount when [Amount1] rupees and [Amount2] rupees are added together.
> 2. If you have [Amount1] rupees and spend [SpentAmount] rupees, how much money do you have left?
> 3. You want to buy [Item] that costs [ItemCost] rupees. How much more money do you need if you have [CurrentAmount] rupees?

### Part 2: Question Content

**Example prompt for the topic "Money" and question type "`You want to buy [Item] that costs [ItemCost] rupees. How much more money do you need if you have [CurrentAmount] rupees?`" would be:**
> Create an educational worksheet for students aged [Years] of [Country] on the [Sub-Topic] of [Difficulty] difficulty level with [Number] questions.
> 
> Instructions:
> 1. Do not include space for answers in the worksheet.
> 2. Include the answers at the end of the worksheet. 
> 3. Do not include instructions in the worksheet.
> 4. Include a mix of question formats, for example: multiple-choice, fill-in-the-blank, and short answer.
> 5. If the sub-topic has arguments, subustitute the arguments with numbers for the questions and answers.
> 6. If images need to be included, please include them in the worksheet in brackets, such as [], and write an accurate description within the brackets.
> 
> Desired Format:
> ```
> Title: [Topic]
> Questions: [Number]
> Topic: [Sub-Topic]
> 
> Questions:
> [List of Questions]
> 
> Answers:
> [List of Answers]
> ```
> 
> Arguments:
> ```
> Years: 8 to 9
> Number: 4
> Difficulty: Easy
> Country: India
> Topic: Money
> Sub-Topic: If you have [Amount1] rupees and spend [SpentAmount] rupees, how much money do you have left?
> ```
> 
> Example:
> ```
> Title: Clocks
> Questions: 5
> Topic: Which clock shows the time indicated by the clock in the question?
> 
> Questions:
> 1. Which of the following clocks indicate 12:45?
>     a.[Clock showing 12:45]
>     b.[Clock showing 1:30]
>     c.[Clock showing 2:15]
>     d.[Clock showing 3:00]
> 2. What is the time indicated by the clock [Clock showing 1:30]?
> 
> Answers:
> 1. a
> 2. 1:30
> ```


**This prompt would generate questions such as:**

> Title: Money Math
> Questions: 4
> Topic: Money
> 
> Questions:
> 1. If you have 500 rupees and you spend 150 rupees, how much money do you have left?
> 2. Sarah has 750 rupees, and she wants to buy a toy that costs 450 rupees. How much money will she have left after buying the toy?
> 3. You want to buy a book for 300 rupees, and your friend owes you 100 rupees. How much more money do you need to buy the book?
> 4. If you have 800 rupees, and you save 250 rupees, how much money will you have saved?
> 
> Answers:
> 1. 350 rupees
> 2. 300 rupees
> 3. 200 rupees
> 4. 550 rupees

## Pipeline

The pipeline for generating questions is as follows:

1. Get the topic title, number of questions, difficulty level, age group, and country of the students from the user.
2. Generate the question type response using the topic title.
3. Parse the question type response to get the question type.
4. Generate the question content prompt using the topic title and question type.
5. Parse the question content response to get the questions.

## Limitations

We right now have no access to the OpenAI API(Paid) nor to a workstation GPU, All we can do is to test the prompt and see if it generates the desired output through the web interface.

Due to this, we cannot:
- Test the answers generated by the GPT LLMs. All we can do is to test the prompt and see if it generates the desired output through the web interface. 
- Test open source LLMs such as LLama on our own.
- Fine-tune on a dataset of questions and answers

## References

Note that below are clickable links to the OpenAI documentation.

#### [Best Practices](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)

#### [Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

#### [Preparing Datasets](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset)
