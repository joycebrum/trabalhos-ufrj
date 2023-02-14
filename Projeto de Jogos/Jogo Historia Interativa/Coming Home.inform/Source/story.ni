"The forgotten treasure" by Thiago Outeiro, Joyce brum, João Pedro and Flávio Sousa

Include Conversation Framework by Eric Eve.

Figure of first floor is the file "1floor.png".
Figure of second floor is the file "2floor.png".


Chapter 1 New Kinds

Inclusion relates a thing (called X) to a thing (called Y) when Y is part of X. The verb to include means the inclusion relation.

Section 1.0 - Variables

Max Approval is a truth state that varies.
Carlie Approval is a truth state that varies.

Section 1.1 The Staircase

A staircase is a kind of door. A staircase is usually open. A staircase is seldom openable. A staircase is scenery.
Instead of climbing a staircase: 
    try entering the noun. 

Section 1.2 Sitting

Understand the command "sit" as something new.
Sitting on is an action applying to one thing.
Understand "sit on [something]" as sitting on.
understand "sit on top of [something]" as sitting on.

Check an actor sitting on a thing:
	If the noun is occupied, say "You can't sit in the [the noun], it is occupied" instead;
	If the noun is not enterable, say "You can't sit on [the noun]" instead.

Check an actor entering a thing:
	If the thing is occupied, say "You can't sit in a occupied chair" instead;

Section 1.3 Chairs

A chair is a kind of supporter that is enterable with carrying capacity 1. 
Definition: A chair is occupied if something is on it.

Carry out sitting on a chair:
	silently try entering the noun.

Report sitting on a chair:
	say "You feel confortable".

	
Section 1.4 Kitchens

A kitchen is a kind of room.

A refrigerator is a kind of container. A refrigerator is usually closed and openable. A refrigerator is usually fixed in place. A refrigerator is usually scenery. Understand "fridge" as refrigerator.

A freezer compartment is a kind of container. A freezer compartment is usually closed and openable. A freezer compartment is part of every refrigerator.

A stove is a kind of supporter. It is usually scenery.
An oven is a kind of container. An oven is usually openable and closed. One oven is a part of every stove.
A switch is a kind of device. A switch is part of every stove. A switch is part of every oven.
Understand "[something related by reversed incorporation] switch" as a switch.

A sink is a kind of container. A sink is usually fixed in place and scenery. A tap is a kind of switch. A tap is a part of every sink. Understand "faucet" or "taps" as a tap. Understand "[something related by reversed incorporation] tap/faucet/taps" as a tap.
Instead of opening a tap, try switching on the noun. Instead of closing a tap, try switching off the noun.

Report switching on a tap (this is the standard report switching taps on rule):
	say "You turn on [the noun]." instead. [since "switch on" sounds weird in this context.]

Report switching off a tap (this is the standard report switching taps off rule):
	say "You turn off [the noun]." instead.

After examining something which includes a switched on tap (called relevant tap) (this is the report flowing water rule):
	say "The water is flowing from [the relevant tap]."
	
A cabinet is a kind of fixed in place container. A cabinet is usually openable and closed.
	Understand "cupboard" or "cupboards" or "cabinets" as a cabinet.

A counter is a kind of supporter. It is scenery.
	Understand "countertop" as a counter.
	
A drain is a kind of container. A drain is part of every sink. Understand "plughole" as the drain. Understand "[something related by reversed incorporation] drain/plughole" as a drain.

Instead of inserting something into a drain (this is the no clogging drains rule), say "Pointless."

A counter is in every kitchen.
A refrigerator is in every kitchen.
A sink is in every kitchen.
A stove is in every kitchen.

Section 1.5 Bathrooms

A bathroom is a kind of room.

A toilet is a kind of supporter. A toilet is usually fixed in place and enterable and scenery.

A bath is a kind of container. A bath is usually fixed in place and enterable and scenery. A tap is part of every bath. A drain is part of every bath. A drain is part of every bath. Understand "bathtub" or "shower" as a bath.

