def block():
	r=open("/etc/hosts","r")
	lines=r.readlines()
	r.close()

	w=open("/etc/hosts","a+")

	to_write_w_newline="\n\n0.0.0.0 spclient.wg.spotify.com"
	to_write_wo_newline="\n0.0.0.0 spclient.wg.spotify.com"

	if "\n" in lines[-1]:
		w.write(to_write_wo_newline)
	else:
		w.write(to_write_w_newline)

	w.close()

block()