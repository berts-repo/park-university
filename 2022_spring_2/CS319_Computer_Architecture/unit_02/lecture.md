# Unit 2: Lecture

Select the tabs below to view each topic

 [link: #fragment-1] IEEE 754

 [link: #fragment-2] More on IEEE 754

 [link: #fragment-3] Boolean Algebra

 [link: #fragment-4] K-Map

 [link: #fragment-5] Why Karnaugh Map Works

 [link: https://canvas.park.edu/courses/67161/files/9056011?verifier=xYNg7VtGHbuFN7gXCieyCbiKHjsKbTPxLJ0GtmpI&wrap=1] Unit2_1_IEEE754.pptx  Script:  [link: https://canvas.park.edu/courses/67161/files/9056012?verifier=zCJV1W4UKk3WdUpTpdFH0YKChBaIEZs2PzB2Vnjd&wrap=1] Unit2_1_script.txt 

 [link: https://canvas.park.edu/courses/67161/files/9057820?verifier=bBVWmyzV8As6HKST8r8YIil29gsT96k1zlAHMUSN&wrap=1] Unit2_2_IEEE754.pptx Script:  [link: https://canvas.park.edu/courses/67161/files/9057821?verifier=maQ42p40rzscVwGbv79T8GqNOnl5V3yULfpXUkDe&wrap=1] Unit2_2_script.txt

 [link: https://canvas.park.edu/courses/67161/files/9182641?verifier=7mtpeMG7Bnx9skk9S8wi3cSq7bs2T74tHYR76vax&wrap=1] Unit2_3_BooleanAlgebra.pptx Script:  [link: https://canvas.park.edu/courses/67161/files/9182642?verifier=JlH9cwdQBeHIfPCMzcCzCXE6lbEInERD1PD7D8iW&wrap=1] Unit2_3_script.txt

 [link: https://canvas.park.edu/courses/67161/files/9182639?verifier=TBhfw0MQ5SmrbMTJ16K9woIIudFiZk6FimK5GIZa&wrap=1] Unit2_4_K-map.pptx Script:  [link: https://canvas.park.edu/courses/67161/files/9182640?verifier=Eu1cRniqrYEkV9OpY7XZtkf5adSHw7KCKgakOVPx&wrap=1] Unit2_4_script.txt

Karnaugh Map (K-map) is covered in ch7 of our 2nd textbook (by Tarnoff). ch7.1 explains how input combinations are mapped to cells of a k-map. ch7.2 explains the rationale behind simplification using k-map, how to, and examples. ch7.3 talks about don't care cells.

K-map is a visual tool for simplifying boolean expressions. It's still based on boolean algebra rules, mainly those four:

A +  = 1              // #1
A•C + B•C = (A + B)•C   // #2. distributive law
A•1 = A                 // #3
A + A = A               // #4

Now combine the first three rules to get to a derived rule we rely on in K-map simplification:

// derived rule
A•C + •C = (A + )•C // based on #2 distributive law
           = 1•C        // based on #1
           = C          // based on #3 

Converting a grouping of 1s (plus don't care cells) in k-map into a simpler term is based on our derived rule. Adjacent cells in k-map have common portions C and one same variable in both forms A and  (because the labels follow Gray code), so A can be removed.

When we overlap groupings, it's based on #4 to repeat a cell in multiple groups. K-map makes it easy to decide which cells should be repeated for the benefit of simplification.

Let me borrow the example from Fig 7-6 of ch7.2 (p130). X' means :

  \ C | 0  1
AB 00 | 0  1     000 input/A'•B'•C'     001 input/A'•B'• C
   01 | 1  1     010 input/A'•B •C'     011 input/A'•B • C
   11 | 1  1     110 input/A •B •C'     111 input/A •B • C
   10 | 0  0     100 input/A •B'•C'     101 input/A •B'• C

The original boolean expression is: (bottom of p129)

X = A'•B'•C + A'•B •C + A •B •C' + A •B •C + A •B'•C'   

Based on the K-map, we will be able to get two groups:

  #1.
  \ C | 0 1
AB 00 | 0 1      000 input/A'•B'•C'     001 input/A'•B'•C 
   01 | 1 1      010 input/A'•B •C'     011 input/A'•B •C
   11 | 1 1      110 input/A •B •C'     111 input/A •B •C
   10 | 0 0      100 input/A •B'•C'     101 input/A •B'•C

and

  #2.
  \ C | 0 1
AB 00 | 0 1      000 input/A'•B'•C'     001 input/A'•B'•C
   01 | 1 1      010 input/A'•B •C'     011 input/A'•B •C
   11 | 1 1      110 input/A •B •C'     111 input/A •B •C
   10 | 0 0      100 input/A •B'•C'     101 input/A •B'•C

#1 group: based on K-map rules, it covers two rows (AB being 01 and 11) where A exists in both 0 and 1 but B only exists in 1, so A is eliminated. It covers two columns where C exists in both 0 and 1 so C is eliminated. This means we end up with just B for group #1.

if we directly apply boolean algebra rules on group #1:
   A'•B•C' + A'•B•C + A•B•C' + A•B•C 
= (A'•B•C' + A'•B•C) + (A•B•C' + A•B•C) 
= A'•B•(C' + C)      + A•B•(C' + C)
= A'•B•1             + A•B•1 
= A'•B               + A•B
= (A' + A)•B
= 1•B
= B

#2 group: based on K-map rules, it covers two rows (AB being 00 and 01) where B and B' exist but only one value of A (i.e. A'), so B is eliminated. It covers one single column C, so C stays. We end up with A'•C.

if we directly apply boolean algebra rules on group #2: 
    A'•B'•C + A'•B•C 
= A'•C•(B' + B)
= A'•C

A'• B• C is repeated in both groups.  Without K-map, I know I won't be able to figure out that this term should be repeated for the benefit of simplification. 

Together, the expression represented by the K-map in Fig 7-6 is simplified to B + A'•C.
