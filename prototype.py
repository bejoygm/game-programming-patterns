class Monster:
    def clone(self):
        pass

class Ghost(Monster):
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed
    
    def clone(self):
        return Ghost(self.health, self.speed)

class Spawner:
    def __init__(self, prototype):
        self.prototype = prototype
    
    def spawn_monster(self):
        return self.prototype.clone()

ghost_prototype = Ghost(15, 3)
ghost_spawner = Spawner(ghost_prototype)

clone = ghost_spawner.spawn_monster()