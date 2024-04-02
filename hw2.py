class Superhero:
 people = 'people'

 def __init__(self,name,nickname,superpower,
                health_points,catchphrase):
       self.name = name
       self.nickname = nickname
       self.superpower = superpower
       self.health_points = health_points
       self.catchphrase = catchphrase

 def get_name(self):
       return self.name

 def double_health(self):
       self.health_points *= 2

 def __str__(self):
    return f"Nickname:{self.nickname},Superpower:{self.superpower},Health:{self.health_points}"

 def __len__(self):
       return (
       len(self.catchphrase))
hero = Superhero("Iron Man","Toni Stark","Genius",100,"I am Iron Man")


print(hero.get_name())
hero.double_health()
print(hero)
print(len(hero))
