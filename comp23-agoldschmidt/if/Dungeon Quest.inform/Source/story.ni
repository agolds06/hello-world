"Dungeon Quest" by "Alex"

didTrade is a number variable. didTrade is 0.
didKill is a number variable. didKill is 0.
didBribe is a number variable. didBribe is 0.
didFind is a number variable. didFind is 0.

		
trading is an action applying to one carried thing and one visible thing.
Understand "trade [carried thing] with [visible thing]" as trading.


carry out trading:
	if the visible thing is the Cursed Man and didTrade is 0 and the carried thing is Potion:
		say "Thank you so much for the potion. I really needed that. Here, have this. I found it wandering around looking for a cure.";
		increment didTrade;
		award 5 points;
		remove Potion from play;
	otherwise if the visible thing is Cursed Man and didTrade is 1:
		say "I have nothing else for you, child";
	otherwise if the visible thing is the Guard and didKill is 0 and didBribe is 0 and the carried thing is Gold:
		say "Thanks for the gold kid. Feel free to pass. I won't tell.";
		award 5 points;
		increment didBribe;
		remove Gold from play;
	otherwise if the visible thing is the Guard and didKill is 1 and carried thing is Gold:
		say "I don't think he has any need for gold.";
	otherwise if the visible thing is Guard and didKill is 0 and didBribe is 1:
		say "Thanks for the gold";
	otherwise if the visible thing is the Priest and didFind is 0 and the carried thing is the Cross:
		say "Bless you child. Here, take this. It will serve you better than I.";
		increment didFind;
		award 5 points;
		remove Cross from play;
	otherwise if the visible thing is Priest and didFind is 1:
		say "Thank you for finding this";
		
talking is an action applying to one visible thing.
Understand "talk to [visible thing]" as talking.

carry out talking:
	if the visible thing is the Cursed Man and didTrade is 0:
		say "Please, sir. I need some potion to cure this curse. I have something you might need.";
	otherwise if the visible thing is the Cursed Man and didTrade is 1:
		say "Thank you for the potion";
	otherwise if the visible thing is the Guard and didKill is 0 and didBribe is 0:
		say "No can do kid. Can't let anyone pass.";
	otherwise if the visible thing is the Guard and didKill is 1:
		say ". . . He's dead";
	otherwise if the visible thing is the Guard and didKill is 0 and didBribe is 1:
		say "Thanks for the money";
	otherwise if the visible thing is the Prisoner:
		say "Help me, please";
	otherwise if the visible thing is the Horse:
		say "Nay!";
	otherwise if the visible thing is the Priest and didFind is 0:
		say "Please, I have lost my Cross in this forsaken dungeon. I can give you this potion if you find it for me.";
	otherwise if the visible thing is the Priest and didFind is 1:
		say "Thank you for the cross";





		
When play begins:
say "You find yourself chained to a wall in a dark, dank dungeon. You have no idea how you got here, but you should probably try to find a way out. You look up and you begin to devise an escape plan."

The Dungeon is a room. The description is "The Dungeon has crumbling stone walls and a dirt floor. There is a dark hallway extending west."

The Dungeon Door is a door. The dungeon door is north of the dungeon. The steel key unlocks the dungeon door. The description of the dungeon door is "An iron studded door. It doesn't look like it's gonna budge."

Instead of opening the dungeon door:
	If the steel key is held and horseFree is 0:
		say "The light pours into the cell. You step outside, and take in the fresh air. You are free.";
		end the game in victory;
	otherwise if the steel key is held and horseFree is 1:
		say "The light pours into the cell. You ride out on your majestic steed into the sunset.";
		end the game in victory;
	otherwise:
		say "You can't open the door";
		
A leaflet is a thing in the Dungeon. The description is "Good luck trying to get out of here. Your buddy next to you thought he could get out too. Mwahaha!"

A brass key is a thing in the Dungeon. It unlocks the Shackles. The description is "Huh. Looks like the same metal as these shackles on the prisoner."

The Prisoner is a person in the Dungeon. The description is "I don't think he has anything interesting to say to me".

The Shackles are a container in the Dungeon. The Shackles are locked and lockable. The brass key unlocks the Shackles. The description of the Shackles is "[if locked]These look like they need a key to unlock them[otherwise]Some metal chains just lying around[end if]."

Instead of talking the prisoner:
	if shackles are locked:
		say "Please help me";
	otherwise if shackles are unlocked:
		say "Thank you";

