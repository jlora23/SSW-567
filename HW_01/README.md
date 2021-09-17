# Deliverable 3

## What challenges did you encounter with this assignment, if any? 

In this assignment the main trouble I had with this assignment was understanding exactly what I should be trying to accomplish as far as testing goes. When I first attempted this assignment I did not test as much aspects of the program as I should have. Once I realized this I made sure to add more cases to further prove the program is working as expected.

## What did you think about the requirements specification for this assignment?

The requirements specification was decent overall. It was easy to understand each of the deliverables and what is expected. The only issue I had with the requirements is that I did not understand that we needed to include some bugs on purpose as to display the testing is working as expected. To accomodate for this I removed certain error checking I originally had in order to be able to break the code at times.

## What challenges did you encounter with the tools?

I did not encounter many challenges with the tools if at all. I had previous experience with Python and IDLE before which made things quite simple. The only issue is understanding unittest since I do not have much prior experience with that tool. Once I read some documentation it was quite simple as well.

## Describe the criteria you used to determine that you had sufficient test cases, i.e. how did you know you were done?

To determine I had sufficient test cases I made sure to have cases for each different possible outcome. To do this I had cases for each type of triangle and input that could possibly "break" the program. I even included some test cases to show that errors will be shown if there is an invalid input for example. Also, I included an 'assertNotEqual' case for each triangle to show that it would not mistakingly classify any triangle. Overall I ensured that each possible input was focused on, except for those that I purposely included to output an error.