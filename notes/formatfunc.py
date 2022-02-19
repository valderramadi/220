"""
.format = string functions 1
"hi my name is {}.format("Eric")
>> 'My name is Eric'
"My name is {} and I am {} years old".format('Eric', 7)
>>My name is Eric and I am 7 years if old.
"My name is {1} and I am {0} years old.format("Eric", 7)
>>My name is 7 and I am Eric years old.
"My name is {0:10} and I am {1} years old".format("eric", 7)
>> My name is Eric         and I am 7 years old.

{:2} = gives a space by default to the right of the parameter that is 0, 1....
{:0>2} = adds a zero to the space that would be by default to the left of it ...
# formatting comes after the colon : {}
{:.2f} = will make variable and output two decimal places ...
money = 0.129848247
"I have ${:.2f}.format(money)
>>I have $0.13




"""