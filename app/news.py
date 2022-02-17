class News:
    '''
    Movie class to define News Objects
    '''

    def __init__(self,id,name,author,title,description,image,published_date,content,link):
        self.id =id
        self.title = title
        self.name = name
        self.author = author
        self.description = description
        self.published_date = published_date
        self.image = image
        self.content = content
        self.link = link