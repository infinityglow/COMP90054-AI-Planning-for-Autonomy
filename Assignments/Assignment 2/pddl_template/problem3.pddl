;It's recommended to install the misc-pddl-generators plugin 
;and then use Network generator to create the graph
(define (problem p3-dangeon)
  (:domain Dangeon)
  (:objects
            cell1_1 cell1_2 cell1_3 cell1_4 cell1_5 cell2_1 cell2_2 cell2_3 cell2_4 cell2_5 cell3_1 cell3_2 cell3_3 cell3_4 cell3_5 cell4_1 cell4_2 cell4_3 cell4_4 cell4_5 - cells
            sword1 sword2 sword3 sword4 - swords
  )
  (:init
  
    ;Initial Hero Location
    (at-hero cell4_5)
    
    ;He starts with a free arm
    (arm-free)
    
    ;Initial location of the swords
    (at-sword sword1 cell1_5)
    (at-sword sword2 cell2_3)
    (at-sword sword3 cell3_1)
    (at-sword sword4 cell4_3)
    
    ;Initial location of Monsters
    (has-monster cell1_3)
    (has-monster cell1_4)
    (has-monster cell2_2)
    (has-monster cell3_2)
    (has-monster cell3_4)
    (has-monster cell4_2)
    (has-monster cell4_4)
    
    ;Initial lcocation of Traps
    (has-trap cell1_2)
    (has-trap cell2_1)
    (has-trap cell2_4)
    (has-trap cell2_5)
    (has-trap cell3_3)
    (has-trap cell4_1)
    
    ;Graph Connectivity
    (connected cell1_1 cell1_2)
    (connected cell1_2 cell1_1)
    (connected cell1_2 cell1_3)
    (connected cell1_3 cell1_2)
    (connected cell1_3 cell1_4)
    (connected cell1_4 cell1_3)
    (connected cell1_4 cell1_5)
    (connected cell1_5 cell1_4)
    (connected cell2_1 cell2_2)
    (connected cell2_2 cell2_1)
    (connected cell2_2 cell2_3)
    (connected cell2_3 cell2_2)
    (connected cell2_3 cell2_4)
    (connected cell2_4 cell2_3)
    (connected cell2_4 cell2_5)
    (connected cell2_5 cell2_4)
    (connected cell3_1 cell3_2)
    (connected cell3_2 cell3_1)
    (connected cell3_2 cell3_3)
    (connected cell3_3 cell3_2)
    (connected cell3_3 cell3_4)
    (connected cell3_4 cell3_3)
    (connected cell3_4 cell3_5)
    (connected cell3_5 cell3_4)
    (connected cell4_1 cell4_2)
    (connected cell4_2 cell4_1)
    (connected cell4_2 cell4_3)
    (connected cell4_3 cell4_2)
    (connected cell4_3 cell4_4)
    (connected cell4_4 cell4_3)
    (connected cell4_4 cell4_5)
    (connected cell4_5 cell4_4)
    (connected cell1_1 cell2_1)
    (connected cell2_1 cell1_1)
    (connected cell2_1 cell3_1)
    (connected cell3_1 cell2_1)
    (connected cell3_1 cell4_1)
    (connected cell4_1 cell3_1)
    (connected cell1_2 cell2_2)
    (connected cell2_2 cell1_2)
    (connected cell2_2 cell3_2)
    (connected cell3_2 cell2_2)
    (connected cell3_2 cell4_2)
    (connected cell4_2 cell3_2)
    (connected cell1_3 cell2_3)
    (connected cell2_3 cell1_3)
    (connected cell2_3 cell3_3)
    (connected cell3_3 cell2_3)
    (connected cell3_3 cell4_3)
    (connected cell4_3 cell3_3)
    (connected cell1_4 cell2_4)
    (connected cell2_4 cell1_4)
    (connected cell2_4 cell3_4)
    (connected cell3_4 cell2_4)
    (connected cell3_4 cell4_4)
    (connected cell4_4 cell3_4)
    (connected cell1_5 cell2_5)
    (connected cell2_5 cell1_5)
    (connected cell2_5 cell3_5)
    (connected cell3_5 cell2_5)
    (connected cell3_5 cell4_5)
    (connected cell4_5 cell3_5)
  )
  (:goal (and
            ;Hero's Goal Location
            (at-hero cell1_1)
  ))
  
)
