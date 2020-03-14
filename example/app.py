#!/usr/bin/env python

from example.common.smart_door import SmartDoor
# ou :  from ..common.smart_door import SmartDoor


def run():
    door = SmartDoor('Ma porte')
    door.open()
    door.close()
    return 'Programme terminé'
