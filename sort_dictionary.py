dict={
'OS':89,
'WT':87,
'DS':78,
'JAVA':79,
'PYTHON':98
}
print("Original Dictionary:\n",dict)
sort_by_keys=sorted(dict.items(), key=lambda x:x[0])
sort_by_values=sorted(dict.items(), key=lambda x:x[1], reverse=True)
print("Dictionary Sorted by Keys:\n",sort_by_keys)
print("Dictionary Sorted by Values Dscending Order:\n",sort_by_values)
