(define (domain Dangeon)

    (:requirements
        :typing
        :negative-preconditions
    )

    (:types
        swords cells
    )

    (:predicates
        ;Hero's cell location
        (at-hero ?loc - cells)
        
        ;Sword cell location
        (at-sword ?s - swords ?loc - cells)
        
        ;Indicates if a cell location has a monster
        (has-monster ?loc - cells)
        
        ;Indicates if a cell location has a trap
        (has-trap ?loc - cells)
        
        ;Indicates if a cell or sword has been destroyed
        (is-destroyed ?obj)
        
        ;connects cells
        (connected ?from ?to - cells)
        
        ;Hero's hand is free
        (arm-free)
        
        ;Hero's holding a sword
        (holding ?s - swords)
    
        ;It becomes true when a trap is disarmed
        (trap-disarmed ?loc)
        
    )

    ;Hero can move if the
    ;    - hero is at current location
    ;    - cells are connected, 
    ;    - there is no trap in current loc, and 
    ;    - destination does not have a trap/monster/has-been-destroyed
    ;Effects move the hero, and destroy the original cell. No need to destroy the sword.
    (:action move
        :parameters (?from ?to - cells)
        :precondition (and  
                            (connected ?from ?to)
                            (at-hero ?from)
                            (not (has-trap ?from))
                            (not (has-trap ?to))
                            (not (has-monster ?to))
                            (not (is-destroyed ?to))
        )
        :effect (and    
                    (at-hero ?to)
                    (not (at-hero ?from))
                    (is-destroyed ?from)
                )
    )
    
    ;When this action is executed, the hero gets into a location with a trap
    (:action move-to-trap
        :parameters (?from ?to - cells)
        :precondition (and  
                            (connected ?from ?to)
                            (at-hero ?from)
                            (not (has-trap ?from))
                            (not (is-destroyed ?to))
                            (has-trap ?to)
                            (arm-free)
        )
        :effect (and    
                    (at-hero ?to)
                    (not (at-hero ?from))
                    (is-destroyed ?from)
                )
    )

    ;When this action is executed, the hero gets into a location with a monster
    (:action move-to-monster
        :parameters (?from ?to - cells ?s - swords)
        :precondition (and  
                            (connected ?from ?to)
                            (at-hero ?from)
                            (not (is-destroyed ?to))
                            (has-monster ?to)
                            (holding ?s)
        )
        :effect (and    
                    (at-hero ?to)
                    (not (at-hero ?from))
                    (is-destroyed ?from)
                )
    )
    
    ;Hero picks a sword if he's in the same location
    (:action pick-sword
        :parameters (?loc - cells ?s - swords)
        :precondition (and 
                            (at-hero ?loc)
                            (at-sword ?s ?loc)
                            (arm-free)
                      )
        :effect (and
                    (holding ?s)
                    (not (arm-free))
                )
    )
    
    ;Hero destroys his sword. 
    (:action destroy-sword
        :parameters (?loc - cells ?s - swords)
        :precondition (and 
                            (at-hero ?loc)
                            (holding ?s)
                            (not (has-trap ?loc))
                            (not (has-monster ?loc))
                      )
        :effect (and
                    (not (holding ?s))
                    (not (at-sword ?s ?loc))
                    (arm-free)
                )
    )
    
    ;Hero disarms the trap with his free arm
    (:action disarm-trap
        :parameters (?loc - cells)
        :precondition (and 
                            (at-hero ?loc)
                            (has-trap ?loc)
                            (not (trap-disarmed ?loc))
                            (arm-free)
                      )
        :effect (and
                    (trap-disarmed ?loc)
                    (not (has-trap ?loc))
                )
    )
    
)