from UserClass import user
from GraphClass import Graph

## Create test users to check how will my code deal with 

user1 = user("Jacob","Schmith","J_smith","B12","jabo.smith@gmail.com","food lover")
user2 = user("charles","Darwin","Charles.D","B13","charles.darwin@gmail.com","the animals")
user3 = user("Michael", "Johnson", "M_johnson", "B872", "michael.johnson@gmail.com", "nature enthusiast")
user4 = user("Sarah", "Miller", "S_miller", "B483", "sarah.miller@gmail.com", "bookworm")
user5 = user("David", "Brown", "D_brown", "B927", "david.brown@gmail.com", "music lover")
user6 = user("Emily", "Jones", "E_jones", "B364", "emily.jones@gmail.com", "art fanatic")
user7 = user("Daniel", "Garcia", "D_garcia", "B175", "daniel.garcia@gmail.com", "travel addict")
user8 = user("Jessica", "Martinez", "J_martinez", "B981", "jessica.martinez@gmail.com", "fitness guru")
user9 = user("James", "Rodriguez", "J_rodriguez", "B504", "james.rodriguez@gmail.com", "tech geek")
user10 = user("Amanda", "Wilson", "A_wilson", "B762", "amanda.wilson@gmail.com", "movie buff")
user11 = user("Joshua", "Anderson", "J_anderson", "B628", "joshua.anderson@gmail.com", "history nerd")
user12 = user("Megan", "Thomas", "M_thomas", "B319", "megan.thomas@gmail.com", "foodie")
user13 = user("Andrew", "Taylor", "A_taylor", "B534", "andrew.taylor@gmail.com", "gamer")
user14 = user("Lauren", "Moore", "L_moore", "B746", "lauren.moore@gmail.com", "dog lover")
user15 = user("Brandon", "Jackson", "B_jackson", "B291", "brandon.jackson@gmail.com", "photography enthusiast")
user16 = user("Hannah", "Martin", "H_martin", "B359", "hannah.martin@gmail.com", "yoga practitioner")
user17 = user("Matthew", "Lee", "M_lee", "B684", "matthew.lee@gmail.com", "cyclist")
user18 = user("Elizabeth", "Perez", "E_perez", "B543", "elizabeth.perez@gmail.com", "reader")
user19 = user("Anthony", "White", "A_white", "B872", "anthony.white@gmail.com", "movie lover")
user20 = user("Olivia", "Harris", "O_harris", "B298", "olivia.harris@gmail.com", "blogger")
user21 = user("Christopher", "Clark", "C_clark", "B152", "christopher.clark@gmail.com", "adventure seeker")
user22 = user("Ashley", "Lewis", "A_lewis", "B639", "ashley.lewis@gmail.com", "craft maker")
user23 = user("Alexander", "Robinson", "A_robinson", "B785", "alexander.robinson@gmail.com", "gardening lover")
user24 = user("Stephanie", "Walker", "S_walker", "B423", "stephanie.walker@gmail.com", "dancer")
user25 = user("Ryan", "Young", "R_young", "B940", "ryan.young@gmail.com", "car enthusiast")
user26 = user("Laura", "King", "L_king", "B218", "laura.king@gmail.com", "singer")
user27 = user("Nicholas", "Wright", "N_wright", "B536", "nicholas.wright@gmail.com", "painter")
user28 = user("Rachel", "Lopez", "R_lopez", "B784", "rachel.lopez@gmail.com", "actor")
user29 = user("Jonathan", "Hill", "J_hill", "B492", "jonathan.hill@gmail.com", "chef")
user30 = user("Emily", "Scott", "E_scott", "B357", "emily.scott@gmail.com", "diver")
user31 = user("Zachary", "Green", "Z_green", "B678", "zachary.green@gmail.com", "swimmer")
user32 = user("Kimberly", "Adams", "K_adams", "B189", "kimberly.adams@gmail.com", "pianist")
user33 = user("Jacob", "Baker", "J_baker", "B740", "jacob.baker@gmail.com", "violinist")
user34 = user("Alexis", "Gonzalez", "A_gonzalez", "B832", "alexis.gonzalez@gmail.com", "cellist")
user35 = user("Tyler", "Nelson", "T_nelson", "B549", "tyler.nelson@gmail.com", "runner")
user36 = user("Samantha", "Carter", "S_carter", "B217", "samantha.carter@gmail.com", "skier")
user37 = user("Jordan", "Mitchell", "J_mitchell", "B893", "jordan.mitchell@gmail.com", "snowboarder")
user38 = user("Natalie", "Perez", "N_perez", "B638", "natalie.perez@gmail.com", "golfer")
user39 = user("Dylan", "Roberts", "D_roberts", "B172", "dylan.roberts@gmail.com", "tennis player")
user40 = user("Victoria", "Turner", "V_turner", "B735", "victoria.turner@gmail.com", "chess player")
user41 = user("Adam", "Phillips", "A_phillips", "B421", "adam.phillips@gmail.com", "footballer")
user42 = user("Madison", "Campbell", "M_campbell", "B568", "madison.campbell@gmail.com", "cricketer")
user43 = user("Ethan", "Parker", "E_parker", "B379", "ethan.parker@gmail.com", "basketball player")
user44 = user("Sophia", "Evans", "S_evans", "B487", "sophia.evans@gmail.com", "volleyball player")
user45 = user("Austin", "Edwards", "A_edwards", "B192", "austin.edwards@gmail.com", "baseball player")
user46 = user("Brittany", "Collins", "B_collins", "B742", "brittany.collins@gmail.com", "hiker")
user47 = user("Jack", "Stewart", "J_stewart", "B384", "jack.stewart@gmail.com", "mountain climber")
user48 = user("Jenna", "Sanchez", "J_sanchez", "B827", "jenna.sanchez@gmail.com", "biker")
user49 = user("Isaac", "Morris", "I_morris", "B213", "isaac.morris@gmail.com", "runner")
user50 = user("Alexandra", "Rogers", "A_rogers", "B361", "alexandra.rogers@gmail.com", "triathlete")
user51 = user("Nathan", "Reed", "N_reed", "B452", "nathan.reed@gmail.com", "marathoner")
user52 = user("Melissa", "Cook", "M_cook", "B178", "melissa.cook@gmail.com", "sprinter")
user53 = user("Aaron", "Morgan", "A_morgan", "B640", "aaron.morgan@gmail.com", "long jumper")
user54 = user("Alyssa", "Bell", "A_bell", "B831", "alyssa.bell@gmail.com", "pole vaulter")
user55 = user("Justin", "Murphy", "J_murphy", "B582", "justin.murphy@gmail.com", "high jumper")
user56 = user("Michaela", "Bailey", "M_bailey", "B193", "michaela.bailey@gmail.com", "javelin thrower")
user57 = user("Samuel", "Rivera", "S_rivera", "B472", "samuel.rivera@gmail.com", "discus thrower")
user58 = user("Brianna", "Cooper", "B_cooper", "B182", "brianna.cooper@gmail.com", "shot putter")
user59 = user("Gabriel", "Richardson", "G_richardson", "B529", "gabriel.richardson@gmail.com", "weightlifter")
user60 = user("Amber", "Cox", "A_cox", "B328", "amber.cox@gmail.com", "gymnast")
user61 = user("Lucas", "Ward", "L_ward", "B194", "lucas.ward@gmail.com", "figure skater")
user62 = user("Katie", "Howard", "K_howard", "B257", "katie.howard@gmail.com", "ice dancer")
user63 = user("Christian", "Peterson", "C_peterson", "B829", "christian.peterson@gmail.com", "speed skater")
user64 = user("Courtney", "Gray", "C_gray", "B169", "courtney.gray@gmail.com", "bobsledder")
user65 = user("Connor", "Ramirez", "C_ramirez", "B781", "connor.ramirez@gmail.com", "skater")
user66 = user("Allison", "James", "A_james", "B468", "allison.james@gmail.com", "paraglider")
user67 = user("Sean", "Watson", "S_watson", "B572", "sean.watson@gmail.com", "windsurfer")
user68 = user("Chloe", "Brooks", "C_brooks", "B624", "chloe.brooks@gmail.com", "kite surfer")
user69 = user("Eli", "Kelly", "E_kelly", "B835", "eli.kelly@gmail.com", "free diver")
user70 = user("Andrea", "Sanders", "A_sanders", "B268", "andrea.sanders@gmail.com", "sailor")
user71 = user("Jason", "Price", "J_price", "B395", "jason.price@gmail.com", "water polo player")
user72 = user("Sabrina", "Bennett", "S_bennett", "B517", "sabrina.bennett@gmail.com", "rower")
user73 = user("Kevin", "Wood", "K_wood", "B749", "kevin.wood@gmail.com", "canoeist")
user74 = user("Christina", "Barnes", "C_barnes", "B176", "christina.barnes@gmail.com", "kayaker")
user75 = user("Evan", "Ross", "E_ross", "B592", "evan.ross@gmail.com", "surfer")
user76 = user("Tiffany", "Henderson", "T_henderson", "B843", "tiffany.henderson@gmail.com", "diver")
user77 = user("Benjamin", "Coleman", "B_coleman", "B364", "benjamin.coleman@gmail.com", "snorkeler")
user78 = user("Haley", "Jenkins", "H_jenkins", "B498", "haley.jenkins@gmail.com", "fisher")
user79 = user("Patrick", "Perry", "P_perry", "B682", "patrick.perry@gmail.com", "boater")
user80 = user("Erica", "Powell", "E_powell", "B795", "erica.powell@gmail.com", "jet skier")
user81 = user("Blake", "Long", "B_long", "B289", "blake.long@gmail.com", "water skier")
user82 = user("Rebecca", "Patterson", "R_patterson", "B576", "rebecca.patterson@gmail.com", "wakeboarder")
user83 = user("Lucas", "Hughes", "L_hughes", "B483", "lucas.hughes@gmail.com", "river rafter")
user84 = user("Amber", "Flores", "A_flores", "B184", "amber.flores@gmail.com", "swimmer")
user85 = user("Brandon", "Washington", "B_washington", "B731", "brandon.washington@gmail.com", "freeskier")
user86 = user("Brooke", "Butler", "B_butler", "B469", "brooke.butler@gmail.com", "freerunner")
user87 = user("Derek", "Simmons", "D_simmons", "B924", "derek.simmons@gmail.com", "parkour athlete")
user88 = user("Katie", "Foster", "K_foster", "B513", "katie.foster@gmail.com", "trampolinist")
user89 = user("Zachary", "Gonzalez", "Z_gonzalez", "B682", "zachary.gonzalez@gmail.com", "cheerleader")
user90 = user("Kelsey", "Bryant", "K_bryant", "B473", "kelsey.bryant@gmail.com", "diver")
user91 = user("Logan", "Alexander", "L_alexander", "B582", "logan.alexander@gmail.com", "rugby player")
user92 = user("Kelly", "Russell", "K_russell", "B274", "kelly.russell@gmail.com", "lacrosse player")
user93 = user("Caleb", "Griffin", "C_griffin", "B648", "caleb.griffin@gmail.com", "ultimate frisbee player")
user94 = user("Hailey", "Diaz", "H_diaz", "B359", "hailey.diaz@gmail.com", "cricket player")
user95 = user("Gabrielle", "Hayes", "G_hayes", "B592", "gabrielle.hayes@gmail.com", "handball player")
user96 = user("Shane", "Myers", "S_myers", "B743", "shane.myers@gmail.com", "hockey player")
user97 = user("Riley", "Ford", "R_ford", "B281", "riley.ford@gmail.com", "field hockey player")
user98 = user("Jared", "Hamilton", "J_hamilton", "B542", "jared.hamilton@gmail.com", "softball player")
user99 = user("Jillian", "Graham", "J_graham", "B375", "jillian.graham@gmail.com", "lacrosse player")
user100 = user("Erik", "Fisher", "E_fisher", "B481", "erik.fisher@gmail.com", "rollerblader")



