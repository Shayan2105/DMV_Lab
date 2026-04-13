import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Paste your dataset as a string
data = """AppID,Name,Release_Date,Primary_Genre,All_Tags,Price_USD,Discount_Pct,Review_Score_Pct,Total_Reviews,Steam_Deck_Status,Estimated_Owners,24h_Peak_Players
730,Counter-Strike 2,########,Action,FPS;Shooter,0,0,83,4980365,Unknown,1.49E+08,1013936
2868840,Slay the Spire 2,########,Indie,Strategy,24.99,0,97,49549,Unknown,1486470,0
3321460,Crimson Desert,########,Action,Open World,69.99,0,0,0,Unknown,0,0
3065800,Marathon,########,Action,Shooter,39.99,0,90,24360,Unknown,730800,0
3764200,Resident Evil Requiem,########,Action,Horror,69.99,0,96,79667,Unknown,2390010,0
2157830,John Carpenter's Toxic Commando,########,Action,Zombies;Shooter;Online Co-Op;FPS;PvE;Action;Adventure;Looter Shooter;Action-Adventure;First-Person,39.99,0,83,2765,Unknown,82950,0
1144200,Ready or Not,########,Action,Tactical;Realistic;FPS;Shooter;Multiplayer;Singleplayer;Co-op;Horror;First-Person;Action,49.99,0,85,243810,Unknown,7314300,4296
1172470,Apex Legends™,########,Action,Free to Play;Multiplayer;Battle Royale;FPS;Shooter;First-Person;PvP;Action;Hero Shooter;Team-Based,0,0,65,1577,Unknown,47310,124262
1808500,ARC Raiders,########,Action,Extraction Shooter;Multiplayer;PvE;PvP;Third-Person Shooter;Post-apocalyptic;Shooter;Online Co-Op;Survival;Sci-fi,39.99,0,79,264150,Unknown,7924500,0
2852190,Monster Hunter Stories 3: Twisted Reflection,########,Adventure,RPG;Creature Collector;JRPG;Exploration;Turn-Based Combat;Cartoony;Adventure;Dragons;Character Customization;Singleplayer,69.99,0,75,1570,Unknown,47100,0
1167630,Teardown,########,Action,Destruction;Physics;Sandbox;Voxel;Multiplayer;Heist;Singleplayer;Indie;Replay Value;First-Person,14.99,50,94,115777,Unknown,3473310,1984
2552430,KINGDOM HEARTS -HD 1.5+2.5 ReMIX-,########,Action,Action;RPG;Adventure;JRPG;Great Soundtrack;Action-Adventure;Emotional;Story Rich;Singleplayer;Fantasy,24.99,50,89,8167,Unknown,245010,886
4069520,Super Battle Golf,########,Casual,Multiplayer;Online Co-Op;Co-op;Sports;Physics;Exploration;Comedy;3D;Action;Adventure,7.99,0,95,4025,Unknown,120750,0
2767030,Marvel Rivals,########,Action,Free to Play;Multiplayer;Hero Shooter;Third-Person Shooter;Superhero;PvP;Action;Team-Based;Competitive;Shooter,0,0,68,0,Unknown,0,106611
1222670,The Sims™ 4,########,Adventure,Life Sim;Free to Play;Character Customization;Building;Simulation;Romance;Singleplayer;Sandbox;Dating Sim;Relaxing,0,0,79,82661,Unknown,2479830,25276
2778610,Over The Top: WWI,########,Action,Multiplayer;Action;World War I;Third-Person Shooter;FPS;Shooter;Historical;Simulation;3D;Cinematic,16.26,15,88,3572,Unknown,107160,0
359550,Tom Clancy's Rainbow Six Siege,########,Action,FPS;PvP;Multiplayer;Shooter;Tactical;eSports;Competitive;Online Co-Op;Action;Hero Shooter,0,0,75,1234092,Unknown,37022760,51847
553850,HELLDIVERS™ 2,########,Action,Online Co-Op;PvE;Third-Person Shooter;Multiplayer;Shooter;Action;Co-op;Sci-fi;Extraction Shooter;Capitalism,39.99,0,70,807861,Unknown,24235830,53399
230410,Warframe,########,Action,Free to Play;Looter Shooter;Action RPG;Third-Person Shooter;Action;RPG;Third Person;Massively Multiplayer;Online Co-Op;Character Customization,0,0,90,2880,Unknown,86400,36195
2357570,Overwatch®,########,Action,Free to Play;Hero Shooter;FPS;Multiplayer;Team-Based;MOBA;First-Person;Third-Person Shooter;Third Person;PvP,0,0,60,257,Unknown,7710,0
236390,War Thunder,########,Action,Free to Play;Simulation;Vehicular Combat;Combat;Flight;World War II;VR;War;Military;Tanks,0,0,76,1961,Unknown,58830,50478
3472040,NBA 2K26,########,Sports,Gambling;Sports;Basketball;Simulation;eSports;3D;Multiplayer;Controller;Singleplayer;Character Customization,19.99,75,74,12634,Unknown,379020,0
1462040,FINAL FANTASY VII REMAKE INTERGRADE,########,Action,RPG;JRPG;Action RPG;Singleplayer;Action-Adventure;Party-Based RPG;Spectacle fighter;Third Person;Action;Adventure,19.99,50,84,37281,Unknown,1118430,761
3240220,Grand Theft Auto V Enhanced,########,Action,Open World;Action;Sexual Content;Multiplayer;Crime;Mature;Shooter;Third Person;First-Person;Adventure,19.79,56,89,152083,Unknown,4562490,39502
1149460,ICARUS,########,Action,Survival;Open World Survival Craft;Multiplayer;Base Building;Online Co-Op;Crafting;Open World;Exploration;Building;Co-op,11.89,66,77,49598,Unknown,1487940,1492
2975950,Solasta II,########,Adventure,Early Access;Adventure;RPG;Strategy;Party-Based RPG;Turn-Based Strategy;CRPG;Strategy RPG;3D;Top-Down,35.99,10,73,1277,Unknown,38310,0
1086940,Baldur's Gate 3,########,Adventure,RPG;Character Customization;Choices Matter;Dungeons & Dragons;Turn-Based Combat;Story Rich;Sexual Content;CRPG;Fantasy;Adventure,59.99,0,94,730296,Unknown,21908880,54771
3564740,Where Winds Meet,########,Action,Open World;Free to Play;Multiplayer;Souls-like;Action RPG;Online Co-Op;MMORPG;Adventure;Action;Story Rich,0,0,79,0,Unknown,0,0
252490,Rust,########,Action,Survival;Crafting;Multiplayer;Open World;Open World Survival Craft;Building;PvP;Sandbox;Adventure;First-Person,39.99,0,84,1116689,Unknown,33500670,143870
381210,Dead by Daylight,########,Action,Horror;Multiplayer;Survival Horror;Online Co-Op;Co-op;Survival;Gore;Team-Based;Blood;Third Person,19.99,0,79,647076,Unknown,19412280,44886
"""

# Convert string to dataframe
df = pd.read_csv(StringIO(data))

# Clean column names
df.columns = df.columns.str.strip()

# Convert numeric columns
df['Total_Reviews'] = pd.to_numeric(df['Total_Reviews'], errors='coerce')
df['24h_Peak_Players'] = pd.to_numeric(df['24h_Peak_Players'], errors='coerce')

# -------------------------------
# 📊 BAR CHART
# -------------------------------
plt.figure(figsize=(8,4))
plt.bar(df['Name'], df['Total_Reviews'], color='skyblue')
plt.xticks(rotation=45)
plt.title('Total Reviews by Game')
plt.show()
plt.grid(True)

# -------------------------------
# 📈 LINE CHART
# -------------------------------
plt.figure(figsize=(8,4))
plt.plot(df['Name'], df['24h_Peak_Players'], marker='o')
plt.xticks(rotation=45)
plt.title('24h Peak Players')
plt.show()
plt.grid(True)

# -------------------------------
# 🍰 PIE CHART
# -------------------------------
genre_counts = df['Primary_Genre'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title('Genre Distribution')
plt.show()
plt.grid(True)