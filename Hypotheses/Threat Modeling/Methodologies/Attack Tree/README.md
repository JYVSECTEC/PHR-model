# Attack Tree

Attack Tree is a visual model that describes ways that computer system can be attacked. Method was developed in 1999 by Bruce Schneier. Tree contains nodes called leafes which correspond to attacker goals in the computer system. Subnodes under each node are subgoals that attacker has to accomplish before reaching the upper node. Tree may include AND nodes and OR nodes. OR nodes can be used to describe several ways that attacker can reach a goal, whereas AND nodes are connected to each other and all their goals have to be achieved before attacker can move to upper node. Attackers ultimate goal is to climb up the tree hierarchy and reach root node. After the tree structure is created, each leaf should be given a value based on the attackers cost of accomplishing the goal in the leaf and damage cost to company which occurs if the attack succeeds. There isn't an actual basis for the damage/attack cost calculations, since costs can differ a lot depending on organization structure and the system targeted. Organization using attack tree as part of threat modeling should brainstorm all the individual costs reflecting their own enviroment.

Image below contains example of an attack tree with costs included.

![Attack tree with costs for leafs](https://github.com/JYVSECTEC/PHR-model/blob/master/Hypotheses/Threat%20Modeling/Methodologies/Attack%20Tree/attack.gif?raw=true)


**Benefits**:

<ul>
    <li>Tree structure is easy to modify if more leafes need to be added to the structure later on.</li>
    <li>Graphical embodiment of the model makes it easier to understand.</li>
</ul>

### References

<ul>
    <li>https://www.schneier.com/academic/archives/1999/12/attack_trees.html</li>
    <li>http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.875.9918&rep=rep1&type=pdf</li>
    <li>https://www.theseus.fi/bitstream/handle/10024/220967/Selin_Juuso.pdf?sequence=2&isAllowed=y</li>
</ul>
