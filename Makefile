all:
	sh runGame.sh
clean:
	rm *.log || echo "No log files";
	rm *.hlt || echo "No replay files";
compile:
	# Create temp dir for zipping
	mkdir Submission || (rm -r Submission && mkdir Submission);
	# Copy bot and library files to temp dir
	cp MyBot.py Submission
	cp hlt.py Submission
	# Zip & remove temp dir
	zip -r -X Submission.zip Submission
	rm -r Submission
	# Overwrite old bot file with new code for testing future improvements
	cat MyBot.py > RandomBot.py
