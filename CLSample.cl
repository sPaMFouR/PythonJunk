# Twelve Pre-declared Variables(Hidden Parameters) in CL:

#   1) Character Strings - s1, s2, s3
#   2) Booleans - b1, b2, b3
#   3) Integers - i, j, k
#   4) Reals - x, y, z



# Terminal Script Examples:-

#   1) Single Command Line:-
#        cl> clear; cd database; dir
#   2) Compound Statement:-
#        cl> {
#        >>> clear
#        >>> cd database
#        >>> dir
#        >>> }



# Modes Of CL:-

#   1) Command Mode:-
#        Default Mode + Minimizes Need Of Character Strings
#   2) Program Mode:-
#        Requires Full Syntax Of CL + Entered Within The Body Of The Procedure + Entered Within
#        Parenthesized Expressions + Entered On The Right-Hand Side Of An Equal Sign (=) 

###################################################
#            CL Scripting Notes			  #
###################################################

# Sample Codes In Different Modes:-

#   1) Command Mode:- 
#        cl> print s1
#        s1

#        cl> print "s1"
#        s1

#   2) Program Mode:-
#        cl> print (s1)
#        Hi There!                      [if CL variable  s1 = "Hi There!"]

#        cl> print ("s1")
#        s1

######---Unquoted Identifiers Are Treated As Character Strings In Command Mode---######
#######---Unquoted Identifiers Are Treated As Variable Names In Program Mode---########
######---Always Quote Character Strings And Always Parenthesize Expressions---######



#####---Sample Terminal Script---#####

# cl> sections data*.fits > contour.list    (1)
# cl> list = "contour.list"                 (2)
# cl> while (fscan (list, s1) != EOF) {     (3)
# >>> contour (s1, dev="stdplot")           (4)
# >>> }                                     (5)
# cl> gflush                                (6)

# 1) Produces text file contour.list of images to be contoured; Commands "files" or "sections" can be used
# 2) Assigns text file, "contour.list", to the file variable 'list'
# 3) "fscan" statement reads the list; First non-blank entity is assigned to the string variable 's1';
#     Each execution of "fscan" reads a new line; "fscan" returns the number of items read; 
#     EOF is returned when end-of-file is encountered
# 4) Does the contour plot, sending 's1' to the system variable 'stdplot'
# 5) Marks the end of while loop
# 6) Flushes the plot buffer to appropriate device(here 'stdplot')

# Statements 2, 3, 4 are in Program mode:- File "contour.list" is quoted; Variable 's1' is parenthesized
# Statements 1, 6 are in Command mode:-



#####---Sample Code When We Need To Operate On The Same Image---##### 
######---A Few Times, Changing The Task Parameters Each Time---######

# cl> list = "coord.list"                       (1)
# cl> while (fscan (list, x, y) != EOF) {       (2)
# >>>     imcntr data001 x y >> data001.cen     (3)
# >>> }                                         (4)
# cl> type data001.cen                          (5)
# [data001] x: 230.46   y:  12.17
# [data001] x: 187.50   y:  33.85
# [data001] x: 161.59   y:  18.91
# [data001] x: 115.55   y:  67.56
# [data001] x:  63.88   y:  53.11
# cl> ^list                                     (6)
# list = "coord.lis"
# cl> ^while:p                                  (7)
# while (fscan (list, x, y) != EOF) {
# imcntr data001 x y >> data001.cen
# }
# cl> ^001^002^g                                (8)
# while (fscan (list, x, y) != EOF) {
# imcntr data002 x y >> data002.cen
# }

# 1) Assigns "coord.list" to the file variable 'list'
# 2) Sets up a while loop based on whether "fscan" hits EOF
# 3) Calls IMCNTR on image "data001"; Initial x, y coordinates are set to current variables x, y;
#    Output is being redirected to the text file "data001.cen"; ('>>') is append redirection;
#    This statement is in command mode; Command mode interprets identifiers as character strings;
#    CL can recognize that x, y are not numbers and interprets them as variables
# 4) Marks the end of while loop
# 5) Examines the output file "data001.cen"
# 6) Caret (^) is used to call the most recent 'list' definition
# 7) Caret-colon-p to recall while loop to the most recent spot in history
# 8) Globally replaces instances of 001 and 002 in the most recent command and executes the command
 


#####---Code To Copy Exposure-Time Under The Keyword 'INT' Into A New Keyword 'EXPTIME'---#####

# cl> sections data∗.fits > datalist                      (1)
# cl> list = "datalist"                                   (2)
# cl> while (fscan (list, s1) != EOF) {                   (3)
# >>>     imgets (s1, "int")                              (4)
# >>>     hedit (s1, "exptime", imgets.value, add+, ver-) (5)
# >>> }                                                   (6)

# (1) Makes a file with the names of the images whose headers need modification.
# (2) Assigns the text file to the variable 'list'
# (3) Sets up a while loop based on whether fscan hits the EOF while reading the image name.
# (4) Uses the IMGETS task to get the value of the keyword INT for the image 's1'; The value is stored #     in the imgets parameter value
# (5) Uses HEDIT to create the new keyword, EXPTIME, and give it the value of the key-word, INT
#     Note how the IMGETS parameter, value, is directly referenced and that verify = no ( i.e., ver-) is #     used so that the user will not have to verify each HEDIT operation.
# (6) Marks the end of the while loop

# (4) & (5) could be replaced by a single line:- [hedit data∗.fits exptime "(int)" add+ ver-]



#####---Sample CL Script(Center.cl)---#####

# list = "coord.list"                      (1)
# while (fscan (list, x, y) != EOF) {      (2)
# 	imcntr (s1, x, y,>> s1//".cen")    (3)
# }                                        (4)

# (3) Uses full syntax of CL language; String variable 's1' is concatenated (//) with the string 
      literal ".cen"; The variable is not quoted, but the literal is quoted; I/O redirection occurs
      inside the parentheses

# To use the script(Center.cl) on any image

# cl> s1 = "data001"               (1)
# cl> cl < center.cl               (2)
# cl> s1 = "data002"               (3)
# cl> ^cl                          (4)
# cl> s1 = "data101"               (5)
# cl> ^cl                          (6)


#####---Sample CL Script For Operating On Multiple Images---#####

# for (i=1; i <= 550; i+=1) {                           (1)
# 	if (i < 10)                                     (2)
# 		s1 = "data00"//i

# 	else if (i < 100)
# 		s1 = "data0"//i
# 	else
# 		s1 = "data"//i
# 	if (access (s1 // ".fits")) {                   (3)
# 		list = "coord.list"                     (4)
# 		while (fscan (list, x, y) != EOF)       (5)
# 		imcntr (s1, x, y, >> s1//".cen")        (6)
# }
# ;                                                     (7)
# }



# string ∗list1                                         (1)
# list1 = "data.list"                                   (2)
# while (fscan (list1, s1) != EOF) {                    (3)
# 	list = "coord.list"                             (4)
# 	while (fscan (list, x, y) != EOF)               (5)
# 		imcntr (s1, x, y, >> s1//".cen")        (6)
# }                                                     (7)
# list = ""; list1 = "" 



# string ∗list1 = "data.list"                                     (1)
# list = "coord.lis"                                              (2)
# while (fscan (list1, s1) != EOF && fscan (list, x, y) != EOF)   (3)
# 	imcntr (s1, x, y, >> s1//".cen")                          (4)
  
