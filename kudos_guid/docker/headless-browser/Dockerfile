FROM debian:buster-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
	curl \
	gnupg \
	--no-install-recommends \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable \
	fontconfig \
	fonts-ipafont-gothic \
	fonts-wqy-zenhei \
	fonts-thai-tlwg \
	fonts-kacst \
	fonts-symbola \
	fonts-noto \
	fonts-freefont-ttf \
	--no-install-recommends \
	timelimit \
	&& apt-get purge --auto-remove -y curl gnupg \
	&& rm -rf /var/lib/apt/lists/*


# Create a directory for your scripts
WORKDIR /app

# Copy your script to the container
COPY script.sh .

# Make the script executable
RUN chmod +x script.sh

# Set up the entry point
CMD ["/bin/sh", "./script.sh"]
