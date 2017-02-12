import string
print string.punctuation

st_in = " this is a sentence full of crap character such as %%*&(*)@*)_@_ i wasnt to see what happens with punctuation"
st_out = st_in.translate(None, string.punctuation)
print st_out