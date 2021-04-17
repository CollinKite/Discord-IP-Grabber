# Discord-IP-Grabber
## Creates a Fake Youtube Video Embed to phish user into clicking Grabify Link
# Real
![realEmbed](/img/original.png "Real-Embed") 
# Fake
![FakeEmbed](/img/FakeEmbed.png "Fake-Embed")
##### This Script will use this Youtube Template pictured above if you don't replace the video parameters.
### This is a Custom script that works with the Nighty Self Bot which can be purchased here -> https://nighty.one

# Setup
* Go to https://grabify.link and create a tracker forwarding to the youtube video you'd like to spoof.
* Copy the script from [custom.py](custom.py) and pastr it into the file at --> Nighty Folder < Data < custom.py
* Copy the file [Youtube.json](Youtube.json) to Nighty Folder < Data < themes
*After that, restart Nighty then run ```(prefix)theme Youtube``` and you're good to go! 


# Usage
* type the following command in the DM with the user you'd like to target. (Server Channels NOT recommended)  ```(prefix)ipgrab "https://your-grabify-url-here"```
##### (prefix)ipgrab "Link" (REQUIRED) videoName (optional) "videoAuthor" (optional) "thumbnailURL" (optional)

# Example
```(prefix)ipgrab "https://google.com" "PSY - GANGNAM STYLE(강남스타일 M/V" "officalpsy" "https://i.ytimg.com/vi/9bZkp7q19f0/hq720.jpg"```  
![Example](/img/example.png "Example")

* Refer to https://discordpy.readthedocs.io/en/latest/ and https://nighty.one/docs/#customscripts for addtional documentation

# Discord Foreign Link Warning
![warning](/img/warning.png "warning")
### Discord will warn the user about any link when they click on a URL, where it will send them. We can hide our link behind a YouTube redirect link from any video on YouTube giving a better chance if for the user to continue if they don't inspect the url as carefully

# Masking Our Link
* First Lets find a video on youtube that has a link in the description, I'll use the video from the example from before  
![findURL](/img/findURL.png "findURL")
#### All we have to do is find a link that doesn't refer to another YouTube Channel or Video. This one will do the Job
* Next let's Copy and Examine the URL!
```https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbU5tNzBxekhPdW5rU2lXT1E0MzNLb1ZXcXRyZ3xBQ3Jtc0trbGRRSnQ5RTZkOGRvTFQzOUo5R0dHa09nWWlxdjRBTWFDeXFCRWZvU2VuVnBxd2xKaDZaTHV1dTh1ZEc2N29SWXMxdEJteEM4Q3RqbW9hQm1DQ25jV1AweFplQm1QajNkZW04TFkycm5RdWxpWEVGQQ&q=https%3A%2F%2Fsmarturl.it%2FPSY_8thAlbum```
#### All we care about is the section at the end of the url that looks like this, It'll always start with ```"q="``` followed buy a weird looking variation of the URL we just selected. It would be ```q=https%3A%2F%2Fsmarturl.it%2FPSY_8thAlbum``` in this case
* Next lets disect what the different parts of the url mean, a tradtional URL looks like ```https://website.com/``` but as we can see with this one the all of the "/"s are replaced with "%2F" and the ":" is replaced with a "3F". So let's try replaceing this last part of the url with our link instead! Make sure to follow the format and see if it works! For this example I'll replace it to redirect to https://discordpy.readthedocs.io/en/latest/ .
* Following the formatting you should get ```q=https%3A%2F%2Fdiscordpy.readthedocs.io%2Fen%2Flatest%2F```
* Now lets put that back into the big url and run our script and see if it works!
```(prefix)ipgrab "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbU5tNzBxekhPdW5rU2lXT1E0MzNLb1ZXcXRyZ3xBQ3Jtc0trbGRRSnQ5RTZkOGRvTFQzOUo5R0dHa09nWWlxdjRBTWFDeXFCRWZvU2VuVnBxd2xKaDZaTHV1dTh1ZEc2N29SWXMxdEJteEM4Q3RqbW9hQm1DQ25jV1AweFplQm1QajNkZW04TFkycm5RdWxpWEVGQQ&q=https%3A%2F%2Fdiscordpy.readthedocs.io%2Fen%2Flatest%2F" "PSY - GANGNAM STYLE(강남스타일 M/V" "officalpsy" "https://i.ytimg.com/vi/9bZkp7q19f0/hq720.jpg"```
### Now if done correctly we should now get this when we click on the link!  
![redirect](/img/redirect.png "redirect")
### And if we click "Yes" on discord it directly takes us to the discord.py documentation!  
![newURL](/img/newURL.png "newURL")
