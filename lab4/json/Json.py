import json

data = open("m", "r")

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")

for el in data["imdata"]:
    DN = el["l1PhysIf"]["attributes"]["dn"]
    Description = el["l1PhysIf"]["attributes"]["descr"]
    Speed = el["l1PhysIf"]["attributes"]["speed"]
    MTU = el["l1PhysIf"]["attributes"]["mtu"]
    if len(DN) == 42:
        print(DN, Description, "                           ", Speed, " ", MTU)
    else:
        print(DN, Description, "                            ", Speed, " ", MTU)