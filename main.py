import time
import random

def delayPrint(text, delay=2):
    print(text)
    time.sleep(delay)

# === Scenes ===
def intro():
    darrow = "Darrow"
    delayPrint("Red Rising: A Text RPG\n", 2)
    delayPrint("You are a Helldiver.")
    delayPrint("You live and die beneath the surface of Mars, mining helium-3.")
    delayPrint("You are told it's for the good of mankind.")
    delayPrint("But you begin to question the lies...")

    delayPrint(f"\nYour name is {darrow} of Lykos.")
    delayPrint("Your hands are calloused. Your lungs are scorched.")
    delayPrint("You were born in the darkness, and they expect you to die in it.")
    delayPrint("The drill shudders. The dust burns your lungs.")
    delayPrint("Uncle Narol yells something, but the roar drowns him out.")
    delayPrint("You're deep. Too deep.")

    choice = input("\nDo you:\n1. Keep drilling - it's quota day.\n2. Stop and check the safety levels.\n> ")

    if choice == "1":
        delayPrint("\nYou keep drilling. You hit a rich vein - helium-3 floods the meter.")
        delayPrint("But something's wrong.")
        delayPrint("A tremor shakes the tunnel. Screams echo from the lower shaft.")
        delayPrint("You disobeyed safety protocols...")
        delayPrint("Some of your crew didn't make it.\n")
    elif choice == "2":
        delayPrint("\nYou stop the drill. Safety first.")
        delayPrint("Uncle Narol nods in approval.")
        delayPrint("But the foreman marks you for low yield. Quota not met.")
        delayPrint("No Laurel for your family this month.\n")
    else:
        delayPrint("\nYou freeze up. The moment passes, and with it, your chance.\n")

    return darrow

def gardenScene():
    delayPrint("\nLater that night, Eo takes your hand.")
    delayPrint("You sneak past rusted steel pipes and broken tunnels...")
    delayPrint("...to the place you call the Garden.")
    delayPrint("There's no real garden — only fungus and scrap.")
    delayPrint("But here, she dances barefoot beneath the dripping lights.\n")

    delayPrint("She hums a tune. Then, softly, she sings:")
    delayPrint("\"We are the sons of Ares... the sons of Mars.\"")
    delayPrint("It's forbidden. Treason. Beauty.\n")

    delayPrint("She stops, looking at you with fire in her eyes.")
    delayPrint("\"Do you ever wonder if this is all a lie, Darrow?\"")

    choice = input("\nDo you say:\n1. 'It doesn’t matter. This is our life.'\n2. 'Yes. I feel it too.'\n> ")

    if choice == "1":
        delayPrint("\nShe looks away, disappointed.")
        delayPrint("“You’re a good man, Darrow,” she says. “But not yet a great one.”")
    elif choice == "2":
        delayPrint("\nShe smiles. A sad, knowing smile.")
        delayPrint("“Then maybe one day, you’ll break the chains.”")
    else:
        delayPrint("\nSilence. Her eyes say everything. You just hold her tighter.")

    delayPrint("\nSuddenly you hear footsteps in the tunnels.")
    delayPrint("Too late. The Greys found you.")
    delayPrint("You both freeze. Eo squeezes your hand.")
    delayPrint("The guards approach, their guns raised.")

    delayPrint("\nThey drag you both away in chains.")
    delayPrint("Eo doesn't scream. She just looks at you.")

def arrestScene():
    delayPrint("\nThey drag you both to the square in chains.")
    delayPrint("Crowds gather. Children. Elders. The Greys stand ready.\n")

    delayPrint("They strap Eo to the post.")
    delayPrint("The lashmaster raises his whip.\n")

    delayPrint("You scream, “Stop!” But the lash falls.")
    delayPrint("Again. And again.\n")

    delayPrint("Eo cries out — but then... she lifts her head.")
    delayPrint("Bloodied. Broken. Smiling.\n")

    delayPrint("She sings.")
    delayPrint("\"We are the sons of Ares... sons of Mars...\"")
    delayPrint("The forbidden song echoes across the square.\n")

    delayPrint("Gasps. Murmurs. Then silence.")
    delayPrint("The ArchGovernor orders her death.\n")

