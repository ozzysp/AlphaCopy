def copy (file_from: str, file_to: str):
	with open(file_from) as f_read:
		with open(file_to, "w") as f_write:
			f_write.write(f_read.read())