## create a graph using the above users

SocialNetworkWeb = Graph()

SocialNetworkWeb.addUserToGraph(user1.username)
SocialNetworkWeb.addUserToGraph("user2")
SocialNetworkWeb.addUserToGraph("user3")
SocialNetworkWeb.addUserToGraph("user4")
SocialNetworkWeb.addUserToGraph("user5")
SocialNetworkWeb.addUserToGraph("user6")
SocialNetworkWeb.addUserToGraph("user7")
SocialNetworkWeb.addUserToGraph("user8")
SocialNetworkWeb.addUserToGraph("user9")
SocialNetworkWeb.addUserToGraph("user10")
SocialNetworkWeb.addUserToGraph("user11")
SocialNetworkWeb.addUserToGraph("user12")
SocialNetworkWeb.addUserToGraph("user13")
SocialNetworkWeb.addUserToGraph("user14")
SocialNetworkWeb.addUserToGraph("user15")
SocialNetworkWeb.addUserToGraph("user16")
SocialNetworkWeb.addUserToGraph("user17")
SocialNetworkWeb.addUserToGraph("user18")
SocialNetworkWeb.addUserToGraph("user19")
SocialNetworkWeb.addUserToGraph("user20")
SocialNetworkWeb.addUserToGraph("user21")
SocialNetworkWeb.addUserToGraph("user22")
SocialNetworkWeb.addUserToGraph("user23")
SocialNetworkWeb.addUserToGraph("user24")
SocialNetworkWeb.addUserToGraph("user25")
SocialNetworkWeb.addUserToGraph("user26")
SocialNetworkWeb.addUserToGraph("user27")
SocialNetworkWeb.addUserToGraph("user28")
SocialNetworkWeb.addUserToGraph("user29")
SocialNetworkWeb.addUserToGraph("user30")
SocialNetworkWeb.addUserToGraph("user31")
SocialNetworkWeb.addUserToGraph("user32")
SocialNetworkWeb.addUserToGraph("user33")
SocialNetworkWeb.addUserToGraph("user34")
SocialNetworkWeb.addUserToGraph("user35")
SocialNetworkWeb.addUserToGraph("user36")
SocialNetworkWeb.addUserToGraph("user37")
SocialNetworkWeb.addUserToGraph("user38")
SocialNetworkWeb.addUserToGraph("user39")
SocialNetworkWeb.addUserToGraph("user40")
SocialNetworkWeb.addUserToGraph("user41")
SocialNetworkWeb.addUserToGraph("user42")
SocialNetworkWeb.addUserToGraph("user43")
SocialNetworkWeb.addUserToGraph("user44")
SocialNetworkWeb.addUserToGraph("user45")
SocialNetworkWeb.addUserToGraph("user46")
SocialNetworkWeb.addUserToGraph("user47")
SocialNetworkWeb.addUserToGraph("user48")
SocialNetworkWeb.addUserToGraph("user49")
SocialNetworkWeb.addUserToGraph("user50")
SocialNetworkWeb.addUserToGraph("user51")
SocialNetworkWeb.addUserToGraph("user52")
SocialNetworkWeb.addUserToGraph("user53")
SocialNetworkWeb.addUserToGraph("user54")
SocialNetworkWeb.addUserToGraph("user55")
SocialNetworkWeb.addUserToGraph("user56")
SocialNetworkWeb.addUserToGraph("user57")
SocialNetworkWeb.addUserToGraph("user58")
SocialNetworkWeb.addUserToGraph("user59")
SocialNetworkWeb.addUserToGraph("user60")
SocialNetworkWeb.addUserToGraph("user61")
SocialNetworkWeb.addUserToGraph("user62")
SocialNetworkWeb.addUserToGraph("user63")
SocialNetworkWeb.addUserToGraph("user64")
SocialNetworkWeb.addUserToGraph("user65")
SocialNetworkWeb.addUserToGraph("user66")
SocialNetworkWeb.addUserToGraph("user67")
SocialNetworkWeb.addUserToGraph("user68")
SocialNetworkWeb.addUserToGraph("user69")
SocialNetworkWeb.addUserToGraph("user70")
SocialNetworkWeb.addUserToGraph("user71")
SocialNetworkWeb.addUserToGraph("user72")
SocialNetworkWeb.addUserToGraph("user73")
SocialNetworkWeb.addUserToGraph("user74")
SocialNetworkWeb.addUserToGraph("user75")
SocialNetworkWeb.addUserToGraph("user76")
SocialNetworkWeb.addUserToGraph("user77")
SocialNetworkWeb.addUserToGraph("user78")
SocialNetworkWeb.addUserToGraph("user79")
SocialNetworkWeb.addUserToGraph("user80")
SocialNetworkWeb.addUserToGraph("user81")
SocialNetworkWeb.addUserToGraph("user82")
SocialNetworkWeb.addUserToGraph("user83")
SocialNetworkWeb.addUserToGraph("user84")
SocialNetworkWeb.addUserToGraph("user85")
SocialNetworkWeb.addUserToGraph("user86")
SocialNetworkWeb.addUserToGraph("user87")
SocialNetworkWeb.addUserToGraph("user88")
SocialNetworkWeb.addUserToGraph("user89")
SocialNetworkWeb.addUserToGraph("user90")
SocialNetworkWeb.addUserToGraph("user91")
SocialNetworkWeb.addUserToGraph("user92")
SocialNetworkWeb.addUserToGraph("user93")
SocialNetworkWeb.addUserToGraph("user94")
SocialNetworkWeb.addUserToGraph("user95")
SocialNetworkWeb.addUserToGraph("user96")
SocialNetworkWeb.addUserToGraph("user97")
SocialNetworkWeb.addUserToGraph("user98")
SocialNetworkWeb.addUserToGraph("user99")
SocialNetworkWeb.addUserToGraph("user100")