def eoHangingScene():
    delayPrint("\nThey bring her to the gallows.")
    delayPrint("You're forced to watch — beaten, bruised, held down.\n")

    delayPrint("She turns to you, smiling through bloodied lips.")
    delayPrint("\"Break the chains,\" she says. \"Live for more.\"\n")

    delayPrint("The noose tightens around her neck.")
    delayPrint("The floor falls away.")
    delayPrint("Her neck snaps.")
    delayPrint("Eo is gone.\n")

    choice = input("Do you:\n1. Collapse in despair.\n2. Charge the guards.\n> ")

    if choice == "1":
        delayPrint("\nYou fall to your knees. A scream claws its way from your chest.")
        delayPrint("The world is cold. Dead.")
    elif choice == "2":
        delayPrint("\nYou roar and break free.")
        delayPrint("You reach her body. Cut her down.")
        delayPrint("The lashers beat you into the dirt.")
    else:
        delayPrint("\nYou stare, hollow. Empty. The fire goes quiet, but not out.")

def darrowHangingScene():
    delayPrint("\nDays pass. You’re barely fed. No trial. No mercy.\n")
    delayPrint("They hang you in the square where Eo died.")
    delayPrint("You feel the rope. Smell the metal.")
    delayPrint("Then— darkness.\n")

def burialScene():
    delayPrint("You wake up gasping — dirt in your mouth.")
    delayPrint("You were buried. But someone dug you out.")
    delayPrint("A masked man kneels above you.\n")

    delayPrint("\"Your wife believed in something greater,\" he says.")
    delayPrint("\"So do we. I am Dancer. Welcome to the Sons of Ares.\"")

def dancerScene():
    delayPrint("\nThey take you to a hidden chamber — lit with red glowlamps.")
    delayPrint("You see other Reds. Fighters. Believers.")
    delayPrint("Dancer looks at you.\n")

    delayPrint("\"We can make you a Gold, Darrow. We can send you into their world.\"")
    delayPrint("\"But it will hurt. And you will never be the same.\"\n")

    choice = input("Do you:\n1. Accept.\n2. Refuse.\n> ")

    if choice == "1":
        delayPrint("\nYou clench your fists. 'Do it.'")
        delayPrint("Dancer smiles. 'Then let’s begin.'")
    elif choice == "2":
        delayPrint("\nYou shake your head. 'I'm not ready.'")
        delayPrint("He frowns. 'Then you’re no better than they say.'")
    else:
        delayPrint("\nYou say nothing. But your eyes answer for you.")

def transformationScene():
    delayPrint("\nThe Carver’s room smells of blood and antiseptic.")
    delayPrint("Mickey grins — too many teeth, too much silk.\n")

    delayPrint("\"We're going to make a masterpiece,\" he says.\n")

    delayPrint("They strap you to the table.")
    delayPrint("You scream. Bones are broken, skin peeled, muscles stretched.")
    delayPrint("You die. You live. You become something else.\n")

    delayPrint("You are no longer Red.")
    delayPrint("You are Gold.\n")

    delayPrint("=== ACT 1 COMPLETE ===\n")
    
def arrivalScene():
    delayPrint("\nYou fly across Mars - not as a Red, but reborn as a Gold.")
    delayPrint("The shuttle lands. Before you lies a mountain fortress: the Institute.")
    delayPrint("Golds in armor. Proctors in robes. Silent servants.")
    delayPrint("you are among wolves now.\n")
    
def passageAnnouncementScene():
    delayPrint("A Proctor floats above the crowd using gravBoots.")
    delayPrint("\"Welcome, children of the Society,\" he says.")
    delayPrint("\"Tonight, you face the Passage. You will be paired with another Gold.\"")
    delayPrint("\"Survive, and you may earn a place among us. Fail, and you will die.\"")
    delayPrint("\"Let the games begin.\"\n")

def julianIntroScene():
    delayPrint("The cell door opens with a hiss of air.")
    delayPrint("A boy is thrown inside. Blonde. Soft-featured. About your age.\n")
    delayPrint("He scrambles to his feet, dusts himself off, and looks at you.\n")

    delayPrint("\"Well, this is awkward,\" he says, trying to smile.")
    delayPrint("\"Julian Bellona,\" he offers, holding out a hand.")

    choice = input("\nDo you:\n1. Shake his hand.\n2. Ignore him.\n> ")

    if choice == "1":
        delayPrint("\nYou shake it. His grip is soft. Too soft for this place.")
        delayPrint("“Darrow,” you say quietly.")
    elif choice == "2":
        delayPrint("\nYou say nothing. His hand drops awkwardly.")
        delayPrint("“Alright then,” he mumbles.")
    else:
        delayPrint("\nSilence. Julian just shrugs, trying to ease the tension.")

    delayPrint("\nHe sits against the wall across from you.")
    delayPrint("“They say we have to fight. But maybe… maybe they’re lying?”")
    delayPrint("“Maybe they’re testing our mercy.”")
    delayPrint("You want to believe him.")
    delayPrint("But you know better.")

