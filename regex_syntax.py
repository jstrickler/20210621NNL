
junk = """

pat   p, a, t     "A pattern language"  "pat the baby"  "She spat it out"   

p.t    p, <any 1 char>, t   "spittoon"  "pot head"  "x marks the spot" 
               "keep to the right"

p[aeiou]t  p, <any vowel>, t
p[a-z]t
p[0-9]t

[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]
[0123456789][0123456789][0123456789]-[0123456789][0123456789]-[0123456789][0123456789][0123456789][0123456789]
\d\d\d-\d\d-\d\d\d\d   

\d any digit
\s any ' ' \t \n \r \f 
\w any  [a-zA-Z0-9_]  alphanumeric + underscore  "word"

pat        one a
pa+t       one or more    pa{1,}t
pa*t       zero or more   pa{0,}t
pa?t       zero or one    pa(0,1}t
pa{2}t     exactly 2
pa{1,2}t   one through two 
pa{2,}t    two or more

\d{3}-\d{2}-\d{4}   SSN

\w+\.(com|org|mil|gov|net|edu)    nnl.gov  google.com   harvard.edu   tiobe.net

^   beginning of text
$   end of text
\b  beginning or end of word     \w+

foo.*bar   foobar   foo+bar foo.bar foo_bar
        fooblah blah blha blha blah blah blah blah blah bar

"""
