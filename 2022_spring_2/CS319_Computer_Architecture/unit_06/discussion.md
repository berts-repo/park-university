# Unit 6: Discussion

Due Dates:

First post due 11:59 p.m., Wednesday, CT. 

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Guidelines: see  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406742] Unit 1 Discussion

Discussion questions:  [link: https://canvas.park.edu/courses/67161/files/9099283?verifier=THmBVtI6m0OwS4prUTQ2Etct1XXQZPPpZdmiGsJJ&wrap=1]  [link: https://canvas.park.edu/courses/67161/files/9133641?verifier=rQI6P2BwyhactLXSCrdl1t79kGVIZnk484lYAnZw&wrap=1] Unit6_Discussion.docx

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-04-20T05:43:29Z

16. Provide a segment of pseudo code/Python/Java which involves a loop and then translate it to LMC 
program. Do not use examples from the lecture slides. Use at least one label in your program. Must 
comment each line of your code. Your comment should be relevant to the pseudo code. (Reply posts: 
comment on the correctness and efficiency of the code).

 

Class,

my for-loop takes two inputs for the range of the loop, then uses the higher range value and subtracts it from the lower range value, for the length of the loop, it then prints the value of 'i' for each iteration. I really don't know if this is the most efficient process, any recommendations would be appreciated.

low = int(input())
high = int(input())
for i in range(low,high):
    print(i)
	inp		//input lower range
	STA low         //store lower range
	STA i		//store iteration
	inp		//input lower range
	STA high	//store upper range
	SUB low 	//high - low = length
	STA len	        //store length	
loop	LDA len	        //start loop
	BRZ end  	//exit loop if 0
	SUB one	        //length - 1
	STA len	        //store length
	LDA i		//iteration
	OUT		//print
	ADD one	        //iterate
	STA i		//store iteration
	BRA loop	//loop
end	HLT		//end program
len	DAT 0		//initiate length
i	DAT 0		//initiate iteration
low	DAT 0		//initate low value for range
high	Dat 0		//initate high value for range
one	DAT 1		//constant 1

---


### Feedback

**[INSTRUCTOR]:** Good job with the discussion in spite of your schedule last week!
