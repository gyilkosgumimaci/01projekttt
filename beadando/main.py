from beadando_KPM import create_screen_KPM, BlackjackKPM

def main():
    screen = create_screen_KPM()
    game = BlackjackKPM(screen)
    game.run()

if __name__ == "__main__":
    main()
