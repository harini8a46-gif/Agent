
def get_vid(query):

  try:
     encode = urllib.parse.quote(query)

     url = (
         "https://www.youtube.com/results"
         "?search_query=" + encoded
     )

     request = urllib.request.Resquest(
         url,
         headers={
             "user-agent":"Mozilla/5.0"
         }
     )

  data = urllib.request.urlopen(
       request,
       timeout=5
  ).read().decode("utf-8" , errors="ignore")

  ids = re.findall(
      r'"videoId":"([^"]+)"',
      data
  )

  return ids[0] if ids else None

except Exception:
     return None

def create_youtube_url(command):

   text = command.lower().strip()

   patterns = [
       r"play\s+song\s+(.+)",
       r"play\s+music\s+(.+)",
       r"play\s+(.+)",
       r"youtube\s+(.+)"
   ]

   query = command

  for pattern in patterns:

      match = re.search(
         pattern,
         text
      )

      if match:

            query = match.group(1)
            break
   query = query.sript()  

   video_id = get_vid(query)

   if not video_id:
      return None
