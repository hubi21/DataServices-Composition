#Define the structure of a data service
class Data_Service:
    count=0
    def __init__(self,name=None,inputs=None,outputs=None, view=None,response_time=None,reputation=None,reliability=None,availibility=None, cost=None,avg=None,critical=None,calls_number=None):
        Data_Service.count+=1
        self.ide= Data_Service.count
        self.name=name
        self.inputs=inputs
        self.outputs=outputs
        self.view = view
        self.reputation=reputation
        self.reliability=reliability
        self.availibility=availibility
        self.response_time=response_time
        self.cost=cost
        self.avg=avg
        self.critical=0
        self.calls_number=calls_number

##Define the Service view  structure     
class View:
    def __init__(self,name=None,view=None):
        self.name=name
        self.view=view


class book:  
    def __init__(self,name=None,Title=None, ISBN=None,BookPublisher=None,BookAuthor=None,Edition=None,Language=None): 
        self.name =name
        self.Title = Title
        self.ISBN = ISBN 
        self.BookPublisher = BookPublisher 
        self.BookAuthor = BookAuthor
        self.Edition = Edition
        self.Language = Language

instances={}
instances['book']=set()
instances['author']=set()
instances['publisher']=set()
instances['actor']=set()
instances['movie']=set()
instances['role']=set()
instances['recording']=set()
instances['artist']=set()
instances['lyrics']=set()
instances['album']=set()
instances['tag']=set()
instances['track']=set()
instances['biography']=set()
instances['wiki']=set()

def Book(o): 
    b = str(o)
    c = book(o)
    instances['book'].update({c})
    globals()[b] = c
    sig=['Book']
    sig.append(c)
    return sig
def Title(o, Title):
    o.Title=Title
    sig=['Title']
    sig.append(Title)
    return sig
def Subject(o, Title):
    o.Subject=Title
    sig=['Subject']
    sig.append(Title)
    return sig
def ISBN(o, Title):
    o.ISBN=Title
    sig=['ISBN']
    sig.append(Title)
    return sig
def BookPublisher(o, Title):
    o.BookPublisher=Title
    sig=['BookPublisher']
    sig.append(Title)
    return sig
def BookAuthor(o, Title):
    o.BookAuthor=Title
    sig=['BookAuthor']
    sig.append(Title)
    return sig
def Edition(o, Title):
    o.Edition=Title
    sig=['Edition']
    sig.append(Title)
    return sig
def Language(o, Title):
    o.Language=Title
    sig=['Language']
    sig.append(Title)
    return sig
class relationship:  
    def __init__(self,Pname=None):
        self.name='relationship'
        ######Publisher
class publisher:  
    def __init__(self,name= None,PublisherName=None, Location=None):
        self.name =name
        self.PublisherName = PublisherName
        self.Location = Location
def Publisher(o):
    b = str(o)
    c = publisher(o)
    instances['publisher'].update({c})
    globals()[b] = c
    sig=['Publisher']
    sig.append(c)
    return sig
def PublisherName(o, Title):
    o.PublisherName = Title
    sig=['PublisherName']
    sig.append(Title)
    return sig
def Location(o, Title):  
    o.Location = Title  
    sig=['Location']
    sig.append(Title)
    return sig

def NationalityP(o, Title):  
    o.NationalityP = Title  
    sig=['NationalityP']
    sig.append(Title)
    return sig
class publication:  
    def __init__(self,Publisher,Book):
        self.Publisher = publisher()
        self.Book = book()
###Author
class author:  
    def __init__(self,name=None,AuthorName=None,Date_of_birthA=None,NationalityA=None):
        self.name=name
        self.AuthorName = AuthorName
        self.Date_of_birthA=Date_of_birthA
        self.NationalityA = NationalityA
def Author(o):
    b = str(o)
    c = author(o)
    instances['author'].update({c})
    globals()[b] = c
    sig=['Author']
    sig.append(c)
    return sig
    #o.__class.__name
def AuthorName(o, Title):  
    o.AuthorName = Title
    sig=['AuthorName']
    sig.append(Title)
    return sig
def Date_of_birthA(o, Title):  
    o.Date_of_birthA = Title
    sig=['Date_of_birthA']
    sig.append(Title)
    return sig

def NationalityA(o, movie):
    o.NationalityA=movie
    sig=['NationalityA']
    sig.append(movie)
    return sig
class wrote:  
    def __init__(self,Author=None,Book=None):
        self.Author = author()
        self.Book = book()
def Wrote(o1,o2):
    sig=['Wrote']
    sig.append(o1)
    sig.append(o2)
    sig.append(relationship())
    return sig
def Publication(o1,o2):
    sig=['Publication']
    sig.append(o1)
    sig.append(o2)
    sig.append(relationship())
    return sig
    ######################################################Actor############################################
class actor:  
    def __init__(self,Id=None,Name=None,Gender=None,BirthDate=None,DeathDate=None,Nationality=None): 
        self.Id= Id
        self.Name =Name
        self.Gender = Gender
        self.BirthDate = BirthDate
        self.DeathDate = DeathDate 
        self.Nationality = Nationality
def Actor(o): 
    b = str(o)
    c = actor(o)
    instances['actor'].update({c})
    globals()[b] = c
    sig=['Actor']
    sig.append(c)
    return sig  

def Nationality(o, movie):
    o.Nationality=movie
    sig=['Nationality']
    sig.append(movie)
    return sig

def Id(o, movie):
    o.Id=movie
    sig=['id']
    sig.append(movie)
    return sig

def Name(o, movie):
    o.Last_name=movie
    sig=['name']
    sig.append(movie)
    return sig

def Gender(o, movie):
    o.First_name=movie
    sig=['gender']
    sig.append(movie)
    return sig

def BirthDate(o, movie):
    o.BirthDate=movie
    sig=['birthdate']
    sig.append(movie)
    return sig

def DeathDate(o, movie):
    o.BirthDate=movie
    sig=['deathdate']
    sig.append(movie)
    return sig
    #######################################Role###############################################""
class role:  
    def __init__(self,Name=None,Actor_name=None,Movie_title=None): 
        #self.id= str(id)
        self.Name =Name
        self.Actor_name = Actor_name
        self.Movie_title = Movie_title 
def Role(o): 
    b = str(o)
    c = role(o)
    instances['role'].update({c})
    globals()[b] = c
    sig=['Role']
    sig.append(c)
    return sig   
def Actor_name(o, Actor_name):
    o.Actor_name=Actor_name
    sig=['Actor_name']
    sig.append(Actor_name)
    return sig

def Movie_title(o, movie):
    o.Movie_title=movie
    sig=['Movie_title']
    sig.append(movie)
    return sig

def Name(o, movie):
    o.Name=movie
    sig=['name']
    sig.append(movie)
    return sig
#####BIOGRAPHY
class biography:  
    def __init__(self,Id=None,Published=None,Summary=None,Content=None): 
        self.Id= Id
        self.Published =Published
        self.Summary = Summary
        self.Content = Content
def Biography(o): 
    b = str(o)
    c = biography(o)
    instances['biography'].update({c})
    globals()[b] = c
    sig=['Biography']
    sig.append(c)
    return sig 

def bID(o, movie):
    o.ID=movie
    sig=['id']
    sig.append(movie)
    return sig 

def bPublished(o, movie):
    o.Published=movie
    sig=['published']
    sig.append(movie)
    return sig 

def bSummary(o, movie):
    o.Summary=movie
    sig=['summary']
    sig.append(movie)
    return sig 

def bContent(o, movie):
    o.Content=movie
    sig=['content']
    sig.append(movie)
    return sig 
#####WIKI
class wiki:  
    def __init__(self,Id=None,Published=None,Summary=None,Content=None): 
        self.Id= Id
        self.Published =Published
        self.Summary = Summary
        self.Content = Content
def Wiki(o): 
    b = str(o)
    c = wiki(o)
    instances['wiki'].update({c})
    globals()[b] = c
    sig=['Wiki']
    sig.append(c)
    return sig 

def wID(o, movie):
    o.ID=movie
    sig=['id']
    sig.append(movie)
    return sig 

def wPublished(o, movie):
    o.Published=movie
    sig=['published']
    sig.append(movie)
    return sig 

