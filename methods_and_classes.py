import sqlite3
class Single():
    def __init__(self,name,singer,albume,pro_comp,duration):
        self.name = name
        self.singer = singer
        self.albume = albume
        self.pro_comp = pro_comp
        self.duration = duration
    def __str__(self):
        data = "Song Name: {}\n Singer: {}\nAlbume: {}\nProduction Company: {}\nSong Duration: {}"
        return data.format(self.name,self.singer,self.albume,self.pro_comp,self.duration)
class SingleLibrary():
    def __init__(self):
        self.connection = sqlite3.connect("single_library.db")
        self.cursor = self.connection.cursor()
        self.cre_def_sin_tab()
        self.total_dur = 0
    def cre_def_sin_tab(self):
        self.cursor.execute("create table if not exists singles(name TEXT,singer TEXT,albume TEXT,prod TEXT,durat INT)")
        self.connection.commit()
    def calc_total_am(self):
        self.cursor.execute("select * from singles")
        singles = self.cursor.fetchall()
        for single in singles:
            self.total_dur += single[4]
        minutes = self.total_dur // 60
        seconds = self.total_dur % 60
        print("Total duration is {} minutes and {} seconds".format(minutes,seconds))
    def add_song(self,a,b,c,d,e):
        query = "insert into singles Values(?,?,?,?,?)"
        self.cursor.execute(query,(a,b,c,d,e))
        self.connection.commit()
    def delete_song(self,name):
        query = "delete from singles where name = ?"
        self.cursor.execute(query,(name,))
        self.connection.commit()
single_library = SingleLibrary()

        

        
