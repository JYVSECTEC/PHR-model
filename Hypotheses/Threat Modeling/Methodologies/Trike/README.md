# Trike

Trike is a conceptual open source framework for security auditing from a risk management perspective through the generation of threat models. Trike requirement model focuses on looking at actors interacting with system, what things the system acts upon, actions taken by personnel that the system is supposed to support and rules that define situations where an action can occur. Requirement model also includes organization assets and Actor-Asset-Action Matrix, which is explained in next chapter. When the requirements are gathered, next step is implementation model. In this step, system actions that do not fit into intended actions framework are checked and how actions interact with state of the system is also checked. Then the model looks into different software and hardware components fit together, which is visualized in data flow diagram. Data flow diagram is also used for visualising actions and state of the system. Actual threat model is then build based on the generated DFDs. DFDs are thoroughly explored and all the potential threats are identified. Risk model can then be build, which is not properly implemented to Trike.

Trike categories all threats into one of two categories, either denial of service or elevation of privilege. Trike uses actor-asset-action matrix to represent all data about the requirements model in grid format. The columns of the matrix represent the assets in the system, and the rows represent the roles that actors can take on. Matrix cells are divided into four for each action in CRUD, which stands for "create”, “read”, “update”, and “delete”. Each action-cell can be set to one of three different values that are disallowed action, action with rules and allowed action. Rule tree is then attached to these cells.

Trike appears to be no longer maintained and the latest Trike tool can be found from [here](https://github.com/octotrike/trike).

**Benefits**:

<ul>
    <li>Trike is open source and its materials are available to everybody.</li>
    <li>Trike is good at threat modeling automation.</li>
</ul>

### References

<ul>
    <li>https://www.octotrike.org/papers/Trike_v1_Methodology_Document-draft.pdf</li>
    <li>https://www.theseus.fi/bitstream/handle/10024/220967/Selin_Juuso.pdf?sequence=2&isAllowed=y</li>
    <li>https://www.esecurityplanet.com/networks/selecting-a-threat-risk-model-for-your-organization-part-two/</li>
</ul>
