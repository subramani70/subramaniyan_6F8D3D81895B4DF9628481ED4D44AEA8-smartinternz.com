class Player:
  def  play(self):
     print("The players is playing cricket")
class Batsman(Player):
   def play(self):
    print("The Batsman is batting ")
class Bowler(Player):
   def  play(self):
    print("The bowler is bowling")
Player1=Batsman()
Player1.play()
Player2=Bowler()
Player2.play()