Gold is a thing in the Dungeon. 
Instead of taking the gold:
	if shackles are locked:
		say "I can't reach the gold. I need to unlock this prisoner first.";
		stop the action;
	otherwise if shackles are unlocked:
		continue the action;

The Armory is a room. It is west of the Dungeon. The description of the armory is "This appears to be an armory. I should look around for weapons. There are dark hallways to the north, south, and west"

A Sword is a thing in the Armory. The description is "Looks like an ordinary sword".

After taking the sword:
	award 5 points;

A Shield is a thing in the Armory. The description is "Looks like an ordinary shield".

After taking the shield:
	award 5 points;
	
The Sanctum is a room. It is north of the Armory. The description of the Sanctum is "Some sort of religious room. Nothing here but an altar and a priest."

A Priest is a person in the Sanctum.

Instead of talking the Priest:
	If the cross is held:
		say "Oh, you have the cross! Would you trade the cross with me?";
	otherwise:
		continue the action;
		
Instead of taking the potion:
	If didFind is 0:
		say "I can't take this until I give the priest the cross";
	otherwise if didFind is 1:
		continue the action;

A Potion is a thing in the Sanctum. A potion is edible. The description is "Looks pretty funky. I probably shouldn't drink this."

Instead of eating the potion:
	say "You feel warm inside. Warmer and warmer; it's getting uncomfortable. You're insides are boiling. You struggle to stand, until your whole world turns red, and then fades into blackness...";
	end the game in death;
	
A Dark\ Room is a room. It is south from the Armory. The description of the Dark\ Room is "A Dark Room. It's kind of scary. The darkness extends north, east, and south."

A Cell is a room. It is south from the Dark\ Room. The description of the cell is "A cell with a sickly looking prisoner inside."

A Cursed Man is a person in the Cell. The description is "[if didTrade is 0]This man looks ill[otherwise]He looks a lot better[end if]."

Instead of taking the iron key:
	If didtrade is 0:
		say "I need to find the potion first";
		stop the action;
	otherwise:
		continue the action;

An iron key is a thing in the Cell. It unlocks the Mahogany Door. The description of the iron key is "An ordinary iron key."

A Creepy\ Room is a room. It is east from the Dark\ Room. The description of the Creepy\ Room is "This room looks the same as the last one. The hallway continues into the darkness east and west."

A Cross is a thing in the Creepy\ Room. The description is "A wooden Cross. Wonder why it's lying around in a dungeon."

A Darker\ Room is a room. It is east from the Creepy\ Room. The description of the Darker\ Room is "This room is even darker than the last one."

A Guard is a person in the Darker\ Room.
		
Instead of going south:
	if guard is not visible:
		continue the action;
	otherwise if didKill is 1 or didBribe is 1:
		continue the action;
	otherwise if didKill is 0:
		say "The guard refuses to let you pass.";
		
	
A Darkest\ Room is a room. A Darkest\ Room is north from the Darker\ Room. The description of the Darkest\ Room is "Wow. It's really dark in here."

A wooden key is in the Darkest\ Room. It unlocks the Wooden Door. The description of the wooden key is "A wooden key."

A Stable is a room. It is north from the Darkest\ Room. The description of the Stable is "How is there a stable underground in a dungeon?"

A Horse is a person in the Stable.
horseFree is a number variable. horseFree is 0.

Instead of talking the horse:
	if the silver key is held:
		say "You free the horse!";
		increment horseFree;
		remove silver key from play;
		award 100 points;
	otherwise if horseFree is 0:
		say "The horse struggles under the ropes";
	otherwise:
		say "The horse whinnies happily.";


A Guard\ Room is a room. It is south from the Darker\ Room. The description of the Guard\ Room is "The room guarded by the Guard. Looks like there are a bunch of important looking locked doors here."

A Treasury is a room. It is west of the Mahogany Door. The description of the treasury is "Holy cow! Look at all this gold that I can't take!".

A steel key is a thing in the Treasury. The description is "A steel key." It unlocks the Dungeon Door.

A Study is a room. A study is east of the Wooden Door. The description of the Study is "This is nice. I'm glad that whoever built this dungeon takes the time to study."

A silver key is a thing in the Study. The description is "A silver key."

A Wooden Door is a door. A wooden door is east of the Guard\ Room and west of the Study. It is locked and lockable. The wooden key unlocks it. The description of the Wooden Door is "A sturdy looking wooden door".
				
A Mahogany Door is a door. A Mahogany Door is west of the Guard\ Room and east of the Treasury. It is locked and lockable. The description of the mahogany door is "A massive door. It smells of...rich mahogany". An iron key unlocks the mahogany door.
