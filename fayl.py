def get_redd_mem():    
    url = 'https://www.reddit.com/r/memes'
    res = requests.get(url)
    data = res.json()
    return data['url']
