#Define the base class player
class Player:
  def play(self):
    print("The player is playing cricket.")
    
#define the derived class Batsman
class Batsman(Player):
  def play(self):
     print("The batsman is batting.")

#define the derived class bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#create objects of batsman and bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play() method for each object
batsman.play()
bowler.play()



        