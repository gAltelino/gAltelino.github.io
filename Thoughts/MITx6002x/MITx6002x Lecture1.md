I usually do some EDx courses by my own, mostly not verified (not because I don't think they are worth it, but because I'm usually without much extra cash) and sometimes late.
This is hte case with the MITx 6.00.2x course, I subscribed to it, and then started to do all of the Microsoft .NET Core courses, and end up forgetting about it.
Today I was browsing in the course dashboard, I decided to take some courses that I had never really started.

And as a way to revise and better understand each lesson, I will start to make blog posts for each one. There is that common phrase that says, "you really learn something once I can teach it", or something like this.

The Introduction to Computational Thinking and Data Science course from MITx seens like a nice one to refresh my 'computational thinking' while learning new stuff.

In the lecture 1, they start with the Knapsack Problem, 0/1 (everything or nothing) or continuous integration, it's shown as something quite simple, for problem solving as an optimizing method, for example, if you are going to backpack around europe, you could have a certain amounth of kilos in your packpack, limited by comfort and air plane flights allowance, and so after you determine your limit, let's say, 14 kilos, you need to decide with itens you will take, in this limit.
The algorithms then, takes each item and multiply it by a value (in this case each item value could be the need of each item in the travel, for example if you are travelling to sweden a boot may have a value of 10, while sandals a value of 2), and sums it all in the end. You could theoretically maximaze your backpack value doing this, getting the max value in the weight limit. 
The problem began when we start to take in consideration that multiple items may be in that list, and so, who could we find a solution that solves the problem for real, taking the backpack example again, you could end up with four boots and no sleep shorts in your backpack. Or you could end up with multiple solutions with the same max value.

Professor says they are going to explore solutions to these problem in the next lecture, which I guess could be related to turning the algotithm "smarter", by using more conditions or rules.

Bellow is a small python code that I wrote to easily visualy the first exercise, keep in mind that the metric one is commented because it crashes the code, due to the 0 division, and you can also see that by using only the max weight as a limit, we end up with the 'problemSet' item that reduces our max value in all the metrics. Keep it mind that you could also write the functions (metrics) directly into the key as a lambda.