A sink is in every bathroom.
A toilet is in every bathroom.
A cabinet is in every bathroom.

report opening a cabinet:
	say "You can se some cleaning products".

Section 1.6 Home Office

A book is a kind of thing. It has some text called printing.

Understand the command read as something new. Reading is an action applying to a thing. Understand "read [something]" as reading.

Check reading:
	if the noun is a book, say "[printing][line break]";
	Else say "You can't read this.".

Section 1.7 - Bedroom

A bedroom is a kind of room.

Section 1.7.1- Bed 

A  bed is a kind of supporter. A bed is enterable and scenery with carrying capacity 2.

A bed is in every bedroom.

Definition: A bed is occupied if something is on it.

Carry out sitting on a bed:
	silently try entering the noun.

Report sitting on a bed:
	say "You feel confortable".

Section 1.7.2 - wardrobe

A wardrobe is a kind of container. A wardrobe is usually closed and openable. A wardrobe is usually fixed in place.

A drawer is a kind of container. A drawer is usually closed and openable.

Section 1.8 - Dining Room

Dining room is a room.

The dining table is a fixed in place supporter. The dining table is in the Dining room.
The pot is a container. dead flowers are in the pot. The pot is on the dining table.

The bar is a fixed in place supporter. The bar is in the Dining room.
The bottle of wine, bottle of scotch whisky  and a bottle of vodka is a container. 
grape juice is in the bottle of wine.
The bottle of wine, bottle of scotch whisky  and a bottle of vodka is on the bar.
There are four glasses on the table.
There are four plates on the table.

There are four chairs in the Dining room.

Section 1.9 - Switching devices

Understand "turn on [something switched off]" as switching on. Understand "turn off  [something switched on]" as switching off.

Understand "flip [something switched off]" as switching on. Understand "flip [something switched on]" as switching off. Understand "flip [something]" as switching on.

Section 1.10 - Burning

A thing can be flammable or impervious. A thing is usually impervious.
A thing can be lighting or unlighting.  A thing is usually unlighting.

Section 1.10.1 - Lighting Objects

Instead of burning a lit lighting object:
	say "The [noun] is already lit."

Understand "blow out [something]" as blowing out. Understand "blow [something] out" as blowing out. Blowing out is an action applying to one thing.

Carry out blowing out a lighting object:
	now the noun is unlit.

Report blowing out a thing:
	if the thing was lit, say "You blow out [the noun].";
	otherwise say "You blow on [the noun], to little effect."

Section 1.10.2 - Simple Burning 

Understand the commands "light" and "burn" as something new.

Understand "burn [something] with [strikable-match]" as burning it with. Understand "burn [something] with [something preferably held]" as burning it with. Burning it with is an action applying to one thing and one carried thing.

Understand the command "light" as "burn".

Check burning something with something (this is the burn only with flaming matches rule):
	if the second noun is not a strikable-match, say "You can only light things with matches." instead;
	if the second noun is not flaming, say "[The second noun] needs to be burning first." instead.

Check burning something with something (this is the burn only flammable things rule):
	if the noun is unlighting and the noun is impervious, say "[The noun] cannot be burned." instead.

Check burning an unlighting thing with something (this is the burn only things not held rule):
	say "[one of]It occurs to you to set down [the noun] before burning, just for safety's sake. [or]Again, you decide to put down [the noun] prior to burning. [or]You try setting down [the noun] as usual. [stopping][run paragraph on]";
	silently try the player dropping the noun;
	if the player encloses the noun, stop the action.

Carry out burning something with something (this is the simplistic burning rule):
	if the noun is a lighting thing, now the noun is lit;
	if the noun is not a lighting thing: 
		now the noun is nowhere;
		say "'You have no respect with this house sir', you hear a voice saying in your back.

		Max is very close to you and he seems very angry.

		'I'm afraid I can't no longer allow you to stay', he says.

		Then everything goes dark.";
		end the story saying "You have died".

Report burning something with something:
	if the noun is an unlighting thing, say "You burn up [the noun].";
	otherwise say "You light up [the noun].".

