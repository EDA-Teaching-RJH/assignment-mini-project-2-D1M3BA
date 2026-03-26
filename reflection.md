# Reflection

## Project Summary
I created a personal expense tracker CLI application. The program allows users to create and manage a CSV file of financial transactions. Users can add, edit, delete, and view transactions. They can also manage categories, check their balance, and create graphs of their spending data.

## Course Concepts Used
I used command line arguments introduced in workshop 7. This allows users to pass a mode and a filename directly when running the script. Workshop 7 also introduced matplotlib, which I used to implement three different types of graphs. Additionally, I used the re module extensively to validate user inputs like amounts, dates, and descriptions.

For testing, I used unittest instead of pytest since I was more familiar with it. I followed the same principles: separating tests into classes, testing edge cases, and keeping tests self-contained with setUp and tearDown.

For file input and output, I used the csv module to read and write transaction data. Throughout development, I constantly thought about potential issues. I made sure to use try and except when needed and validated inputs before using them.

## Development Process
I had a clear idea of the main functions my program needed from the start. I kept it simple and built one piece at a time, starting with file handling. Then I added features like transactions, categories, and plotting. I used Git to document each step with descriptive commit messages.

## Challenges
The hardest part was figuring out how much Python abstracts away. I spent time trying to implement sorting algorithms that didn't work, only to find that Python had built-in tools for that. Lambda functions were also new to me being able to define a small function inline in just a few characters was something I hadn't encountered before and I found it very useful.

Regex was also challenging at first. It looked confusing, but after breaking it down symbol by symbol, it started to make sense. I look forward to using it again.

## What I Would Do Differently
I would focus more on improving the terminal UI. I'm not satisfied with how the program looks. Slowing down certain elements or adding clearer formatting would enhance the user experience. I also wish I had planned my file structure better from the beginning. My main file became very large, making it hard to find things. Using more custom libraries earlier could have kept things cleaner.