def wSummary(o, movie):
    o.Summary=movie
    sig=['summary']
    sig.append(movie)
    return sig 

def wContent(o, movie):
    o.Content=movie
    sig=['content']
    sig.append(movie)
    return sig 

#####TAG
class tag:  
    def __init__(self,Id=None,Name=None,URl=None,Count=None): 
        self.Id= Id
        self.Name =Name
        self.URl=URl
        self.Count=Count
def Tag(o): 
    b = str(o)
    c = tag(o)
    instances['tag'].update({c})
    globals()[b] = c
    sig=['Tag']
    sig.append(c)
    return sig  


def tagId(o, movie):
    o.ID=movie
    sig=['id']
    sig.append(movie)
    return sig 


def tagName(o, movie):
    o.Name=movie
    sig=['name']
    sig.append(movie)
    return sig 


def tagUrl(o, movie):
    o.URL=movie
    sig=['url']
    sig.append(movie)
    return sig 

def tagCount(o, movie):
    o.Count=movie
    sig=['count']
    sig.append(movie)
    return sig 
#####Artist
class artist:  
    def __init__(self,Id=None,PlayCount=None,TagCount=None,mbid=None,Name=None,Location=None, Gender=None,BirthDate=None,DeathDate=None,Nationality=None,Listeners=None, Plays=None,Biography=None,Similars=None,Streamable=None,URl=None,Tags=None,Tracks=None): 
        self.Id= Id
        self.Name =Name
        self.Gender = Gender
        self.BirthDate = BirthDate
        self.DeathDate = DeathDate 
        self.Nationality = Nationality
        self.Listeners = Listeners
        self.Plays = Plays
        self.Streamable = Streamable 
        self.mbid = mbid
        self.URl=URl
        self.Similars=Similars
        self.Biography=Biography
        self.Tracks=Tracks
        self.Tags=Tags
        self.PlayCount=PlayCount
        self.Address=Location
        self.TagCount=TagCount
def Artist(o): 
    b = str(o)
    c = artist(o)
    instances['artist'].update({c})
    globals()[b] = c
    sig=['Artist']
    sig.append(c)
    return sig  

def aNationality(o, movie):
    o.Nationality=movie
    sig=['nationality']
    sig.append(movie)
    return sig

def aAddress(o, movie):
    o.Adress=movie
    sig=['adress']
    sig.append(movie)
    return sig

def aPlayCount(o, movie):
    o.PlayCount=movie
    sig=['playcount']
    sig.append(movie)
    return sig

def aTagCount(o, movie):
    o.TagCount=movie
    sig=['tagcount']
    sig.append(movie)
    return sig

def aId(o, movie):
    o.Id=movie
    sig=['id']
    sig.append(movie)
    return sig

def aName(o, movie):
    o.Last_name=movie
    sig=['name']
    sig.append(movie)
    return sig

def aGender(o, movie):
    o.First_name=movie
    sig=['gender']
    sig.append(movie)
    return sig

def aBirthDate(o, movie):
    o.BirthDate=movie
    sig=['birthdate']
    sig.append(movie)
    return sig

def aDeathDate(o, movie):
    o.BirthDate=movie
    sig=['deathdate']
    sig.append(movie)
    return sig
def aUrl(o, movie):
    o.URL=movie
    sig=['url']
    sig.append(movie)
    return sig

def MBID(o, movie):
    o.mbid=movie
    sig=['mbid']
    sig.append(movie)
    return sig

def Plays(o, movie):
    o.Plays=movie
    sig=['plays']
    sig.append(movie)
    return sig

def Listeners(o, movie):
    o.Listeners=movie
    sig=['listeners']
    sig.append(movie)
    return sig
def aTag(o, movie):
    o.Tags=movie
    sig=['tags']
    sig.append(movie)
    return sig

def aBiography(o, movie):
    o.Biography=movie
    sig=['biography']
    sig.append(movie)
    return sig

def aTrack(o, movie):
    o.Tracks=movie
    sig=['tracks']
    sig.append(movie)
    return sig


def aStreamable(o, movie):
    o.Streamable=movie
    sig=['streamable']
    sig.append(movie)
    return sig
####Recording
class recording:  
    def __init__(self,ID=None,MBID=None,PUID=None,Title=None,Country=None,Location=None,Streamable=None,URL=None,PlayCount=None,Listeners=None,Artists=None,Directors=None,Duration=None, Ratings=None, Genres=None,ReleaseDate=None,Language=None,Budget=None,Revenue=None): 
        self.ID=ID
        self.PUID=PUID 
        self.MBID=MBID
        self.Title =Title
        self.Artists = Artists
        self.ReleaseDate = ReleaseDate 
        self.Language = Language
        self.Directors=Directors
        self.Duration=Duration
        self.Ratings=Ratings
        self.Budget=Budget
        self.Revenue=Revenue
        self.Genres=Genres
        self.Listeners=Listeners
        self.PlayCount=PlayCount
        self.URL=URL
        self.Country=Country
        self.Location=Location
        self.Streamable=Streamable
def Recording(o): 
    b = str(o)
    c = recording(o)
    instances['recording'].update({c})
    globals()[b] = c
    sig=['Recording']
    sig.append(c)
    return sig

def TitleR(o, movie):
    o.Title=movie
    sig=['title']
    sig.append(movie)
    return sig

def rId(o, movie):
    o.ID=movie
    sig=['id']
    sig.append(movie)
    return sig

def rMBID(o, movie):
    o.MBID=movie
    sig=['mbid']
    sig.append(movie)
    return sig

def rStreamable(o, movie):
    o.Streamable=movie
    sig=['streamable']
    sig.append(movie)
    return sig

def RCountry(o, movie):
    o.Country=movie
    sig=['country']
    sig.append(movie)
    return sig

def RLocation(o, movie):
    o.Location=movie
    sig=['location']
    sig.append(movie)
    return sig

def rListeners(o, movie):
    o.Listeners=movie
    sig=['listeners']
    sig.append(movie)
    return sig

def rURL(o, movie):
    o.URL=movie
    sig=['url']
    sig.append(movie)
    return sig

def PlayCount(o, movie):
    o.PlayCount=movie
    sig=['PlayCount']
    sig.append(movie)
    return sig

def PUID(o, movie):
    o.PUID=movie
    sig=['puid']
    sig.append(movie)
    return sig

def Artists(o, movie):
    o.Artists=movie
    sig=['artists']
    sig.append(movie)
    return sig

def DirectorsR(o, movie):
    o.Directors =movie
    sig=['directors']
    sig.append(movie)
    return sig


def Duration(o, movie):
    o.Duration =movie
    sig=['duration']
    sig.append(movie)
    return sig

def BudgetR(o, movie):
    o.Budget =movie
    sig=['budget']
    sig.append(movie)
    return sig


def RevenueR(o, movie):
    o.Revenue =movie
    sig=['revenue']
    sig.append(movie)
    return sig


def RatingsR(o, movie):
    o.Ratings =movie
    sig=['ratings']
    sig.append(movie)
    return sig


def GenresR(o, movie):
    o.Genres =movie
    sig=['genres']
    sig.append(movie)
    return sig

def ReleaseDateR(o, movie):
    o.ReleaseDate=movie
    sig=['releaseDate']
    sig.append(movie)
    return sig

def LanguageR(o, movie):
    o.Language=movie
    sig=['language']
    sig.append(movie)
    return sig
####Lyrics
class lyrics:  
    def __init__(self,PUID=None,Title=None,Artists=None,Language=None): 
        self.ID=PUID 
        self.Body =Title
        self.CopyrightL = Artists
        self.Language = Language
def Lyrics(o): 
    b = str(o)
    c = lyrics(o)
    instances['lyrics'].update({c})
    globals()[b] = c
    sig=['Lyrics']
    sig.append(c)
    return sig

def Body(o, movie):
    o.Budy=movie
    sig=['body']
    sig.append(movie)
    return sig

def IDl(o, movie):
    o.ID=movie
    sig=['id']
    sig.append(movie)
    return sig
def CopyrightL(o, movie):
    o.CopyrightL=movie
    sig=['copyright']
    sig.append(movie)
    return sig

