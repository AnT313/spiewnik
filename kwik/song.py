class song:
    def __init__(self):
        self.title=''
        self.subtitle=''
        self.text=[]
        self.chords=[]

    def __init__(self,title,subtitle,text,chords):
        self.title=title
        self.subtitle=subtitle
        self.text=text
        self.chords=chords

    def plainText(self):
        body=[self.text[i]+'\t'+self.chords[i] for i in range(len(self.text))]
        body='\n'.join(body)
        return self.title+"\n"+self.subtitle+"\n"+body