# === Battle System ===
def battle(player, enemy):
    player_hp = player['hp']
    quick_dmg = player['quickAttackDamage']
    heavy_dmg = player['heavyAttackDamage']
    
    enemy_hp = enemy['hp']
    enemy_attack = enemy['attackDamage']
    enemy_name = enemy['name']
    
    delayPrint(f"\nThe fight begins: {player['name']} vs {enemy_name}!")

    while enemy_hp > 0 and player_hp > 0:
        delayPrint(f"\n{player['name']} HP: {player_hp} — {enemy_name} HP: {enemy_hp}")
        choice = input("Choose your action:\n1. Quick attack\n2. Heavy attack\n3. Defend\n4. Hesitate\n> ")
        
        defending = False

        if choice == "1":
            dmg = random.randint(*player['quickAttackDamage'])
            delayPrint(f"\nYou strike quickly at {enemy_name} for {dmg} damage!")
            enemy_hp -= dmg
        elif choice == "2":
            dmg = random.randint(*player['heavyAttackDamage'])
            delayPrint(f"\nYou swing hard at {enemy_name} for {dmg} damage!")
            enemy_hp -= dmg
        elif choice == "3":
            delayPrint("\nYou raise your guard, bracing for impact.")
            defending = True
        elif choice == "4":
            delayPrint("\nYou hesitate... doubt creeps in.")
        else:
            delayPrint("\nYou fumble, losing precious seconds!")
        
        if enemy_hp <= 0:
            break

        if defending:
            dmg = random.randint(*enemy['attackDamage']) // 2
            delayPrint(f"\n{enemy_name} attacks, but you block part of the damage!")
        else:
            dmg = random.randint(*enemy['attackDamage'])
            delayPrint(f"\n{enemy_name} attacks fiercely!")
            
        player_hp -= dmg
        delayPrint(f"You take {dmg} damage.")
        
    if player_hp <= 0:
        delayPrint("\nYou have been defeated...")
        return False
    
    delayPrint(f"\n{enemy_name} falls. You have survived.")
    return True

def passageFightScene():
    delayPrint("\nA voice crackles through a hidden speaker.")
    delayPrint("\"Begin. Only one of you may leave.\"\n")

    delayPrint("Julian's eyes widen. \"Wait... what?\"")
    delayPrint("He looks around for a weapon. There is none.")
    delayPrint("Just stone walls. Just you. Just him.\n")

    delayPrint("“They can’t mean this,” he whispers. “We’re not animals.”")
    delayPrint("You say nothing. You know the truth.\n")

    delayPrint("Julian backs into a corner, fists trembling.")
    delayPrint("“Please,” he says. “We can fight someone else. We don’t have to—”\n")

    delayPrint("But the door stays shut.\n")

    player = {
        'name': 'Darrow',
        'hp': 100,
        'quickAttackDamage': (10, 20),
        'heavyAttackDamage': (20, 40)
    }
    
    enemy = {
        'name': 'Julian Bellona',
        'hp': 60,
        'attackDamage': (10, 15)
    }
    
    result = battle(player, enemy)
    
    if result:
        delayPrint("\nYou kneel over Julian's body. Tears mix with blood.")
        delayPrint("He didn't deserve this. None of you did.")
        delayPrint("But you remember Eo. And you live.\n")

        delayPrint("The door opens. Light floods the cell.")
        delayPrint("You're dragged out. They say nothing. No praise. No shame.")
        delayPrint("Only silence.\n")
        
    return True

# === Main ===
def main():
    darrow = intro()
    gardenScene()
    arrestScene()
    eoHangingScene()
    darrowHangingScene()
    burialScene()
    dancerScene()
    transformationScene()
    delayPrint(f"{darrow}, reborn, now walks among the enemy...\n")
    arrivalScene()
    passageAnnouncementScene()
    julianIntroScene()
    passageFightScene()
    delayPrint("\nTo be continues...\n")


if __name__ == "__main__":
    main()