def LyricsLanguage(o, movie):
    o.Language=movie
    sig=['language']
    sig.append(movie)
    return sig
####Album
class album:  
    def __init__(self,ID=None,Streamable=None,Name=None,MBID=None,Tracks=None,Tags=None,Artist=None,PlayCount=None,Rating=None,Listeners=None,URL=None,count=None,Date=None,artist_name=None,artist_id=None,music_genre=None,release_type=None,copyright=None): 
        self.ID=ID
        self.Name=Name
        self.Rating=Rating
        self.track_count=count
        self.ReleaseDate=Date
        self.artist_name=artist_name
        self.artist_id=artist_id
        self.music_genre=music_genre
        self.release_type=release_type
        self.Copyright = copyright
        self.Listeners=Listeners
        self.Artist=Artist
        self.URL=URL
        self.MBID=MBID
        self.Tracks=Tracks
        self.Tags=Tags
        self.PlayCount=PlayCount
        self.Streamable=Streamable
def Album(o): 
    b = str(o)
    c = album(o)
    instances['album'].update({c})
    globals()[b] = c
    sig=['Album']
    sig.append(c)
    return sig

def alName(o, movie):
    o.Name=movie
    sig=['name']
    sig.append(movie)
    return sig

def alStreamable(o, movie):
    o.Streamable=movie
    sig=['streamable']
    sig.append(movie)
    return sig

def alId(o, movie):
    o.ID=movie
    sig=['id']
    sig.append(movie)
    return sig
def alUrl(o, movie):
    o.URL=movie
    sig=['url']
    sig.append(movie)
    return sig
def alListeners(o, movie):
    o.Listeners=movie
    sig=['listeners']
    sig.append(movie)
    return sig
def alArtist(o, movie):
    o.Artist=movie
    sig=['artist']
    sig.append(movie)
    return sig
def alPlayCount(o, movie):
    o.PlayCount=movie
    sig=['playcount']
    sig.append(movie)
    return sig
def alCopyright(o, movie):
    o.Copyright=movie
    sig=['copyright']
    sig.append(movie)
    return sig
def alMBID(o, movie):
    o.MBID=movie
    sig=['mbid']
    sig.append(movie)
    return sig

def TrackCount(o, movie):
    o.track_count=movie
    sig=['track_count']
    sig.append(movie)
    return sig
def ReleaseDateAL(o, movie):
    o.ReleaseDate=movie
    sig=['releaseDate']
    sig.append(movie)
    return sig

def MusicGenre(o, movie):
    o.music_genre=movie
    sig=['music_genre']
    sig.append(movie)
    return sig
def ArtistName(o, movie):
    o.artist_name=movie
    sig=['artist_name']
    sig.append(movie)
    return sig
def ArtistId(o, movie):
    o.artist_id=movie
    sig=['artist_id']
    sig.append(movie)
    return sig
def ReleaseType(o, movie):
    o.release_type=movie
    sig=['release_type']
    sig.append(movie)
    return sig
def Rating(o, movie):
    o.Rating=movie
    sig=['rating']
    sig.append(movie)
    return sig

    #######################################Movie###############################################""
class movie:  
    def __init__(self,Id=None,Title=None,Year=None,Writer=None,ImdbRatings=None,ImdbVotes=None,Metascore=None,Type=None,DVD=None,BoxOffice=None,Production=None,Poster=None,Awards=None,Country=None,Runtime=None,Actors=None,Directors=None,Descriptions=None, Ratings=None, Genres=None,ReleaseDate=None,OriginalLanguage=None,Budget=None,Revenue=None): 
        self.Id=Id 
        self.Title =Title
        self.Actors = Actors
        self.ReleaseDate = ReleaseDate 
        self.OriginalLanguage = OriginalLanguage
        self.Directors=Directors
        self.Descriptions=Descriptions
        self.Ratings=Ratings
        self.Budget=Budget
        self.Revenue=Revenue
        self.Genres=Genres
        self.Year=Year
        self.Runtime=Runtime
        self.Writer=Writer
        self.Country=Country
        self.Awards=Awards
        self.Poster=Poster
        self.ImdbRatings=ImdbRatings
        self.ImdbVotes=ImdbVotes
        self.Metascore=Metascore
        self.Type=Type
        self.DVD=DVD
        self.BoxOffice=BoxOffice
        self.Production=Production
        self.Website=Website
def Movie(o): 
    b = str(o)
    c = movie(o)
    instances['movie'].update({c})
    globals()[b] = c
    sig=['Movie']
    sig.append(c)
    return sig

def TitleM(o, movie):
    o.Title=movie
    sig=['title']
    sig.append(movie)
    return sig
def Metascore(o, movie):
    o.Metascore=movie
    sig=['metascore']
    sig.append(movie)
    return sig
def Poster(o, movie):
    o.Poster=movie
    sig=['poster']
    sig.append(movie)
    return sig

def BoxOffice(o, movie):
    o.BoxOffice=movie
    sig=['boxoffice']
    sig.append(movie)
    return sig

def DVD(o, movie):
    o.DVD=movie
    sig=['dvd']
    sig.append(movie)
    return sig
def Production(o, movie):
    o.Production=movie
    sig=['production']
    sig.append(movie)
    return sig
def Country(o, movie):
    o.Country=movie
    sig=['country']
    sig.append(movie)
    return sig
def Awards(o, movie):
    o.Awards=movie
    sig=['awards']
    sig.append(movie)
    return sig
def ImdbRatings(o, movie):
    o.ImdbRatings=movie
    sig=['imdbratings']
    sig.append(movie)
    return sig
def ImdbVotes(o, movie):
    o.ImdbVotes=movie
    sig=['imdbvotes']
    sig.append(movie)
    return sig 
def Imdbid(o, movie):
    o.Imdbid=movie
    sig=['imdbid']
    sig.append(movie)
    return sig     
def Website(o, movie):
    o.Website=movie
    sig=['website']
    sig.append(movie)
    return sig
def Type(o, movie):
    o.type=movie
    sig=['type']
    sig.append(movie)
    return sig

def IDm(o, movie):
    o.Id=movie
    sig=['id']
    sig.append(movie)
    return sig

def Actors(o, movie):
    o.Actors=movie
    sig=['actors']
    sig.append(movie)
    return sig

def Directors(o, movie):
    o.Directors =movie
    sig=['directors']
    sig.append(movie)
    return sig


def Descriptions(o, movie):
    o.Descriptions =movie
    sig=['descriptions']
    sig.append(movie)
    return sig

def Budget(o, movie):
    o.Budget =movie
    sig=['budget']
    sig.append(movie)
    return sig


def Revenue(o, movie):
    o.Revenue =movie
    sig=['revenue']
    sig.append(movie)
    return sig


def Ratings(o, movie):
    o.Ratings =movie
    sig=['ratings']
    sig.append(movie)
    return sig


def Genres(o, movie):
    o.Genres =movie
    sig=['genres']
    sig.append(movie)
    return sig

def Year(o, movie):
    o.Year =movie
    sig=['year']
    sig.append(movie)
    return sig

def ReleaseDate(o, movie):
    o.ReleaseDate=movie
    sig=['releaseDate']
    sig.append(movie)
    return sig

def OriginalLanguage(o, movie):
    o.Language=movie
    sig=['language']
    sig.append(movie)
    return sig

