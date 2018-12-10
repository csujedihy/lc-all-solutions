class Codec:

  def encode(self, longUrl):
    """Encodes a URL to a shortened URL.
    
    :type longUrl: str
    :rtype: str
    """
    return longUrl

  def decode(self, shortUrl):
    """Decodes a shortened URL to its original URL.
    
    :type shortUrl: str
    :rtype: str
    """
    return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