SocialNetworkWeb.addConnection(user1.username, "user2")
SocialNetworkWeb.addConnection(user1.username,"user3")
SocialNetworkWeb.addConnection(user1.username, "user47")
SocialNetworkWeb.addConnection(user1.username, "user52")
SocialNetworkWeb.addConnection(user1.username, "user23")
SocialNetworkWeb.addConnection(user1.username, "user35")
SocialNetworkWeb.addConnection("user2", "user39")
SocialNetworkWeb.addConnection("user2", "user9")
SocialNetworkWeb.addConnection("user2", "user17")
SocialNetworkWeb.addConnection("user2", "user7")
SocialNetworkWeb.addConnection("user3", "user96")
SocialNetworkWeb.addConnection("user3", "user10")
SocialNetworkWeb.addConnection("user3", "user60")
SocialNetworkWeb.addConnection("user3", "user86")
SocialNetworkWeb.addConnection("user4", "user5")
SocialNetworkWeb.addConnection("user4", "user90")
SocialNetworkWeb.addConnection("user4", "user25")
SocialNetworkWeb.addConnection("user5", "user56")
SocialNetworkWeb.addConnection("user5", "user83")
SocialNetworkWeb.addConnection("user6", "user33")
SocialNetworkWeb.addConnection("user6", "user15")
SocialNetworkWeb.addConnection("user6", "user44")
SocialNetworkWeb.addConnection("user7", "user21")
SocialNetworkWeb.addConnection("user7", "user92")
SocialNetworkWeb.addConnection("user7", "user46")
SocialNetworkWeb.addConnection("user8", "user41")
SocialNetworkWeb.addConnection("user8", "user27")
SocialNetworkWeb.addConnection("user9", "user53")
SocialNetworkWeb.addConnection("user9", "user11")
SocialNetworkWeb.addConnection("user10", "user84")
SocialNetworkWeb.addConnection("user10", "user91")
SocialNetworkWeb.addConnection("user11", "user43")
SocialNetworkWeb.addConnection("user11", "user28")
SocialNetworkWeb.addConnection("user12", "user37")
SocialNetworkWeb.addConnection("user12", "user95")
SocialNetworkWeb.addConnection("user13", "user65")
SocialNetworkWeb.addConnection("user13", "user14")
SocialNetworkWeb.addConnection("user14", "user75")
SocialNetworkWeb.addConnection("user14", "user71")
SocialNetworkWeb.addConnection("user15", "user26")
SocialNetworkWeb.addConnection("user15", "user57")
SocialNetworkWeb.addConnection("user16", "user58")
SocialNetworkWeb.addConnection("user16", "user20")
SocialNetworkWeb.addConnection("user17", "user63")
SocialNetworkWeb.addConnection("user17", "user42")
SocialNetworkWeb.addConnection("user18", "user54")
SocialNetworkWeb.addConnection("user18", "user87")
SocialNetworkWeb.addConnection("user19", "user73")
SocialNetworkWeb.addConnection("user19", "user80")
SocialNetworkWeb.addConnection("user20", "user85")
SocialNetworkWeb.addConnection("user20", "user36")
SocialNetworkWeb.addConnection("user21", "user66")
SocialNetworkWeb.addConnection("user21", "user55")
SocialNetworkWeb.addConnection("user22", "user81")
SocialNetworkWeb.addConnection("user22", "user79")
SocialNetworkWeb.addConnection("user23", "user50")
SocialNetworkWeb.addConnection("user23", "user76")
SocialNetworkWeb.addConnection("user24", "user88")
SocialNetworkWeb.addConnection("user24", "user62")
SocialNetworkWeb.addConnection("user25", "user72")
SocialNetworkWeb.addConnection("user25", "user74")
SocialNetworkWeb.addConnection("user26", "user94")
SocialNetworkWeb.addConnection("user26", "user29")
SocialNetworkWeb.addConnection("user27", "user64")
SocialNetworkWeb.addConnection("user27", "user32")
SocialNetworkWeb.addConnection("user28", "user70")
SocialNetworkWeb.addConnection("user28", "user40")
SocialNetworkWeb.addConnection("user29", "user77")
SocialNetworkWeb.addConnection("user29", "user45")
SocialNetworkWeb.addConnection("user30", "user61")
SocialNetworkWeb.addConnection("user30", "user18")
SocialNetworkWeb.addConnection("user31", "user49")
SocialNetworkWeb.addConnection("user31", "user69")
SocialNetworkWeb.addConnection("user32", "user68")
SocialNetworkWeb.addConnection("user32", "user12")
SocialNetworkWeb.addConnection("user33", "user78")
SocialNetworkWeb.addConnection("user33", "user24")
SocialNetworkWeb.addConnection("user34", "user48")
SocialNetworkWeb.addConnection("user34", "user98")
SocialNetworkWeb.addConnection("user35", "user22")
SocialNetworkWeb.addConnection("user35", "user19")
SocialNetworkWeb.addConnection("user36", "user38")
SocialNetworkWeb.addConnection("user36", "user67")
SocialNetworkWeb.addConnection("user37", "user31")
SocialNetworkWeb.addConnection("user37", "user59")
SocialNetworkWeb.addConnection("user38", "user30")
SocialNetworkWeb.addConnection("user38", "user16")
SocialNetworkWeb.addConnection("user39", "user82")
SocialNetworkWeb.addConnection("user39", "user34")
SocialNetworkWeb.addConnection("user40", "user51")
SocialNetworkWeb.addConnection("user40", "user93")
SocialNetworkWeb.addConnection("user41", "user99")
SocialNetworkWeb.addConnection("user41", "user89")
SocialNetworkWeb.addConnection("user42", "user13")
SocialNetworkWeb.addConnection("user42", "user1")
SocialNetworkWeb.addConnection("user43", "user60")
SocialNetworkWeb.addConnection("user43", "user3")
SocialNetworkWeb.addConnection("user44", "user6")
SocialNetworkWeb.addConnection("user44", "user5")
SocialNetworkWeb.addConnection("user45", "user17")
SocialNetworkWeb.addConnection("user45", "user68")
SocialNetworkWeb.addConnection("user46", "user8")
SocialNetworkWeb.addConnection("user46", "user47")
SocialNetworkWeb.addConnection("user47", "user15")
SocialNetworkWeb.addConnection("user47", "user4")
SocialNetworkWeb.addConnection("user48", "user63")
SocialNetworkWeb.addConnection("user48", "user21")
SocialNetworkWeb.addConnection("user49", "user72")
SocialNetworkWeb.addConnection("user49", "user90")
SocialNetworkWeb.addConnection("user50", "user98")
SocialNetworkWeb.addConnection("user50", "user37")
SocialNetworkWeb.addConnection("user51", "user44")
SocialNetworkWeb.addConnection("user51", "user57")
SocialNetworkWeb.addConnection("user52", "user42")
SocialNetworkWeb.addConnection("user52", "user75")
SocialNetworkWeb.addConnection("user53", "user84")
SocialNetworkWeb.addConnection("user53", "user70")
SocialNetworkWeb.addConnection("user54", "user49")
SocialNetworkWeb.addConnection("user54", "user60")
SocialNetworkWeb.addConnection("user55", "user20")
SocialNetworkWeb.addConnection("user55", "user23")
SocialNetworkWeb.addConnection("user56", "user97")
SocialNetworkWeb.addConnection("user56", "user33")
SocialNetworkWeb.addConnection("user57", "user65")
SocialNetworkWeb.addConnection("user57", "user41")
SocialNetworkWeb.addConnection("user58", "user2")
SocialNetworkWeb.addConnection("user58", "user26")
SocialNetworkWeb.addConnection("user59", "user25")
SocialNetworkWeb.addConnection("user59", "user29")
SocialNetworkWeb.addConnection("user60", "user12")
SocialNetworkWeb.addConnection("user60", "user28")
SocialNetworkWeb.addConnection("user61", "user48")
SocialNetworkWeb.addConnection("user61", "user50")
SocialNetworkWeb.addConnection("user62", "user45")
SocialNetworkWeb.addConnection("user62", "user14")
SocialNetworkWeb.addConnection("user63", "user55")
SocialNetworkWeb.addConnection("user63", "user11")
SocialNetworkWeb.addConnection("user64", "user67")
SocialNetworkWeb.addConnection("user64", "user38")
SocialNetworkWeb.addConnection("user65", "user31")
SocialNetworkWeb.addConnection("user65", "user19")
SocialNetworkWeb.addConnection("user66", "user22")
SocialNetworkWeb.addConnection("user66", "user9")
SocialNetworkWeb.addConnection("user71","user98")

## visualize the graph using an internal method

SocialNetworkWeb.dijkstra("user3")

## try DFS on the new graph 