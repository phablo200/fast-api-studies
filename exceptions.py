class StoryException(Exception):
  def __init__(self, descritpion: str):
    self.descritpion = descritpion