Rule for implicitly taking the second noun while burning something with something which is not a strikable-match:
	say "You can only light things with matches.";
	stop the action.

Section 1.11 - Matches

A strikable-match is a kind of thing. The plural of strikable-match is s-matches.

A strikable-match has a number called duration. The duration of a strikable-match is usually 3.

Rule for printing the name of a strikable-match: say "match".
Rule for printing the plural name of a strikable-match: say "matches".

Understand "match" as a strikable-match. Understand "matches" as a strikable-match.

Flame-state is a kind of value. The flame-states are burnt, flaming, and new. Understand "burning" or "lit" as flaming. Understand "unused" as new.

A strikable-match has a flame-state. A strikable-match is usually new. Understand the flame-state property as describing a strikable-match.

Before printing the name of a strikable-match while asking which do you mean:
	say "[flame-state] ".

Before printing the name of a strikable-match while taking inventory:
	say "[flame-state] ".
Before printing the plural name of a strikable-match while taking inventory:
	say "[flame-state] ".

Before printing the name of a strikable-match while clarifying the parser's choice of something:
	if not taking inventory, say "[flame-state] ".

After printing the name of a strikable-match (called special-target) while clarifying the parser's choice of something:
	if the player carries the special-target:
		say " you're carrying";
	otherwise if the special-target is in the location:
		say " on the ground";
	otherwise:
		say " [if the holder of the special-target is a container]in[otherwise]on[end if] [the holder of the special-target]".

Understand "strike [something]" as attacking.

Understand "strike [strikable-match]" as striking. Striking is an action applying to one carried thing.

Understand "burn [strikable-match]" as striking.

Does the player mean striking a new strikable-match:
	it is very likely.

Does the player mean striking a burnt strikable-match:
	it is unlikely.

Check striking a strikable-match (this is the strike only new matches rule):
	if the noun is burnt, say "[The noun] has already burnt down and cannot be relit." instead;
	if the noun is flaming, say "[The noun] is already burning." instead.

Carry out striking a strikable-match (this is the standard striking rule):
	now the noun is flaming;
	now the noun is lit.

Report striking a strikable-match (this is the standard report striking rule):
	say "You light [the noun]."

Before burning something with a new strikable-match (this is the prior lighting rule):
	say "(first [if the player does not carry the second noun]taking and [end if]lighting [the second noun])[command clarification break]";
	silently try striking the second noun;
	if the second noun is not flaming, stop the action.

Rule for implicitly taking a strikable-match (called target) while striking:
	try silently taking the target.

Does the player mean burning something with a flaming strikable-match:
	it is very likely.

Does the player mean burning something with a new strikable-match:
	it is likely.

Does the player mean burning something with a burnt strikable-match:
	it is unlikely.

Instead of burning a burnt strikable-match with something:
	say "[The noun] is completely consumed and cannot be relit."
	
Section 1.12 - Putting the Matches Out

