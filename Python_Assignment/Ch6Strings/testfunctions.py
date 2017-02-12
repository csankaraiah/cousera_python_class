text = "X-DSPAM-Confidence:    0.8475";
text_f = text.find('.')
text_s = text[text_f-1:]
text_f = float(text_s)
print text_f