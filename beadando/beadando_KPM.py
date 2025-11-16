import random
import turtle

def create_screen_KPM():
    screen = turtle.Screen()
    screen.title("Blackjack KPM")
    return screen

class BlackjackKPM:
    def __init__(self, screen):
        self.screen = screen
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.deck = []
        self.player = []
        self.dealer = []
        self.show_all_dealer = False

    def create_deck_KPM(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = ranks * 4
        random.shuffle(deck)
        return deck

    def hand_value_KPM(self, hand):
        total = 0
        aces = 0
        for rank in hand:
            if rank in ["J", "Q", "K"]:
                total += 10
            elif rank == "A":
                total += 11
                aces += 1
            else:
                if rank != "?":
                    total += int(rank)
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def format_hand_KPM(self, hand):
        result = []
        for rank in hand:
            if rank == "A":
                result.append("A(11/1)")
            else:
                result.append(rank)
        return "[" + ", ".join(result) + "]"

    def draw_text_KPM(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(-300, 150)
        self.t.write("Osztó:", font=("Arial", 16, "bold"))
        if self.show_all_dealer:
            visible_dealer = self.dealer
            dealer_score_text = str(self.hand_value_KPM(self.dealer))
        else:
            if len(self.dealer) > 0:
                visible_dealer = [self.dealer[0], "?"]
            else:
                visible_dealer = []
            dealer_score_text = "?"
        self.t.goto(-300, 120)
        self.t.write(self.format_hand_KPM(visible_dealer), font=("Arial", 14))
        self.t.goto(-300, 90)
        self.t.write("Pont: " + dealer_score_text, font=("Arial", 14))
        self.t.goto(-300, 30)
        self.t.write("Játékos:", font=("Arial", 16, "bold"))
        self.t.goto(-300, 0)
        self.t.write(self.format_hand_KPM(self.player), font=("Arial", 14))
        self.t.goto(-300, -30)
        self.t.write("Pont: " + str(self.hand_value_KPM(self.player)), font=("Arial", 14))

    def start_round_KPM(self):
        self.deck = self.create_deck_KPM()
        self.player = [self.deck.pop(), self.deck.pop()]
        self.dealer = [self.deck.pop(), self.deck.pop()]
        self.show_all_dealer = False
        self.draw_text_KPM()
        print("\nÚj kör:")
        print("Osztó:", self.format_hand_KPM([self.dealer[0], "?"]))
        print("Játékos:", self.format_hand_KPM(self.player))

    def run(self):
        print("KPM Blackjack")
        print("i = kérek lapot, n = megállok, v = kilépés")

        while True:
            self.start_round_KPM()

            while True:
                valasz = input("\nLapot? (i/n/v): ").lower().strip()

                if valasz == "v":
                    print("Kilépés a játékból.")
                    turtle.bye()
                    return

                if valasz == "i":
                    self.player.append(self.deck.pop())
                    print("Játékos:", self.format_hand_KPM(self.player))
                    self.draw_text_KPM()
                    if self.hand_value_KPM(self.player) > 21:
                        self.show_all_dealer = True
                        self.draw_text_KPM()
                        print("Túl sok! Vesztettél.")
                        print("Osztó teljes keze:", self.format_hand_KPM(self.dealer))
                        break

                elif valasz == "n":
                    self.show_all_dealer = True
                    while self.hand_value_KPM(self.dealer) < 17 and len(self.deck) > 0:
                        self.dealer.append(self.deck.pop())
                    self.draw_text_KPM()
                    print("Osztó:", self.format_hand_KPM(self.dealer))

                    player_val = self.hand_value_KPM(self.player)
                    dealer_val = self.hand_value_KPM(self.dealer)

                    print("Játékos pont:", player_val)
                    print("Osztó pont:", dealer_val)

                    if dealer_val > 21 or player_val > dealer_val:
                        print("Nyertél!")
                    elif dealer_val == player_val:
                        print("Döntetlen!")
                    else:
                        print("Vesztettél.")
                    break

                else:
                    print("Érvénytelen válasz.")
