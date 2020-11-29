;It's recommended to install the misc-pddl-generators plugin 
;and then use Network generator to create the graph
(define (problem p2-dangeon)
  (:domain Dangeon)
  (:objects
            cell1 cell2 cell3 cell4 cell5 cell6 cell7 cell8 cell9 cell10 cell11 cell12  - cells
            sword1 sword2 - swords
  )
  (:init
  
    ;Initial Hero Location
    (at-hero cell7)
    
    ;He starts with a free arm
    (arm-free)
    
    ;Initial location of the swords
    (at-sword sword1 cell10)
    (at-sword sword2 cell6)
    
    ;Initial location of Monsters
    (has-monster cell4)
    (has-monster cell5)
    (has-monster cell9)
    
    ;Initial lcocation of Traps
    (has-trap cell2)
    (has-trap cell3)
    (has-trap cell8)
    (has-trap cell11)
    (has-trap cell12)
    
    ;Graph Connectivity
    (connected cell1 cell2)
    (connected cell2 cell1)
    (connected cell1 cell8)
    (connected cell8 cell1)
    (connected cell2 cell3)
    (connected cell3 cell2)
    (connected cell2 cell9)
    (connected cell9 cell2)
    (connected cell3 cell8)
    (connected cell8 cell3)
    (connected cell8 cell9)
    (connected cell9 cell8)
    (connected cell3 cell4)
    (connected cell4 cell3)
    (connected cell3 cell10)
    (connected cell10 cell3)
    (connected cell4 cell9)
    (connected cell9 cell4)
    (connected cell9 cell10)
    (connected cell10 cell9)
    (connected cell4 cell5)
    (connected cell5 cell4)
    (connected cell4 cell11)
    (connected cell11 cell4)
    (connected cell5 cell10)
    (connected cell10 cell5)
    (connected cell10 cell11)
    (connected cell11 cell10)
    (connected cell5 cell6)
    (connected cell6 cell5)
    (connected cell5 cell12)
    (connected cell12 cell5)
    (connected cell6 cell11)
    (connected cell11 cell6)
    (connected cell11 cell12)
    (connected cell12 cell11)
    (connected cell6 cell7)
    (connected cell7 cell6)
    (connected cell7 cell12)
    (connected cell7 cell12)
    
  )
  (:goal (and
            ;Hero's Goal Location
            (at-hero cell1)
  ))
  
)