###########################################################Important Test###################################"
########################################## Definition of data services in the service lake#####################################
####### FOR 9 services --> execution duration= 50 seconds
getPublisher=Data_Service('getPublisher',['isbn','title'],['publisher','author'],View('VgetPublisher(t1, isbn1, p1)',[Book("ob1"), Title(ob1, "t1"), ISBN(ob1, "isbn1"), BookPublisher(ob1,"p1"), Publisher("op1"), PublisherName(op1, "p1"), Publication(op1,ob1)]),10,0.59,0.28,0.7,19,7)
getBook=Data_Service('getBook',['isbn','title'],['isbn','edition','language','publisher'],View('VgetBook(t2, a2, isbn2, e2, l2, p2)',[Book('ob2'), Title(ob2, "t2"), ISBN(ob2, "isbn2"), Edition(ob2, "e2"),BookPublisher(ob2, "p2"), Language(ob2, "l2"), BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"), Wrote(oa2, ob2), Publisher("op2"),PublisherName(op2, "p2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)
getPublication=Data_Service('getPublication',['isbn'],['publisher','title','location'],View('VgetPublication(isbn3, p3, lc3)',[Book('ob3'), ISBN(ob3, "isbn3"), Publisher("op3"), PublisherName(op3, "p3"),Location(op3, "lc3"), Publication(op3, ob3)]),5,0.78,0.28,0.3,15,7)
getActor=Data_Service('getActor',['name'],['birthDate','nationality','gender','deathDate'],View('VgetActor(n,b,d,g,na)',[Actor('o1'), Name(o1, "n"), Gender(o1, "g"),BirthDate(o1, "b"), Nationality(o1, "na"), DeathDate(o1,"d"),Role("o2"),Actor_name(o2, "n")]),12,0.79,0.49,0.3,28,18)
getAuthor=Data_Service('getAuthor', ['isbn'],['author', 'title'],View('getAuthor(isbn3,a3,t3)',[Book("o3"),Title(o3,"t"),ISBN(o3, "isbn3"),BookAuthor(o3,"a"), Author("oa1"),AuthorName(oa1,"a"),Wrote(oa1,o3)]),13,0.29,0.78,0.6,21,23)
getBook2=Data_Service('getBook2',['isbn','title'],['isbn','edition','language','publisher'],View('VgetBook2(t2, a2, isbn2, e2, l2, p2)',[Book('ob2'), Title(ob2, "t2"), ISBN(ob2, "isbn2"), Edition(ob2, "e2"),BookPublisher(ob2, "p2"), Language(ob2, "l2"), BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"), Wrote(oa2, ob2), Publisher("op2"),PublisherName(op2, "p2"), Publication(op2, ob2)]),14,0.39,0.49,0.3,28,28)
getPublication2=Data_Service('getPublication2',['isbn'],['publisher','title','location'],View('VgetPublication2(isbn3, p3, lc3)',[Book('ob3'), ISBN(ob3, "isbn3"), Publisher("op3"), PublisherName(op3, "p3"),Location(op3, "lc3"), Publication(op3, ob3)]),2,0.52,0.38,0.3,15,17)
#getActor2=Data_Service('getActor2',['First_name','Last_name'],['Date_of_birth','nationality'],View('VgetActor2(f,l,d, n)',[Actor('o1'), First_name(o1, "f"), Last_name(o1, "l"),Date_of_birth(o1, "d"), Nationality(o1, "n"), Role("o2"),Actor_name(o2, "l")]),13,0.79,0.49,0.3,28,18)
#getAuthor2=Data_Service('getAuthor2', ['isbn'],['author', 'title'],View('getAuthor2(isbn3,a3,t3)',[Book("o3"),Title(o3,"t"),ISBN(ob3, "isbn3"),BookAuthor(o3,"a"), Author("oa1"),AuthorName(oa1,"a"),Wrote(oa1,o3)]),13,0.29,0.78,0.6,21,23)
#############The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users. 
###Movies 
getMovieInfoByTitle=Data_Service('getMovieInfoByTitle',['title'],['title','year','country','imdbid','imdbrating','type','dvd','boxoffice','production','imdbvotes','poster','awards','website','directors','descriptions','ratings','genres','budget','revenue','releaseDate','language','actors'],View('VgetMovieInfoByTitle(id,t,d,de,r,g,b,re,rd,l,v,rt,ac,d,tt,m,rd,c,aw,bo,pr)',[Movie('o'),Metascore(o,'m'),Website(o,'w'),Year(o,'y'),ReleaseDate(o,'rd'),Country(o,'c'),Awards(o,'aw'), Imdbid(o,"id"),ImdbVotes(o,'v'),ImdbRatings(o,'rt'),Actors(o,'ac'),TitleM(o, "t"),ReleaseDate(o,"rd"),Directors(o, "d"),Descriptions(o,"de"),Ratings(o,"r"),OriginalLanguage(o,"l"),Genres(o,"g"),Poster(o,"b"),DVD(o,'d'),Type(o,'tt'),BoxOffice(o,'bo'),Production(o,'pr')]),12,0.79,0.49,0.3,15,18)
getMovieInfoByTitle1=Data_Service('getMovieInfoByTitle1',['title','year'],['title','year','country','imdbid','imdbrating','type','dvd','boxoffice','production','imdbvotes','poster','awards','website','directors','descriptions','ratings','genres','budget','revenue','releaseDate','language','actors'],View('VgetMovieInfoByTitle1(id,t,d,de,r,g,b,re,rd,l,v,rt,ac,d,tt,m,rd,c,aw,bo,pr,y)',[Movie('o'),Metascore(o,'m'),Website(o,'w'),Year(o,'y'),ReleaseDate(o,'rd'),Country(o,'c'),Awards(o,'aw'), Imdbid(o,"id"),ImdbVotes(o,'v'),ImdbRatings(o,'rt'),Actors(o,'ac'),TitleM(o, "t"),ReleaseDate(o,"rd"),Directors(o, "d"),Descriptions(o,"de"),Ratings(o,"r"),OriginalLanguage(o,"l"),Genres(o,"g"),Poster(o,"b"),DVD(o,'d'),Type(o,'tt'),BoxOffice(o,'bo'),Production(o,'pr')]),12,0.79,0.49,0.3,15,18)
################LastFm.com (26 data services)
####Albums (3 methods)--> different signatures: 5 methods
getAlbumInfo1=Data_Service('getAlbumInfo1',['name','name'],['name','mbid','url','playcount','tags','listeners','name','streamable'],View('VgetAlbumInfo1(n1, n2, m,u,t1,l,p,b,s,si)',[Artist('ob2'), aName(ob2,'n2'),Album('o'),alName(o,'n2'),alUrl(o,'u'),alListeners(o,'l'),alPlayCount(o,'p'),alId(o,'i'),ReleaseDateAL(o,'r'),Tag('ob1'),tagId(ob1,'t1'),tagName(ob1,'nt'),tagUrl(ob1,'uc'),Recording('a'),Duration(a,'d'),TitleR(a,'rr'),Artist('si'),aName(si,'na'),aUrl(si,'ur'),MBID(si,'s')]),12,0.79,0.49,0.3,15,18)
getAlbumInfo2=Data_Service('getAlbumInfo2',['name','name'],['name','mbid','url','playcount','tags','listeners','name','streamable'],View('VgetAlbumInfo2(n1, n2, m,u,t1,l,p,b,s,si)',[Artist('ob2'), aName(ob2,'n2'),Album('o'),alName(o,'n2'),alUrl(o,'u'),alListeners(o,'l'),alPlayCount(o,'p'),alId(o,'i'),ReleaseDateAL(o,'r'),Tag('ob1'),tagId(ob1,'t1'),tagName(ob1,'nt'),tagUrl(ob1,'uc'),Recording('a'),Duration(a,'d'),TitleR(a,'rr'),Artist('si'),aName(si,'na'),aUrl(si,'ur'),MBID(si,'s')]),12,0.79,0.49,0.3,15,18)
getAlbumTags1=Data_Service('getAlbumTags1',['name','name'],['name','url'],View('VgetAlbumTags1(n1,n, n2,u)',[Artist('ob2'), aName(ob2,'n1'),Album('o'),alName(o,'n'),Tag('ob1'),tagName(ob1,'n2'),tagUrl(ob1,'u')]),12,0.79,0.49,0.3,15,18)
getAlbumTags2=Data_Service('getAlbumTags2',['name','name','mbid'],['name','url'],View('VgetAlbumTags2(n1,n,m, n2,u)',[Artist('ob2'), aName(ob2,'n1'),Album('o'),alName(o,'n'),alMBID(o,'m'),Tag('ob1'),tagName(ob1,'n2'),tagUrl(ob1,'u')]),12,0.79,0.49,0.3,15,18)
getAlbumsBySearch=Data_Service('getAlbumsBySearch',['name'],['name','url','streamable','id','streamable'],View('VgetAlbumsBySearch(n1,m, n2,u)',[Artist('ob2'), aName(ob2,'n1'),Album('o'),alName(o,'n2'),alUrl(o,'u'),alId(o,'i'),alStreamable(o,'m')]),12,0.79,0.49,0.3,15,18)
####Artists (7 methods with different fonctionalities --> 12)
getArtistCorrection=Data_Service('getArtistCorrection',['name'],['name','mbid','url'],View('VgetArtistCorrection(n1, n2, m,u)',[Artist('ob1'), aName(ob1,"n1"), Artist('ob2'), aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u')]),12,0.79,0.49,0.3,15,18)
getArtistInfo1=getArtistInfo2=Data_Service('getArtistInfo2',['name','mbid'],['name','mbid','url','tracks','tags','listeners','plays','biography','streamable','artist'],View('VgetArtistInfo2(n1, n2, m,u,t1,l,p,b,s,si)',[Artist('ob2'), aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u'),Tag('ob1'),tagId(ob1,'t1'),tagName(ob1,'nt'),tagUrl(ob1,'uc'),Plays(ob2,'p'),Listeners(ob2,'l'),aStreamable(ob2,'s'),Biography('ob4'),bPublished(ob4,'bp'),bSummary(ob4,'su'), bContent(ob4,'c'),Artist('si'),aName(si,'na'),aUrl(si,'ur')]),12,0.79,0.49,0.3,15,18)
getArtistTags1=Data_Service('getArtistTags1',['name'],['name','url'],View('VgetArtistTags1(n1, n2,u)',[Artist('ob2'), aName(ob2,'n1'),Tag('ob1'),tagName(ob1,'n2'),tagUrl(ob1,'u')]),12,0.79,0.49,0.3,15,18)
getArtistTags2=Data_Service('getArtistTags2',['name','mbid'],['name','url'],View('VgetArtistTags2(n1,m,n2,u)',[Artist('ob2'), aName(ob2,'n1'),MBID(ob2,'m'),Tag('ob1'),tagName(ob1,'n2'),tagUrl(ob1,'u')]),12,0.79,0.49,0.3,15,18)
getTopAlbumsByArtist1=Data_Service('getTopAlbumsByArtist1',['name','mbid'],['name','url','Listeners'],View('VgetTopAlbumsByArtist1(n1,m,n2,u,l)',[Artist('ob2'), aName(ob2,'n1'),MBID(ob2,'m'),Album('ob1'),alName(ob1,'n2'),alUrl(ob1,'u'),alListeners(ob1,'l')]),12,0.79,0.49,0.3,15,18)
getTopAlbumsByArtist2=Data_Service('getTopAlbumsByArtist2',['name'],['name','url','listeners'],View('VgetTopAlbumsByArtist1(n1,n2,u,l)',[Artist('ob2'), aName(ob2,'n1'),Album('ob1'),alName(ob1,'n2'),alUrl(ob1,'u'),alListeners(ob1,'l')]),12,0.79,0.49,0.3,15,18)
getSimilarArtists1=Data_Service('getSimilarArtists1',['name'],['name','mbid','url','streamable'],View('VgetSimilarArtists1(n1, n2, m,u,s)',[Artist('ob1'), aName(ob1,"n1"), Artist('ob2'), aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u'),aStreamable(ob2,'s')]),12,0.79,0.49,0.3,15,18)
getSimilarArtists2=Data_Service('getSimilarArtists2',['name','mbid'],['name','mbid','url','streamable'],View('VgetSimilarArtists2(n1, n2,mm, m,u,s)',[Artist('ob1'), aName(ob1,"n1"),MBID(ob1, "mm"), Artist('ob2'), aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u'),aStreamable(ob2,'s')]),12,0.79,0.49,0.3,15,18)
getTopTracksByArtist1=Data_Service('getTopTracksByArtist1',['name','mbid'],['title','url','playcount','listeners'],View('VgetTopTracksByArtist1(n1,m,t,u,l,p)',[Artist('ob2'), aName(ob2,'n1'),MBID(ob2,'m'),Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),rListeners(ob1,'l'),PlayCount(ob1,'p')]),12,0.79,0.49,0.3,15,18)
getTopTracksByArtist2=Data_Service('getTopTracksByArtist2',['name'],['title','url','playcount','listeners'],View('VgetTopTracksByArtist2(n1,t,u,l,p)',[Artist('ob2'), aName(ob2,'n1'),Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),rListeners(ob1,'l'),PlayCount(ob1,'p')]),12,0.79,0.49,0.3,15,18)
getArtistsBySearch=Data_Service('getArtistsBySearch',['name'],['name','mbid','url','streamable'],View('VgetArtistsBySearch(n1,m,u,s)',[Artist('ob2'), aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u'),aStreamable(ob2,'s')]),12,0.79,0.49,0.3,15,18)
getAllArtists=Data_Service('getAllArtists',['Artist'],['name','mbid','url','playcount','tagcount','streamable'],View('VgetAllArtists(n,m,u,t,p,s)',[Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'u'),aStreamable(ob2,'s'),aPlayCount(ob2,'p'),aTagCount(ob2,'t')]),12,0.79,0.49,0.3,15,18)
####Charts (3 methods without required inputs)---> do we need it!!!
# getTopArtists=
# getTopTags=
# getTopTracks=
####Geo (2 methods)--> 4 methods with different signatures
getTopArtistsByCountry=Data_Service('getTopArtistsByCountry',['nationalityA'],['Artist','name','mbid','url','playcount','streamable'],View('VgetTopArtistsByCountry(c,n1,m,u,p,s)',[Artist('ob2'), aNationality(ob2,'c'),aPlayCount(ob2,'p'),aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u'),aStreamable(ob2,'s')]),12,0.79,0.49,0.3,15,18)
getTopTracksByCountry=Data_Service('getTopTracksByCountry',['country'],['Recording','title','playcount','url','streamable','Artist','name','mbid','url'],View('VgetTopTracksByCountry(c,r,n,m,u,p,s,ua)',[Recording('ob1'),RCountry(ob1,'c'),TitleR(ob1,'t'),PlayCount(ob1,'p'),rURL(ob1,'u'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua')]),12,0.79,0.49,0.3,15,18)
getTopArtistsByCountry1=Data_Service('getTopArtistsByCountry1',['nationalityA','address'],['Artist','name','mbid','url','playcount','streamable'],View('VgetTopArtistsByCountry1(a,c,n1,m,u,p,s)',[Artist('ob2'), aNationality(ob2,'c'),aAddress(ob2,'a'), aPlayCount(ob2,'p'),aName(ob2,'n2'),MBID(ob2, "m"),aUrl(ob2,'u'),aStreamable(ob2,'s')]),12,0.79,0.49,0.3,15,18)
getTopTracksByCountry1=Data_Service('getTopTracksByCountry1',['country','location'],['Recording','title','playcount','url','streamable','Artist','name','mbid','url'],View('VgetTopTracksByCountry1(l,c,r,n,m,u,p,s,ua)',[Recording('ob1'),RCountry(ob1,'c'),RLocation(ob1,'l'),TitleR(ob1,'t'),PlayCount(ob1,'p'),rURL(ob1,'u'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua')]),12,0.79,0.49,0.3,15,18)
####Tracks (5 methods)
getTrackCorrection=Data_Service('getTrackCorrection',['title','name'],['Recording','title','url','Artist','name','mbid','url'],View('VgetTrackCorrection(t,n,u,m,ua)',[Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua')]),12,0.79,0.49,0.3,15,18)
getTrackInfo1=Data_Service('getTrackInfo1',['title','name','mbid'],['Recording','id','title','url','Artist','name','mbid','url','Album','name','url','mbid','Tag','name','url','Wiki','published','content','summary'],View('VgetTrackInfo1(rt,t,t,i,n,u,s,p,rl,d,m,ua,au,am,na,tn,tu,wp,wc,ws)',[Recording('ob1'),rMBID(ob1,'rt'),TitleR(ob1,'t'),rId(ob1,'i'),Duration(ob1,'d'),rURL(ob1,'u'),rStreamable(ob1,'s'),PlayCount(ob1,'p'),rListeners(ob1,'rl'), Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua'),Album('o'),alName(o,'na'),alUrl(o,'au'),alMBID(o,'am'),Tag('ob'),tagName(ob,'tn'),tagUrl(ob,'tu'),Wiki('ob4'),wPublished(ob4,'wp'),wSummary(ob4,'ws'), wContent(ob4,'wc')]),12,0.79,0.49,0.3,15,18)
getTrackInfo=Data_Service('getTrackInfo',['title','name'],['Recording','id','title','url','Artist','name','mbid','url','Album','name','url','mbid','Tag','name','url','Wiki','published','content','summary'],View('VgetTrackInfo(t,i,n,u,s,p,rl,d,m,ua,au,am,na,tn,tu,wp,wc,ws)',[Recording('ob1'),TitleR(ob1,'t'),rId(ob1,'i'),Duration(ob1,'d'),rURL(ob1,'u'),rStreamable(ob1,'s'),PlayCount(ob1,'p'),rListeners(ob1,'rl'), Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua'),Album('o'),alName(o,'na'),alUrl(o,'au'),alMBID(o,'am'),Tag('ob'),tagName(ob,'tn'),tagUrl(ob,'tu'),Wiki('ob4'),wPublished(ob4,'wp'),wSummary(ob4,'ws'), wContent(ob4,'wc')]),12,0.79,0.49,0.3,15,18)
getSimilarTracks=Data_Service('getSimilarTracks',['title','name'],['Recording','title','url','streamable','Artist','name','mbid','url'],View('VgetSimilarTracks(t,n,u,m,s,ua)',[Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua')]),12,0.79,0.49,0.3,15,18)
getSimilarTracks1=Data_Service('getSimilarTracks1',['title','name','mbid'],['Recording','title','url','streamable','Artist','name','mbid','url'],View('VgetSimilarTracks1(t,mt,n,u,m,s,ua)',[Recording('ob1'),rMBID(ob1,'rt'),TitleR(ob1,'t'),rURL(ob1,'u'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua')]),12,0.79,0.49,0.3,15,18)
getTrackTags=Data_Service('getTrackTags',['title','name'],['Tag','name','url','count'],View('VgetTrackTags(t,n,tn,tu,tc)',[Recording('ob1'),TitleR(ob1,'t'),Artist('ob2'), aName(ob2,'n'),Tag('ob'),tagName(ob,'tn'),tagUrl(ob,'tu'),tagCount(ob,'tc')]),12,0.79,0.49,0.3,15,18)
getTrackTags1=Data_Service('getTrackTags1',['title','name','mbid'],['Tag','name','url','count'],View('VgetTrackTags1(t,m,n,tn,tu,tc)',[Recording('ob1'),rMBID(ob1,'m'),TitleR(ob1,'t'),Artist('ob2'), aName(ob2,'n'),Tag('ob'),tagName(ob,'tn'),tagUrl(ob,'tu'),tagCount(ob,'tc')]),12,0.79,0.49,0.3,15,18)
getTracksBySearch=Data_Service('getTracksBySearch',['title','name'],['Recording','title','url','Artist','name','url','streamable','listeners'],View('VgetTracksBySearch(t,n,u,s,l)',[Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),rListeners(ob1,'l'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n')]),12,0.79,0.49,0.3,15,18)
getTracksBySearch1=Data_Service('getTracksBySearch1',['title'],['Recording','title','url','Artist','name','url','streamable','listeners'],View('VgetTracksBySearch1(t,n,u,s,l)',[Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),rListeners(ob1,'l'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n')]),12,0.79,0.49,0.3,15,18)
####Tags (6 methods)
getTopTracksByTag=Data_Service('getTopTracksByTag',['Tag','name'],['Recording','title','url','streamable','Artist','name','mbid','url'],View('VgetTopTracksByTag(r,n,m,u,p,s,ua)',[Tag('c'),tagName(c,'n'),Recording('ob1'),TitleR(ob1,'t'),rURL(ob1,'u'),rStreamable(ob1,'s'),Artist('ob2'), aName(ob2,'n'),MBID(ob2, "m"),aUrl(ob2,'ua')]),12,0.79,0.49,0.3,15,18)
getTopArtistsByTag=Data_Service('getTopArtistsByTag',['Tag','name'],['streamable','Artist','name','mbid','url'],View('VgetTopArtistsByTag(n,m,s,na,ua)',[Tag('c'),tagName(c,'n'),Artist('ob2'), aName(ob2,'na'),MBID(ob2, "m"),aUrl(ob2,'ua'),aStreamable(ob2,'s')]),12,0.79,0.49,0.3,15,18)
getTopAlbumsByTag=Data_Service('getTopAlbumsByTag',['Tag','name'],['Album','name','url','Artist','name','url','mbid',],View('VgetTopAlbumsByTag(n,n1, n2, m,u,ua)',[Tag('c'),tagName(c,'n'),Artist('ob2'), aName(ob2,'n1'),aUrl(ob2,'ua'), Album('o'),alName(o,'n2'),alUrl(o,'u'),MBID(ob2,'m')]),12,0.79,0.49,0.3,15,18)
# getTagInfo=
# getSimilarTags=
# getWeeklyChartList=
############################################# data services from the isbndb###################################"########
#####Books API ######
getBookByIsbn=Data_Service('getBookByIsbn',['isbn'],['title','edition','language','subject'],View('VgetBookByIsbn(t2, isbn2, e2, l2,s2)',[Book('ob2'), Title(ob2, "t2"),Subject(ob2,"s2"), Edition(ob2, "e2"), Language(ob2, "l2")]),12,0.79,0.49,0.3,15,18)
getBookByAuthor=Data_Service('getBookByAuthor',['author'],['isbn','title','edition','language','subject'],View('VgetBookByAuthor(t2, a2, isbn2, e2, l2,s2)',[Book('ob2'), Title(ob2, "t2"),Subject(ob2,"s2"), ISBN(ob2, "isbn2"), Edition(ob2, "e2"), Language(ob2, "l2"), BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"), Wrote(oa2, ob2)]),12,0.79,0.49,0.3,15,18)
getBookByPublisher=Data_Service('getBookByPublisher',['publisher'],['isbn','edition','language','title','subject'],View('VgetBookByPublisher(t2, isbn2, e2, l2, p2,s2)',[Book('ob2'), Subject(ob2,"s2"),Title(ob2, "t2"), ISBN(ob2, "isbn2"), Edition(ob2, "e2"),BookPublisher(ob2, "p2"), Language(ob2, "l2"), Publisher("op2"),PublisherName(op2, "p2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)

#####Authors API#####
getAuthorByIsbn=Data_Service('getAuthorByIsbn',['isbn'],['AuthorName','Date_of_birthA','nationalityA'],View('VgetAuthorByIsbn(isbn2, a2, d2,n2)',[Book('ob2'), ISBN(ob2, "isbn2"),BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"),Date_of_birthA(oa2,"d2"),NationalityA(oa2,"n2"), Wrote(oa2, ob2)]),12,0.79,0.49,0.3,15,18)
getAuthorByTitle=Data_Service('getAuthorByTitle',['title'],['AuthorName','Date_of_birthA','nationalityA'],View('VgetAuthorByTitle(isbn2, a2, d2,n2)',[Book('ob2'), Title(ob2, "isbn2"),BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"),Date_of_birthA(oa2,"d2"),NationalityA(oa2,"n2"),Wrote(oa2, ob2)]),12,0.79,0.49,0.3,15,18)
getAuthor1ByIsbn=Data_Service('getAuthorByIsbn',['isbn'],['AuthorName','Date_of_birthA','nationalityA'],View('VgetAuthorByIsbn(isbn2, a2, d2,n2)',[Book('ob2'), ISBN(ob2, "isbn2"),BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"),Date_of_birthA(oa2,"d2"),NationalityA(oa2,"n2"), Wrote(oa2, ob2)]),12,0.79,0.49,0.3,15,18)
getAuthor2ByTitle=Data_Service('getAuthorByTitle',['title'],['AuthorName','Date_of_birthA','nationalityA'],View('VgetAuthorByTitle(isbn2, a2, d2,n2)',[Book('ob2'), Title(ob2, "isbn2"),BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"),Date_of_birthA(oa2,"d2"),NationalityA(oa2,"n2"),Wrote(oa2, ob2)]),12,0.79,0.49,0.3,15,18)

# #####Publishers API#####

getPublisherByIsbn=Data_Service('getPublisherByIsbn',['isbn'],['PublisherName','Location','NationalityP'],View('VgetPublisherByIsbn(isbn2, p2, l2,n2)',[Book('ob2'), ISBN(ob2, "isbn2"),BookPublisher(ob2, "p2"),Publisher("op2"), PublisherName(op2, "p2"),Location(op2,"l2"),NationalityP(op2,"n2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)
getPublisherByTitle=Data_Service('getPublisherByTitle',['title'],['PublisherName','Location','NationalityP'],View('VgetPublisherByTitle(title2, a2, d2,n2)',[Book('ob2'), Title(ob2, "title2"),BookPublisher(ob2, "p2"),Publisher("op2"), PublisherName(op2, "p2"),Location(op2,"l2"),NationalityP(op2,"n2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)
getPublisherByIsbn2=Data_Service('getPublisherByIsbn',['isbn'],['PublisherName','Location','NationalityP'],View('VgetPublisherByIsbn(isbn2, p2, l2,n2)',[Book('ob2'), ISBN(ob2, "isbn2"),BookPublisher(ob2, "p2"),Publisher("op2"), PublisherName(op2, "p2"),Location(op2,"l2"),NationalityP(op2,"n2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)
getPublisherByTitle2=Data_Service('getPublisherByTitle',['title'],['PublisherName','Location','NationalityP'],View('VgetPublisherByTitle(title2, a2, d2,n2)',[Book('ob2'), Title(ob2, "title2"),BookPublisher(ob2, "p2"),Publisher("op2"), PublisherName(op2, "p2"),Location(op2,"l2"),NationalityP(op2,"n2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)

###Movies API
##IVA offers a complete movie metadata package of official studio data sourced and curated from multiple 
#official sites and programmatically checked or hand verified for consistency and accuracy. IVA's Movie API
 #is your connection to a treasure trove of metadata, images, and video essential to any entertainment, 
 #content discovery, or recommendation system. 
getMovieById=Data_Service('getMovieById',['id'],['title','directors','descriptions','ratings','genres','budget','revenue','releaseDate','language'],View('VgetMovieById(id,t,d,de,r,g,b,re,rd,l)',[Movie('o'), IDm(o,"id"),TitleM(o, "t"),ReleaseDate(o,"rd"),Directors(o, "d"),Descriptions(o,"de"),Ratings(o,"r"),Revenue(o,"re"),OriginalLanguage(o,"l"),Genres(o,"g"),Budget(o,"b")]),12,0.79,0.49,0.3,15,18)
getMovieByTitle=Data_Service('getMovieByTitle',['title'],['id','directors','descriptions','ratings','genres','budget','revenue','releaseDate','language'],View('VgetMovieById(id,t,d,de,r,g,b,re,rd,l)',[Movie('o'), IDm(o,"id"),TitleM(o, "t"),ReleaseDate(o,"rd"),Directors(o, "d"),Descriptions(o,"de"),Ratings(o,"r"),Revenue(o,"re"),OriginalLanguage(o,"l"),Genres(o,"g"),Budget(o,"b")]),12,0.79,0.49,0.3,15,18)
getMovieById1=Data_Service('getMovieById',['id'],['title','directors','descriptions','ratings','genres','budget','revenue','releaseDate','language'],View('VgetMovieById(id,t,d,de,r,g,b,re,rd,l)',[Movie('o'), IDm(o,"id"),TitleM(o, "t"),ReleaseDate(o,"rd"),Directors(o, "d"),Descriptions(o,"de"),Ratings(o,"r"),Revenue(o,"re"),OriginalLanguage(o,"l"),Genres(o,"g"),Budget(o,"b")]),12,0.79,0.49,0.3,15,18)
getMovieByTitle1=Data_Service('getMovieByTitle',['title'],['id','directors','descriptions','ratings','genres','budget','revenue','releaseDate','language'],View('VgetMovieById(id,t,d,de,r,g,b,re,rd,l)',[Movie('o'), IDm(o,"id"),TitleM(o, "t"),ReleaseDate(o,"rd"),Directors(o, "d"),Descriptions(o,"de"),Ratings(o,"r"),Revenue(o,"re"),OriginalLanguage(o,"l"),Genres(o,"g"),Budget(o,"b")]),12,0.79,0.49,0.3,15,18)

###
getMovie=Data_Service('getMovie',['title','releaseDate'],['id','language','ratings'],View('VgetMovie(t, re, id, l,ra)',[Movie("o1"), TitleM(o1, "t"), ReleaseDate(o1, "re"), Ratings(o1,"ra"), OriginalLanguage(o1,"l"), IDm(o1,"id")]),10,0.59,0.28,0.7,19,7)
###Music API
##provide metadata about an astonishing range of music because it aggregates existing, well maintained, online databases. 
####musicbrainz.com 
####Recording API
getRecordingByPUID=Data_Service('getRecordingByPUID',['puid'],['title','directors','artists','duration'],View('VgetRecordingByPUID(puid, d, t,ar,di)',[Recording('ob2'), PUID(ob2, "puid"),Duration(ob2, "d"),TitleR(ob2,"t"), Artists(ob2, "ar"),DirectorsR(ob2,"di")]),12,0.79,0.49,0.3,15,18)
getRecordingByTitle=Data_Service('getRecordingByTitle',['title'],['puid','directors','artists','duration','genres','language','releaseDate','ratings','budget','revenue'],View('VgetRecordingByTitle(title2, a2, d2,n2)',[Recording('ob2'), PUID(ob2, "puid"),Duration(ob2, "d"),TitleR(ob2,"t"), Artists(ob2, "ar"),DirectorsR(ob2,"di"), RevenueR(ob2, "re"),BudgetR(ob2, "b"),RatingsR(ob2,"ra"), GenresR(ob2, "g"),LanguageR(ob2,"l")]),12,0.79,0.49,0.3,15,18)
####Cover Art Archive
####...
####MusixMatch.com API (https://developer.musixmatch.com/documentation/input-parameters)
###Lyrics Endpoint
getLyricsByTrack=Data_Service('getLyricsByTrack',['id'],['id','language','body','copyright'],View('VgetLyricsByTrack(i1, i2, l,b,c)',[Recording('ob2'), PUID(ob2, "i1"),Lyrics('ob1'),Body(ob1,"b"), IDl(ob1, "i2"),CopyrightL(ob1,"c"),LyricsLanguage(ob1,"l")]),12,0.79,0.49,0.3,15,18)
####Albums Endpoint
getAlbumByArtistName=Data_Service('getAlbumByArtistName',['id'],['id','language','body','copyright'],View('VgetAlbumByArtistName(i1, i2, l,b,c)',[Recording('ob2'), PUID(ob2, "i1"),Lyrics('ob1'),Body(ob1,"b"), IDl(ob1, "i2"),CopyrightL(ob1,"c"),LyricsLanguage(ob1,"l")]),12,0.79,0.49,0.3,15,18)
getAlbumByArtistId=Data_Service('getAlbumByArtistId',['id'],['id','language','body','copyright'],View('VgetAlbumByArtistId(i1, i2, l,b,c)',[Recording('ob2'), PUID(ob2, "i1"),Lyrics('ob1'),Body(ob1,"b"), IDl(ob1, "i2"),CopyrightL(ob1,"c"),LyricsLanguage(ob1,"l")]),12,0.79,0.49,0.3,15,18)
getAlbumById=Data_Service('getAlbumById',['id'],['id','language','body','copyright'],View('VgetAlbumById(i1, i2, l,b,c)',[Recording('ob2'), PUID(ob2, "i1"),Lyrics('ob1'),Body(ob1,"b"), IDl(ob1, "i2"),CopyrightL(ob1,"c"),LyricsLanguage(ob1,"l")]),12,0.79,0.49,0.3,15,18)
getAlbumByArtistTitle=Data_Service('getAlbumByArtistTitle',['id'],['id','language','body','copyright'],View('VgetAlbumByArtistTitle(i1, i2, l,b,c)',[Recording('ob2'), PUID(ob2, "i1"),Lyrics('ob1'),Body(ob1,"b"), IDl(ob1, "i2"),CopyrightL(ob1,"c"),LyricsLanguage(ob1,"l")]),12,0.79,0.49,0.3,15,18)


getPublisher3=Data_Service('getPublisher3',['isbn1','title1'],['publisher1','author1'],View('VgetPublisher3(t1, isbn1, p1)',[Book("ob1"), Title(ob1, "t1"), ISBN(ob1, "isbn1"), BookPublisher(ob1,"p1"), Publisher("op1"), PublisherName(op1, "p1"), Publication(op1,ob1)]),10,0.59,0.28,0.7,19,7)
getBook3=Data_Service('getBook3',['isbn','title1'],['isbn','edition','language1','publisher1'],View('VgetBook3(t2, a2, isbn2, e2, l2, p2)',[Book('ob2'), Title(ob2, "t2"), ISBN(ob2, "isbn2"), Edition(ob2, "e2"),BookPublisher(ob2, "p2"), Language(ob2, "l2"), BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"), Wrote(oa2, ob2), Publisher("op2"),PublisherName(op2, "p2"), Publication(op2, ob2)]),12,0.79,0.49,0.3,15,18)
getPublication3=Data_Service('getPublication3',['isbn'],['publisher','title','location'],View('VgetPublication3(isbn3, p3, lc3)',[Book('ob3'), ISBN(ob3, "isbn3"), Publisher("op3"), PublisherName(op3, "p3"),Location(op3, "lc3"), Publication(op3, ob3)]),5,0.78,0.28,0.3,15,7)
# #getMovie=Data_Service('getMovie',['Title','Date'],['Actors','Language'],View('VgetMovie(t, d, ac, l)',[Movie("o1"), Title(o1, "t"), Date(o1, "d"), Actors(o1,"ac"), Language(o1,"l"), Role("o"), Movie_title(o,"t")]),10,0.59,0.28,0.7,19,7)
# getActor3=Data_Service('getActor3',['First_name1','Last_name1'],['Date_of_birth1','nationality'],View('VgetActor3(f,l,d, n)',[Actor('o1'), First_name(o1, "f"), Last_name(o1, "l"),Date_of_birth(o1, "d"), Nationality(o1, "n"), Role("o2"),Actor_name(o2, "l")]),12,0.79,0.49,0.3,28,18)
# getAuthor3=Data_Service('getAuthor3', ['isbn'],['author', 'title1'],View('getAuthor3(isbn3,a3,t3)',[Book("o3"),Title(o3,"t"),ISBN(ob3, "isbn3"),BookAuthor(o3,"a"), Author("oa1"),AuthorName(oa1,"a"),Wrote(oa1,o3)]),13,0.29,0.78,0.6,21,23)
# getBook4=Data_Service('getBook4',['isbn','title'],['isbn','edition1','language','publisher1'],View('VgetBook4(t2, a2, isbn2, e2, l2, p2)',[Book('ob2'), Title(ob2, "t2"), ISBN(ob2, "isbn2"), Edition(ob2, "e2"),BookPublisher(ob2, "p2"), Language(ob2, "l2"), BookAuthor(ob2, "a2"),Author("oa2"), AuthorName(oa2, "a2"), Wrote(oa2, ob2), Publisher("op2"),PublisherName(op2, "p2"), Publication(op2, ob2)]),14,0.39,0.49,0.3,28,28)
# getPublication4=Data_Service('getPublication4',['isbn'],['publisher1','title','location1'],View('VgetPublication4(isbn3, p3, lc3)',[Book('ob3'), ISBN(ob3, "isbn3"), Publisher("op3"), PublisherName(op3, "p3"),Location(op3, "lc3"), Publication(op3, ob3)]),2,0.52,0.38,0.3,15,17)
# getActor4=Data_Service('getActor4',['First_name1','Last_name1'],['Date_of_birth1','nationality'],View('VgetActor4(f,l,d, n)',[Actor('o1'), First_name(o1, "f"), Last_name(o1, "l"),Date_of_birth(o1, "d"), Nationality(o1, "n"), Role("o2"),Actor_name(o2, "l")]),13,0.79,0.49,0.3,28,18)
# getAuthor4=Data_Service('getAuthor4', ['isbn'],['author', 'title'],View('getAuthor4(isbn3,a3,t3)',[Book("o3"),Title(o3,"t"),ISBN(ob3, "isbn3"),BookAuthor(o3,"a"), Author("oa1"),AuthorName(oa1,"a"),Wrote(oa1,o3)]),13,0.29,0.78,0.6,21,23)
#define other data services that can not deliver the desired missing information... (60 data services)
###53 data services 
Service_lake=[]
Service_lake.append(getPublisher)#1
Service_lake.append(getBook)#2
Service_lake.append(getPublication)#3
#Service_lake.append(getMovie)
Service_lake.append(getActor)#4
Service_lake.append(getAuthor)#5
#Service_lake.append(getBook2)#6
#Service_lake.append(getPublication2)#7
#Service_lake.append(getActor2)
#Service_lake.append(getAuthor2)
# print("check for service ide")
# for service in Service_lake:
#     print(service.ide)
###Append data services from the isbndb site (we added 7 services till now)
Service_lake.append(getBookByPublisher)#8
Service_lake.append(getBookByIsbn)#9
#Service_lake.append(getBookByAuthor)
Service_lake.append(getAuthorByTitle)#10
Service_lake.append(getAuthorByIsbn)#11
#Service_lake.append(getAuthor2ByTitle)
#Service_lake.append(getAuthor1ByIsbn)
Service_lake.append(getMovieById)#12
Service_lake.append(getMovieByTitle)#13
Service_lake.append(getMovieById1)#14
Service_lake.append(getMovieByTitle1)#15
#Service_lake.append(getPublisherByTitle)
#Service_lake.append(getPublisherByIsbn)
Service_lake.append(getRecordingByTitle)#16
Service_lake.append(getRecordingByPUID)#17
Service_lake.append(getLyricsByTrack)#18
#Service_lake.append(c)
#Service_lake.append(getPublisher3)
#Service_lake.append(getBook3)
#Service_lake.append(getPublication3)
# #Service_lake.append(getMovie)
# Service_lake.append(getActor3)
# Service_lake.append(getAuthor3)
# Service_lake.append(getBook4)
# Service_lake.append(getPublication4)
# Service_lake.append(getActor4)
# Service_lake.append(getAuthor4)
Service_lake.append(getArtistCorrection)#19
Service_lake.append(getSimilarArtists2)#20
Service_lake.append(getSimilarArtists1)#21
Service_lake.append(getArtistInfo2)#22
Service_lake.append(getArtistInfo1)#23
Service_lake.append(getArtistTags1)#24
Service_lake.append(getArtistTags2)#25
Service_lake.append(getTopAlbumsByArtist1)#26
Service_lake.append(getTopAlbumsByArtist2)#27
Service_lake.append(getTopTracksByArtist1)#28
Service_lake.append(getTopTracksByArtist2)#29
Service_lake.append(getArtistsBySearch)#30
Service_lake.append(getAlbumTags2)#31
Service_lake.append(getAlbumTags1)#32
Service_lake.append(getAlbumInfo2)#33
Service_lake.append(getAlbumInfo1)#34
Service_lake.append(getAlbumsBySearch)#35
Service_lake.append(getTopTracksByCountry1)#36
Service_lake.append(getTopTracksByCountry)#37
Service_lake.append(getTopArtistsByCountry1)#38
Service_lake.append(getTopArtistsByCountry)#39
Service_lake.append(getTrackCorrection)#40
Service_lake.append(getTrackInfo)#41
Service_lake.append(getTrackInfo1)#42
Service_lake.append(getSimilarTracks1)#43
Service_lake.append(getSimilarTracks)#44
Service_lake.append(getTrackTags)#45
Service_lake.append(getTrackTags1)#46
Service_lake.append(getTracksBySearch1)#47
Service_lake.append(getTracksBySearch)#48
Service_lake.append(getTopTracksByTag)#49
Service_lake.append(getTopAlbumsByTag )#50
Service_lake.append(getTopArtistsByTag )#51
Service_lake.append(getMovieInfoByTitle1)#52
Service_lake.append(getMovieInfoByTitle)#53
