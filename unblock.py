def remove_trailing_whitespaces(to_write):
	while "\n" == to_write[-1]:
		to_write.pop(-1)

	if "\n" in to_write[-1]:
		to_write[-1] = to_write[-1].rstrip()

def unblock():
	r=open("/etc/hosts","r")
	lines_r=r.readlines()
	r.close()

	w=open("/etc/hosts","w")
	to_write=[]

	for line in lines_r:
		if line.rstrip()!= "0.0.0.0 spclient.wg.spotify.com":
			to_write.append(line)

	remove_trailing_whitespaces(to_write)
	w.write(''.join(to_write))
	w.close()

unblock()