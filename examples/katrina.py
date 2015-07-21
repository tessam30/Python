# Answering questions about Katrina text using Python text handling abilities

f = open("katrina_advisory.txt")
text = f.read()
f.close()
print 'Content of "katrina_advisory.txt"'
print '-' * 51
print
print text

# Q1. Strip leading spaces and make everything lowercase
text_clean = text.lower().strip()
print text_clean

# Q2. Count the number of times keywords appear in the text
wrd_lst = ["killed", "destroyed", "death", "devastating"]
text_count = 0.0
for word in wrd_lst:
    print text_clean.count(word) 
    text_count += text_clean.count(word) 
print text_count

# Q3. Is the advisory urgent?
is_urgent = text_clean.startswith("urgent")
print is_urgent

no_words = len(text.split())
print no_words

# What is the ratio of alarming words to total words?
print text_count / no_words
print "Alarming words ratio = {:.3f}".format(text_count/no_words)
