str_in = 'X-DSPAM-Confidence: 0.8475'
loc = str_in.find(':')
str_out = float(str_in[loc+1:])
print str_out


