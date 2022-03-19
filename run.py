if __name__ == "__main__":
	try:
		__import__("Instagram").checkin()
	except Exception as e:
		exit(str(e))
