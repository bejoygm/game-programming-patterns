from enum import Enum

class ObserverEvents(Enum):
    EVENT_START_FALL = 1

class Observer:
    def on_notify(self, entity, event):
        pass

class AchievementsObserver(Observer):
    ACHIEVEMENT_FELL_OFF_BRIDGE = 1
    def unlock(self, achievemnt):
        pass

    def on_notify(self, entity, event):
        if event == ObserverEvents.EVENT_START_FALL:
            if entity.is_hero() and entity.was_on_bridge():
                self.unlock(self.ACHIEVEMENT_FELL_OFF_BRIDGE)


class Subject:
    observers = []

    def add_observers(self, observer):
        self.observers.append(observer)
    
    def remove_observers(self, observer):
        self.observers.append(observer)
    
    def __notify(self, entity, event):
        for observer in self.observers:
            observer.on_notify(entity, event)

class Physics(Subject):
    GRAVITY = 9.8

    def update_entity(self, entity):
        was_on_surface = entity.is_on_surface()
        entity.accelerate(self.GRAVITY)
        entity.update()

        if was_on_surface and not entity.is_on_surface():
            self._Subject__notify(entity, ObserverEvents.EVENT_START_FALL)


# General supporting classes for above code, not necessary to understand pattern
class Entity:
    def accelerate(self, force):
        pass

    def update(self):
        pass

    def is_on_surface(self):
        pass

    def is_hero(self):
        pass

class Hero(Entity):
    def is_hero(self):
        return True

    def was_on_bridge(self):
        pass