Every turn:
	let N be 0; [here we track how many matches are being put out during this turn, so that we don't have to mention each match individually if several go out during the same move]
	repeat with item running through flaming s-matches:
		decrement the duration of the item;
		if the duration of the item is 0:
			now the item is burnt;
			now the item is unlit;
			if the item is visible, increment N;
	if N is 1:
		say "[if the number of visible flaming s-matches is greater than 0]One of the matches [otherwise if the number of burnt visible s-matches is greater than 1]Your last burning match [otherwise]The match [end if]goes out.";
	otherwise if N is greater than 1:
		let enumeration be "[N in words]";
		if N is the number of visible s-matches:
			if N is two, say "Both";
			otherwise say "All [enumeration]";
		otherwise:
			say "[enumeration in title case]";
		say " matches go out[if a visible strikable-match is flaming], leaving [number of visible flaming s-matches in words] still lit[end if]."
		
Section 1.13 - look

Understand the command "look" as something new.
looking to is an action applying to one thing.
Understand "look to [something]" as looking to.
understand "see the [something]" as looking to.

check an actor looking to a thing:
	if the noun is the first floor map:
		display the Figure of first floor;
	if the noun is the second floor map:
		display the Figure of second floor.


Chapter 2 Geography

Section 2.1 The House

Porch is a room. "The porche is not very large but has a very beautiful garden. The main door leads inside the house".  
Hall is room.  "You are in an empty hall. There is a stair that leads to the second door. You can see doors on north and east, leading to other rooms.

On the left side of the door you can see a map in a frame.".

Main door is a door. It is north of Porch and south of Hall. Main door is closed and locked.
The matching key of the Main door is first key.

Living Room is a room. "The living room is huge and clean. There are some pictures on the wall showing a very serious and not friendly family: the mom, the dad and their little girl. The three of them seem to be very rich and unpleased.". Living room is north of Hall.

Home Office is a room."In the Home Office you can see a desk and a bookshelf. There is also a computer on the desk."

Home office door is a door. It is scenery. It is east of Living Room and west of Home Office. Home office door is closed and locked.
The matching key of the Home office door is second key.


Garage is a room. "The Garage seems not being used regularly. There are no windows and the main door are closed. There are no car in here too.".

Garage door is a door. It is scenery. It is west of Living Room and east of Garage. Garage door is closed and locked.
The matching key of the Garage door is Garage key.

Main Kitchen is a kitchen. "The main kitchen has one cabinet with a sink and one refrigerator, and, on the opposite wall, a counter and one stove" .
Dining Room is a room. "The dinning room is a huge room with simple furnitures. There is a room on the west and another on the south.".Dining room is east of Main Kitchen. Dining Room is north of Living Room.
Lavabo is a bathroom. "The Lavabo is a very small toilet and it seems that it is not being used for decades.

It has a cabinet with a sink right on the left of the door and a toilet on the other side.". Lavabo is east of Hall.
Stairs is a staircase. It is above Hall and below Upper Hall.

[Segundo andar] 
Upper Hall is a room. "You can see a door in every direction, and in one corner you can see the stairs down to the Hall.

In the corner betwen the north and east door, you can see a litlle corner table, with a lampshade and a container with dead flowers. 

On the side of the stair, you can see a map of the house in a frame". 
Large Bedroom is a bedroom. "This seems to be the bedroom of the owner of the house. There is some pictures on the wall and a red carpet in the center of the room. There is an inner room on the west.

The bed is a double bed and is very large.". Large Bedroom is north of Upper Hall.
Medium Bedroom is a a bedroom."This room looks like a guest room, but is empty, just with the basic furniture.

The bed doesn't have a mattress.".  Medium Bedroom is east of Upper Hall.
Small Bedroom is a room. "This seems to be the smallest bedroom of the house, just like a child bedroom. There are just a bed and a small wardrobe in here.". Small Bedroom is west of Upper Hall.
Upper Bathroom is a bathroom."The upper bathroom is large and fancy. The cabinet on the right side of the door seems to be made with quality wood. There is a sink on the cabinet and, on the left side, there is a toilet. On the oposite wall, there is a white bathtub.". Upper Bathroom is south of Upper Hall.
Inner Bathroom is a bathroom. "It is a small bathroom, just with a toilet and a cabinet with a simple sink on it. It is not very fancy, but it is still very organized. Next to the cabinet there is a bathtub". Inner Bathroom is west of Large Bedroom.
First Floor is a region. The Hall, Living Room, Garage, Main Kitchen, Dining Room, Home Office and Lavabo are in First Floor.
Second Floor is a region. The Upper Hall, The Large Bedroom, the medium bedroom,  The Small Bedroom, The Upper Bathroom and the Inner Bathroom are in Second Floor.

Chapter 3 Things

first key is in the old box.
second key is in the bottom drawer.
Garage key is in the can full of coins.

Section 3.1 On the Porch

Wooden chair is a chair.  Wooden chair is in Porch.

Old box is a container. Old box is in Porch.

candle is an unlit lighting thing. string is a thing. bucket is a container.
candle, string are in Old box.

bucket is in Porch.

Section 3.2 On the Hall

Max is a man. "Max, who is a very thin and midium-aged man dressed as a buttler, is standing in front of you. He stares at you with a smile.".
Max is in Hall.

The first floor map is a thing. 
the first floor map is in the hall.

Section 3.3 On the Living Room

The red couch is a fixed in place chair. It is in the Living Room. The red couch is flammable.
The center table is a fixed in place supporter. "The center table is in front of the couch". The center table is in the Living Room. The center table is flammable.
The vase is a container. The vase is on the center table.
The flower is a thing. "a very beautiful red flower, which is not dead yet". The flower is in the vase. The flower is flammable.

Section 3.4 On the Upper Bathroom

The inner bathtub is a bath. The inner bathtub is in Inner Bathroom.
The white bathtub is a bath. The white bathtub is in Upper Bathroom.

Section 3.5 - Large Bedroom

The parents wardrobe is a wardrobe. "The wardrobe is open, and you can see a lot of clothes on the ground, seems like someone took everything in a hurry.

The wardrobe has two drawers.". The parents wardrobe is in large bedroom. The parents wardrobe is open.

The top drawer is a drawer. The top drawer is part of parents wardrobe.
Understand "first drawer" as the top drawer.

The bottom drawer is a drawer. The bottom drawer is part of parents wardrobe.
Understand "second drawer" as the bottom drawer.

After opening the top drawer, say "You see inside the drawer a broken picture frame with a photo of a young girl".

After opening the bottom drawer, say "You see inside the drawer a key".

Section 3.7 - Medium Bedroom

The woden wardrobe is a wardrobe. The woden wardrobe is in medium bedroom. The woden wardrobe is closed.

Section 3.8 - Small Bedroom

Carlie Approval is a truth state that varies.

The small wardrobe is a closed wardrobe. The small wardrobe is in small bedroom.

Carlie is a woman. "Carlie, a little girl, is sitted on the bed looking at you. She looked very happy to see you". Carlie is in the small bedroom.

Section 3.9 - Home Office

The office table is a fixed in place supporter. It is scenery. The office table is in the Home Office.
The computer is a switched off device. It is scenery. The computer is on the office table.

Computer Note Seen is a truth state that varies.
Third Book Seen is a truth state that varies.

After switching on the computer: 
    	say "When you turn the computer on, a message is displaying, saying:[line break][line break]    'Honey, don't forget to put the third book on the shelf in the lavabo. - John'";
	now Computer Note Seen is true.

The shelf is a supporter in the Home Office. It is scenery.
book 1 is on the shelf. The description is "A recipe book". It is a book with printing "You read instructions on how to bake a cake.".
book 2 is on the shelf. The description is "A parenting book.". It is a book with printing "You read about how to take care of a children.".
book 3 is on the shelf. The description is "Margareth's diary". It is a book with printing "'... she is our daughter, but this is the only way to save her. I am going to put the poison on her food, and she won't even feel anything. I wish there was another w...'[line break]The rest is blurred by what looks like water drops.".
book 4 is on the shelf. The description is "A detective book". It is a book with printing "You read the story of a detective solving a crime.".
book 5 is on the shelf. The description is "A psychology book.". It is a book with printing "You read about clinical depression.".
Understand "Margareth's diary", "diary" as book 3.

The book 1, book 2, book 3, book 4, book 5, the office table are flammable.

Carry out reading book 3:
	now Third Book Seen is true.
	
On the shelf is a dvd.

The can full of coins is a container. A can full of coins is closed and openable.
can full of coins is on shelf.

Report taking the can full of coins:
	say "The can seems to have something bigger than a coin inside".

There is a flammable chair in the Home Office. It is scenery.

The Safe is a container. The Safe is closed and fixed in place. Understand "dial" as the Safe. The Safe is in the Home Office. "You can see a safe in here, with a dial which can spin to any number. It seems to be a very heavy.".
In the Safe is a diamond necklace.

Spinning it to is an action applying to one thing and one number. Check spinning it to: if the noun is not the Safe, say "[The noun] does not spin." instead. Report spinning it to: say "Click! and nothing else happens."

Understand "spin [something] to [a number]" as spinning it to.

After spinning the closed Safe to 1306: 
		now the Safe is open; 
		say "Clonk! and the safe door swings slowly open, revealing [a list of things in the Safe]."
		
Section 3.10 Garage

The Chest is a container. The Chest is closed and fixed in place. Understand "keybord" as the Chest. The Chest is in the garage. "You see a very old chest with the name Carlie written in it. It has a small keybord which makes you believe it was locked and it can only be open if you type the correct password".

the doll is a thing.

In the Chest is the doll, a dress, a teddy bear, a sketchbook and a princess crown.
doll, dress, teddy bear, sketchbook are flammable.

Understand "type [a number] on [something]" as typing it on.
Typing it on is an action applying to one number and one thing. 

Check typing it on: if the second noun is not the Chest, say "There is no keybord for you to type it on" instead. 

Report typing it on: say "You hear a sound of failure coming from the keybord and nothing else happens.".

After typing 2211 on the Chest:
	now the chest is open;
	say "A good sound comes from the keybord and the chest opens, revealing [a list of things in the Chest].". 

garage is a dark room. The light switch is a switched off device in the garage. It is fixed in place.

After deciding the scope of the player when the location is the garage:
	place the light switch in scope.

Report switching off the light switch:
	say "Nothing happens, there is no lights".
	
Report switching on the light switch:
	say "Nothing happens, there is no lights".	

A tool box is a locked container. The tool box is in garage.

Understand "box" as a tool box.

hammer is a thing. screw is a thing. screwdriver is a thing.
hammer, screw, screwdriver are in the tool box.

the medallion is a closed and openable container. The medallion is impervious closed. The medallion is in the Inner Bathroom.
the photo is a impervious thing. The photo is in the medallion. 

Rule for printing the name of the photo: say "photo. It is a photo of what seems to be the owners of the house in their weddind. There is the date 13/06 wrote in it.".


Section 3.11 - Kitchen

The tinderbox is an open container with carrying capacity 10. 
10 s-matches are in the tinderbox.

The red cabinet is a cabinet. The red cabinet is in the Main Kitchen.
The tinderbox is in the red cabinet.

The garbage basket is a closed and openable container. The garbage basket is in the Main Kitchen.
The poison is a container. Rule for printing the name of the poison: say "bottle (a small bottle with a liquid inside)".
Understand "bottle" as the poison.
The poison is in the garbage basket.

Instead of drinking the poison:
	say "That was dumb.";
	end the story saying "You have died.".
	
Section 3.12 - upper hall

The second floor map is a thing.
The second floor map is in the upper hall.

Chapter 4 Dialogs

Section 4.1 Max

After saying hello to max, say "'Hello, friend', you say.

'Hello and welcome, sir', he answers, still smiling. How he could be so calm?"

After quizzing Max about Max: 
	say "'Humm... who are you my friend?', you ask.
	
	'I am Max and I work here for mister and misters Whinehouse. Or I use to work a long time ago, before I... .', Max answers and stare to nothing.".
After asking Max about "the house":
	say "'What do you know about this house? Is this your house?', you ask.

	'This is the house of mister and misters Whinehouse. Since I am no longer alive, I believe I can't prevent you from entering. So, feel free to look around', he answers, looking at you with a suspicious smile.".
	
Instead of asking Max about "house", try asking Max about "the house".

After asking Max about "treasure":
	if Max Approval is false:
		say "'Do you know where could be a treasure in this house?', you ask. 

		He stares at you and he, for the first time, is not smiling anymore.
		'I suggest you go away, sir. This house is under my responsability and I certainly will not allow you to take anything.', he answers.";
	otherwise:
		say "'Do you know where could be a treasure in this house?', you ask. 
		
		'You was capable of find the truth about my death. I'm sure you can handle to find a litlle treasure my friend.'He answers.".

Instead of asking Max about "the treasure", try asking Max about "treasure".

After asking Max about "dead", say "'Are you really dead?', you ask.

'Yes, I've died a long time ago. Don't ask me how, because I can't remember', he answer, but he doesn't seem being honest.".
Instead of asking Max about "his dead", try asking Max about "dead".

After quizzing Max about the computer:
	if Computer Note Seen is true, say "'Do you know about that note on the computer?', you ask.

	'The note? No, I don't know about any note. I can't go in the home office, the Mr, and Mrs Whinehouse don't allow me to.', he answers.";
	if Computer Note Seen is false, say "'That computer still works?',  you ask.

	'Have you tried to turn it on?', he answers with a smile."

After informing Max about the book 3:
	say "'Listen, Max. I saw the Mrs. Whinehouse's diary and she tried to kill her own daughter with poison. I don't know why, but she seemed to believe that this was the only way'

	Max looked at you with disbelif.

	'That can't be true... she's loved little miss Whinehosue. Of course that miss Whinehouse was always sick and demanded a lot of attention, but she couldn't have done this. It was me. I'm sure that I used something spoiled and...', he answers.

	'It wouldn't be enough. Just spoiled food wouldn't kill you both. She did it to miss Whinehouse. But how it killed you?', you intervenied.

	'I always tried the food before give it to miss Whinehouse, to know if it is too salty or sweety. That was enough to kill me, what it seems. Thank you, my friend. You can't imagine how much weight you just take off my back', he answers with relief";
	now Max Approval is true.
Instead of telling Max about "the truth", try informing Max about the book 3.
Instead of telling Max about "truth", try informing Max about the book 3.
Instead of telling Max about "death", try informing Max about the book 3.
Instead of telling Max about "dead", try informing Max about the book 3.
Instead of telling Max about "his death", try informing Max about the book 3.
Instead of telling Max about "Carlie's death", try informing Max about the book 3.
Instead of telling Max about "poison", try informing Max about the book 3.
Instead of telling Max about "the poison", try informing Max about the book 3.
	
After quizzing Max about Carlie, say "'That little girl upstairs... do you know her?', you ask.

	'Ah, little miss Whinehouse... she is so sweet and lovely. How could I be so displiscent... If I was more careful, she wouldn't be dead now.... forget about it, it is just an old man regreting his past.', he answers";


The block giving rule is not listed in the check giving it to rules

Check an actor giving a thing to Max:
	if the noun is the flower, say "Max smile and accept the flower. He put it in his pocket and then say: 'Its a beautiful flower, thank you.'";
	otherwise say "Max doesn't seem interested." instead.
	
Section 4.2 Carlie

After saying hello to Carlie, say "'Hello little girl.', you say.

	'Hello! I am Carlie! I'm so happy that now I have someone to play with'.".

After quizzing Carlie about Carlie, say "'Who are you? Did you live here?', you ask.

'Ah, yeah, this is my house. Mama and Papa are not at home but I can take care of the house by myself. I am Carlie Whinehouse', she answers proudly.".

After asking Carlie about "treasure": 
	if Carlie has the doll, say "'Now you could tell me where are the treasure?', you ask.

	'Well... You help me to find my treasure so maybe I can help you with yours. Mama and Papa has a very huge safe in their office. I'm sure they keep a treasure there.', she says";
	otherwise say "'Do you know where could be a treasure in this house?', you ask. 

	'Treasure? Ah, I have a treasure. Marly, my little doll is so beautiful and funny. She is perfect, just like a treasure. But...', her eyes filled with water. She was about to cry 'I don't know where Marly is. She is my favourite doll and... and... I lost her'.".
Instead of asking Carlie about "the treasure", try asking Carlie about "treasure".
	
After asking Carlie about "age", say "'How old are you Carlie?', you ask.

'I am 8 years old', she answer and give you a happy smile.".

After asking Carlie about "dead":
	say "'Are you dead?', you ask.

	She stares at you and, suddenly, she starts to cry. You try to confort her but she just keeps repeating 'I'm not dead. I'm not a ghost. Mama... Papa...'.
	
	Just as sudden as she started to cry, she looks at you and say: 'YOU ARE THE ONE WHO ARE DEAD NOW'.

	She runs into you and everything goes dark.";
	end the story saying "You have died".
Instead of asking Carlie about "her death", try asking Carlie about "dead".
Instead of asking Carlie about "death", try asking Carlie about "dead".	
Instead of asking Carlie about "being dead", try asking Carlie about "dead".
Instead of telling Carlie about something, try asking Carlie about it.

After asking Carlie about "important number":
	say "'Carlie you have some number you like, or some important number?'
	
	'Hmm... OH!!, I love the number of my birthay, is 22/11, is like 4 numbers, but have just 2' she laught and seems to be very happy".
Instead of asking Carlie about "number", try asking Carlie about "important number".
Instead of asking Carlie about "numbers", try asking Carlie about "important number".
Instead of asking Carlie about "important numbers", try asking Carlie about "important number".
Instead of asking Carlie about "password", try asking Carlie about "important number".

After quizzing Carlie about Max, say "'That man downstairs... do you know him, right?', you ask. 

	'Of course I know. He is Max and he is very careful with me. He always tastes my food to know if it is too salty or sweety, even though mama and papa say he is spoiling me', she answers, laughing".
	
The block giving rule is not listed in the check giving it to rules.

Check an actor giving a thing to Carlie:
	if the noun is the doll: 
		say "She looks at the doll with tears in her eyes, but she seems very happy. She taked the doll from you and hugged it very tigh.

	'You are REALLY my best friend. You find my treasure. Thanks!', she says.";
		now Carlie Approval is true;
	Otherwise: 
		say "Carlie doesn't seem interested." instead; 
	
Chapter 5 What Happens when entering

Being Outside the House is a Scene. 
Being Outside the House begins when play begins.
Being Outside the House ends when player is in Hall.

Before taking the first key during Being Outside the House:
	Say "A chill runs up your spine".

Chapter 6 Inside the house

Being Inside the House is a Scene.
Being Inside the House begins when player is in First Floor.
Being Inside the House ends when player has the diamond necklace.

Before taking the diamond necklace during Being Inside the House:
	Say "You've found your treasure, congratulations. Now you just have get the hell out of here. It will be easy... right?
	
	A chill runs up your spine".


Chapter 7 Running out the house

Running out the house is a Scene.
Running out the house begins when player has the diamond necklace.
Running out the house ends when player is in Porch.

Check going west when player is carrying the diamond necklace during Running out the house:
	if Max Approval is false:
		 say "You heard Max on your left looking at you. He is still smiling but his eyes show you that he is not happy at all. He is scary. He says 'Dear guest, I'm afraid that you are no worth of anything in this house. So you can't no longer stay.'.";
	if Carlie Approval is false: 
		say "On your right you [if Max Approval is false]also [end if]heard Carlie crying. She looks at you and she seems to be mad. 'Now that you have your treasure you are leaving right. I can't let you. I'll be alone. You have to stay here FOREVER!', she says.";
	if Max Approval is false or Carlie Approval is false: 
		say "Then everything goes dark";
		end the story saying "You have died".
	
Check going to Porch during Running out the house:
	say "You leave the house feeling that, even though you had some difficulties, you have no regrets on dealing with those two ghosts. 

	Somehow, when you step out of the house, you feel that they are no longer in there. They have left to a better place, since there is nothing holding them here anymore. And you are rich.";
	end the story saying "You won.".

Chapter 8 - Inicio

Player is in the porch.

When play begins: 
	say "[bold type]Introduction:[roman type]
	
	You are in a long time abandoned house, in the middle of the forest. Its windows are broken but it is possible for you to see that some of its furnitures are intact inside.

	You heard some rumors saying that this house is haunted, but it holds a very awesome treasure.
	
	A lot of treasure hunters tried their best adventuring in this house. Some never get out of there and those who left have never spoken a word about it.

	You are confident that you will be the one who will find the treasure and prove, to everyone, that you are the greatest treasure hunter in the world.

	Let us see if you are right...".